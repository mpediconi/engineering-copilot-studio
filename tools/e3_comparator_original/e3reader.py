# -*- coding: utf-8 -*-
"""
e3reader - leitor de projetos Elipse E3 (.prj)

O .prj e um container OLE2 (Compound File). Dentro dele o E3 usa o "EFS":
  <storage>/EFSIndex      -> lista de filhos: nome real (UTF-16) + GUID.
                             O nome do storage filho = base32(GUID) (alfabeto a-z012345,
                             little-endian, 26 chars) - por isso os nomes parecem aleatorios.
  <storage>/EFSFileLib    -> tabela de classes (Class{n}Name/LIBID/CLSID/LibModuleName)
  <storage>/EFSFileIndex  -> tabela de objetos (offset,size) dentro do EFSFileData
  <storage>/EFSFileData   -> objetos serializados (bloco base binario + propriedades nomeadas)
"""
import re, struct, hashlib
import olefile

ALPHA = "abcdefghijklmnopqrstuvwxyz012345"
NAME_RE = re.compile(r'^[A-Za-z_][A-Za-z0-9_.\[\]]{0,79}$')


def guid_to_storage(g16):
    v = int.from_bytes(g16, 'little')
    s = []
    for _ in range(26):
        s.append(ALPHA[v & 31]); v >>= 5
    return ''.join(s)


def fmt_guid(g16):
    a, b, c = struct.unpack('<IHH', g16[:8])
    return '{%08X-%04X-%04X-%s-%s}' % (a, b, c, g16[8:10].hex().upper(), g16[10:16].hex().upper())


class Node:
    __slots__ = ('name', 'guid', 'path', 'children', 'storage', 'objects', 'classes',
                 'rec_hash', 'rec_extra', 'has_data', 'data_size', 'tree_ok', 'is_stream', 'res_hash', 'loaded')

    def __init__(self, name, guid, path, storage):
        self.name = name; self.guid = guid; self.path = path; self.storage = storage
        self.children = []; self.objects = []; self.classes = []
        self.is_stream = False; self.res_hash = ''; self.loaded = False; self.tree_ok = True; self.rec_hash = ''; self.rec_extra = b''; self.has_data = False; self.data_size = 0


# --------------------------------------------------------------------------- valores
_FIXED = {0x02: 2, 0x03: 4, 0x04: 4, 0x05: 8, 0x07: 8, 0x0a: 4, 0x0b: 2, 0x10: 1, 0x11: 1,
          0x12: 2, 0x13: 4, 0x14: 8, 0x15: 8, 0x16: 4, 0x17: 4}
_FMT = {0x02: '<h', 0x03: '<i', 0x04: '<f', 0x05: '<d', 0x0a: '<I', 0x10: '<b', 0x11: '<B',
        0x12: '<H', 0x13: '<I', 0x14: '<q', 0x15: '<Q', 0x16: '<i', 0x17: '<I'}


def _read_value(b, p, vt, end):
    """devolve (valor, nova_pos) ou None."""
    if vt == 0x00: return (None, p)                  # VT_EMPTY: sem payload
    if vt == 0x01: return ('<Null>', p)              # VT_NULL: sem payload
    if vt == 0x08:
        if p + 4 > end: return None
        n = struct.unpack_from('<I', b, p)[0]
        if n > 4_000_000 or p + 4 + 2 * n > end: return None
        if n == 0: return ('', p + 4)
        raw = b[p + 4:p + 4 + 2 * n]
        return (raw.decode('utf-16le', 'replace').rstrip('\x00'), p + 4 + 2 * n)
    sz = _FIXED.get(vt)
    if sz is None or p + sz > end: return None
    raw = b[p:p + sz]
    if vt == 0x0b: return (bool(struct.unpack('<h', raw)[0]), p + sz)
    if vt == 0x07: return (struct.unpack('<d', raw)[0], p + sz)
    return (struct.unpack(_FMT[vt], raw)[0], p + sz)


