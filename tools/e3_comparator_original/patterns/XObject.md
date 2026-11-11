# XObject — classes das bibliotecas Matrix Energy e suas propriedades

Fonte: arquivos `.lib` em `C:\SCADA_Eng01\01_MatrixEnergy\02_Libraries`. **30 classes**, **299 propriedades/métodos próprios**.

XObject = **objeto de dados/cálculo** com tags e propriedades próprias (prefixo `o`).

Formato de cada item: metadados da classe (`_CLSID`, `_IID`, `IconPath`…) → propriedades próprias (`XMethod`: tipo, padrão, flags) → tags internas → estrutura interna → associações → scripts → elementos gráficos.

## Propriedades base (herdadas por todas as classes XObject)

Valem para toda classe deste tipo, além das próprias (tabela de cada classe). "Gravado como" = nome no `.prj`; **derivada** = não existe no arquivo, é calculada pelo E3 em tempo de execução. Categorias provisórias (ver `e3base.py`).

| Categoria | Propriedade | Gravado como | Origem | Tipo | Descrição |
|---|---|---|---|---|---|
| Alarme | `AlarmVerify` | `AreaAlarmVerify` | gravada | Boolean | Habilita/desabilita a verificação de alarmes da área |
| Alarme | `IsAlarmArea` | `AreaIsArea` | gravada | Boolean | Verdadeiro se o objeto tem comportamento de Área de Alarme |
| Alarme | `UserFields.Count` | `AreaUserFieldsCount` | gravada | Long | Quantidade de campos de usuário da área de alarme |
| Alarme | `UserFields.IsValueForced#` | `AreaUserFieldIsValueForced#` | gravada | Boolean | Valor do campo de usuário # é forçado |
| Alarme | `UserFields.Link#.Name` | `AreaUserFieldLink#.Name` | gravada | String | Nome do campo de usuário # (família numerada) |
| Alarme | `UserFields.Value#` | `AreaUserFieldValue#` | gravada | Variant | Valor forçado do campo de usuário # |
| Identificação | `DocString` | `DocString` | gravada | String | Texto de documentação do objeto |
| Identificação | `Name` | `Name` | gravada | String | Nome do objeto |
| Identificação | `PathContainer` | — | derivada | String | Nome completo da pasta/unidade que contém o objeto |
| Identificação | `PathName` | — | derivada | String | Caminho completo do objeto (ex.: Usinas.UFV_CSA.BD.UFV_CSA.SE01) |
| Identificação | `PathVolume` | — | derivada | String | Arquivo do volume (.PRJ/.LIB) onde o objeto está armazenado |

## Índice

