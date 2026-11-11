# -*- coding: utf-8 -*-
"""
comparar.py - compara dois projetos E3 do MESMO ativo e informa, objeto a objeto, DE -> PARA.

    Projeto novo sofreu alterações:
      Tela Usina
        Objeto Grupo1/equipInversor10 (cEquipInversor)
          X: de 4498 para 4510
          Y: de 1200 para 1216

O que e comparado (por objeto, alinhado por GUID - sobrevive a renomear/mover - com fallback por caminho):
  * propriedades nomeadas (nome, tipo, valor; booleanos/enums/cores formatados pela type lib)
  * geometria dos objetos de tela: X, Y, Width, Height (decodificados do retangulo binario) e Angle
  * componentes anexados: associacoes (AgSimple/TableBind/...), scripts (evento a evento), alarmes etc.
  * objetos/nos adicionados e removidos, objetos renomeados/movidos, versao das bibliotecas de classe
  * campos binarios ainda NAO decodificados (cores, estilos...) aparecem como "campo binario @offset: de <hex> para <hex>"
Coordenadas em Himetric (1000 unidades = 1 cm).  Senhas/tokens sao mascarados.

Uso:
  python comparar.py ANTIGO.prj NOVO.prj [-o pasta_logs] [--cm]
  python comparar.py --lote PASTA_ANTIGA PASTA_NOVA [-o pasta_logs]      (compara todos os .prj de mesmo caminho relativo)
"""
import os, sys, re, json, glob, struct, math, hashlib, difflib, argparse, datetime, collections, time
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from e3reader import Project, scan_props, embedded_objects

PAT = os.path.join(AQUI, 'patterns')
LOGS = os.path.join(AQUI, 'logs')
SECRET = re.compile(r'(pwd|passw|senha|secret|token|apikey)', re.I)
HEAD = ('Tip', 'Angle', 'Layer', 'Visible', 'Enabled', 'TabStop')
ESPECIAIS = {'AgScript', 'AgSimple', 'TableBind', 'AnimationBind', 'AnalogBind', 'MultiSourceBind'}
ILEGAIS = re.compile('[\x00-\x08\x0b\x0c\x0e-\x1f\ufffe\uffff]')
IGNORAR = re.compile(r'^(_EventCount|_Event\d+\..*|_LayerCount)$')


def agora():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


# --------------------------------------------------------------------------- metadados (patterns)
class Meta:
    def __init__(self):
        self.grafico = {}; self.tipos = {}; self.enums = {}
        mp = os.path.join(PAT, 'modelo.json')
        if os.path.exists(mp):
            for k, c in json.load(open(mp, encoding='utf-8'))['classes'].items(): self.grafico[k] = bool(c.get('grafico'))
        pp = os.path.join(PAT, 'E3_Pattern.propriedades.json')
        if os.path.exists(pp):
            for c in json.load(open(pp, encoding='utf-8')):
                d = self.tipos.setdefault(c['classe'], {})
                for p in c['propriedades']:
                    arq = re.sub(r' \((?:apelido[^)]*|família)\)$', '', p['nome_no_prj'])
                    tl = p['nome'].split('[')[0]
                    if arq and arq != '—': d[arq.lower()] = (tl, p['tipo'])
                    d.setdefault(tl.lower(), (tl, p['tipo']))
        ep = os.path.join(PAT, 'E3_Pattern.json')
        if os.path.exists(ep):
            for m in json.load(open(ep, encoding='utf-8')):
                for e in m['enums']: self.enums[e['nome']] = {int(v): n for n, v in e['valores']}
        for k in ('XFolder', 'XControl', 'XObject'):
            xp = os.path.join(PAT, k + '.json')
            if os.path.exists(xp):
                for c in json.load(open(xp, encoding='utf-8')):
                    d = self.tipos.setdefault(c['nome'], {})
                    for m in c['membros']: d.setdefault(m['nome'].lower(), (m['nome'], m['tipo']))

    def info(self, classe, nome):
        """-> (nome de exibicao, tipo da type lib/lib)"""
        n = self.tipos.get(classe, {}).get(nome.lower())
        if not n: return nome, ''
        return (nome if n[0].lower() == nome.lower() else '%s (%s)' % (nome, n[0])), n[1]

    def fmt(self, v, tipo, nome=''):
        if SECRET.search(nome) and isinstance(v, str) and v: return '***' + hashlib.sha1(v.encode()).hexdigest()[:6]
        if v is None: return 'Empty'
        if isinstance(v, bool): return 'True' if v else 'False'
        if tipo == 'Boolean' and isinstance(v, int): return 'True' if v else 'False'
        if tipo in self.enums and isinstance(v, int): return '%s (%d)' % (self.enums[tipo].get(v, '?'), v)
        if tipo in ('OLE_COLOR', 'ECO_COLOR') and isinstance(v, int): return '#%02X%02X%02X' % (v & 255, (v >> 8) & 255, (v >> 16) & 255)
        if isinstance(v, float): return ('%.6g' % v)
        if isinstance(v, str):
            if v == '': return 'Empty'
            if ILEGAIS.search(v): return '<dados binários, %d caracteres>' % len(v)
            t = v.replace('\r\n', '↵').replace('\n', '↵')
            return t if len(t) <= 140 else t[:140] + '…'
        return str(v)


META = None