def scan_props(b, start=0, end=None, spans=False):
    """Varre um buffer procurando registros [nchars][nome UTF16][vt u16][valor].
    Tolerante: bytes que nao casam sao ignorados (blocos binarios de geometria etc.)."""
    if end is None: end = len(b)
    out = []; i = start
    while i + 10 <= end:
        n = struct.unpack_from('<I', b, i)[0]
        if 2 <= n <= 80 and i + 4 + 2 * n + 2 <= end and b[i + 2 + 2 * n:i + 4 + 2 * n] == b'\x00\x00':
            raw = b[i + 4:i + 4 + 2 * n - 2]
            if all(raw[k] and not raw[k + 1] and 32 <= raw[k] < 127 for k in range(0, len(raw), 2)):
                nm = raw.decode('utf-16le')
                if NAME_RE.match(nm):
                    vt = struct.unpack_from('<H', b, i + 4 + 2 * n)[0]
                    r = _read_value(b, i + 6 + 2 * n, vt, end)
                    if r is not None:
                        out.append((nm, vt, r[0], i, r[1]) if spans else (nm, vt, r[0], i)); i = r[1]; continue
        i += 1
    return out


# --------------------------------------------------------------------------- projeto
class Project:
    def __init__(self, path):
        self.path = path
        self.ole = olefile.OleFileIO(path)     # path ou file-like (BytesIO)
        self._streams = {}
        for e in self.ole.listdir(streams=True, storages=True):
            self._streams[tuple(x.lstrip('\x03').lower() for x in e)] = e
        self.root = Node('<root>', '', '', ())

    # -- acesso
    def _real(self, key):
        return self._streams.get(tuple(k.lower() for k in key))

    def read_stream(self, storage_key, name):
        e = self._real(tuple(storage_key) + (name,))
        if e is None: return None
        return self.ole.openstream(e).read()

    # -- indice
    @staticmethod
    def parse_index(d):
        """lista de (nome, guid16, extra64) de um EFSIndex."""
        out = []
        if not d or len(d) < 48: return out
        for off in range(48, len(d) - 143, 144):
            nm = d[off:off + 64].decode('utf-16le', 'replace').split('\x00')[0]
            out.append((nm, d[off + 64:off + 80], d[off + 80:off + 144]))
        return out

    def build(self, load_objects=True):
        top = self.parse_index(self.read_stream((), 'EFSIndex'))
        for nm, g, ex in top:
            self._walk(self.root, nm, g, ex, (), load_objects)
        return self.root

    def _walk(self, parent, name, guid, extra, parent_key, load_objects):
        sto = guid_to_storage(guid)
        key = parent_key + (sto,)
        path = (parent.path + '/' + name) if parent.path else name
        n = Node(name, fmt_guid(guid), path, key)
        n.rec_extra = extra
        n.rec_hash = hashlib.sha1(extra).hexdigest()[:12]
        parent.children.append(n)
        real = self._real(key)
        if real is None:
            n.name = name + ' <storage ausente>'
            return n
        if self.ole.get_type(real) == olefile.STGTY_STREAM:      # recurso (imagem, som...) = stream direto
            raw = self.ole.openstream(real).read()
            n.is_stream = True; n.data_size = len(raw); n.res_hash = hashlib.sha1(raw).hexdigest()
            return n
        n.has_data = self._real(key + ('EFSFileData',)) is not None
        if n.has_data:
            n.data_size = self.ole.get_size(self._real(key + ('EFSFileData',)))
            if load_objects: self._load_objects(n)
        for cn, cg, cex in self.parse_index(self.read_stream(key, 'EFSIndex')):
            self._walk(n, cn, cg, cex, key, load_objects)
        return n

    def _load_objects(self, n):
        key = n.storage
        lib = self.read_stream(key, 'EFSFileLib') or b''
        idx = self.read_stream(key, 'EFSFileIndex') or b''
        dat = self.read_stream(key, 'EFSFileData') or b''
        n.has_data = True; n.data_size = len(dat); n.loaded = True
        # classes
        cls = {}
        for nm, vt, val, _ in scan_props(lib):
            m = re.match(r'Class(\d+)(\w+)$', nm)
            if m: cls.setdefault(int(m.group(1)), {})[m.group(2)] = val
        n.classes = [cls[k] for k in sorted(cls)]
        # tabela de objetos: registro de 40 bytes a partir do byte 16:
        #   +0 GUID do objeto (zeros p/ componentes) | +16 tipo (-1 = componente: AgScript/AgSimple/TableBind...)
        #   +20 indice da classe | +24 offset | +28 tamanho | +32 n componentes anexados | +36 n filhos
        cnt = max(0, (len(idx) - 16) // 40)
        for i in range(cnt):
            base = 16 + 40 * i
            if base + 40 > len(idx): break
            g = idx[base:base + 16]
            kind, cidx, off, size, ncomp, nchild = struct.unpack_from('<iIIIII', idx, base + 16)
            if off + size > len(dat): continue
            blob = dat[off:off + size]
            cidx = cidx if cidx < len(n.classes) else -1
            cname = n.classes[cidx].get('Name', '?') if cidx >= 0 else '?'
            props = scan_props(blob, 4)
            nm = next((v for a, vt, v, _ in props if a == 'Name' and isinstance(v, str)), '')
            n.objects.append({'idx': i, 'class_idx': cidx, 'class': cname, 'kind': kind,
                              'guid': fmt_guid(g) if any(g) else '', 'name': nm,
                              'offset': off, 'size': size, 'nchild': nchild, 'ncomp': ncomp,
                              'sha1': hashlib.sha1(blob).hexdigest()[:16], 'props': props})
        self._link_objects(n)

    @staticmethod
    def _link_objects(n):
        """reconstroi a hierarquia (pre-ordem + contagem de filhos); componentes (kind=-1) pertencem
        ao ultimo objeto 'real'. Preenche o['path'] e o['owner'] ; n.tree_ok indica consistencia."""
        stack = []          # [obj, filhos_restantes]
        last = None
        ok = True
        for o in n.objects:
            if o['kind'] == -1:
                o['owner'] = last['idx'] if last else -1
                o['depth'] = (len(stack) if last else 0)
                o['opath'] = (last['opath'] if last else '') + '|' + o['class']
                continue
            while stack and stack[-1][1] == 0: stack.pop()
            parent = stack[-1][0] if stack else None
            if stack: stack[-1][1] -= 1
            elif last is not None: ok = False
            o['owner'] = parent['idx'] if parent else -1
            o['depth'] = len(stack)
            nm = o['name'] or ('<%s#%d>' % (o['class'], o['idx']))
            o['opath'] = ((parent['opath'] + '/') if parent else '') + nm
            stack.append([o, o['nchild']])
            last = o
        if any(s[1] for s in stack): ok = False
        n.tree_ok = ok

    def load_node(self, n):
        """carrega (parse) os objetos de um no sob demanda."""
        if n.has_data and not n.loaded:
            self._load_objects(n)
        return n

    @staticmethod
    def free_node(n):
        n.objects = []; n.classes = []; n.loaded = False

    def first_class(self, n):
        """nome da classe do 1o objeto do no, sem parsear o EFSFileData (barato)."""
        if not n.has_data: return ''
        lib = self.read_stream(n.storage, 'EFSFileLib') or b''
        idx = self.read_stream(n.storage, 'EFSFileIndex') or b''
        if len(idx) < 56: return ''
        cidx = struct.unpack_from('<I', idx, 16 + 20)[0]
        cls = {}
        for nm, vt, val, _ in scan_props(lib):
            m = re.match(r'Class(\d+)Name$', nm)
            if m: cls[int(m.group(1))] = val
        return cls.get(cidx, '?')

    def digest(self, n):
        """sha1 dos 3 streams de dados do no (sem parse) - deteccao rapida de no alterado."""
        if n.is_stream: return n.res_hash
        if not n.has_data: return ''
        h = hashlib.sha1()
        for nm in ('EFSFileLib', 'EFSFileIndex', 'EFSFileData'):
            h.update(self.read_stream(n.storage, nm) or b'')
        return h.hexdigest()

    def walk(self, node=None):
        node = node or self.root
        for c in node.children:
            yield c
            yield from self.walk(c)


OLE_MAGIC = bytes([0xd0, 0xcf, 0x11, 0xe0, 0xa1, 0xb1, 0x1a, 0xe1])


def embedded_objects(blob):
    """Algumas propriedades (ex.: XCoClass.Methods) guardam um OLE2 inteiro dentro do valor.
    Devolve (classes, objetos) desse container interno, ou None."""
    import io
    i = blob.find(OLE_MAGIC)
    if i < 0: return None
    p = Project(io.BytesIO(blob[i:]))
    leaf = Node('<embutido>', '', '<embutido>', ())
    leaf.has_data = True
    p._load_objects(leaf)
    return leaf
