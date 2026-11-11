# -*- coding: utf-8 -*-
"""
e3base - propriedades BASE (herdadas) dos objetos XFolder / XObject / XControl e categorias da ficha de instancia.

Fontes:
  * nomes/tipos/descricoes: type library (classe ExtArea em Panel/E3Sys) - ver patterns/E3_Pattern.md
  * nome gravado no .prj x nome da type lib: observado nos .prj (ex.: AreaIsArea = IsAlarmArea)
  * CATEGORIAS (Alarme / Diversos / Identificacao ...): PROVISORIAS - reproduzem o exemplo da grade do E3 Studio
    informado pelo usuario; nao existem na type lib nem nos arquivos. Ajustar em CATEGORIA_* se necessario.

origem:  'gravada'  -> existe no .prj (so e gravada quando difere do padrao)
         'derivada' -> calculada em tempo de execucao pelo E3 (nao esta no .prj); aqui reconstruida da arvore (HIPOTESE)
"""
import re

CAT_ID, CAT_ALARME, CAT_DIV, CAT_GRAFICO = 'Identificação', 'Alarme', 'Diversos', 'Aparência / Gráfico'

# (nome_typelib, nome_gravado ou None, categoria, origem, tipo, aplica a, descricao)
BASE = [
    ('Name', 'Name', CAT_ID, 'gravada', 'String', ('XFolder', 'XObject', 'XControl'), 'Nome do objeto'),
    ('DocString', 'DocString', CAT_ID, 'gravada', 'String', ('XFolder', 'XObject', 'XControl'), 'Texto de documentação do objeto'),
    ('PathName', None, CAT_ID, 'derivada', 'String', ('XFolder', 'XObject', 'XControl'), 'Caminho completo do objeto (ex.: Usinas.UFV_CSA.BD.UFV_CSA.SE01)'),
    ('PathVolume', None, CAT_ID, 'derivada', 'String', ('XFolder', 'XObject', 'XControl'), 'Arquivo do volume (.PRJ/.LIB) onde o objeto está armazenado'),
    ('PathContainer', None, CAT_ID, 'derivada', 'String', ('XFolder', 'XObject', 'XControl'), 'Nome completo da pasta/unidade que contém o objeto'),
    ('IsAlarmArea', 'AreaIsArea', CAT_ALARME, 'gravada', 'Boolean', ('XFolder', 'XObject'), 'Verdadeiro se o objeto tem comportamento de Área de Alarme'),
    ('AlarmVerify', 'AreaAlarmVerify', CAT_ALARME, 'gravada', 'Boolean', ('XFolder', 'XObject'), 'Habilita/desabilita a verificação de alarmes da área'),
    ('UserFields.Count', 'AreaUserFieldsCount', CAT_ALARME, 'gravada', 'Long', ('XFolder', 'XObject'), 'Quantidade de campos de usuário da área de alarme'),
    ('UserFields.Link#.Name', 'AreaUserFieldLink#.Name', CAT_ALARME, 'gravada', 'String', ('XFolder', 'XObject'), 'Nome do campo de usuário # (família numerada)'),
    ('UserFields.IsValueForced#', 'AreaUserFieldIsValueForced#', CAT_ALARME, 'gravada', 'Boolean', ('XFolder', 'XObject'), 'Valor do campo de usuário # é forçado'),
    ('UserFields.Value#', 'AreaUserFieldValue#', CAT_ALARME, 'gravada', 'Variant', ('XFolder', 'XObject'), 'Valor forçado do campo de usuário #'),
    ('X', None, CAT_GRAFICO, 'binária', 'Double', ('XControl',), 'Posição horizontal = x1 do retângulo gravado após o cabeçalho'),
    ('Y', None, CAT_GRAFICO, 'binária', 'Double', ('XControl',), 'Posição vertical = y1 do retângulo'),
    ('Width', None, CAT_GRAFICO, 'binária', 'Double', ('XControl',), 'Largura = x2 − x1'),
    ('Height', None, CAT_GRAFICO, 'binária', 'Double', ('XControl',), 'Altura = y2 − y1'),
    ('Tip', 'Tip', CAT_GRAFICO, 'gravada', 'String', ('XControl',), 'Dica (tooltip) do objeto gráfico'),
    ('Angle', 'Angle', CAT_GRAFICO, 'gravada', 'Long', ('XControl',), 'Ângulo de rotação'),
    ('Layer', 'Layer', CAT_GRAFICO, 'gravada', 'Long', ('XControl',), 'Camada (0xFFFFFFFF = todas)'),
    ('Visible', 'Visible', CAT_GRAFICO, 'gravada', 'Boolean', ('XControl',), 'Objeto visível'),
    ('Enabled', 'Enabled', CAT_GRAFICO, 'gravada', 'Boolean', ('XControl',), 'Objeto habilitado'),
    ('TabStop', 'TabStop', CAT_GRAFICO, 'gravada', 'Boolean', ('XControl',), 'Participa da ordem de tabulação'),
]
# valor padrao assumido quando a propriedade base nao esta gravada (None = nao determinado)
PADRAO_BASE = {'Name': '', 'DocString': '', 'Tip': '', 'Angle': 0, 'Layer': 4294967295, 'Visible': True, 'Enabled': True, 'TabStop': False,
               'UserFields.Count': 0}

GRAVADO_PARA_BASE = {}
for nome, grav, cat, org, tipo, ap, desc in BASE:
    if grav: GRAVADO_PARA_BASE[re.sub(r'#', r'\\d+', re.escape(grav).replace(r'\#', '#'))] = (nome, cat, tipo)


def base_de(nome_gravado):
    """-> (nome_typelib, categoria, tipo) se for propriedade base gravada, senao None."""
    for pad, v in GRAVADO_PARA_BASE.items():
        if re.fullmatch(pad, nome_gravado): return v
    if re.fullmatch(r'(_Event\d+\..+|_EventCount|_Layer\d+\..+|_LayerCount|_NewLayerZoom|Inherit\d+|Expose)', nome_gravado):
        return (nome_gravado, 'Framework (eventos/camadas)', '')
    return None


def tabela_base(tipo_classe):
    return [b for b in BASE if tipo_classe in b[5]]


def fmt_valor(v, tipo=''):
    """formata como a grade do E3: Empty, True/False, numero."""
    if v is None: return 'Empty'
    if isinstance(v, bool): return 'True' if v else 'False'
    if tipo == 'Boolean' and isinstance(v, (int, float)): return 'True' if v else 'False'
    if isinstance(v, str): return v if v != '' else 'Empty'
    if isinstance(v, float): return ('%g' % v)
    return str(v)