# --------------------------------------------------------------------------- leitura de um no
def papel(n, primeira):
    if n.is_stream: return 'Recurso'
    if not n.has_data: return 'Pasta'
    if primeira == 'DataServer': return 'Servidor de Dados'
    if primeira.endswith('Driver'): return 'Driver'
    if primeira == 'Screen': return 'Tela'
    if primeira == 'AlarmServer': return 'Servidor de Alarmes'
    if primeira in ('DBServer', 'Hist', 'HistServer'): return 'Banco de Dados'
    if primeira in ('Frame', 'Viewer', 'FrameSet'): return 'Viewer/Frames'
    if primeira in ('XFolder', 'XControl', 'XObject'): return 'Classe de biblioteca (%s)' % primeira
    return 'Nó (%s)' % primeira


def comp_disc(o, ordem):
    pm = {a: v for a, vt, v, _ in o['props']}
    for k in ('Property', 'OnProperty', 'Name'):
        if pm.get(k): return str(pm[k])
    return '#%d' % ordem


class NoLido:
    """objetos de um no, prontos para alinhar/comparar."""

    def __init__(self, proj, n):
        proj.load_node(n)
        self.n = n; self.dat = proj.read_stream(n.storage, 'EFSFileData')
        self.classes = {c.get('Name'): c for c in n.classes}
        self.objs = [o for o in n.objects if o['kind'] != -1]
        by = {o['idx']: o for o in n.objects}
        self.comps = collections.defaultdict(list)
        cont = collections.Counter()
        for o in n.objects:
            if o['kind'] == -1 and o.get('owner') in by:
                k = (o['owner'], o['class']); cont[k] += 1
                o['_disc'] = comp_disc(o, cont[k] - 1)
                self.comps[o['owner']].append(o)
        gc = collections.Counter(o['guid'] for o in self.objs if o['guid'])
        for o in self.objs:
            o['_id'] = 'g:' + o['guid'] if o['guid'] and gc[o['guid']] == 1 else None
        self.by_id = {o['_id']: o for o in self.objs if o['_id']}
        self.by_path = collections.defaultdict(list)
        for o in self.objs: self.by_path[o['opath']].append(o)

    def blob(self, o):
        return self.dat[o['offset']:o['offset'] + o['size']]


def geometria(blob, classe):
    if not META.grafico.get(classe): return None
    head = struct.unpack_from('<I', blob, 0)[0]
    if len(blob) < head + 33: return None
    x1, y1, x2, y2 = struct.unpack_from('<4d', blob, head + 1)
    if not all(math.isfinite(v) for v in (x1, y1, x2, y2)): return None
    return {'X': x1, 'Y': y1, 'Width': x2 - x1, 'Height': y2 - y1}


PONTOS = {'DrawLine', 'DrawBezier', 'DrawConnector'}


def pontos(blob, g):
    """pontos (x, y) de DrawLine/DrawBezier/DrawConnector: pares de doubles contiguos cujo envelope coincide com o retangulo do objeto.
    -> (offset_inicial, [(x, y), ...]) ou None. Correspondem a DrawLinePoint.X/Y da type lib."""
    if not g: return None
    head = struct.unpack_from('<I', blob, 0)[0]
    x1, y1, x2, y2 = g['X'], g['Y'], g['X'] + g['Width'], g['Y'] + g['Height']; tol = 1.0
    n = len(blob); melhor = None; st = head + 33
    while st + 32 <= n:
        run = []; k = st
        while k + 16 <= n:
            x, y = struct.unpack_from('<2d', blob, k)
            if not (math.isfinite(x) and math.isfinite(y) and x1 - tol <= x <= x2 + tol and y1 - tol <= y <= y2 + tol): break
            run.append((x, y)); k += 16
        if len(run) >= 2:
            xs = [p[0] for p in run]; ys = [p[1] for p in run]
            if abs(min(xs) - x1) <= tol and abs(max(xs) - x2) <= tol and abs(min(ys) - y1) <= tol and abs(max(ys) - y2) <= tol:
                if melhor is None or len(run) > len(melhor[1]): melhor = (st, run)
                st = k; continue
        st += 1
    return melhor


def ocupacao(blob, geom, pts=None):
    """intervalos (cabecalho, retangulo, propriedades nomeadas) -> o 'resto' e a parte binaria ainda nao decodificada."""
    head = struct.unpack_from('<I', blob, 0)[0]
    spans = [(i, e) for _, _, _, i, e in scan_props(blob, 4, spans=True)]
    oc = sorted([(0, head)] + ([(head, head + 33)] if geom else []) + ([(pts[0], pts[0] + 16 * len(pts[1]))] if pts else []) + spans)
    # prefixos de tamanho de secao (u32 de 4 bytes logo antes de propriedades nomeadas) nao sao dados do objeto
    bordas = {i for i, _ in oc} | {e for _, e in oc} | {len(blob)}
    extra = []; pos = 0
    for i, e in oc:
        if i - pos >= 4 and pos + 4 <= len(blob):                      # 1o u32 de cada lacuna
            v = struct.unpack_from('<I', blob, pos)[0]
            if 4 <= v <= len(blob) - pos and (pos + v) in bordas: extra.append((pos, pos + 4))
        pos = max(pos, e)
    return sorted(oc + extra)


def resto(blob, ocup):
    out = bytearray(); pos = 0
    for i, e in ocup:
        if i > pos: out += blob[pos:i]
        pos = max(pos, e)
    out += blob[pos:]
    return bytes(out)


def _dbl(buf):
    v = struct.unpack('<d', buf)[0]
    return v if math.isfinite(v) and (v == 0 or 1e-4 < abs(v) < 1e8) else None