| Biblioteca | Classes |
|---|---|
| `matrixenergylibxobjectbtc.lib` | [oMineradorBtc](#omineradorbtc), [oDadosAtivoBtc](#odadosativobtc), [oDadosContainerBtc](#odadoscontainerbtc), [oConfigCardBtc](#oconfigcardbtc) |
| `matrixenergylibxobjectpv.lib` | [oConfigHeader](#oconfigheader), [oConfigNavegacaoScreens](#oconfignavegacaoscreens), [oDashConfigCardGeralUsinas](#odashconfigcardgeralusinas), [oDashConfigGauge](#odashconfiggauge), [oCfgObjGraph](#ocfgobjgraph), [oQueryPerformanceSQL](#oqueryperformancesql), [oAddDemoTag](#oadddemotag), [oAddTimeStampAlarm](#oaddtimestampalarm), [oTempScripts](#otempscripts), [oCalcSum](#ocalcsum), [oMedidaDigitalCalculada](#omedidadigitalcalculada), [oCalcResumoInversores](#ocalcresumoinversores), [oSimulateIOTag](#osimulateiotag), [oMedidaAnalogicaCalculada](#omedidaanalogicacalculada), [oNotaOperativa](#onotaoperativa), [oMedidaDigitalBit](#omedidadigitalbit), [oMonitorCorrenteStrings](#omonitorcorrentestrings), [oStatusTrackers](#ostatustrackers), [oCalcBitDec](#ocalcbitdec), [temp](#temp) |
| `matrixenergylibxobjectse.lib` | [oConfigHeader0se](#oconfigheader0se), [oConfigNavegacaoScreens0se](#oconfignavegacaoscreens0se), [oDashConfigCardGeralUsinas0se](#odashconfigcardgeralusinas0se), [oDashConfigGauge0se](#odashconfiggauge0se), [oMedidaDigitalCalculada0se](#omedidadigitalcalculada0se), [oMedidaAnalogicaCalculada0se](#omedidaanalogicacalculada0se) |

---

## Biblioteca `matrixenergylibxobjectbtc.lib`

<a id="omineradorbtc"></a>
### oMineradorBtc

- Biblioteca: `matrixenergylibxobjectbtc.lib`  ·  tipo: **XObject**  ·  Dados dos Miners de BTC; Consulta dos dados em JSON
- Metadados: `_CLSID` = {AEF66F34-FB08-4994-8CFB-1B357B63134A} · `_IID` = {99AB27D7-A2F5-4E4C-A6A0-418B89A3FD38} · `_EVENTIID` = {363A132B-F490-4A24-981D-6A4AC5A59D4B} · `IconPath` = imgMiner · `InstanceName` = MINER0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `DB.e3`, `Panel.e3`
- Classes que usa internamente: `TimerTag`, `DiscreteAlarmSource`, `DiscreteAlarm`, `TableBind`

**Propriedades / métodos próprios (10)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgUpdateOrder` | Integer |  | S | S |  |  | Configura a ordem de update. |  |
| 2 | `cfgMinerId` | Variant |  | S | S | S |  |  |  |
| 3 | `cfgMinerName` | Variant |  | S | S | S |  |  |  |
| 4 | `cfgMinerIP` | Variant |  | S | S | S |  |  |  |
| 5 | `disStatus` | Variant |  | S | S | S |  |  |  |
| 6 | `disActive` | Variant |  | S | S | S |  |  |  |
| 7 | `anlMinerHashRate` | Variant |  | S | S | S |  |  |  |
| 8 | `anlTimeStamp` | Variant |  | S | S | S |  |  |  |
| 9 | `disTriggerUpdate` | Boolean | Boolean `False` | S | S |  |  |  |  |
| 10 | `cfgNominalHashRate` | Variant |  | S | S |  |  |  |  |

**Tags internas (7):** `updateValues` (TimerTag), `MaxHashRate`, `MinHashRate`, `HashRate`, `Effic`, `statusResumido`, `StatusCom`

**Estrutura interna (classe ×qtd):**

```
TimerTag ×1 (updateValues)
InternalTag ×6 (MaxHashRate, MinHashRate, HashRate, …)
```

**Eventos com script:** `oMineradorBtc.CustomConfig` (125 linhas), `updateValues.OnPreset` (123 linhas)

<a id="odadosativobtc"></a>
### oDadosAtivoBtc

- Biblioteca: `matrixenergylibxobjectbtc.lib`  ·  tipo: **XObject**  ·  Dados das Plantas de BTC; Consulta dos dados em JSON
- Metadados: `_CLSID` = {60B0ED0A-2663-477B-AAF2-C2E54C07C2B2} · `_IID` = {51FFDD38-D615-4959-A466-CAD46BDD3817} · `_EVENTIID` = {7ECA9C1A-90FB-4C21-A46C-DE22E8C7C6B9} · `IconPath` = imgBTC · `InstanceName` = btcPlantData0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`
- Classes que usa internamente: `TimerTag`, `TableBind`

**Propriedades / métodos próprios (19)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgClientId` | Variant |  | S | S | S |  |  |  |
| 2 | `cfgGroupId` | Variant |  | S | S | S |  |  |  |
| 3 | `cfgPlantName` | Variant |  | S | S |  |  |  |  |
| 4 | `anlTimeStamp` | Variant |  | S | S | S |  | TimeStamp da consulta ao JSON |  |
| 5 | `anlPlantHashRate` | Variant |  | S | S | S |  |  |  |
| 6 | `anlPowerDraw` | Variant |  | S | S |  |  |  |  |
| 7 | `anlMinersTotal` | Variant |  | S | S |  |  |  |  |
| 8 | `anlMinersOnline` | Variant |  | S | S |  |  |  |  |
| 9 | `anlMinersOffline` | Variant |  | S | S |  |  |  |  |
| 10 | `anlMinersPending` | Variant |  | S | S |  |  |  |  |
| 11 | `anlMinersDisabled` | Variant |  | S | S |  |  |  |  |
| 12 | `anlMinersHashing` | Variant |  | S | S |  |  |  |  |
| 13 | `anlMinersSleeping` | Variant |  | S | S |  |  |  |  |
| 14 | `anlMinersDeployed` | Variant |  | S | S |  |  |  |  |
| 15 | `anlMinersInRepair` | Variant |  | S | S |  |  |  |  |
| 16 | `anlMinersRetired` | Variant |  | S | S |  |  |  |  |
| 17 | `cfgNominalHashRate` | Variant |  | S | S |  |  |  |  |
| 18 | `disTriggerUpdate` | Boolean | Boolean `True` | S | S |  |  |  |  |
| 19 | `cfgNominalPower` | Variant |  | S | S |  |  |  |  |

**Tags internas (5):** `updateValues` (TimerTag), `HashRate`, `Effic`, `PowerDraw`, `StatusCom`

**Estrutura interna (classe ×qtd):**

```
TimerTag ×1 (updateValues)
InternalTag ×4 (HashRate, Effic, PowerDraw, …)
```

**Eventos com script:** `oDadosAtivoBtc.CustomConfig` (188 linhas), `updateValues.OnPreset` (191 linhas)

<a id="odadoscontainerbtc"></a>
### oDadosContainerBtc

- Biblioteca: `matrixenergylibxobjectbtc.lib`  ·  tipo: **XObject**  ·  Dados dos Contêineres de BTC; Consulta dos dados em JSON
- Metadados: `_CLSID` = {EAAEAA41-A668-4278-8696-429821AAD7D4} · `_IID` = {88AD9C15-7866-4423-A367-B54058F7CBB2} · `_EVENTIID` = {57B621C1-1DE2-4D25-8616-5C2FB645C405} · `IconPath` = imgContainerMiner · `InstanceName` = ContainerData0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`
- Classes que usa internamente: `TimerTag`, `TableBind`

**Propriedades / métodos próprios (20)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `anlTimeStamp` | Variant |  | S | S | S |  |  |  |
| 2 | `disTriggerUpdate` | Boolean | Boolean `True` | S | S |  |  |  |  |
| 3 | `cfgNominalHashRate` | Variant |  | S | S |  |  |  |  |
| 4 | `anlMinersHashing` | Variant |  | S | S |  |  |  |  |
| 5 | `anlMinersOnline` | Variant |  | S | S |  |  |  |  |
| 6 | `anlMinersTotal` | Variant |  | S | S |  |  |  |  |
| 7 | `anlAverageHashRate` | Variant |  | S | S |  |  |  |  |
| 8 | `anlTotalHashRate` | Variant |  | S | S |  |  |  |  |
| 9 | `cfgModel` | Variant |  | S | S |  |  |  |  |
| 10 | `cfgContainerGroup` | Variant |  | S | S |  |  |  |  |
| 11 | `cfgContainerModel` | Variant |  | S | S |  |  |  |  |
| 12 | `cfgBatchSize` | Integer |  | S | S |  |  |  |  |
| 13 | `cfgUpdateIntervalMs` | Integer |  | S | S |  |  |  |  |
| 14 | `anlCurrentIndex` | Variant |  | S | S |  |  |  |  |
| 15 | `anlCiclyeId` | Variant |  | S | S |  |  |  |  |
| 16 | `anlUpdatedCount` | Variant |  | S | S |  |  |  |  |
| 17 | `anlErrorCount` | Variant |  | S | S |  |  |  |  |
| 18 | `disUpdateState` | Variant |  | S | S |  |  |  |  |
| 19 | `disLastSnapshot` | Variant |  | S | S |  |  |  |  |
| 20 | `disLasterror` | Variant |  | S | S |  |  |  |  |

**Tags internas (9):** `updateValues` (TimerTag), `HashRate`, `Effic`, `statusResumido`, `StatusCom`, `AverageHashRate`, `totalMiners`, `totalMinersOnline`, `totalMinersHashing`

**Estrutura interna (classe ×qtd):**

```
TimerTag ×1 (updateValues)
InternalTag ×8 (HashRate, Effic, statusResumido, …)
```

**Eventos com script:** `oDadosContainerBtc.CustomConfig` (197 linhas), `updateValues.OnPreset` (197 linhas)

<a id="oconfigcardbtc"></a>
### oConfigCardBtc

- Biblioteca: `matrixenergylibxobjectbtc.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {37F5AF5F-EE0B-4FA1-BD9D-C3821A07D8BD} · `_IID` = {9E7B5271-57D6-4465-94DF-DD8AFA1AD8E6} · `_EVENTIID` = {AE44EA5F-C898-4DE7-95C6-53EF60CF72B6} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fAtivoBTC |  | S | S |  |  |  |  |
| 2 | `linkScreen` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 3 | `linkGaugeB` | oDashConfigGauge |  | S | S |  |  |  |  |
| 4 | `linkStatusComGTW01` | IOTag |  | S | S |  |  |  |  |
| 5 | `linkStatusComGTW02` | IOTag |  | S | S |  |  |  |  |

**Tags internas (15):** `cfgPlantName`, `PowerDraw`, `disActiveAlarms`, `TagInterno4`, `TagInterno5`, `TagInterno6`, `TagInterno7`, `TagInterno8`, `TagInterno9`, `anlTimeStamp`, `anlMinersTotal`, `anlMinersOnline`, `cfgNominalHashRate`, `HashRate`, `statusCom`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×15 (cfgPlantName, PowerDraw, disActiveAlarms, …)
```

---

## Biblioteca `matrixenergylibxobjectpv.lib`

<a id="oconfigheader"></a>
### oConfigHeader

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {A7ECA9A0-DB4F-4647-A16B-AA60D75728FA} · `_IID` = {88DDFC87-9367-4BB8-81F6-869DC5D24E16} · `_EVENTIID` = {4C609D83-26A8-473D-A666-D62CC46025DB} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (9)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `botao01` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 2 | `botao02` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 3 | `botao03` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 4 | `botao04` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 5 | `botao05` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 6 | `botao06` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 7 | `botao07` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 8 | `botao08` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 9 | `cfgFrameType` | Integer | Integer `2` | S | S |  |  | Frame a ser aberto: 0 -> Main Frame \| 1 -> Plant Frame \| 2-> Focus Frame |  |

<a id="oconfignavegacaoscreens"></a>
### oConfigNavegacaoScreens

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {7FCC725F-1752-4E3A-A45E-B40286DA07C9} · `_IID` = {0802DEF6-834B-46D6-954E-C0F207733AD8} · `_EVENTIID` = {C597F798-CC7C-4446-904A-B77AE9AF7287} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (6)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `NomeTela` | Variant |  | S | S |  |  | Caption Tela |  |
| 2 | `cfgIdAtivo` | Variant |  | S | S |  |  | Name Tela |  |
| 3 | `Path` | Variant |  | S | S |  |  | PathContainer Tela |  |
| 4 | `PathPainelLateral` | Variant |  | S | S |  |  | PathContainer Tela |  |
| 5 | `PathHeader` | Variant |  | S | S |  |  | PathContainer Tela |  |
| 6 | `FiltroAlarmes` | Variant |  | S | S |  |  | Inserir o Filtro de Alarmes |  |

<a id="odashconfigcardgeralusinas"></a>
### oDashConfigCardGeralUsinas

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {7B1B19BD-98ED-4848-8781-2A9717C1D4CD} · `_IID` = {FD9046A5-765E-44FA-9F7A-F4413DAD9CF5} · `_EVENTIID` = {76E6413C-F5B2-4BE8-B609-AF73A3D816C1} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (12)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `UFV` | Variant |  | S | S |  |  |  |  |
| 2 | `linkScreen` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |
| 3 | `ConfigGaugeA` | oDashConfigGauge |  | S | S |  |  |  |  |
| 4 | `ConfigGaugeB` | oDashConfigGauge |  | S | S |  |  |  |  |
| 5 | `anlGHI` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 6 | `anlFatorPotencia` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 7 | `anlTensaoAtual` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 8 | `linkStatusComGTW01` | IOTag |  | S | S |  |  |  |  |
| 9 | `linkStatusComGTW02` | IOTag |  | S | S |  |  |  |  |
| 10 | `bdUFV` | fUsinaPV |  | S | S |  |  |  |  |
| 11 | `cfgTensaoNominal` | Variant |  | S | S |  |  |  |  |
| 12 | `linkAlarms` | Variant |  | S |  |  |  |  |  |

**Tags internas (3):** `statusCom`, `activeAlarms`, `fatorCapacidade`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×3 (statusCom, activeAlarms, fatorCapacidade)
```

**Eventos com script:** `oDashConfigCardGeralUsinas.CustomConfig` (11 linhas)

<a id="odashconfiggauge"></a>
### oDashConfigGauge

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {8EE13D71-5002-4FA6-B6D2-DA7B46F86304} · `_IID` = {99B885D3-EFBC-4383-8F7D-DD3D9DC3E761} · `_EVENTIID` = {BED9ED76-3E96-4FCF-A19A-B8F4EEFC7D53} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `NomeGrafico` | Variant |  | S | S |  |  |  |  |
| 2 | `ValorMaximo` | Variant |  | S | S |  |  |  |  |
| 3 | `ValorAtual` | Variant |  | S | S |  |  |  |  |
| 4 | `ValorAlvo` | Variant |  | S | S |  |  |  |  |
| 5 | `UnidadeMedida` | Variant |  | S | S |  |  |  |  |

**Tags internas (1):** `ValorFiltrado`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×1 (ValorFiltrado)
```

<a id="ocfgobjgraph"></a>
### oCfgObjGraph

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {5DAE4C36-AC19-462E-93C6-6529E822D4BC} · `_IID` = {1A4C20E4-97C2-4E93-A9AA-10B145D055E7} · `_EVENTIID` = {FAC57434-9A02-4805-B67D-367DDD9BFF38} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgPen01Path` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 2 | `cfgPen02Path` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 3 | `cfgMaxLimit` | Double |  | S | S |  |  |  |  |
| 4 | `cfgMinLimit` | Double |  | S | S |  |  |  |  |

<a id="oqueryperformancesql"></a>
### oQueryPerformanceSQL

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {F9E5BDAF-464F-4FAD-AA7D-1CFEB5EEF614} · `_IID` = {A9608067-E717-43E6-AE65-4880A72C262A} · `_EVENTIID` = {96ED7227-A552-4B30-88C0-6DB267F6FA8D} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`
- Classes que usa internamente: `TimerTag`

**Propriedades / métodos próprios (16)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `runQuery` | Boolean |  | S | S |  |  |  |  |
| 2 | `almRS` | Variant |  | S | S |  |  |  |  |
| 3 | `almUS` | Variant |  | S | S |  |  |  |  |
| 4 | `epmRS` | Variant |  | S | S |  |  |  |  |
| 5 | `epmUS` | Variant |  | S | S |  |  |  |  |
| 6 | `measRS` | Variant |  | S | S |  |  |  |  |
| 7 | `measUS` | Variant |  | S | S |  |  |  |  |
| 8 | `sysRS` | Variant |  | S | S |  |  |  |  |
| 9 | `sysUS` | Variant |  | S | S |  |  |  |  |
| 10 | `almFS` | Variant |  | S | S |  |  |  |  |
| 11 | `epmFS` | Variant |  | S | S |  |  |  |  |
| 12 | `measFS` | Variant |  | S | S |  |  |  |  |
| 13 | `sysFS` | Variant |  | S | S |  |  |  |  |
| 14 | `cfgEnableTimer` | Boolean | Boolean `False` | S | S |  |  |  |  |
| 15 | `timerRepeatInterval` | Date |  | S | S |  |  |  |  |
| 16 | `timerNextExecTime` | Date |  | S | S |  |  |  |  |

**Tags internas (14):** `SCADA_SQL_EPM_used-storage`, `SCADA_SQL_EPM_reserved-storage`, `SCADA_SQL_Alarms_reserved-storage`, `SCADA_SQL_Measures_reserved-storage`, `SCADA_SQL_System_reserved-storage`, `SCADA_SQL_Alarms_used-storage`, `SCADA_SQL_Measures_used-storage`, `SCADA_SQL_System_used-storage`, `ExecTimer` (TimerTag), `SCADA_SQL_Alarms_free-storage`, `SCADA_SQL_EPM_free-storage`, `SCADA_SQL_System_free-storage`, `SCADA_SQL_Measures_free-storage`, `Query`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×13 (SCADA_SQL_EPM_used-storage, SCADA_SQL_EPM_reserved-storage, SCADA_SQL_Alarms_reserved-storage, …)
TimerTag ×1 (ExecTimer)
```

**Eventos com script:** `ExecTimer.OnPreset` (3 linhas), `Query.runQuery` (100 linhas)

<a id="oadddemotag"></a>
### oAddDemoTag

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {0025550A-6AA0-43EC-BB3B-12317971EB76} · `_IID` = {2FB48423-D73B-4B6B-92AD-07A445EBC74E} · `_EVENTIID` = {CEE26C0E-B643-4559-9127-C2DEBB7590F4} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Initial` | Link |  | S | S |  |  |  |  |

**Eventos com script:** `oAddDemoTag.CustomConfig` (46 linhas)

<a id="oaddtimestampalarm"></a>
### oAddTimeStampAlarm

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {D6729FDB-D406-44E5-8DC2-5EE8C58E8CE3} · `_IID` = {DCC316D6-9A98-44F9-BED9-73CBB670E22A} · `_EVENTIID` = {BC0803A6-F663-475B-85B1-4F91EA28FBA9} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `folder` | Link |  | S | S |  |  |  |  |

**Eventos com script:** `oAddTimeStampAlarm.CustomConfig` (33 linhas)

<a id="otempscripts"></a>
### oTempScripts

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {55C0633C-079B-4812-A61D-86C97ACC352A} · `_IID` = {2F6672A2-7B28-435C-AFC5-84E9F68F1323} · `_EVENTIID` = {AD516D62-B9F4-4067-A98F-93EA24C2015F} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `ini` | Link |  | S | S |  |  |  |  |

**Eventos com script:** `oTempScripts.CustomConfig` (10 linhas)

<a id="ocalcsum"></a>
### oCalcSum

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {39F559EC-0EDF-4900-91C5-919429CF1541} · `_IID` = {CA8F3008-A087-41A9-8BBD-7EDB6596CFD4} · `_EVENTIID` = {0EBED6E9-4925-4F16-9D83-78BC003525F0} · `IconPath` = imgCalcSum · `EnableTagBehavior` = True · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (45)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `anlVar01` | InternalTag |  | S | S |  |  |  |  |
| 2 | `anlVar02` | InternalTag |  | S | S |  |  |  |  |
| 3 | `anlVar03` | InternalTag |  | S | S |  |  |  |  |
| 4 | `anlVar04` | InternalTag |  | S | S |  |  |  |  |
| 5 | `anlVar05` | InternalTag |  | S | S |  |  |  |  |
| 6 | `anlVar06` | InternalTag |  | S | S |  |  |  |  |
| 7 | `anlVar07` | InternalTag |  | S | S |  |  |  |  |
| 8 | `anlVar08` | InternalTag |  | S | S |  |  |  |  |
| 9 | `anlVar09` | InternalTag |  | S | S |  |  |  |  |
| 10 | `anlVar10` | InternalTag |  | S | S |  |  |  |  |
| 11 | `anlVar11` | InternalTag |  | S | S |  |  |  |  |
| 12 | `anlVar12` | InternalTag |  | S | S |  |  |  |  |
| 13 | `anlVar13` | InternalTag |  | S | S |  |  |  |  |
| 14 | `anlVar14` | InternalTag |  | S | S |  |  |  |  |
| 15 | `anlVar15` | InternalTag |  | S | S |  |  |  |  |
| 16 | `anlVar16` | InternalTag |  | S | S |  |  |  |  |
| 17 | `anlVar17` | InternalTag |  | S | S |  |  |  |  |
| 18 | `anlVar18` | InternalTag |  | S | S |  |  |  |  |
| 19 | `anlVar19` | InternalTag |  | S | S |  |  |  |  |
| 20 | `anlVar20` | InternalTag |  | S | S |  |  |  |  |
| 21 | `anlVar21` | InternalTag |  | S | S |  |  |  |  |
| 22 | `anlVar22` | InternalTag |  | S | S |  |  |  |  |
| 23 | `anlVar23` | InternalTag |  | S | S |  |  |  |  |
| 24 | `anlVar24` | InternalTag |  | S | S |  |  |  |  |
| 25 | `anlVar25` | InternalTag |  | S | S |  |  |  |  |
| 26 | `anlVar26` | InternalTag |  | S | S |  |  |  |  |
| 27 | `anlVar27` | InternalTag |  | S | S |  |  |  |  |
| 28 | `anlVar28` | InternalTag |  | S | S |  |  |  |  |
| 29 | `anlVar29` | InternalTag |  | S | S |  |  |  |  |
| 30 | `anlVar30` | InternalTag |  | S | S |  |  |  |  |
| 31 | `anlVar31` | InternalTag |  | S | S |  |  |  |  |
| 32 | `anlVar32` | InternalTag |  | S | S |  |  |  |  |
| 33 | `anlVar33` | InternalTag |  | S | S |  |  |  |  |
| 34 | `anlVar34` | InternalTag |  | S | S |  |  |  |  |
| 35 | `anlVar35` | InternalTag |  | S | S |  |  |  |  |
| 36 | `anlVar36` | InternalTag |  | S | S |  |  |  |  |
| 37 | `anlVar37` | InternalTag |  | S | S |  |  |  |  |
| 38 | `anlVar38` | InternalTag |  | S | S |  |  |  |  |
| 39 | `anlVar39` | InternalTag |  | S | S |  |  |  |  |
| 40 | `anlVar40` | InternalTag |  | S | S |  |  |  |  |
| 41 | `Value` | Variant |  | S |  |  |  |  |  |
| 42 | `Quality` | Word |  | S |  |  |  |  |  |
| 43 | `Timestamp` | Date |  | S |  |  |  |  |  |
| 44 | `cfgMultiplier` | Double | Integer `1` | S | S |  |  |  |  |
| 45 | `Format` | Format |  | S | S |  |  |  |  |

**Tags internas (2):** `varResult`, `resultado`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×2 (varResult, resultado)
```

**Eventos com script:** `varResult.ValueChange` (9 linhas), `varResult.OnStartRunning` (3 linhas)

<a id="omedidadigitalcalculada"></a>
### oMedidaDigitalCalculada

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {28F0F887-5608-445B-8A63-828FA53C680B} · `_IID` = {D463AB32-E1B9-4D13-921E-32734BECEE01} · `_EVENTIID` = {83A480F0-FB7A-4733-A256-29A1BF7DB1F6} · `IconPath` = imgCalcDiscrete · `FriendlyName` = calcDigital · `InstanceName` = digitalCalc0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`, `matrixenergylibxfolderse .lib`
- Classes que usa internamente: `fDados0se`, `AnimationBind`, `TableBind`

**Propriedades / métodos próprios (7)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTypeMeasurement` | Integer |  | S | S |  |  | -> Status Inversor: [2] Huawei 250KTL , [3] TBEA , [4] Sungrow, [5] WEG SIW 700, [6] WEG SIW 750 |  |
| 2 | `cfgDescritivoValores` | Variant |  | S |  |  |  | Configurar com conexão por tabela, onde deverá ser configurado o valor para cada status. Exemplo: 0 (False) = Desabilitado \| 1 (True) = Habilitado |  |
| 3 | `disDigital01` | fMedidaDigital0se |  | S | S |  |  |  |  |
| 4 | `disDigital02` | fMedidaDigital0se |  | S | S |  |  |  |  |
| 5 | `Value` | Variant |  | S |  |  |  |  |  |
| 6 | `TimeStamp` | Date |  | S |  |  |  |  |  |
| 7 | `Quality` | Integer |  | S |  |  |  |  |  |

**Tags internas (12):** `away`, `operating`, `standby`, `fail`, `Status`, `Status`, `Status`, `Status`, `Status`, `attValues`, `dis01Qual`, `dis02Qual`

**Estrutura interna (classe ×qtd):**

```
fDados0se ×1 (preConfigTypes)
  fDados0se ×1 (solarInverterStatus)
    fDados0se ×4 (HUAWEI, SUNGROW, TBEA, …)
      fDados0se ×1 (250KTL)
        InternalTag ×5 (away, operating, standby, …)
InternalTag ×3 (attValues, dis01Qual, dis02Qual)
```

**Eventos com script:** `attValues.attValues` (58 linhas)

<a id="ocalcresumoinversores"></a>
### oCalcResumoInversores

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**  ·  totalAway, totalFail, totalOperating, totalStandby
- Metadados: `_CLSID` = {AC84A2E6-2DAF-4D47-BA1F-6654101F587A} · `_IID` = {B0D0C3F6-5BB2-4D3E-8103-6E7044D9639B} · `_EVENTIID` = {3DD0EB61-30B9-4AC5-90BE-C3021EBF665E} · `Contexts` = totalAway,totalFail,totalOperating,totalStandby · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`, `matrixenergylibxfolderpv.lib`, `matrixenergylibxobjectpv.lib`
- Classes que usa internamente: `fDados`, `TableBind`, `oCalcSum`

**Propriedades / métodos próprios (40)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `linkInversor01` | fInversor |  | S | S |  |  |  |  |
| 2 | `linkInversor02` | fInversor |  | S | S |  |  |  |  |
| 3 | `linkInversor03` | fInversor |  | S | S |  |  |  |  |
| 4 | `linkInversor04` | fInversor |  | S | S |  |  |  |  |
| 5 | `linkInversor05` | fInversor |  | S | S |  |  |  |  |
| 6 | `linkInversor06` | fInversor |  | S | S |  |  |  |  |
| 7 | `linkInversor07` | fInversor |  | S | S |  |  |  |  |
| 8 | `linkInversor08` | fInversor |  | S | S |  |  |  |  |
| 9 | `linkInversor09` | fInversor |  | S | S |  |  |  |  |
| 10 | `linkInversor10` | fInversor |  | S | S |  |  |  |  |
| 11 | `linkInversor11` | fInversor |  | S | S |  |  |  |  |
| 12 | `linkInversor12` | fInversor |  | S | S |  |  |  |  |
| 13 | `linkInversor13` | fInversor |  | S | S |  |  |  |  |
| 14 | `linkInversor14` | fInversor |  | S | S |  |  |  |  |
| 15 | `linkInversor15` | fInversor |  | S | S |  |  |  |  |
| 16 | `linkInversor16` | fInversor |  | S | S |  |  |  |  |
| 17 | `linkInversor17` | fInversor |  | S | S |  |  |  |  |
| 18 | `linkInversor18` | fInversor |  | S | S |  |  |  |  |
| 19 | `linkInversor19` | fInversor |  | S | S |  |  |  |  |
| 20 | `linkInversor20` | fInversor |  | S | S |  |  |  |  |
| 21 | `linkInversor21` | fInversor |  | S | S |  |  |  |  |
| 22 | `linkInversor22` | fInversor |  | S | S |  |  |  |  |
| 23 | `linkInversor23` | fInversor |  | S | S |  |  |  |  |
| 24 | `linkInversor24` | fInversor |  | S | S |  |  |  |  |
| 25 | `linkInversor25` | fInversor |  | S | S |  |  |  |  |
| 26 | `linkInversor26` | fInversor |  | S | S |  |  |  |  |
| 27 | `linkInversor27` | fInversor |  | S | S |  |  |  |  |
| 28 | `linkInversor28` | fInversor |  | S | S |  |  |  |  |
| 29 | `linkInversor29` | fInversor |  | S | S |  |  |  |  |
| 30 | `linkInversor30` | fInversor |  | S | S |  |  |  |  |
| 31 | `linkInversor31` | fInversor |  | S | S |  |  |  |  |
| 32 | `linkInversor32` | fInversor |  | S | S |  |  |  |  |
| 33 | `linkInversor33` | fInversor |  | S | S |  |  |  |  |
| 34 | `linkInversor34` | fInversor |  | S | S |  |  |  |  |
| 35 | `linkInversor35` | fInversor |  | S | S |  |  |  |  |
| 36 | `linkInversor36` | fInversor |  | S | S |  |  |  |  |
| 37 | `linkInversor37` | fInversor |  | S | S |  |  |  |  |
| 38 | `linkInversor38` | fInversor |  | S | S |  |  |  |  |
| 39 | `linkInversor39` | fInversor |  | S | S |  |  |  |  |
| 40 | `linkInversor40` | fInversor |  | S | S |  |  |  |  |

**Tags internas (164):** `totalAway`, `totalOperating`, `totalFail`, `totalStandby`, `away01`, `away02`, `away03`, `away04`, `away05`, `away06`, `away07`, `away08`, `away09`, `away10`, `away11`, `away12`, `away13`, `away14`, `away15`, `away16`, `away17`, `away18`, `away19`, `away20`, `away21`, `away22`, `away23`, `away24`, `away25`, `away26`, `away27`, `away28`, `away29`, `away30`, `away31`, `away32`, `away33`, `away34`, `away35`, `away36`, `away37`, `away38`, `away39`, `away40`, `operating01`, `operating02`, `operating03`, `operating04`, `operating05`, `operating06`, `operating07`, `operating08`, `operating09`, `operating10`, `operating11`, `operating12`, `operating13`, `operating14`, `operating15`, `operating16` …

**Estrutura interna (classe ×qtd):**

```
InternalTag ×4 (totalAway, totalOperating, totalFail, …)
fDados ×4 (calcAway, calcOperating, calcStandby, …)
  InternalTag ×40 (away01, away02, away03, …)
  oCalcSum ×1 (sumAway)
```

**Eventos com script:** `oCalcResumoInversores.CustomConfig` (16 linhas)

<a id="osimulateiotag"></a>
### oSimulateIOTag

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {559AB710-19F9-4B91-94CE-65AB357E527C} · `_IID` = {3A720163-6BAE-4C9C-9C66-928023BF0B51} · `_EVENTIID` = {143AB07C-BA03-4B6A-9896-657B70E914FB} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`
- Classes que usa internamente: `DemoTag`, `TableBind`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Fonte` | IOTag |  | S | S |  |  |  |  |
| 2 | `cfgEnableSim` | Boolean | Boolean `True` | S | S |  |  |  |  |
| 3 | `cfgTypeTag` | Integer | Integer `0` | S | S |  |  | 0 - Digital \| 1 - Analog \| 2 - Discrete (0, 1, 2, 3) |  |
| 4 | `cfgMaxValue` | Variant |  | S | S |  |  |  |  |

**Tags internas (2):** `simu` (DemoTag), `valor`

**Estrutura interna (classe ×qtd):**

```
DemoTag ×1 (simu)
InternalTag ×1 (valor)
```

**Eventos com script:** `valor.valueChange` (10 linhas)

<a id="omedidaanalogicacalculada"></a>
### oMedidaAnalogicaCalculada

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {0F62287E-0515-4137-BA47-BA8BB5B36893} · `_IID` = {546CC97C-A8BF-45FE-8C5E-A78BEB6489D2} · `_EVENTIID` = {E89B5C37-2D2A-4D4D-B069-BBD01132017F} · `IconPath` = imgCalcAnalog · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`, `matrixenergylibxfolderpv.lib`
- Classes que usa internamente: `fDados`

**Propriedades / métodos próprios (16)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTypeMeasurement` | Integer |  | S | S |  |  | 0 - Correção de Escala [Analog01 apenas] \| 1 - Média \| 2 - Potência Estimada (MW)  |  |
| 2 | `anlAnalog01` | IOTag |  | S | S |  |  |  |  |
| 3 | `anlAnalog02` | IOTag |  | S | S |  |  |  |  |
| 4 | `anlAnalog03` | IOTag |  | S | S |  |  |  |  |
| 5 | `anlAnalog04` | IOTag |  | S | S |  |  |  |  |
| 6 | `anlAnalog05` | IOTag |  | S | S |  |  |  |  |
| 7 | `anlAnalog06` | IOTag |  | S | S |  |  |  |  |
| 8 | `TimeStamp` | Date |  | S |  |  |  |  |  |
| 9 | `Value` | Variant |  | S |  |  |  |  |  |
| 10 | `Quality` | Integer |  | S |  |  |  |  |  |
| 11 | `Format` | Format |  | S | S |  |  |  |  |
| 12 | `cfgMultiplier` | Double | Integer `1` | S | S |  |  | Multiplicador para conversão de Valores |  |
| 13 | `cfgConstantA` | Double |  | S | S |  |  |  |  |
| 14 | `cfgConstantB` | Double |  | S | S |  |  |  |  |
| 15 | `cfgConstantC` | Double |  | S | S |  |  |  |  |
| 16 | `cfgLimit01` | Double |  | S | S |  |  |  |  |

**Tags internas (8):** `CalcTag`, `analog01`, `analog02`, `analog03`, `analog04`, `analog05`, `analog06`, `Resultado`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×2 (CalcTag, Resultado)
fDados ×1 (Medidas)
  InternalTag ×6 (analog01, analog02, analog03, …)
```

**Eventos com script:** `CalcTag.CalcTag` (111 linhas)

<a id="onotaoperativa"></a>
### oNotaOperativa

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {B07739E6-C300-40E8-AE8F-91721284DA2F} · `_IID` = {7A5B14F0-001C-45B9-BEBD-314141340573} · `_EVENTIID` = {42FB3933-6656-4AF4-97DC-45463AD6E7CA} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (8)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIdNote` | String |  | S | S |  |  |  |  |
| 2 | `cfgTargetPathName` | String |  | S | S |  |  |  |  |
| 3 | `cfgTitle` | String |  | S | S |  |  |  |  |
| 4 | `cfgDescription` | String |  | S | S |  |  |  |  |
| 5 | `cfgStatus` | String |  | S | S |  |  |  |  |
| 6 | `cfgCreationDate` | String |  | S | S |  |  |  |  |
| 7 | `cfgUser` | String |  | S | S |  |  |  |  |
| 8 | `cfgLastMod` | String |  | S | S |  |  |  |  |

<a id="omedidadigitalbit"></a>
### oMedidaDigitalBit

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {F3FD171B-59D3-45E0-B9DB-014FDC1F4B16} · `_IID` = {523B9A2B-FD6B-43C2-BC7C-C4C359D27A83} · `_EVENTIID` = {5E9830C4-9734-487B-BA14-C1708C4B2B10} · `IconPath` = imgMedidaDigitalBit · `InstanceName` = Bit0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `DB.e3`, `Panel.e3`
- Classes que usa internamente: `DigitalAlarmSource`, `DigitalAlarm`

**Propriedades / métodos próprios (12)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Fonte` | IOTag | String `Parent.Fonte` | S | S |  |  |  |  |
| 2 | `cfgDescritivoAlarme` | Variant | String `- Preencher - ` | S | S |  |  |  |  |
| 3 | `cfgCriticidadeAlarme` | EAlarmSeverity |  | S | S |  |  |  |  |
| 4 | `cfgIsEvent` | Boolean | Boolean `False` | S | S |  |  | Mudar para True em caso de Evento |  |
| 5 | `cfgHabilitarAlarme` | Boolean | Boolean `True` | S | S |  |  |  |  |
| 6 | `cfgPosicaoBit` | Integer | Integer `0` | S | S |  |  |  |  |
| 7 | `cfgCondicaoAlarme` | Boolean | Boolean `True` | S | S |  |  | Ajustar conforme necessário. Se True, o Alarme atuará quando o Bit estiver atuado. Em False, o Alarme atuará quando o Bit for False. |  |
| 8 | `cfgDelayAlarm` | DWord | Long `0` | S | S |  |  | Ajuste conforme necessário. |  |
| 9 | `Value` | Variant |  | S |  |  |  |  |  |
| 10 | `Quality` | Word |  | S |  |  |  |  |  |
| 11 | `Timestamp` | Date |  | S |  |  |  |  |  |
| 12 | `cfgDescritivoValores` | Variant | String `- Preencher - ` | S | S |  |  |  |  |

**Tags internas (2):** `valorBit`, `digital`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×2 (valorBit, digital)
  DigitalAlarmSource ×1 (AlarmeDigital)
```

**Eventos com script:** `valorBit.attValues` (35 linhas)

<a id="omonitorcorrentestrings"></a>
### oMonitorCorrenteStrings

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {B65E6C84-3C1B-4A59-9CF6-98AEF2F9E7C7} · `_IID` = {8245EF26-F6D8-4BE1-8DC5-21EC5F7C56B1} · `_EVENTIID` = {BA2B32FA-5377-4866-BA07-679C53964326} · `IconPath` = imgMonitorAnalog · `InstanceName` = MonitorCorrente · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `DB.e3`, `Panel.e3`, `matrixenergylibxobjectpv.lib`
- Classes que usa internamente: `oCalcSum`, `DigitalAlarmSource`, `DigitalAlarm`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `linkGrupoStrings` | fGrupoStrings |  | S | S |  |  |  |  |
| 2 | `linkInversor` | fInversor |  | S | S |  |  |  |  |

**Tags internas (1):** `calcTag`

**Estrutura interna (classe ×qtd):**

```
oCalcSum ×1 (somaCorrentes)
InternalTag ×1 (calcTag)
  DigitalAlarmSource ×1 (alarmeString)
```

**Eventos com script:** `oMonitorCorrenteStrings.CustomConfig` (4 linhas), `calcTag.onValueChange` (586 linhas)

<a id="ostatustrackers"></a>
### oStatusTrackers

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {C3724E11-A9F6-42DF-B434-63ACC8807192} · `_IID` = {4869E050-FE0B-4904-ADD8-16775B515CAF} · `_EVENTIID` = {2AE85F4C-5BFD-4D9D-9CAE-BB40944CD2EA} · `InstanceName` = statusTracker · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `DB.e3`, `Panel.e3`, `matrixenergylibxfolderpv.lib`
- Classes que usa internamente: `fMedidaDigital`, `TableBind`, `DiscreteAlarmSource`, `DiscreteAlarm`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `linkStatus` | IOTag | String `Parent` | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
fMedidaDigital ×1 (STATUS)
  DiscreteAlarmSource ×3 (mainStateAlarm, safePositionAlarm, sleepStateAlarm)
```

<a id="ocalcbitdec"></a>
### oCalcBitDec

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {41E62FA5-2B51-4CAF-A70C-6390208851A5} · `_IID` = {440D34BD-6C42-495A-A91B-23436363F296} · `_EVENTIID` = {310BF320-6A22-460D-A97C-07BCB3787975} · `InstanceName` = posDec0 · `EnableTagBehavior` = True · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Bit` | oMedidaDigitalBit |  | S | S |  |  |  |  |
| 2 | `Value` | Variant |  | S |  |  |  |  |  |
| 3 | `Quality` | Word |  | S |  |  |  |  |  |
| 4 | `Timestamp` | Date |  | S |  |  |  |  |  |
| 5 | `cfgPosicaoBitCalc` | Integer |  | S | S |  |  |  |  |

**Tags internas (1):** `Valor`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×1 (Valor)
```

**Eventos com script:** `Valor.changeValue` (5 linhas)

<a id="temp"></a>
### temp

- Biblioteca: `matrixenergylibxobjectpv.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {226B2220-BD7C-4D00-A7F3-98D244F9EF2B} · `_IID` = {DE21F186-D9EF-49D6-A326-8DCEF5E6A592} · `_EVENTIID` = {48EA967D-3DFE-454D-AEC1-B1056213F6E2} · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgPathName` | Variant |  | S | S |  |  |  |  |

**Eventos com script:** `temp.CustomConfig` (485 linhas)

---

## Biblioteca `matrixenergylibxobjectse.lib`

<a id="oconfigheader0se"></a>
### oConfigHeader0se

- Biblioteca: `matrixenergylibxobjectse.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {A59EA20B-114E-4116-B30A-033DC18A26B5} · `_IID` = {2E761CD1-DBF2-45E9-9C57-F80370B8C334} · `_EVENTIID` = {F7CAC9B4-7624-46A1-9555-792B0A46E7ED} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (9)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `botao01` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 2 | `botao02` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 3 | `botao03` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 4 | `botao04` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 5 | `botao05` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 6 | `botao06` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 7 | `botao07` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 8 | `botao08` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 9 | `cfgFrameType` | Integer | Integer `2` | S | S |  |  | Frame a ser aberto: 0 -> Main Frame \| 1 -> Plant Frame \| 2-> Focus Frame \| 3 -> PopUp |  |

<a id="oconfignavegacaoscreens0se"></a>
### oConfigNavegacaoScreens0se

- Biblioteca: `matrixenergylibxobjectse.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {CDA5EA30-2EBD-44CB-804D-C88BC93EA8B9} · `_IID` = {2D52AE7D-708A-4C1C-AB6A-BF6C7022D64D} · `_EVENTIID` = {C67176A6-5FEB-4F4E-AA7E-4C0BC26B71E8} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (6)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `NomeTela` | Variant |  | S | S |  |  | Caption Tela |  |
| 2 | `IDTela` | Variant |  | S | S |  |  | Name Tela |  |
| 3 | `Path` | Variant |  | S | S |  |  | PathContainer Tela |  |
| 4 | `PathPainelLateral` | Variant |  | S | S |  |  | PathContainer Tela |  |
| 5 | `PathHeader` | Variant |  | S | S |  |  | PathContainer Tela |  |
| 6 | `FiltroAlarmes` | Variant |  | S | S |  |  | Inserir o Filtro de Alarmes |  |

<a id="odashconfigcardgeralusinas0se"></a>
### oDashConfigCardGeralUsinas0se

- Biblioteca: `matrixenergylibxobjectse.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {B3322866-34D5-4552-9BCC-E37AB4DC2AEC} · `_IID` = {11B4E39A-858B-462B-A61B-D43CDCABCD86} · `_EVENTIID` = {74889539-B506-4250-92A6-7A3990EE71A5} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (11)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgPlantName` | String |  | S | S |  |  | nome da Planta / Ativo |  |
| 2 | `cfgIDPlanta` | String |  | S | S |  |  | ID da Planta / Ativo |  |
| 3 | `linkScreen` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 4 | `linkConfigGaugeA` | oDashConfigGauge0se |  | S | S |  |  |  |  |
| 5 | `linkConfigGaugeB` | oDashConfigGauge0se |  | S | S |  |  |  |  |
| 6 | `anlAlarmes` | Variant |  | S |  |  |  |  |  |
| 7 | `anlFatorPotencia` | fMedidaAnalogica0se |  | S | S |  |  |  |  |
| 8 | `anlTensaoAtual` | fMedidaAnalogica0se |  | S | S |  |  |  |  |
| 9 | `anlFreq` | fMedidaAnalogica0se |  | S | S |  |  |  |  |
| 10 | `anlTensaoNominal` | Variant |  | S | S |  |  |  |  |
| 11 | `disStatusCom` | Variant |  | S |  |  |  |  |  |

<a id="odashconfiggauge0se"></a>
### oDashConfigGauge0se

- Biblioteca: `matrixenergylibxobjectse.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {249D134C-1228-46CC-8396-60FF66C408BC} · `_IID` = {4CAC092C-703B-4383-A92E-1A07751B34A9} · `_EVENTIID` = {F34ADC41-1848-434A-A372-0A9447CC61E0} · `IconPath` = imgGear · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `NomeGrafico` | Variant |  | S | S |  |  |  |  |
| 2 | `ValorMaximo` | Variant |  | S | S |  |  |  |  |
| 3 | `ValorAtual` | fMedidaAnalogica0se |  | S | S |  |  |  |  |
| 4 | `UnidadeMedida` | Variant |  | S | S |  |  |  |  |

**Tags internas (1):** `ValorFiltrado`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×1 (ValorFiltrado)
```

<a id="omedidadigitalcalculada0se"></a>
### oMedidaDigitalCalculada0se

- Biblioteca: `matrixenergylibxobjectse.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {B006D693-9809-4574-97F1-46ECB61E2417} · `_IID` = {033346BB-9BE9-4413-8CE4-D419F8D57AEA} · `_EVENTIID` = {7FDB3A55-CD2C-48A5-8510-75C346EE8824} · `IconPath` = imgCalcDiscrete · `FriendlyName` = calcDigital · `InstanceName` = digitalCalc0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `DB.e3`, `Panel.e3`, `matrixenergylibxfolderse .lib`
- Classes que usa internamente: `fDados0se`, `TableBind`, `DiscreteAlarmSource`, `DiscreteAlarm`, `DigitalAlarmSource`, `DigitalAlarm`

**Propriedades / métodos próprios (7)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTypeMeasurement` | Integer |  | S | S |  |  | 0 - Posição do Disjuntor (Double Point - Fechado -> Digital 01 ; Aberto -> Digital 02 ), [2] - Caso de Apenas Status de Aberto (Digital01),  [3] - Caso de Apenas Status de Fechado (Digital02) \| Posição Seccionadora  [1] - Normal Closed, [11] - Normal Opened {(Aberto -> Digital 01 , Fechado -> Digital 02 (Se existir))}\|  |  |
| 2 | `cfgDescritivoValores` | Variant |  | S |  |  |  | Configurar com conexão por tabela, onde deverá ser configurado o valor para cada status. Exemplo: 0 (False) = Desabilitado \| 1 (True) = Habilitado |  |
| 3 | `disDigital01` | IOTag |  | S | S |  |  |  |  |
| 4 | `disDigital02` | IOTag |  | S | S |  |  |  |  |
| 5 | `Value` | Variant |  | S |  |  |  |  |  |
| 6 | `TimeStamp` | Date |  | S |  |  |  |  |  |
| 7 | `Quality` | Integer |  | S |  |  |  |  |  |

**Tags internas (15):** `Closed`, `Position`, `Opened`, `Closed`, `Opened`, `Position`, `Opened`, `Closed`, `Position`, `Opened`, `Closed`, `Position`, `attValues`, `digital01`, `digital02`

**Estrutura interna (classe ×qtd):**

```
fDados0se ×2 (preConfigTypes, Medidas)
  fDados0se ×2 (breakerPosition, switchPosition)
    InternalTag ×3 (Closed, Position, Opened)
    fDados0se ×2 (calcOnlyOpenedState, calcOnlyClosedState)
      InternalTag ×3 (Closed, Opened, Position)
InternalTag ×1 (attValues)
  DigitalAlarmSource ×1 (FalhaCom)
```

**Eventos com script:** `attValues.attValues` (130 linhas)

<a id="omedidaanalogicacalculada0se"></a>
### oMedidaAnalogicaCalculada0se

- Biblioteca: `matrixenergylibxobjectse.lib`  ·  tipo: **XObject**
- Metadados: `_CLSID` = {904A3732-FBEC-4267-8828-3B4619F85A1E} · `_IID` = {0B81DDEA-9472-48DA-AE98-5E102279D385} · `_EVENTIID` = {F9DA212C-4ECC-4942-BF67-AD6E45B6E14C} · `IconPath` = imgCalcAnalog · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`, `matrixenergylibxfolderse .lib`
- Classes que usa internamente: `fDados0se`

**Propriedades / métodos próprios (12)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTypeMeasurement` | Integer |  | S | S |  |  | 0 - Correção de Escala [Analog01 apenas] \| 1 - Média \| 2 - Fator de Potência Calculado [analog01 -> Somatória de Potência Ativa], [analog02 -> Somatória de Potência Reativa] \| 3 - Potência Aparente Calculada [01 -> Tensão Média], [02 -> Corrente Média] \| 4 - Ângulo entre Potência Ativa e Potência Aparente [01 - P], [02 -> S] \| 5 - Potência Reativa [01 - Tensão Média], [02 - Corrente Média], [03 - Ângulo entre P e S] \|  6 - Potência Reativa [01 - Potência Aparente], [02 - Ângulo entre Potências] |  |
| 2 | `anlAnalog01` | IOTag |  | S | S |  |  |  |  |
| 3 | `anlAnalog02` | IOTag |  | S | S |  |  |  |  |
| 4 | `anlAnalog03` | IOTag |  | S | S |  |  |  |  |
| 5 | `anlAnalog04` | IOTag |  | S | S |  |  |  |  |
| 6 | `anlAnalog05` | IOTag |  | S | S |  |  |  |  |
| 7 | `anlAnalog06` | IOTag |  | S | S |  |  |  |  |
| 8 | `TimeStamp` | Date |  | S |  |  |  |  |  |
| 9 | `Value` | Variant |  | S |  |  |  |  |  |
| 10 | `Quality` | Integer |  | S |  |  |  |  |  |
| 11 | `Format` | Format |  | S | S |  |  |  |  |
| 12 | `cfgMultiplier` | Double | Integer `1` | S | S |  |  | Multipicador para conversão de Valores |  |

**Tags internas (8):** `CalcTag`, `Resultado`, `analog01`, `analog02`, `analog03`, `analog04`, `analog05`, `analog06`

**Estrutura interna (classe ×qtd):**

```
InternalTag ×2 (CalcTag, Resultado)
fDados0se ×1 (Medidas)
  InternalTag ×6 (analog01, analog02, analog03, …)
```

**Eventos com script:** `CalcTag.calcs` (114 linhas)
