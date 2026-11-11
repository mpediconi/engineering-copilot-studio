# Analisador E3 — modelo de objetos (propriedades + hierarquia)

Fase atual: **modelar o esquema** dos objetos E3 — todas as propriedades existentes e a estrutura hierárquica.
Sem valores atuais, sem associações, sem links.

| Entrega (`patterns/`) | Conteúdo | Gerador |
|---|---|---|
| `E3_Pattern.md/.json` | 178 classes nativas: propriedades (type lib + base gráfica X/Y/Width/Height/Angle + nomes gravados), métodos, eventos, enums | `gerar_pattern_nativo.py` |
| `XFolder.md`, `XControl.md`, `XObject.md` | 68 / 127 / 30 classes das libs Matrix: propriedades base herdadas + próprias (`XMethod`), estrutura interna | `gerar_pattern_libs.py` |
| `HIERARQUIA.md/.json` | pastas → nós → objetos → filhos; componentes anexados | `gerar_hierarquia.py` |
| `modelo.json` | agregados coletados dos 29 `.prj` + 10 `.lib` (nomes de propriedades, tipos, relações pai→filho) | `coletar_modelo.py` |

Fontes: type libs do E3 instalado, `.lib` de `..\02_Libraries`, projetos Main/GC/Substations/GD.
`e3reader.py` = leitor do formato `.prj`/`.lib` (OLE2 + EFS). `e3base.py` = propriedades base herdadas por XFolder/XObject/XControl.

## Geometria dos objetos de tela
Cabeçalho nomeado de 146 bytes (`Tip, Angle, Layer, Visible, Enabled, TabStop`) + 1 byte + **4 doubles `x1,y1,x2,y2`**:
`X=x1`, `Y=y1`, `Width=x2−x1`, `Height=y2−y1`; `Angle` = propriedade nomeada. Ver `E3_Pattern.md`.

## Enriquecimento com os manuais e apelidos de propriedade
`E3_Pattern.md` usa a referência de objetos do repositório de manuais (descrição, **valor padrão**, somente leitura; ⚠ = type lib e manual divergem no acesso).
Nomes gravados no `.prj` que diferem dos da type lib (apelidos) são pareados automaticamente (`gerar_pattern_nativo.py`), verificados com evidências do manual e dos projetos
(`verificar_apelidos.py` → `patterns/APELIDOS_INFERIDOS.md`, `apelidos_decisao.json`) e ajustados por curadoria (`patterns/apelidos_curadoria.json`).
Ordem: `gerar_pattern_nativo.py` → `verificar_apelidos.py` → `gerar_pattern_nativo.py`.

## Regenerar (nesta ordem)
```powershell
pip install olefile pywin32
python coletar_modelo.py          # ~3 min (lê os .prj e .lib)
python gerar_pattern_nativo.py
python gerar_pattern_libs.py
python gerar_hierarquia.py
```
Obs.: a seção 5 de `HIERARQUIA.md` usa `legado/fase2_3_valores_fichas/analise/ufv_gsii.estrutura.json` (árvore real do projeto modelo).
`legado/` guarda as fases anteriores (comparador antigo, estrutura, fichas com valores) apenas como referência.

## Repositório de manuais (`repositorio_manuais/`)
Os 8 manuais oficiais do E3 (Reference and Scripts, User's Manual, Tutorial Developer, Minicourse, Release Notes, Tweak, Event Log, IOKit)
convertidos em texto por seção, com índices pesquisáveis. Comece por `repositorio_manuais/GUIA_DE_CONSULTA.md` e `MAPA_TOPICOS.md`;
`REFERENCIA_OBJETOS.md` traz propriedades/métodos/eventos de 179 objetos (com padrão e somente leitura); `python buscar.py "termo"` consulta tudo.

## Comparador de projetos (`comparar.py`) — de → para
Compara dois projetos do mesmo ativo e informa, por objeto, **o que estava no antigo e foi alterado no novo**:
```
Projeto novo sofreu alterações:
### Tela SE
- Objeto SE/equipChave2 (cEquipChave0se)
  - Y: de 6815.48 para 7987.98
```
```powershell
python comparar.py ANTIGO.prj NOVO.prj [-o logs] [--cm]
python comparar.py --lote ..\temp-backups\04_Projects .. -o logs      # todos os .prj de Main, GC, Substations e GD
```
* Alinha objetos por **GUID** (sobrevive a renomear), depois por caminho; objetos recriados em outro caminho são pareados por classe + nome e reportados como **movidos**.
* Compara propriedades nomeadas (booleanos/enums/cores formatados pela type lib), **X/Y/Width/Height** (Himetric, 1000 = 1 cm) e `Angle`, associações, scripts (linhas diferentes) e versão das libs de classe.
* Campos binários ainda **não identificados** (cores, estilos…) saem como `campo binário @offset: de … para …`.
* Cada relatório traz horário da análise, horário de geração do log e a quantidade de itens alterados; `.json` com os mesmos dados. `logs/RESUMO_LOTE.md` consolida o lote.
* **Excel (.xlsx):** cada comparação gera também um `.xlsx` com as abas **Adicionado**, **Removido** e **Modificado** (colunas: Projeto, Tipo de nó, Nó, Objeto, Classe e, em Modificado, Tipo de alteração, Propriedade, De, Para, Detalhe). No lote, `logs/comparacao_LOTE_*.xlsx` consolida todos os projetos. Para gerar de logs já existentes: `python comparar.py --xlsx-de-logs logs`.
* **Campos binários:** o leitor agora decodifica propriedades `Empty`/`Null` (antes ignoradas) e os **pontos** de `DrawLine`/`DrawBezier`/`DrawConnector` (`Ponto n X/Y`); `TimeStamp` Empty/Null/0 é tratado como equivalente. Em 19 comparações reais, os campos binários não identificados caíram de 68 para 4 (valores derivados de `cObjElectricConnection0se` e 1 em `IODriver`).
* **Calibração de propriedades visuais dos `Draw*`** (cores, estilos): `calibrar_dados.py` casa as exportações CSV do E3 Studio (`06_CSV`) com os blobs e `calibrar_layout.py` procura offsets; ainda faltam exportações completas de telas (clique direito no objeto → *Export*, sem template) para concluir.

## Retorno visual (PowerShell): `E3_Comparador_Visual.ps1`
Janela com as abas **Adicionado**, **Removido** e **Modificado** (filtros por projeto, tipo de alteração e busca; painel de detalhe; botões para comparar A × B, comparar lote, abrir o Excel e a pasta de logs).
Lê `logs\comparacao_*.json` (último de cada projeto). `-Modo Console` imprime o resumo em texto.
```powershell
powershell -ExecutionPolicy Bypass -File .\E3_Comparador_Visual.ps1
```
* Testes do visualizador sem diálogos: `-TesteAB antigo.prj,novo.prj` e `-TesteLote pasta_antiga,pasta_nova` (+ `-PastaLogs`) executam o mesmo código dos botões e imprimem o resultado carregado.
* **Bibliotecas (.lib):** `comparar.py` e o visualizador aceitam `.lib` (A × B e lote com `--ext lib`). O comparador abre o container `XCoClass.Methods` e compara os **membros da classe** (propriedades/métodos: tipo, padrão, ajuda…) e seus **scripts** (`Membro <nome>: Script <evento>`), além dos scripts de evento do objeto raiz.
* **Desempenho do visual:** cada aba mostra no máximo as **100 primeiras linhas** (título "top 100 de N"), respeitando filtros e busca; os totais contam tudo e o Excel/logs são completos. Busca com atraso de 450 ms.