def campos_binarios(ba, bb, ga, gb, pa=None, pb=None):
    """compara SO a parte binaria nao decodificada; [] se igual.
    Devolve [(posicao, de_hex, para_hex, double_de|None, double_para|None)]."""
    oa, ob = ocupacao(ba, ga, pa), ocupacao(bb, gb, pb)
    ra, rb = resto(ba, oa), resto(bb, ob)
    if ra == rb: return []
    if len(ra) != len(rb):
        return [('bloco', '%d bytes' % len(ra), '%d bytes' % len(rb), None, None)]
    diffs = [k for k in range(len(ra)) if ra[k] != rb[k]]
    grupos = []; ini = ant = None
    for k in diffs:
        if ini is None: ini = ant = k
        elif k - ant <= 3: ant = k
        else: grupos.append((ini, ant)); ini = ant = k
    if ini is not None: grupos.append((ini, ant))
    res = []
    for i, e in grupos:
        dbl = None
        if e - i <= 7:                                   # procura uma janela de 8 bytes que decodifique como double nos dois lados
            cand = []
            for st in range(max(0, e - 7), i + 1):
                if st + 8 > len(ra): continue
                da, db = _dbl(ra[st:st + 8]), _dbl(rb[st:st + 8])
                if da is not None and db is not None: cand.append((len(repr(round(da, 4))) + len(repr(round(db, 4))), st, da, db))
            if cand: _, st, da, db = min(cand); dbl = (st, da, db)
        if dbl:
            st, da, db = dbl
            res.append(('@0x%03X' % st, ra[st:st + 8].hex(), rb[st:st + 8].hex(), da, db))
        else:
            a0 = i - (i % 4); b0 = min(len(ra), e + 1 + (3 - e % 4))
            res.append(('@0x%03X' % a0, ra[a0:b0].hex(), rb[a0:b0].hex(), None, None))
    return res


# --------------------------------------------------------------------------- comparacao de objetos
def props_nomeadas(o):
    d = collections.OrderedDict(); cont = collections.Counter()
    for nm, vt, v, _ in o['props']:
        if IGNORAR.match(nm): continue
        cont[nm] += 1
        d[nm if cont[nm] == 1 else '%s#%d' % (nm, cont[nm])] = v
    return d


def linha(nome, de, para, classe, tipo=''):
    return {'prop': nome, 'de': META.fmt(de, tipo, nome), 'para': META.fmt(para, tipo, nome)}


def equivalentes(nm, va, vb):
    """valores iguais para fins de comparacao: Empty/Null/0 em TimeStamp (data zero gravada de formas diferentes)."""
    if nm == 'TimeStamp': return va in (None, '<Null>', 0, 0.0) and vb in (None, '<Null>', 0, 0.0)
    return False


def diff_props(classe, pa, pb, prefixo=''):
    out = []
    for nm in list(pb) + [k for k in pa if k not in pb]:
        va, vb = pa.get(nm, None), pb.get(nm, None)
        if va == vb or (nm in pa and nm in pb and equivalentes(nm, va, vb)): continue
        nome_ex, tipo = META.info(classe, re.sub(r'#\d+$', '', nm))
        if nm not in pa: out.append({'prop': prefixo + nome_ex, 'de': '(não existia)', 'para': META.fmt(vb, tipo, nm)})
        elif nm not in pb: out.append({'prop': prefixo + nome_ex, 'de': META.fmt(va, tipo, nm), 'para': '(removida)'})
        else: out.append({'prop': prefixo + nome_ex, 'de': META.fmt(va, tipo, nm), 'para': META.fmt(vb, tipo, nm)})
    return out


def eventos(o):
    pm = {a: v for a, vt, v, _ in o['props']}
    ev = collections.OrderedDict()
    for i in range(1, (pm.get('_EventCount') or 0) + 1):
        ev[pm.get('_Event%d.Name' % i, 'evento%d' % i)] = pm.get('_Event%d.Pick0Code' % i) or ''
    return ev


def diff_eventos(ea, eb, prefixo=''):
    out = []
    n = lambda c: len([l for l in c.splitlines() if l.strip()])
    for nm in list(eb) + [k for k in ea if k not in eb]:
        if nm not in ea: out.append({'prop': '%sScript %s' % (prefixo, nm), 'de': '(não existia)', 'para': '%d linhas' % n(eb[nm])})
        elif nm not in eb: out.append({'prop': '%sScript %s' % (prefixo, nm), 'de': '%d linhas' % n(ea[nm]), 'para': '(removido)'})
        elif ea[nm] != eb[nm]:
            d = [l for l in difflib.unified_diff(ea[nm].splitlines(), eb[nm].splitlines(), lineterm='', n=0) if not l.startswith(('---', '+++', '@@'))]
            out.append({'prop': '%sScript %s' % (prefixo, nm), 'de': '%d linhas' % len(ea[nm].splitlines()), 'para': '%d linhas' % len(eb[nm].splitlines()),
                        'diff': d[:14] + (['… (+%d linhas)' % (len(d) - 14)] if len(d) > 14 else [])})
    return out


def membros_embutidos(blob):
    """XCoClass.Methods guarda um OLE2 com os XMethod (propriedades/metodos da classe) e seus scripts.
    -> {nome: (propriedades, eventos)} ou None."""
    try: leaf = embedded_objects(blob)
    except Exception: return None
    if leaf is None: return None
    out = {}
    for o in leaf.objects:
        if o['class'] != 'XMethod' or o['kind'] == -1: continue
        pm = props_nomeadas(o); ev = collections.OrderedDict()
        for c in leaf.objects:
            if c['kind'] == -1 and c.get('owner') == o['idx'] and c['class'] == 'AgScript': ev.update(eventos(c))
        out[str(pm.get('Name', '?'))] = (pm, ev)
    return out


def diff_membros(ma, mb):
    out = []
    for nm in list(mb) + [k for k in ma if k not in mb]:
        if nm not in ma:
            pm = mb[nm][0]; out.append({'prop': 'Membro %s' % nm, 'de': '(não existia)', 'para': 'adicionado (%s)' % META.fmt(pm.get('Type'), '', 'Type'), 'tipo': 'membro'}); continue
        if nm not in mb:
            out.append({'prop': 'Membro %s' % nm, 'de': 'existia (%s)' % META.fmt(ma[nm][0].get('Type'), '', 'Type'), 'para': '(removido)', 'tipo': 'membro'}); continue
        pa, pb = dict(ma[nm][0]), dict(mb[nm][0])
        pa.pop('Name', None); pb.pop('Name', None)
        for x in diff_props('XMethod', pa, pb): x['prop'] = 'Membro %s: %s' % (nm, x['prop']); x['tipo'] = 'membro'; out.append(x)
        for x in diff_eventos(ma[nm][1], mb[nm][1], 'Membro %s: ' % nm): x['tipo'] = 'membro'; out.append(x)
    return out


def diff_comp(ca, cb, A=None, B=None):
    cls = cb['class']
    if cls == 'AgScript':
        return diff_eventos(eventos(ca), eventos(cb))
    if cls == 'XCoClass' and A is not None and B is not None:
        ma, mb = membros_embutidos(A.blob(ca)), membros_embutidos(B.blob(cb))
        if ma is not None and mb is not None: return diff_membros(ma, mb)
        return [{'prop': 'Definição dos membros da classe (XCoClass)', 'de': 'alterada', 'para': 'não foi possível abrir o container', 'tipo': 'membro'}]
    pa, pb = props_nomeadas(ca), props_nomeadas(cb)
    d = diff_props(cls, pa, pb)
    if cls == 'AgSimple':
        alvo = str(pb.get('Property') or pa.get('Property') or '?')
        for x in d: x['prop'] = 'Associação %s: %s' % (alvo, x['prop'])
    elif cls in ('TableBind', 'AnimationBind', 'AnalogBind', 'MultiSourceBind'):
        alvo = str(pb.get('OnProperty') or pa.get('OnProperty') or '?')
        for x in d: x['prop'] = 'Associação %s (%s): %s' % (alvo, cls, x['prop'])
    else:
        nome = str(pb.get('Name') or ca.get('_disc') or '')
        for x in d: x['prop'] = '%s %s: %s' % (cls, nome, x['prop'])
    return d


def comparar_no(A, B, caminho):
    """-> (lista de mudancas por objeto, adicionados, removidos, renomeados, mudancas de classe/lib)"""
    emparelhado = {}                # idx A -> idx B
    usados_b = set()
    for idb, ob in B.by_id.items():
        oa = A.by_id.get(idb)
        if oa: emparelhado[oa['idx']] = ob['idx']; usados_b.add(ob['idx'])
    for path, la in A.by_path.items():                      # fallback por caminho (objetos sem GUID unico)
        lb = [x for x in B.by_path.get(path, []) if x['idx'] not in usados_b]
        for oa in la:
            if oa['idx'] in emparelhado: continue
            cand = [x for x in lb if x['idx'] not in usados_b and x['class'] == oa['class']]
            if cand: emparelhado[oa['idx']] = cand[0]['idx']; usados_b.add(cand[0]['idx'])
    A_by = {o['idx']: o for o in A.objs}; B_by = {o['idx']: o for o in B.objs}
    # objetos recriados em outro caminho (GUID novo): pareia por classe + nome (unico) ou pelo trecho final do caminho
    rest_a = [o for o in A.objs if o['idx'] not in emparelhado]; rest_b = [o for o in B.objs if o['idx'] not in usados_b]
    if rest_a and rest_b:
        idx_b = collections.defaultdict(list)
        for o in rest_b: idx_b[(o['class'], o['name'])].append(o)
        idx_a = collections.Counter((o['class'], o['name']) for o in rest_a)
        cands = []
        for oa in rest_a:
            k = (oa['class'], oa['name'])
            lb = idx_b.get(k, [])
            if not lb: continue
            if len(lb) == 1 and idx_a[k] == 1: cands.append((99, oa, lb[0])); continue
            sa = oa['opath'].split('/')[::-1]
            for ob in lb:
                sb = ob['opath'].split('/')[::-1]; comum = 0
                for x, y in zip(sa, sb):
                    if x != y: break
                    comum += 1
                if comum >= 2: cands.append((comum, oa, ob))
        cands.sort(key=lambda t: -t[0])
        for sc, oa, ob in cands:
            if oa['idx'] in emparelhado or ob['idx'] in usados_b: continue
            emparelhado[oa['idx']] = ob['idx']; usados_b.add(ob['idx'])
    removidos = [o for o in A.objs if o['idx'] not in emparelhado]
    adicionados = [o for o in B.objs if o['idx'] not in usados_b]
    mudancas = []; renomeados = []
    for ia, ib in emparelhado.items():
        oa, ob = A_by[ia], B_by[ib]
        ca_, cb_ = A.comps.get(ia, []), B.comps.get(ib, [])
        iguais = (oa['sha1'] == ob['sha1']) and len(ca_) == len(cb_) and all(x['sha1'] == y['sha1'] for x, y in zip(ca_, cb_))
        if oa['name'] != ob['name']:
            renomeados.append({'de': oa['opath'], 'para': ob['opath'], 'classe': ob['class']})
        elif oa['opath'].rsplit('/', 1)[0] != ob['opath'].rsplit('/', 1)[0] and not (oa['owner'] in emparelhado and emparelhado[oa['owner']] == ob['owner']):
            renomeados.append({'de': oa['opath'], 'para': ob['opath'], 'classe': ob['class'], 'movido': True})
        if iguais: continue
        linhas = []
        if oa['class'] != ob['class']: linhas.append({'prop': 'Classe', 'de': oa['class'], 'para': ob['class']})
        if oa['sha1'] != ob['sha1']:
            ba, bb = A.blob(oa), B.blob(ob)
            ga, gb = geometria(ba, oa['class']), geometria(bb, ob['class'])
            if ga and gb:
                for k in ('X', 'Y', 'Width', 'Height'):
                    if abs(ga[k] - gb[k]) > 1e-6: linhas.append({'prop': k, 'de': META.fmt(round(ga[k], 4), 'Double'), 'para': META.fmt(round(gb[k], 4), 'Double'), 'tipo': 'geometria'})
            pta = pontos(ba, ga) if ob['class'] in PONTOS else None; ptb = pontos(bb, gb) if ob['class'] in PONTOS else None
            if pta and ptb:
                if len(pta[1]) != len(ptb[1]): linhas.append({'prop': 'Quantidade de pontos', 'de': str(len(pta[1])), 'para': str(len(ptb[1])), 'tipo': 'geometria'})
                for i, (qa, qb) in enumerate(zip(pta[1], ptb[1]), 1):
                    for eixo, u, v in (('X', qa[0], qb[0]), ('Y', qa[1], qb[1])):
                        if abs(u - v) > 1e-6: linhas.append({'prop': 'Ponto %d %s' % (i, eixo), 'de': META.fmt(round(u, 4), 'Double'), 'para': META.fmt(round(v, 4), 'Double'), 'tipo': 'geometria'})
            pa, pb = props_nomeadas(oa), props_nomeadas(ob)
            linhas += diff_props(ob['class'], pa, pb)
            if ba != bb and oa['sha1'] != ob['sha1']:
                # algo mudou fora do cabecalho/retangulo/nomeadas?
                try:
                    cb = campos_binarios(ba, bb, ga, gb, pta, ptb)
                except Exception:
                    cb = []
                pares_geo = []
                if ga and gb:
                    pares_geo = [(ga['X'], gb['X']), (ga['Y'], gb['Y']), (ga['X'] + ga['Width'], gb['X'] + gb['Width']), (ga['Y'] + ga['Height'], gb['Y'] + gb['Height'])]
                cb2 = []
                for off, de, para, da, db in cb:
                    if da is not None and any(abs(da - x) < 1e-6 and abs(db - y) < 1e-6 for x, y in pares_geo): continue      # copia das coordenadas ja reportadas
                    cb2.append((off, de, para, da, db))
                for off, de, para, da, db in cb2[:8]:
                    if off == 'bloco': linhas.append({'prop': 'bloco binário não decodificado (tamanho)', 'de': de, 'para': para, 'tipo': 'binario'})
                    elif da is not None: linhas.append({'prop': 'campo binário %s (valor decimal, não identificado)' % off, 'de': META.fmt(round(da, 4), 'Double'), 'para': META.fmt(round(db, 4), 'Double'), 'tipo': 'binario'})
                    else: linhas.append({'prop': 'campo binário %s (não identificado)' % off, 'de': de, 'para': para, 'tipo': 'binario'})
                if len(cb2) > 8: linhas.append({'prop': 'campos binários', 'de': '', 'para': '+%d trechos alterados' % (len(cb2) - 8), 'tipo': 'binario'})
        # componentes
        ma = {(c['class'], c['_disc']): c for c in ca_}; mb = {(c['class'], c['_disc']): c for c in cb_}
        for k in list(mb) + [k for k in ma if k not in mb]:
            vazio = lambda c: c['class'] == 'AgScript' and not eventos(c)           # script sem eventos = placeholder
            if k not in ma:
                if not vazio(mb[k]): linhas.append({'prop': 'Componente %s %s' % k, 'de': '(não existia)', 'para': 'adicionado', 'tipo': 'componente'})
            elif k not in mb:
                if not vazio(ma[k]): linhas.append({'prop': 'Componente %s %s' % k, 'de': 'existia', 'para': '(removido)', 'tipo': 'componente'})
            elif ma[k]['sha1'] != mb[k]['sha1']: linhas += diff_comp(ma[k], mb[k], A, B)
        if linhas: mudancas.append({'objeto': ob['opath'], 'classe': ob['class'], 'mudancas': linhas})
    # bibliotecas de classe
    libs = []
    for nm in set(A.classes) | set(B.classes):
        ca, cb = A.classes.get(nm), B.classes.get(nm)
        if ca and cb:
            for f in ('LibVersion', 'LibModuleName', 'CLSID'):
                if ca.get(f) != cb.get(f): libs.append({'classe': nm, 'campo': f, 'de': ca.get(f), 'para': cb.get(f)})
    return mudancas, adicionados, removidos, renomeados, libs


# --------------------------------------------------------------------------- projeto
def comparar_projetos(caminho_a, caminho_b, log=print):
    t0 = agora()
    pa, pb = Project(caminho_a), Project(caminho_b)
    pa.build(load_objects=False); pb.build(load_objects=False)
    na = {n.path: n for n in pa.walk()}; nb = {n.path: n for n in pb.walk()}
    res = {'meta': {'antigo': os.path.abspath(caminho_a), 'novo': os.path.abspath(caminho_b), 'analise_inicio': t0,
                    'antigo_tamanho': os.path.getsize(caminho_a), 'novo_tamanho': os.path.getsize(caminho_b),
                    'antigo_modificado': datetime.datetime.fromtimestamp(os.path.getmtime(caminho_a)).astimezone().isoformat(timespec='seconds'),
                    'novo_modificado': datetime.datetime.fromtimestamp(os.path.getmtime(caminho_b)).astimezone().isoformat(timespec='seconds')},
           'nos': [], 'nos_adicionados': [], 'nos_removidos': [], 'nos_identicos': 0, 'nos_comparados': 0}
    for path in nb:
        if path not in na:
            n = nb[path]; pb.load_node(n)
            res['nos_adicionados'].append({'no': path, 'papel': papel(n, n.objects[0]['class'] if n.objects else ''), 'objetos': len(n.objects)}); pb.free_node(n)
    for path in na:
        if path not in nb:
            n = na[path]; pa.load_node(n)
            res['nos_removidos'].append({'no': path, 'papel': papel(n, n.objects[0]['class'] if n.objects else ''), 'objetos': len(n.objects)}); pa.free_node(n)
    for path in nb:
        if path not in na: continue
        a, b = na[path], nb[path]
        res['nos_comparados'] += 1
        if pa.digest(a) == pb.digest(b): res['nos_identicos'] += 1; continue
        if b.is_stream or a.is_stream:
            res['nos'].append({'no': path, 'papel': 'Recurso', 'mudancas': [], 'adicionados': [], 'removidos': [], 'renomeados': [], 'libs': [], 'recurso_alterado': True}); continue
        A, B = NoLido(pa, a), NoLido(pb, b)
        primeira = B.n.objects[0]['class'] if B.n.objects else ''
        mud, add, rem, ren, libs = comparar_no(A, B, path)
        if mud or add or rem or ren or libs:
            res['nos'].append({'no': path, 'papel': papel(b, primeira), 'mudancas': mud,
                               'adicionados': [{'objeto': o['opath'], 'classe': o['class']} for o in add],
                               'removidos': [{'objeto': o['opath'], 'classe': o['class']} for o in rem], 'renomeados': ren, 'libs': libs})
        pa.free_node(a); pb.free_node(b)
        log('  nó comparado: %s' % path)
    pa.ole.close(); pb.ole.close()
    res['meta']['analise_fim'] = agora()
    objs_alt = sum(len(n['mudancas']) for n in res['nos'])
    props_alt = sum(len(m['mudancas']) for n in res['nos'] for m in n['mudancas'])
    res['resumo'] = {'objetos_alterados': objs_alt, 'propriedades_alteradas': props_alt,
                     'objetos_adicionados': sum(len(n['adicionados']) for n in res['nos']), 'objetos_removidos': sum(len(n['removidos']) for n in res['nos']),
                     'objetos_renomeados_ou_movidos': sum(len(n['renomeados']) for n in res['nos']),
                     'nos_adicionados': len(res['nos_adicionados']), 'nos_removidos': len(res['nos_removidos']),
                     'nos_com_alteracao': len(res['nos']), 'nos_comparados': res['nos_comparados'], 'nos_identicos': res['nos_identicos']}
    r = res['resumo']
    r['itens_alterados'] = r['objetos_alterados'] + r['objetos_adicionados'] + r['objetos_removidos'] + r['objetos_renomeados_ou_movidos'] + r['nos_adicionados'] + r['nos_removidos']
    return res


# --------------------------------------------------------------------------- relatorio
def titulo_no(n):
    nome = n['no'].split('/')[-1]
    return '%s %s' % (n['papel'], nome)


def relatorio_md(res, cm=False):
    L = []; w = L.append
    m = res['meta']; r = res['resumo']
    w('# Comparação de projetos E3\n')
    w('- **Projeto antigo:** `%s` (%.1f MB, modificado em %s)' % (m['antigo'], m['antigo_tamanho'] / 1048576, m['antigo_modificado']))
    w('- **Projeto novo:** `%s` (%.1f MB, modificado em %s)' % (m['novo'], m['novo_tamanho'] / 1048576, m['novo_modificado']))
    w('- **Horário da análise:** %s → %s' % (m['analise_inicio'], m['analise_fim']))
    w('- **Horário de geração do log:** %s' % agora())
    w('- **Itens alterados: %d** — objetos alterados %d · adicionados %d · removidos %d · renomeados/movidos %d · nós adicionados %d · nós removidos %d · propriedades alteradas (de → para) %d' % (
        r['itens_alterados'], r['objetos_alterados'], r['objetos_adicionados'], r['objetos_removidos'], r['objetos_renomeados_ou_movidos'], r['nos_adicionados'], r['nos_removidos'], r['propriedades_alteradas']))
    w('- Nós comparados: %d (idênticos: %d) · coordenadas X/Y/Width/Height em Himetric (1000 = 1 cm)\n' % (r['nos_comparados'], r['nos_identicos']))
    if not r['itens_alterados'] and not res['nos']:
        w('**Nenhuma alteração encontrada.**'); return '\n'.join(L) + '\n'
    w('## Projeto novo sofreu alterações:\n')
    for n in res['nos_adicionados']: w('- **Adicionado:** %s `%s` (%d objetos)' % (n['papel'], n['no'], n['objetos']))
    for n in res['nos_removidos']: w('- **Removido:** %s `%s` (%d objetos)' % (n['papel'], n['no'], n['objetos']))
    if res['nos_adicionados'] or res['nos_removidos']: w('')
    for n in res['nos']:
        w('### %s' % titulo_no(n)); w('`%s`\n' % n['no'])
        if n.get('recurso_alterado'): w('- Conteúdo do recurso alterado\n'); continue
        grp = collections.OrderedDict()
        for l in n['libs']: grp.setdefault((l['campo'], l['de'], l['para']), []).append(l['classe'])
        for (campo, de, para), cl in grp.items():
            w('- Biblioteca de %d classe(s): %s: de %s para %s (%s)' % (len(cl), campo, de, para, ', '.join(sorted(cl)[:12]) + (' …' if len(cl) > 12 else '')))
        for x in n['adicionados']: w('- **Objeto adicionado:** %s (%s)' % (x['objeto'], x['classe']))
        for x in n['removidos']: w('- **Objeto removido:** %s (%s)' % (x['objeto'], x['classe']))
        for x in n['renomeados']: w('- **Objeto %s:** de `%s` para `%s` (%s)' % ('movido' if x.get('movido') else 'renomeado', x['de'], x['para'], x['classe']))
        for o in n['mudancas']:
            w('- **Objeto %s** (%s)' % (o['objeto'], o['classe']))
            for c in o['mudancas']:
                extra = ''
                if cm and c.get('tipo') == 'geometria':
                    try: extra = ' (%.3f cm → %.3f cm)' % (float(c['de']) / 1000, float(c['para']) / 1000)
                    except ValueError: pass
                w('  - %s: de %s para %s%s' % (c['prop'], c['de'] if c['de'] != '' else '—', c['para'], extra))
                for d in c.get('diff', []): w('      `%s`' % d.replace('`', "'"))
        w('')
    return '\n'.join(L) + '\n'


COLS_ADD = ['Projeto', 'Tipo de nó', 'Nó', 'Objeto', 'Classe', 'Observação']
COLS_MOD = ['Projeto', 'Tipo de nó', 'Nó', 'Objeto', 'Classe', 'Tipo de alteração', 'Propriedade', 'De', 'Para', 'Detalhe']


def tipo_alteracao(c):
    p = c['prop']; t = c.get('tipo', '')
    if t == 'geometria': return 'Geometria'
    if t == 'binario': return 'Campo binário (não identificado)'
    if t == 'membro' or p.startswith('Membro '): return 'Membro da classe (propriedade/método)'
    if p.startswith('Associação'): return 'Associação'
    if p.startswith('Script '): return 'Script'
    if p.startswith('Componente '): return 'Componente'
    if p == 'Classe': return 'Classe'
    return 'Propriedade'


def linhas_xlsx(res):
    """-> (adicionados, removidos, modificados): listas de linhas (uma por item)."""
    proj = os.path.basename(res['meta']['novo'])
    add, rem, mod = [], [], []
    for n in res['nos_adicionados']: add.append([proj, n['papel'], n['no'], '(nó inteiro)', '', '%d objetos' % n['objetos']])
    for n in res['nos_removidos']: rem.append([proj, n['papel'], n['no'], '(nó inteiro)', '', '%d objetos' % n['objetos']])
    for n in res['nos']:
        base = [proj, n['papel'], n['no']]
        if n.get('recurso_alterado'): mod.append(base + ['(recurso)', '', 'Recurso', 'Conteúdo', '', 'alterado', '']); continue
        for x in n['adicionados']: add.append(base + [x['objeto'], x['classe'], ''])
        for x in n['removidos']: rem.append(base + [x['objeto'], x['classe'], ''])
        for l in n['libs']: mod.append(base + ['(biblioteca de classe)', l['classe'], 'Biblioteca', l['campo'], str(l['de']), str(l['para']), ''])
        for x in n['renomeados']: mod.append(base + [x['para'], x['classe'], 'Movido' if x.get('movido') else 'Renomeado', 'Caminho', x['de'], x['para'], ''])
        for o in n['mudancas']:
            for c in o['mudancas']:
                mod.append(base + [o['objeto'], o['classe'], tipo_alteracao(c), c['prop'], c['de'], c['para'], '\n'.join(c.get('diff', []))])
    return add, rem, mod


def gravar_xlsx(lista_res, caminho):
    """cria o .xlsx com as abas Adicionado, Removido e Modificado (uma ou varias comparacoes)."""
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    wb = Workbook(); wb.remove(wb.active)
    dados = {'Adicionado': (COLS_ADD, []), 'Removido': (COLS_ADD, []), 'Modificado': (COLS_MOD, [])}
    for res in lista_res:
        a, r, m = linhas_xlsx(res)
        dados['Adicionado'][1].extend(a); dados['Removido'][1].extend(r); dados['Modificado'][1].extend(m)
    cores = {'Adicionado': '1E7B34', 'Removido': 'B3261E', 'Modificado': 'B26A00'}
    larg = {'Projeto': 18, 'Tipo de nó': 18, 'Nó': 44, 'Objeto': 52, 'Classe': 24, 'Observação': 18, 'Tipo de alteração': 26, 'Propriedade': 38, 'De': 42, 'Para': 42, 'Detalhe': 50}
    for nome, (cols, linhas) in dados.items():
        ws = wb.create_sheet(nome)
        ws.append(cols)
        for l in linhas: ws.append([(ILEGAIS.sub('?', str(v))[:32000] if isinstance(v, str) else v) for v in l])
        for i, c in enumerate(cols, 1):
            cel = ws.cell(row=1, column=i); cel.font = Font(bold=True, color='FFFFFF'); cel.fill = PatternFill('solid', fgColor=cores[nome])
            cel.alignment = Alignment(vertical='center'); ws.column_dimensions[get_column_letter(i)].width = larg.get(c, 20)
        ws.freeze_panes = 'A2'
        ws.auto_filter.ref = ws.dimensions
        ws.sheet_properties.tabColor = cores[nome]
        if nome == 'Modificado':
            for row in ws.iter_rows(min_row=2, min_col=8, max_col=10):
                for cel in row: cel.alignment = Alignment(wrap_text=True, vertical='top')
    m0 = lista_res[0]['meta']
    wb.properties.title = 'Comparação de projetos E3'
    wb.properties.description = 'Antigo: %s | Novo: %s | análise %s → %s | gerado em %s' % (m0['antigo'], m0['novo'], m0['analise_inicio'], m0['analise_fim'], agora()) if len(lista_res) == 1 else 'Comparação em lote, gerada em %s' % agora()
    wb.save(caminho)
    return caminho


def gravar(res, saida, cm=False):
    os.makedirs(saida, exist_ok=True)
    a = os.path.splitext(os.path.basename(res['meta']['antigo']))[0]
    stem = 'comparacao_%s_%s' % (a, datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
    md = os.path.join(saida, stem + '.md')
    open(md, 'w', encoding='utf-8-sig').write(relatorio_md(res, cm))
    res['tabelas'] = dict(zip(('adicionado', 'removido', 'modificado'), linhas_xlsx(res)))          # linhas prontas (visualizador PowerShell/Excel)
    json.dump(res, open(os.path.join(saida, stem + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    gravar_xlsx([res], os.path.join(saida, stem + '.xlsx'))
    return md


def main():
    global META
    ap = argparse.ArgumentParser()
    ap.add_argument('antigo', nargs='?'); ap.add_argument('novo', nargs='?'); ap.add_argument('--lote', nargs=2, metavar=('PASTA_ANTIGA', 'PASTA_NOVA'))
    ap.add_argument('-o', '--saida', default=LOGS); ap.add_argument('--cm', action='store_true', help='mostra X/Y/Width/Height tambem em cm')
    ap.add_argument('--ext', default='prj', choices=['prj', 'lib'], help='extensao dos arquivos no modo --lote (lib = bibliotecas)')
    ap.add_argument('--xlsx-de-logs', metavar='PASTA', help='gera .xlsx a partir dos .json ja gerados (sem recomparar); consolidado em comparacao_LOTE_*.xlsx')
    a = ap.parse_args()
    META = Meta()
    if a.xlsx_de_logs:
        js = sorted(glob.glob(os.path.join(a.xlsx_de_logs, 'comparacao_*.json')))
        mais_novo = {}
        for f in js:                                   # ultimo .json de cada projeto
            r = json.load(open(f, encoding='utf-8')); mais_novo[r['meta']['novo']] = (f, r)
        lista = [v[1] for v in mais_novo.values()]
        for f, r in mais_novo.values():
            gravar_xlsx([r], os.path.splitext(f)[0] + '.xlsx')
            if 'tabelas' not in r:
                r['tabelas'] = dict(zip(('adicionado', 'removido', 'modificado'), linhas_xlsx(r)))
                json.dump(r, open(f, 'w', encoding='utf-8'), ensure_ascii=False)
        if lista:
            cons = os.path.join(a.xlsx_de_logs, 'comparacao_LOTE_%s.xlsx' % datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
            gravar_xlsx(lista, cons); print('OK: %d projetos -> %s' % (len(lista), cons))
        return
    pares = []
    if a.lote:
        pa, pb = a.lote
        for f in sorted(glob.glob(os.path.join(pb, '**', '*.' + a.ext), recursive=True)):
            rel = os.path.relpath(f, pb)
            if a.ext == 'prj' and rel.split(os.sep)[0] not in ('01_Main', '02_GC', '03_Substations', '04_GD'): continue
            ant = os.path.join(pa, rel)
            if os.path.exists(ant): pares.append((ant, f))
    elif a.antigo and a.novo: pares = [(a.antigo, a.novo)]
    else: ap.error('informe ANTIGO NOVO ou --lote')
    resumo = []; todos = []
    for ant, nov in pares:
        if a.lote and open(ant, 'rb').read(1 << 20) == open(nov, 'rb').read(1 << 20) and os.path.getsize(ant) == os.path.getsize(nov):
            import filecmp
            if filecmp.cmp(ant, nov, shallow=False):
                print('= idêntico: %s' % nov); resumo.append((nov, None, None)); continue
        print('>> %s  ×  %s' % (ant, nov), flush=True); t = time.time()
        res = comparar_projetos(ant, nov, log=lambda m: print(m, flush=True)); todos.append(res)
        md = gravar(res, a.saida, a.cm); r = res['resumo']
        print('   itens alterados: %d | propriedades (de→para): %d | %.1fs\n   %s' % (r['itens_alterados'], r['propriedades_alteradas'], time.time() - t, md), flush=True)
        resumo.append((nov, r, md))
    if a.lote:
        L = ['# Comparação em lote\n', '- Antigo: `%s`\n- Novo: `%s`\n- Gerado em: %s\n' % (a.lote[0], a.lote[1], agora()),
             '| Projeto | Itens alterados | Objetos alt. | Adic. | Rem. | Prop. de→para | Relatório |', '|---|---:|---:|---:|---:|---:|---|']
        for nov, r, md in resumo:
            if r is None: L.append('| %s | idêntico | | | | | |' % os.path.basename(nov))
            else: L.append('| %s | %d | %d | %d | %d | %d | %s |' % (os.path.basename(nov), r['itens_alterados'], r['objetos_alterados'], r['objetos_adicionados'], r['objetos_removidos'], r['propriedades_alteradas'], os.path.basename(md)))
        open(os.path.join(a.saida, 'RESUMO_LOTE.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
        if todos:
            cons = os.path.join(a.saida, 'comparacao_LOTE_%s.xlsx' % datetime.datetime.now().strftime('%Y%m%d_%H%M%S'))
            print('XLSX consolidado:', gravar_xlsx(todos, cons))


if __name__ == '__main__':
    main()
