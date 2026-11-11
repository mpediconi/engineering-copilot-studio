# XFolder — classes das bibliotecas Matrix Energy e suas propriedades

Fonte: arquivos `.lib` em `C:\SCADA_Eng01\01_MatrixEnergy\02_Libraries`. **68 classes**, **1181 propriedades/métodos próprios**.

XFolder = pasta/objeto de **servidor de dados** com propriedades próprias (prefixo `f`; `0se` = variante de subestação).

Formato de cada item: metadados da classe (`_CLSID`, `_IID`, `IconPath`…) → propriedades próprias (`XMethod`: tipo, padrão, flags) → tags internas → estrutura interna → associações → scripts → elementos gráficos.

## Propriedades base (herdadas por todas as classes XFolder)

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
| `matrixenergylibxfolderbtc.lib` | [fContainerMineracao](#fcontainermineracao), [fInversorFrequencia](#finversorfrequencia), [fAtivoBTC](#fativobtc) |
| `matrixenergylibxfolderpv.lib` | [fUsinaPV](#fusinapv), [fCampoSolar](#fcamposolar), [fChave](#fchave), [fCMB](#fcmb), [fComando](#fcomando), [fDados](#fdados), [fDisjuntor](#fdisjuntor), [fEMET](#femet), [fPPC](#fppc), [fGrupoAnalogicas](#fgrupoanalogicas), [fgrupoChaves](#fgrupochaves), [fGrupoComandos](#fgrupocomandos), [fGrupoDigitais](#fgrupodigitais), [fCluster](#fcluster), [fGrupoTrackers](#fgrupotrackers), [fInversor](#finversor), [fMedidaAnalogica](#fmedidaanalogica), [fMedidaDigital](#fmedidadigital), [fGrupoStrings](#fgrupostrings), [fMultimedidor](#fmultimedidor), [fNCU](#fncu), [fQGBT](#fqgbt), [fRSU](#frsu), [fStringBox](#fstringbox), [fString](#fstring), [fSubestacao](#fsubestacao), [fTracker](#ftracker), [fTransformador](#ftransformador), [fArray](#farray), [fBarramento](#fbarramento), [fConector](#fconector), [fEletrocentro](#feletrocentro), [fCircuito](#fcircuito), [fGerador](#fgerador), [fComCloud](#fcomcloud), [fComConnection](#fcomconnection), [fComConverter](#fcomconverter), [fComFirewall](#fcomfirewall), [fComIED](#fcomied), [fComInternet](#fcominternet), [fComRack](#fcomrack), [fComRouter](#fcomrouter), [fComRTU](#fcomrtu), [fComServer](#fcomserver), [fComSwitch](#fcomswitch), [fComVPN](#fcomvpn), [fMPPT](#fmppt), [fMedidaDigitalBit](#fmedidadigitalbit), [fObjScadaPowerControl](#fobjscadapowercontrol) |
| `matrixenergylibxfolderse .lib` | [fChave0se](#fchave0se), [fCircuito0se](#fcircuito0se), [fComando0se](#fcomando0se), [fTransformador0se](#ftransformador0se), [fSubestacao0se](#fsubestacao0se), [fProtection0se](#fprotection0se), [fMedidaDigital0se](#fmedidadigital0se), [fMedidaAnalogica0se](#fmedidaanalogica0se), [fIED0se](#fied0se), [fGrupoDigitais0se](#fgrupodigitais0se), [fGrupoComandos0se](#fgrupocomandos0se), [fGrupoAnalogicas0se](#fgrupoanalogicas0se), [fElectricPanel0se](#felectricpanel0se), [fDados0se](#fdados0se), [fDisjuntor0se](#fdisjuntor0se), [fRetificador0se](#fretificador0se) |

---

## Biblioteca `matrixenergylibxfolderbtc.lib`

<a id="fcontainermineracao"></a>
### fContainerMineracao

- Biblioteca: `matrixenergylibxfolderbtc.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {5363D1F7-E3E9-4D9D-9D22-89D432F9DC9C} · `_IID` = {9D89C194-DE64-4179-A851-C468055DE135} · `_EVENTIID` = {14B97DC2-B73F-4B03-AA1B-CC10B4A33C8B} · `IconPath` = imgContainerMiner · `InstanceName` = CTN0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `anlTotalHashRate` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 2 | `anlTotalMiners` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 3 | `anlTotalMinersOnline` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 4 | `anlTotalMinersHashing` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 5 | `anlEffic` | fMedidaAnalogica |  | S | S |  |  |  |  |

**Eventos com script:** `fContainerMineracao.CustomConfig` (19 linhas)

<a id="finversorfrequencia"></a>
### fInversorFrequencia

- Biblioteca: `matrixenergylibxfolderbtc.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {8EB15194-0E7D-4CC1-A515-D4A2F33CC0FE} · `_IID` = {002C7F13-14DA-4584-BDF6-DFBD508778D2} · `_EVENTIID` = {0123F5B1-3F64-495D-90A0-C2F9CE3990AD} · `IconPath` = imgFreqInverter · `FriendlyName` = Inversor Frequência · `InstanceName` = invFreq0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 2 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

<a id="fativobtc"></a>
### fAtivoBTC

- Biblioteca: `matrixenergylibxfolderbtc.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {3BC53281-49C1-4BD1-955A-CF78FE4C6DB7} · `_IID` = {A18A4856-7BED-410F-9E17-192727DE953E} · `_EVENTIID` = {26CA45EC-90C2-473D-BF0D-CAC6E3203417} · `IconPath` = imgBTC · `InstanceName` = BTC_0 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgNomeAtivo` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgLocalidade` | Variant |  | S | S |  |  |  |  |
| 3 | `linkDadosAtivo` | oDadosAtivoBtc |  | S | S |  |  |  |  |
| 4 | `anlCritNACKAlarms` | Variant |  | S |  |  |  |  |  |
| 5 | `anlHighNACKAlarms` | Variant |  | S |  |  |  |  |  |

**Eventos com script:** `fAtivoBTC.CustomConfig` (5 linhas)

---

## Biblioteca `matrixenergylibxfolderpv.lib`

<a id="fusinapv"></a>
### fUsinaPV

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {D5959F8A-E582-4905-AFED-9E7BED3F2E1C} · `_IID` = {53F8DEA8-6B5F-4085-9F70-286AB4B14AA9} · `_EVENTIID` = {F676E3D0-AC7E-4BD8-A8F8-23BDD43444FA} · `IconPath` = imgPhotovoltaicPlant · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (20)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `nomeUsina` | Variant |  | S | S |  |  |  |  |
| 2 | `Localidade` | Variant |  | S | S |  |  |  |  |
| 3 | `LatLong` | Variant |  | S | S |  |  |  |  |
| 4 | `Capacidade` | Variant |  | S | S |  |  | Em MW |  |
| 5 | `IniOperacao` | Variant |  | S | S |  |  |  |  |
| 6 | `PotenciaAtiva` | Variant | Integer `0` | S | S |  |  |  |  |
| 7 | `EnergiaDia` | Variant | Integer `0` | S | S |  |  |  |  |
| 8 | `AreaTotal` | Variant | Integer `0` | S | S |  |  | Em m² |  |
| 9 | `ModeloInversores` | Variant | String `` | S | S |  |  |  |  |
| 10 | `PotenciaTotalInversores` | Variant | Integer `0` | S | S |  |  | Em MW |  |
| 11 | `InversoresLigados` | Variant | Integer `0` | S | S |  |  |  |  |
| 12 | `TotalInversores` | Variant | Integer `0` | S | S |  |  |  |  |
| 13 | `TotalStrings` | Variant | Integer `0` | S | S |  |  |  |  |
| 14 | `TensaoConexao` | Variant |  | S | S |  |  | Em kV |  |
| 15 | `PotenciaInstalada` | Variant |  | S | S |  |  | Em MWp |  |
| 16 | `TotalTrackers` | Variant | Integer `0` | S | S |  |  | Quantidade Total de Trackers na Usina |  |
| 17 | `StatusComunicacao` | Boolean | Boolean `False` | S | S |  |  | Vincular condição para que caso perca a comunicação, o resultado seja 'False'. |  |
| 18 | `cfgCaminhoArquivo` | Variant |  | S | S |  |  | Inserir o caminho do arquivo CSV de configuração do nome dos objetos ("$cfg:1") |  |
| 19 | `cfgTypeConfig` | Integer | Integer `0` | S | S |  |  | 0 - Desligado \| 1 - Configuração dos Equipamentos \| 2 - Configuração dos nomes baseado no cfgCaminhoArquivo \| 3 - Exporta Alarmes \| 4 - Exporta objetos por TypeName \| 5 - Exporta associações da propriedade Fonte para XLSX |  |
| 20 | `cfgTensaoNominal` | Double | Integer `0` | S | S |  |  |  |  |

**Eventos com script:** `fUsinaPV.CustomConfig` (2006 linhas)

<a id="fcamposolar"></a>
### fCampoSolar

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {579C94A7-5F72-4D48-9A4E-294391D1DA6C} · `_IID` = {298AFD87-7EB4-4C8E-8EF2-FECAF90774E5} · `_EVENTIID` = {E037AD38-31A4-4CE3-901D-28FDEDA83F38} · `IconPath` = imgSolarField · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `CorrenteCC` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 2 | `linkResumoInversores` | oCalcResumoInversores |  | S | S |  |  |  |  |
| 3 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 4 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fCampoSolar.CustomConfig` (22 linhas)

<a id="fchave"></a>
### fChave

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {C4B22B0E-3867-4A62-AED8-70FC92390663} · `_IID` = {F070621C-1563-46A3-8F68-D184DE890614} · `_EVENTIID` = {57FD8036-F995-4634-B2D0-F96DBE803B86} · `IconPath` = imgSwitch · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (13)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `EST` | Variant | Boolean `True` | S | S | S |  |  |  |
| 2 | `IDOperativo` | Variant |  | S | S | S |  |  |  |
| 3 | `SUPERVISAO` | Integer | Integer `0` | S | S | S |  | Supervisão Habilitada? |  |
| 4 | `CONTROLE` | Integer | Integer `0` | S | S | S |  | Controle Habilitado? |  |
| 5 | `cmdPontoDuplo` | Boolean |  | S | S |  |  | Alterar para True em caso de Comando de Ponto Duplo |  |
| 6 | `cmdSELECT` | Comando |  | S | S |  |  | Vincular ao comando de SELECT \| PONTO DUPLO |  |
| 7 | `cmdEXEC` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE \| PONTO DUPLO |  |
| 8 | `cmdRSTPROT` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 9 | `cmdSELECTRSTPROT` | Comando |  | S | S |  |  | Vincular ao comando de SELECT Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 10 | `cmdABRIR` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE ABRIR \| PONTO SIMPLES |  |
| 11 | `cmdFECHAR` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE FECHAR \| PONTO SIMPLES |  |
| 12 | `cmdSELECTABRIR` | Comando |  | S | S |  |  | Vincular ao comando de SELECT ABRIR \| PONTO SIMPLES |  |
| 13 | `cmdSELECTFECHAR` | Comando |  | S | S |  |  | Vincular ao comando de SELECT FECHAR \| PONTO SIMPLES |  |

<a id="fcmb"></a>
### fCMB

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {1E7FC590-877E-4CA2-9197-8FCD84DC7003} · `_IID` = {9C70277F-6FA2-4543-AC4F-AFA32EBE2028} · `_EVENTIID` = {85FABC60-F4D5-4B51-990A-6767B1A6F29A} · `IconPath` = imgCMB · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (18)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `FABRICANTE` | Variant |  | S | S |  |  |  |  |
| 2 | `MODELO` | Variant |  | S | S |  |  |  |  |
| 3 | `anlPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 4 | `anlEnergia` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 5 | `cmdSPPotAtiva` | fComando |  | S | S |  |  |  |  |
| 6 | `cmdSPPotReativa` | fComando |  | S | S |  |  |  |  |
| 7 | `cmdSPFatorPot` | fComando |  | S | S |  |  |  |  |
| 8 | `cmdLigarInversores` | fComando |  | S | S |  |  |  |  |
| 9 | `cmdDesligarInversores` | fComando |  | S | S |  |  |  |  |
| 10 | `cfgPotAtivaMaxPlanta` | Integer |  | S | S |  |  | Definir o valor em kW |  |
| 11 | `linkGrupoDigitais` | fGrupoDigitais |  | S | S |  |  |  |  |
| 12 | `linkGrupoAnalogicas` | fGrupoAnalogicas |  | S | S |  |  |  |  |
| 13 | `cfgFabricante` | String |  | S | S |  |  |  |  |
| 14 | `cfgModelo` | String |  | S | S |  |  |  |  |
| 15 | `disStatusComunicacao` | fMedidaDigital |  | S | S |  |  |  |  |
| 16 | `linkResumoInversores` | oCalcResumoInversores |  | S | S |  |  | totalAway, totalFail, totalOperating, totalStandby |  |
| 17 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 18 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fCMB.CustomConfig` (27 linhas)

<a id="fcomando"></a>
### fComando

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {EE2FBE84-0073-4C20-B28D-9192C568540D} · `_IID` = {403DEC0D-878F-4081-BB10-CF8A63D0C3DD} · `_EVENTIID` = {91B981FD-7760-4E22-B91B-58E314B5D70F} · `IconPath` = imgCommandv2 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Variant |  | S | S |  |  |  |  |
| 2 | `ID` | Variant |  | S | S |  |  |  |  |
| 3 | `Fonte` | IOTag |  | S | S |  |  | Tag do Driver |  |
| 4 | `Event` | Variant |  | S | S |  |  |  |  |
| 5 | `TimeStamp` | Variant |  | S | S |  |  |  |  |

**Eventos com script:** `fComando.CustomConfig` (5 linhas)

<a id="fdados"></a>
### fDados

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {B9324656-5EF4-45CD-AE59-EF0F703939BA} · `_IID` = {980910D7-C832-4BB3-AB3C-BC622EA3A786} · `_EVENTIID` = {E899E891-CAB5-4593-A6A1-45476D6A983D} · `IconPath` = imgFolderMeasurement · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Eventos com script:** `fDados.CustomConfig` (9 linhas)

<a id="fdisjuntor"></a>
### fDisjuntor

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {9F4840D8-9DE2-4967-832D-063D2CF71A1F} · `_IID` = {88C0B60A-2A92-4C20-A772-EB8E63C2F806} · `_EVENTIID` = {C70AA217-F85D-4DEE-8809-C56A3F3D19F0} · `IconPath` = imgCircuitBreaker · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (29)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `SUPERVISAO` | Boolean | Boolean `False` | S | S | S |  | Se Valor = False, então o equipamento será considerado MANUAL, com tags internas, sem aquisição e sem controle. |  |
| 2 | `StatusComunicacao` | Boolean | Boolean `False` | S | S | S |  | Vincular condição para que caso perca a comunicação, o resultado seja 'False'. |  |
| 3 | `ID` | Variant |  | S | S |  |  |  |  |
| 4 | `EST` | Variant | Integer `-4` | S | S |  |  |  | OnPropertyChanged (5 l.) |
| 5 | `FABRICANTE` | Variant |  | S | S |  |  |  |  |
| 6 | `MODELO` | Variant |  | S | S |  |  |  |  |
| 7 | `UFV` | Variant |  | S | S |  |  |  |  |
| 8 | `Abrir` | Variant |  | S | S |  |  |  |  |
| 9 | `Fechar` | Variant |  | S | S |  |  |  |  |
| 10 | `ResetProt` | Variant |  | S | S |  |  |  |  |
| 11 | `CombEstado` | Variant |  | S | S |  |  |  |  |
| 12 | `Alarmes` | Variant |  | S | S |  |  | Vinculação com os alarmes ativos no equipamento |  |
| 13 | `cmdPontoDuplo` | Boolean |  | S | S |  |  | Alterar para True em caso de Comando de Ponto Duplo |  |
| 14 | `cmdSELECT` | Comando |  | S | S |  |  | Vincular ao comando de SELECT \| PONTO DUPLO |  |
| 15 | `cmdEXEC` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE \| PONTO DUPLO |  |
| 16 | `cmdRSTPROT` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 17 | `cmdSELECTRSTPROT` | Comando |  | S | S |  |  | Vincular ao comando de SELECT Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 18 | `cmdABRIR` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE ABRIR \| PONTO SIMPLES |  |
| 19 | `cmdFECHAR` | Comando |  | S | S |  |  | Vincular ao comando de EXECUTE FECHAR \| PONTO SIMPLES |  |
| 20 | `cmdSELECTABRIR` | Comando |  | S | S |  |  | Vincular ao comando de SELECT ABRIR \| PONTO SIMPLES |  |
| 21 | `cmdSELECTFECHAR` | Comando |  | S | S |  |  | Vincular ao comando de SELECT FECHAR \| PONTO SIMPLES |  |
| 22 | `linkVMedia` | MedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 23 | `linkIMedia` | MedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 24 | `linkFP` | MedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 25 | `linkPotenciaAtiva` | MedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 26 | `linkPotenciaReativa` | MedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 27 | `TagHabilitada` | Boolean | Boolean `False` | S | S | S |  |  |  |
| 28 | `cmdBLOQDESBLOQERAC` | Comando |  | S | S |  |  | Vincular ao comando de BLOQUEAR ERAC \| DESBLOQUEAR ERAC |  |
| 29 | `cmdBLOQDESBLOQRA` | Comando |  | S | S |  |  | Vincular ao comando de BLOQUEAR RELIGAMENTO \| DESBLOQUEAR RELIGAMENTO |  |

**Eventos com script:** `fDisjuntor.CustomConfig` (15 linhas)

<a id="femet"></a>
### fEMET

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {36D26E95-82D3-4AF3-BA9B-DBAA0FDAF8EA} · `_IID` = {150ED390-9938-49AE-A70B-73B32E6467B2} · `_EVENTIID` = {0F382239-F5D4-4442-B820-144810CC9A67} · `IconPath` = imgMeteoStation · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (15)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `FABRICANTE` | Variant |  | S | S |  |  |  |  |
| 2 | `StatusComunicacao` | Boolean | Boolean `False` | S | S |  |  | Vincular condição para que caso perca a comunicação, o resultado seja 'False'. |  |
| 3 | `MODELO` | Variant |  | S | S |  |  |  |  |
| 4 | `anlUmidade` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 5 | `anlTempAmbiente` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 6 | `anlTempModulos` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 7 | `anlChuva` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 8 | `anlGHI` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 9 | `anlPOA` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 10 | `anlAlbedo` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 11 | `anlVelVento` | fMedidaAnalogica |  | S | S |  |  | Format \| Fonte.Value |  |
| 12 | `linkGrupoDigitais` | fGrupoDigitais |  | S | S |  |  |  |  |
| 13 | `linkGrupoAnalogicas` | fGrupoAnalogicas |  | S | S |  |  |  |  |
| 14 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 15 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fEMET.CustomConfig` (18 linhas)

<a id="fppc"></a>
### fPPC

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {C26FB609-8A75-4A8E-A937-EB35DBABCD65} · `_IID` = {54995012-F5FA-4942-9163-69B1340A35D9} · `_EVENTIID` = {2FB248D1-A08F-459D-8BE0-C62BA4BF63CE} · `IconPath` = imgPPC · `FriendlyName` = PPC · `InstanceName` = PPC0 · `CustomConfig` = PPC · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (61)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cmdPartidaUsina` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 2 | `cmdParadaUsina` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 3 | `cmdResetTRIP` | fComando |  | S | S |  |  | WEG |  |
| 4 | `cmdResetAlarmes` | fComando |  | S | S |  |  | WEG |  |
| 5 | `cmdModoControleAVR` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 6 | `cmdModoControleDROOP` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 7 | `cmdHabilitaControleDROOP` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 8 | `cmdHabilitaControleAVR` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 9 | `cmdAplicaSPTensao` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 10 | `cmdAplicaSPPotAtiva` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 11 | `cmdAplicaSPPotReativa` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 12 | `cmdAplicaSPFatorPotencia` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 13 | `cmdModoControleComplexo` | fComando |  | S | S |  |  | AUTOMA |  |
| 14 | `cmdModoCtrlGeracaoComplexo` | fComando |  | S | S |  |  | AUTOMA |  |
| 15 | `cmdNivelControleLR` | fComando |  | S | S |  |  | AUTOMA |  |
| 16 | `cmdModoControleReativa` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 17 | `cmdComutarEstadoInversElc01` | fComando |  | S | S |  |  | AUTOMA |  |
| 18 | `cmdComutarEstadoInversElc02` | fComando |  | S | S |  |  | AUTOMA |  |
| 19 | `cmdComutarEstadoInversElc03` | fComando |  | S | S |  |  | AUTOMA |  |
| 20 | `spPotenciaAtiva` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 21 | `spTensao` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 22 | `spFatorPotencia` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 23 | `spPotenciaReativa` | fComando |  | S | S |  |  | WEG, AUTOMA |  |
| 24 | `spRmpDecPotenciaAtiva` | fComando |  | S | S |  |  | AUTOMA |  |
| 25 | `spRmpSubPotenciaAtiva` | fComando |  | S | S |  |  | AUTOMA |  |
| 26 | `spRmpDecPotenciaReativa` | fComando |  | S | S |  |  | AUTOMA |  |
| 27 | `spRmpSubPotenciaReativa` | fComando |  | S | S |  |  | AUTOMA |  |
| 28 | `spPesoPriorGeracaoParque` | fComando |  | S | S |  |  | AUTOMA |  |
| 29 | `anlRetornoCtrlFatorPotencia` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 30 | `anlRetornoCtrlPotenciaReativa` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 31 | `anlRetornoCtrlPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 32 | `anlRetornoCtrlTensao` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 33 | `anlLeituraTensao` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 34 | `anlLeituraFatorPotencia` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 35 | `anlLeituraPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 36 | `anlLeituraPotenciaReativa` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 37 | `anlLeituraFrequencia` | fMedidaAnalogica |  | S | S |  |  | WEG, AUTOMA |  |
| 38 | `anlLeituraRmpSubPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  | AUTOMA |  |
| 39 | `anlLeituraRmpDecPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  | AUTOMA |  |
| 40 | `anlLeituraRmpSubPotenciaReativa` | fMedidaAnalogica |  | S | S |  |  | AUTOMA |  |
| 41 | `anlLeituraRmpDecPotenciaReativa` | fMedidaAnalogica |  | S | S |  |  | AUTOMA |  |
| 42 | `cfgPotAtivaMaxPlanta` | Variant |  | S | S |  |  | WEG, AUTOMA |  |
| 43 | `cfgPotAparenteMaxPlanta` | Variant |  | S | S |  |  | WEG, AUTOMA |  |
| 44 | `cfgTensaoNominal` | Variant |  | S | S |  |  | WEG, AUTOMA |  |
| 45 | `cfgModeloPPC` | Variant |  | S | S |  |  | WEG, AUTOMA |  |
| 46 | `linkGrupoDigitaisPPC` | fGrupoDigitais |  | S | S |  |  | WEG, AUTOMA |  |
| 47 | `linkGrupoAnalogicasPPC` | fGrupoAnalogicas |  | S | S |  |  | WEG, AUTOMA |  |
| 48 | `linkGrupoDigitaisAVR` | fGrupoDigitais |  | S | S |  |  | WEG |  |
| 49 | `linkGrupoDigitaisDROOP` | fGrupoDigitais |  | S | S |  |  | WEG |  |
| 50 | `disStatusPPC` | fMedidaDigital |  | S | S |  |  | WEG |  |
| 51 | `disComunicacaoPPC` | fMedidaDigital |  | S | S |  |  | WEG, AUTOMA |  |
| 52 | `disModoControleAVR` | fMedidaDigital |  | S | S |  |  | WEG, AUTOMA |  |
| 53 | `disModoControleDROOP` | fMedidaDigital |  | S | S |  |  | WEG, AUTOMA |  |
| 54 | `disCLPAtivo` | fMedidaDigital |  | S | S |  |  | AUTOMA |  |
| 55 | `disCtrlPotAtiva` | fMedidaDigital |  | S | S |  |  | WEG, AUTOMA |  |
| 56 | `disCtrlPotReativa` | fMedidaDigital |  | S | S |  |  | WEG, AUTOMA |  |
| 57 | `disCtrlFatorPot` | fMedidaDigital |  | S | S |  |  | WEG, AUTOMA |  |
| 58 | `disCtrlTensao` | fMedidaDigital |  | S | S |  |  | WEG, AUTOMA |  |
| 59 | `cfgPPCType` | Integer | Integer `0` | S | S |  |  | 0 -> Geral (Controle Geral do complexo) \| 1 -> Parque (Controle localizado / por UFV) |  |
| 60 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 61 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fPPC.CustomConfig` (194 linhas)

<a id="fgrupoanalogicas"></a>
### fGrupoAnalogicas

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {1D7B8FDF-A2B5-4DB9-ABF7-B04266E00290} · `_IID` = {BB1793BD-C2CD-4055-A9C6-6DD68958ABE9} · `_EVENTIID` = {FD54EACF-6EA7-4C77-AD5C-CB24632D4C5E} · `IconPath` = imgFolderAnalog · `CustomConfig` = Vincular Medidas · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (70)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `medidaAnalogica01` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 2 | `medidaAnalogica02` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 3 | `medidaAnalogica03` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 4 | `medidaAnalogica04` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 5 | `medidaAnalogica05` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 6 | `medidaAnalogica06` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 7 | `medidaAnalogica07` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 8 | `medidaAnalogica08` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 9 | `medidaAnalogica09` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 10 | `medidaAnalogica10` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 11 | `medidaAnalogica11` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 12 | `medidaAnalogica12` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 13 | `medidaAnalogica13` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 14 | `medidaAnalogica14` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 15 | `medidaAnalogica15` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 16 | `medidaAnalogica16` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 17 | `medidaAnalogica17` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 18 | `medidaAnalogica18` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 19 | `medidaAnalogica19` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 20 | `medidaAnalogica20` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 21 | `medidaAnalogica21` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 22 | `medidaAnalogica22` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 23 | `medidaAnalogica23` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 24 | `medidaAnalogica24` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 25 | `medidaAnalogica25` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 26 | `medidaAnalogica26` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 27 | `medidaAnalogica27` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 28 | `medidaAnalogica28` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 29 | `medidaAnalogica29` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 30 | `medidaAnalogica30` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 31 | `medidaAnalogica31` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 32 | `medidaAnalogica32` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 33 | `medidaAnalogica33` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 34 | `medidaAnalogica34` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 35 | `medidaAnalogica35` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 36 | `medidaAnalogica36` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 37 | `medidaAnalogica37` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 38 | `medidaAnalogica38` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 39 | `medidaAnalogica39` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 40 | `medidaAnalogica40` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 41 | `medidaAnalogica41` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 42 | `medidaAnalogica42` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 43 | `medidaAnalogica43` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 44 | `medidaAnalogica44` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 45 | `medidaAnalogica45` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 46 | `medidaAnalogica46` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 47 | `medidaAnalogica47` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 48 | `medidaAnalogica48` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 49 | `medidaAnalogica49` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 50 | `medidaAnalogica50` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 51 | `medidaAnalogica51` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 52 | `medidaAnalogica52` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 53 | `medidaAnalogica53` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 54 | `medidaAnalogica54` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 55 | `medidaAnalogica55` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 56 | `medidaAnalogica56` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 57 | `medidaAnalogica57` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 58 | `medidaAnalogica58` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 59 | `medidaAnalogica59` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 60 | `medidaAnalogica60` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 61 | `medidaAnalogica61` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 62 | `medidaAnalogica62` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 63 | `medidaAnalogica63` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 64 | `medidaAnalogica64` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 65 | `medidaAnalogica65` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 66 | `medidaAnalogica66` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 67 | `medidaAnalogica67` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 68 | `medidaAnalogica68` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 69 | `medidaAnalogica69` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |
| 70 | `medidaAnalogica70` | fMedidaAnalogica | String `` | S | S |  |  | link com a medida analógica desejada |  |

**Eventos com script:** `fGrupoAnalogicas.CustomConfig` (32 linhas)

<a id="fgrupochaves"></a>
### fgrupoChaves

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {ABC7545B-4D5C-477E-839D-7703F5C52B15} · `_IID` = {4044AEAB-5DC9-4B85-A627-9FFEEAA662B4} · `_EVENTIID` = {57E27E9B-326E-4046-A647-C12B70F5C7B9} · `IconPath` = imgGroupSwitches · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="fgrupocomandos"></a>
### fGrupoComandos

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {DFDB6881-BFD4-4E46-B2B5-8F625ABCD063} · `_IID` = {CFBB5343-75CC-4B6B-88E6-CFB6CCF2001E} · `_EVENTIID` = {EE68DAEE-920A-4FAA-9D9B-4CA082334795} · `IconPath` = imgFolderCommand · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Eventos com script:** `fGrupoComandos.CustomConfig` (6 linhas)

<a id="fgrupodigitais"></a>
### fGrupoDigitais

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {3372BFF6-8262-47F3-89E4-032B7121BEE7} · `_IID` = {6156960F-01EB-4953-9E91-DA8583D670D2} · `_EVENTIID` = {624B217C-B427-4C30-9771-E71A934DF4F8} · `IconPath` = imgFolderDiscrete · `CustomConfig` = Vincular Medidas · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (70)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `medidaDigital01` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 2 | `medidaDigital02` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 3 | `medidaDigital03` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 4 | `medidaDigital04` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 5 | `medidaDigital05` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 6 | `medidaDigital06` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 7 | `medidaDigital07` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 8 | `medidaDigital08` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 9 | `medidaDigital09` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 10 | `medidaDigital10` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 11 | `medidaDigital11` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 12 | `medidaDigital12` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 13 | `medidaDigital13` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 14 | `medidaDigital14` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 15 | `medidaDigital15` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 16 | `medidaDigital16` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 17 | `medidaDigital17` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 18 | `medidaDigital18` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 19 | `medidaDigital19` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 20 | `medidaDigital20` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 21 | `medidaDigital21` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 22 | `medidaDigital22` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 23 | `medidaDigital23` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 24 | `medidaDigital24` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 25 | `medidaDigital25` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 26 | `medidaDigital26` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 27 | `medidaDigital27` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 28 | `medidaDigital28` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 29 | `medidaDigital29` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 30 | `medidaDigital30` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 31 | `medidaDigital31` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 32 | `medidaDigital32` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 33 | `medidaDigital33` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 34 | `medidaDigital34` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 35 | `medidaDigital35` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 36 | `medidaDigital36` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 37 | `medidaDigital37` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 38 | `medidaDigital38` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 39 | `medidaDigital39` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 40 | `medidaDigital40` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 41 | `medidaDigital41` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 42 | `medidaDigital42` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 43 | `medidaDigital43` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 44 | `medidaDigital44` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 45 | `medidaDigital45` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 46 | `medidaDigital46` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 47 | `medidaDigital47` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 48 | `medidaDigital48` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 49 | `medidaDigital49` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 50 | `medidaDigital50` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 51 | `medidaDigital51` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 52 | `medidaDigital52` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 53 | `medidaDigital53` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 54 | `medidaDigital54` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 55 | `medidaDigital55` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 56 | `medidaDigital56` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 57 | `medidaDigital57` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 58 | `medidaDigital58` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 59 | `medidaDigital59` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 60 | `medidaDigital60` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 61 | `medidaDigital61` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 62 | `medidaDigital62` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 63 | `medidaDigital63` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 64 | `medidaDigital64` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 65 | `medidaDigital65` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 66 | `medidaDigital66` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 67 | `medidaDigital67` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 68 | `medidaDigital68` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 69 | `medidaDigital69` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |
| 70 | `medidaDigital70` | fMedidaDigital | String `` | S | S |  |  | link com a medida digital desejada |  |

**Eventos com script:** `fGrupoDigitais.CustomConfig` (76 linhas)

<a id="fcluster"></a>
### fCluster

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**  ·  Conjunto de MPPTs
- Metadados: `_CLSID` = {765D0C34-28EB-4A3F-BA04-1D93B79A7B58} · `_IID` = {3B1DFFC8-DCCC-4A27-9DFA-1565401B85CD} · `_EVENTIID` = {2220BAC7-B33B-4DEB-8516-F55DBC2E39CD} · `IconPath` = imgCluster · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (9)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `CorrenteAtual` | Variant | Integer `0` | S | S |  |  |  |  |
| 2 | `TensaoMedia` | Variant | Integer `0` | S | S |  |  |  |  |
| 3 | `CorrenteMaxima` | Variant | Integer `0` | S | S |  |  | Corrente em Ponto de Máxima Potência |  |
| 4 | `MPPT01` | MPPT |  | S | S |  |  | Link com o MPPT |  |
| 5 | `MPPT02` | MPPT |  | S | S |  |  | Link com o MPPT |  |
| 6 | `MPPT03` | MPPT |  | S | S |  |  | Link com o MPPT |  |
| 7 | `MPPT04` | MPPT |  | S | S |  |  | Link com o MPPT |  |
| 8 | `MPPT05` | MPPT |  | S | S |  |  | Link com o MPPT |  |
| 9 | `MPPT06` | MPPT |  | S | S |  |  | Link com o MPPT |  |

<a id="fgrupotrackers"></a>
### fGrupoTrackers

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {5A926E40-1DAD-41FE-B492-B3B3B928F42F} · `_IID` = {95325FBE-3FCA-45EF-B5ED-642FBE08D9C5} · `_EVENTIID` = {DD23CB24-5F6B-4FFE-9ED9-1AC3CAA52EFE} · `IconPath` = Motors\ServoMotor2 · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="finversor"></a>
### fInversor

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {92AC6F9A-E41E-4165-9D48-C322B48CE473} · `_IID` = {4010FDF7-93E8-4A38-967A-9B0F48D250F8} · `_EVENTIID` = {27C5F369-9A72-4CCB-93A9-61824D313A63} · `IconPath` = imgInverter · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (27)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `MODELO` | Variant | String `` | S | S |  |  | Modelo do Inversor |  |
| 2 | `FABRICANTE` | Variant | String `-` | S | S |  |  | Fabricante do Inversor: TBEA \| HUAWEI \| WEG \| INTELBRAS \| SUNGROW \| GROWATT |  |
| 3 | `POT_NOMINAL` | Variant | Integer `0` | S | S |  |  | Potência Máxima do Inversor \| Exemplo: 200 (Unidade em kW) |  |
| 4 | `POT_ATIVA` | Variant | Integer `0` | S | S |  |  |  |  |
| 5 | `STATUS` | Variant | Boolean `False` | S | S |  |  |  |  |
| 6 | `COMUNICACAO` | Variant |  | S | S |  |  |  |  |
| 7 | `Alarmes` | Variant | Integer `0` | S | S |  |  | Vinculação com os alarmes ativos no equipamento |  |
| 8 | `cmdSTART` | fComando |  | S | S |  |  | Link comando START na pasta de Dados - BD |  |
| 9 | `cmdSTOP` | fComando |  | S | S |  |  | Link comando STOP na pasta de Dados - BD |  |
| 10 | `linkSTATUS` | fMedidaDigital |  | S | S |  |  | Link com o STATUS do Inversor |  |
| 11 | `linkStrings` | fGrupoStrings |  | S | S |  |  | link com o Grupo de Strings (PV) |  |
| 12 | `FiltroTrk` | Boolean | Boolean `False` | S | S |  |  | Valor atua quando o objeto cEquipFiltro estiver atuado |  |
| 13 | `linkGrupoAnalogicas` | fGrupoAnalogicas |  | S | S |  |  | Analógicas |  |
| 14 | `linkGrupoDigitais` | fGrupoDigitais |  | S | S |  |  | Digitais |  |
| 15 | `disStatusResumido` | fMedidaDigital |  | S | S |  |  |  |  |
| 16 | `anlEnergiaDia` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 17 | `anlPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 18 | `anlTemperatura` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 19 | `cmdManual` | fComando |  | S | S |  |  |  |  |
| 20 | `cmdAutomatico` | fComando |  | S | S |  |  |  |  |
| 21 | `cmdSPPotenciaAtiva` | fComando |  | S | S |  |  |  |  |
| 22 | `cmdSPPotenciaReativa` | fComando |  | S | S |  |  |  |  |
| 23 | `cfgFabricante` | String |  | S | S |  |  |  |  |
| 24 | `cfgModelo` | String |  | S | S |  |  |  |  |
| 25 | `cfgPotenciaNominal` | Variant |  | S | S |  |  |  |  |
| 26 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 27 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fInversor.CustomConfig` (2898 linhas)

<a id="fmedidaanalogica"></a>
### fMedidaAnalogica

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {9DF61B76-D8E5-436B-BDC4-C7C227234564} · `_IID` = {3D1D6DEE-C008-47C7-9B39-79DA3967C4FE} · `_EVENTIID` = {14E9098D-4D2C-41BF-AAAB-2BA0BB265E20} · `IconPath` = imgAnalog · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Format` | Format |  | S | S | S |  |  |  |
| 2 | `Fonte` | IOTag |  | S | S |  |  | IOTag vinculada \| Para acessar as propriedades, necessário realizar ponteiros corretamente. |  |
| 3 | `Value` | Variant |  | S |  | S |  | Vincular com o Valor da Fonte |  |
| 4 | `Quality` | Variant |  | S |  | S |  | Vincular com a Qualidade da Fonte. |  |
| 5 | `TimeStamp` | Variant |  | S |  | S |  | Vincular com o TimeStamp da Fonte. |  |

**Eventos com script:** `fMedidaAnalogica.CustomConfig` (5 linhas)

<a id="fmedidadigital"></a>
### fMedidaDigital

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {800BE9F1-6756-4320-BDAC-7845D03204E9} · `_IID` = {3F697E12-E147-45D7-AB9F-8FD98D49A6FD} · `_EVENTIID` = {D5B62381-EA17-4DB5-9993-D0C21DEC69BE} · `IconPath` = imgDiscrete · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (7)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Variant | Boolean `True` | S |  | S |  |  |  |
| 2 | `Quality` | Variant |  | S |  | S |  |  |  |
| 3 | `TimeStamp` | Variant |  | S |  | S |  |  |  |
| 4 | `Fonte` | IOTag |  | S | S |  |  | Tag do  Driver |  |
| 5 | `cfgDescritivoValores` | Variant |  | S |  | S |  | Configurar com conexão por tabela, onde deverá ser configurado o valor para cada status. Exemplo: 0 (False) = Desabilitado \| 1 (True) = Habilitado |  |
| 6 | `cfgTipoMedidaDigital` | Boolean | Boolean `True` | S | S | S |  | True -> Discreto (Fonte.Value) \| False -> Bit (Parent.Fonte.Bitxx) \| |  |
| 7 | `cfgVirtualMode` | Boolean | Boolean `False` | S | S | S |  | True -> Virtual Point \| False -> Acquisition Point |  |

**Eventos com script:** `fMedidaDigital.CustomConfig` (56 linhas)

<a id="fgrupostrings"></a>
### fGrupoStrings

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {9F5A0DB4-1FA1-4549-861A-533019B92821} · `_IID` = {DEA613B5-B2F2-49C3-87DA-633E6812B18E} · `_EVENTIID` = {EE0653D5-3F1F-464F-9782-184B588388FB} · `IconPath` = imgMPPT · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (36)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `CorrenteAtual` | Variant | Integer `0` | S | S |  |  |  |  |
| 2 | `TensaoMedia` | Variant | Integer `0` | S | S |  |  |  |  |
| 3 | `CorrenteMaxima` | Variant | Integer `0` | S | S |  |  | Corrente em Ponto de Máxima Potência |  |
| 4 | `STG01` | fString |  | S | S |  |  | Link com a STG |  |
| 5 | `STG02` | fString |  | S | S |  |  | Link com a STG |  |
| 6 | `STG03` | fString |  | S | S |  |  | Link com a STG |  |
| 7 | `STG04` | fString |  | S | S |  |  | Link com a STG |  |
| 8 | `STG05` | fString |  | S | S |  |  | Link com a STG |  |
| 9 | `STG06` | fString |  | S | S |  |  | Link com a STG |  |
| 10 | `STG07` | fString |  | S | S |  |  | Link com a STG |  |
| 11 | `STG08` | fString |  | S | S |  |  | Link com a STG |  |
| 12 | `STG09` | fString |  | S | S |  |  | Link com a STG |  |
| 13 | `STG10` | fString |  | S | S |  |  | Link com a STG |  |
| 14 | `STG11` | fString |  | S | S |  |  | Link com a STG |  |
| 15 | `STG12` | fString |  | S | S |  |  | Link com a STG |  |
| 16 | `STG13` | fString |  | S | S |  |  | Link com a STG |  |
| 17 | `STG14` | fString |  | S | S |  |  | Link com a STG |  |
| 18 | `STG15` | fString |  | S | S |  |  | Link com a STG |  |
| 19 | `STG16` | fString |  | S | S |  |  | Link com a STG |  |
| 20 | `STG17` | fString |  | S | S |  |  | Link com a STG |  |
| 21 | `STG18` | fString |  | S | S |  |  | Link com a STG |  |
| 22 | `STG19` | fString |  | S | S |  |  | Link com a STG |  |
| 23 | `STG20` | fString |  | S | S |  |  | Link com a STG |  |
| 24 | `STG21` | fString |  | S | S |  |  | Link com a STG |  |
| 25 | `STG22` | fString |  | S | S |  |  | Link com a STG |  |
| 26 | `STG23` | fString |  | S | S |  |  | Link com a STG |  |
| 27 | `STG24` | fString |  | S | S |  |  | Link com a STG |  |
| 28 | `STG25` | fString |  | S | S |  |  | Link com a STG |  |
| 29 | `STG26` | fString |  | S | S |  |  | Link com a STG |  |
| 30 | `STG27` | fString |  | S | S |  |  | Link com a STG |  |
| 31 | `STG28` | fString |  | S | S |  |  | Link com a STG |  |
| 32 | `STG29` | fString |  | S | S |  |  | Link com a STG |  |
| 33 | `STG30` | fString |  | S | S |  |  | Link com a STG |  |
| 34 | `anlPotenciaCC` | fMedidaAnalogica |  | S | S |  |  | Link com a Potência CC do Inversor |  |
| 35 | `cfgPotNominalInv` | Variant |  | S | S |  |  | Custom Config - Vínculo via associação com o Inversor |  |
| 36 | `cfgStringsConectadas` | Integer |  | S | S |  |  |  |  |

**Eventos com script:** `fGrupoStrings.CustomConfig` (35 linhas)

<a id="fmultimedidor"></a>
### fMultimedidor

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {117B7619-209E-4508-9BF0-35F5317469AF} · `_IID` = {2A81A0B2-3819-4EFC-8FA3-6F85D32E28BA} · `_EVENTIID` = {B9AAA835-CCD4-4AB9-B5E4-B0E641A702A2} · `IconPath` = imgMultimeter · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (13)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `FABRICANTE` | Variant |  | S | S |  |  |  |  |
| 2 | `MODELO` | Variant |  | S | S |  |  |  |  |
| 3 | `StatusComunicacao` | Boolean |  | S | S |  |  | Vincular condição para que caso perca a comunicação, o resultado seja 'False'. |  |
| 4 | `ID` | Variant |  | S | S |  |  | Identificação que será aplicada na tela |  |
| 5 | `anlTensao` | fMedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 6 | `anlCorrente` | fMedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 7 | `anlFatorPotencia` | fMedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 8 | `anlPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 9 | `anlPotenciaReativa` | fMedidaAnalogica |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 10 | `linkGrupoDigitais` | fGrupoDigitais |  | S | S |  |  |  |  |
| 11 | `linkGrupoAnalogicas` | fGrupoAnalogicas |  | S | S |  |  |  |  |
| 12 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 13 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fMultimedidor.CustomConfig` (29 linhas)

<a id="fncu"></a>
### fNCU

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {657E3D17-AA22-4B22-9856-EFF2CEDDC1BE} · `_IID` = {4A878E1E-BA58-4273-9C4A-BE6B5C5755D0} · `_EVENTIID` = {33A30B2C-A0DD-4E11-9E69-2BF677F8AC2D} · `IconPath` = Sensors\InfraredCO2Analyzer · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (196)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgStatusComunicacao` | Boolean | Boolean `False` | S | S |  |  | Vincular condição para que caso perca a comunicação, o resultado seja 'False'. |  |
| 2 | `cfgTotalTrackers` | Variant |  | S | S |  |  |  |  |
| 3 | `TRK001` | fTracker |  | S | S |  |  |  |  |
| 4 | `TRK002` | fTracker |  | S | S |  |  |  |  |
| 5 | `TRK003` | fTracker |  | S | S |  |  |  |  |
| 6 | `TRK004` | fTracker |  | S | S |  |  |  |  |
| 7 | `TRK005` | fTracker |  | S | S |  |  |  |  |
| 8 | `TRK006` | fTracker |  | S | S |  |  |  |  |
| 9 | `TRK007` | fTracker |  | S | S |  |  |  |  |
| 10 | `TRK008` | fTracker |  | S | S |  |  |  |  |
| 11 | `TRK009` | fTracker |  | S | S |  |  |  |  |
| 12 | `TRK010` | fTracker |  | S | S |  |  |  |  |
| 13 | `TRK011` | fTracker |  | S | S |  |  |  |  |
| 14 | `TRK012` | fTracker |  | S | S |  |  |  |  |
| 15 | `TRK013` | fTracker |  | S | S |  |  |  |  |
| 16 | `TRK014` | fTracker |  | S | S |  |  |  |  |
| 17 | `TRK015` | fTracker |  | S | S |  |  |  |  |
| 18 | `TRK016` | fTracker |  | S | S |  |  |  |  |
| 19 | `TRK017` | fTracker |  | S | S |  |  |  |  |
| 20 | `TRK018` | fTracker |  | S | S |  |  |  |  |
| 21 | `TRK019` | fTracker |  | S | S |  |  |  |  |
| 22 | `TRK020` | fTracker |  | S | S |  |  |  |  |
| 23 | `TRK021` | fTracker |  | S | S |  |  |  |  |
| 24 | `TRK022` | fTracker |  | S | S |  |  |  |  |
| 25 | `TRK023` | fTracker |  | S | S |  |  |  |  |
| 26 | `TRK024` | fTracker |  | S | S |  |  |  |  |
| 27 | `TRK025` | fTracker |  | S | S |  |  |  |  |
| 28 | `TRK026` | fTracker |  | S | S |  |  |  |  |
| 29 | `TRK027` | fTracker |  | S | S |  |  |  |  |
| 30 | `TRK028` | fTracker |  | S | S |  |  |  |  |
| 31 | `TRK029` | fTracker |  | S | S |  |  |  |  |
| 32 | `TRK030` | fTracker |  | S | S |  |  |  |  |
| 33 | `TRK031` | fTracker |  | S | S |  |  |  |  |
| 34 | `TRK032` | fTracker |  | S | S |  |  |  |  |
| 35 | `TRK033` | fTracker |  | S | S |  |  |  |  |
| 36 | `TRK034` | fTracker |  | S | S |  |  |  |  |
| 37 | `TRK035` | fTracker |  | S | S |  |  |  |  |
| 38 | `TRK036` | fTracker |  | S | S |  |  |  |  |
| 39 | `TRK037` | fTracker |  | S | S |  |  |  |  |
| 40 | `TRK038` | fTracker |  | S | S |  |  |  |  |
| 41 | `TRK039` | fTracker |  | S | S |  |  |  |  |
| 42 | `TRK040` | fTracker |  | S | S |  |  |  |  |
| 43 | `TRK041` | fTracker |  | S | S |  |  |  |  |
| 44 | `TRK042` | fTracker |  | S | S |  |  |  |  |
| 45 | `TRK043` | fTracker |  | S | S |  |  |  |  |
| 46 | `TRK044` | fTracker |  | S | S |  |  |  |  |
| 47 | `TRK045` | fTracker |  | S | S |  |  |  |  |
| 48 | `TRK046` | fTracker |  | S | S |  |  |  |  |
| 49 | `TRK047` | fTracker |  | S | S |  |  |  |  |
| 50 | `TRK048` | fTracker |  | S | S |  |  |  |  |
| 51 | `TRK049` | fTracker |  | S | S |  |  |  |  |
| 52 | `TRK050` | fTracker |  | S | S |  |  |  |  |
| 53 | `TRK051` | fTracker |  | S | S |  |  |  |  |
| 54 | `TRK052` | fTracker |  | S | S |  |  |  |  |
| 55 | `TRK053` | fTracker |  | S | S |  |  |  |  |
| 56 | `TRK054` | fTracker |  | S | S |  |  |  |  |
| 57 | `TRK055` | fTracker |  | S | S |  |  |  |  |
| 58 | `TRK056` | fTracker |  | S | S |  |  |  |  |
| 59 | `TRK057` | fTracker |  | S | S |  |  |  |  |
| 60 | `TRK058` | fTracker |  | S | S |  |  |  |  |
| 61 | `TRK059` | fTracker |  | S | S |  |  |  |  |
| 62 | `TRK060` | fTracker |  | S | S |  |  |  |  |
| 63 | `TRK061` | fTracker |  | S | S |  |  |  |  |
| 64 | `TRK062` | fTracker |  | S | S |  |  |  |  |
| 65 | `TRK063` | fTracker |  | S | S |  |  |  |  |
| 66 | `TRK064` | fTracker |  | S | S |  |  |  |  |
| 67 | `TRK065` | fTracker |  | S | S |  |  |  |  |
| 68 | `TRK066` | fTracker |  | S | S |  |  |  |  |
| 69 | `TRK067` | fTracker |  | S | S |  |  |  |  |
| 70 | `TRK068` | fTracker |  | S | S |  |  |  |  |
| 71 | `TRK069` | fTracker |  | S | S |  |  |  |  |
| 72 | `TRK070` | fTracker |  | S | S |  |  |  |  |
| 73 | `TRK071` | fTracker |  | S | S |  |  |  |  |
| 74 | `TRK072` | fTracker |  | S | S |  |  |  |  |
| 75 | `TRK073` | fTracker |  | S | S |  |  |  |  |
| 76 | `TRK074` | fTracker |  | S | S |  |  |  |  |
| 77 | `TRK075` | fTracker |  | S | S |  |  |  |  |
| 78 | `TRK076` | fTracker |  | S | S |  |  |  |  |
| 79 | `TRK077` | fTracker |  | S | S |  |  |  |  |
| 80 | `TRK078` | fTracker |  | S | S |  |  |  |  |
| 81 | `TRK079` | fTracker |  | S | S |  |  |  |  |
| 82 | `TRK080` | fTracker |  | S | S |  |  |  |  |
| 83 | `TRK081` | fTracker |  | S | S |  |  |  |  |
| 84 | `TRK082` | fTracker |  | S | S |  |  |  |  |
| 85 | `TRK083` | fTracker |  | S | S |  |  |  |  |
| 86 | `TRK084` | fTracker |  | S | S |  |  |  |  |
| 87 | `TRK085` | fTracker |  | S | S |  |  |  |  |
| 88 | `TRK086` | fTracker |  | S | S |  |  |  |  |
| 89 | `TRK087` | fTracker |  | S | S |  |  |  |  |
| 90 | `TRK088` | fTracker |  | S | S |  |  |  |  |
| 91 | `TRK089` | fTracker |  | S | S |  |  |  |  |
| 92 | `TRK090` | fTracker |  | S | S |  |  |  |  |
| 93 | `TRK091` | fTracker |  | S | S |  |  |  |  |
| 94 | `TRK092` | fTracker |  | S | S |  |  |  |  |
| 95 | `TRK093` | fTracker |  | S | S |  |  |  |  |
| 96 | `TRK094` | fTracker |  | S | S |  |  |  |  |
| 97 | `TRK095` | fTracker |  | S | S |  |  |  |  |
| 98 | `TRK096` | fTracker |  | S | S |  |  |  |  |
| 99 | `TRK097` | fTracker |  | S | S |  |  |  |  |
| 100 | `TRK098` | fTracker |  | S | S |  |  |  |  |
| 101 | `TRK099` | fTracker |  | S | S |  |  |  |  |
| 102 | `TRK100` | fTracker |  | S | S |  |  |  |  |
| 103 | `TRK101` | fTracker |  | S | S |  |  |  |  |
| 104 | `TRK102` | fTracker |  | S | S |  |  |  |  |
| 105 | `TRK103` | fTracker |  | S | S |  |  |  |  |
| 106 | `TRK104` | fTracker |  | S | S |  |  |  |  |
| 107 | `TRK105` | fTracker |  | S | S |  |  |  |  |
| 108 | `TRK106` | fTracker |  | S | S |  |  |  |  |
| 109 | `TRK107` | fTracker |  | S | S |  |  |  |  |
| 110 | `TRK108` | fTracker |  | S | S |  |  |  |  |
| 111 | `TRK109` | fTracker |  | S | S |  |  |  |  |
| 112 | `TRK110` | fTracker |  | S | S |  |  |  |  |
| 113 | `TRK111` | fTracker |  | S | S |  |  |  |  |
| 114 | `TRK112` | fTracker |  | S | S |  |  |  |  |
| 115 | `TRK113` | fTracker |  | S | S |  |  |  |  |
| 116 | `TRK114` | fTracker |  | S | S |  |  |  |  |
| 117 | `TRK115` | fTracker |  | S | S |  |  |  |  |
| 118 | `TRK116` | fTracker |  | S | S |  |  |  |  |
| 119 | `TRK117` | fTracker |  | S | S |  |  |  |  |
| 120 | `TRK118` | fTracker |  | S | S |  |  |  |  |
| 121 | `TRK119` | fTracker |  | S | S |  |  |  |  |
| 122 | `TRK120` | fTracker |  | S | S |  |  |  |  |
| 123 | `TRK121` | fTracker |  | S | S |  |  |  |  |
| 124 | `TRK122` | fTracker |  | S | S |  |  |  |  |
| 125 | `TRK123` | fTracker |  | S | S |  |  |  |  |
| 126 | `TRK124` | fTracker |  | S | S |  |  |  |  |
| 127 | `TRK125` | fTracker |  | S | S |  |  |  |  |
| 128 | `TRK126` | fTracker |  | S | S |  |  |  |  |
| 129 | `TRK127` | fTracker |  | S | S |  |  |  |  |
| 130 | `TRK128` | fTracker |  | S | S |  |  |  |  |
| 131 | `TRK129` | fTracker |  | S | S |  |  |  |  |
| 132 | `TRK130` | fTracker |  | S | S |  |  |  |  |
| 133 | `TRK131` | fTracker |  | S | S |  |  |  |  |
| 134 | `TRK132` | fTracker |  | S | S |  |  |  |  |
| 135 | `TRK133` | fTracker |  | S | S |  |  |  |  |
| 136 | `TRK134` | fTracker |  | S | S |  |  |  |  |
| 137 | `TRK135` | fTracker |  | S | S |  |  |  |  |
| 138 | `TRK136` | fTracker |  | S | S |  |  |  |  |
| 139 | `TRK137` | fTracker |  | S | S |  |  |  |  |
| 140 | `TRK138` | fTracker |  | S | S |  |  |  |  |
| 141 | `TRK139` | fTracker |  | S | S |  |  |  |  |
| 142 | `TRK140` | fTracker |  | S | S |  |  |  |  |
| 143 | `TRK141` | fTracker |  | S | S |  |  |  |  |
| 144 | `TRK142` | fTracker |  | S | S |  |  |  |  |
| 145 | `TRK143` | fTracker |  | S | S |  |  |  |  |
| 146 | `TRK144` | fTracker |  | S | S |  |  |  |  |
| 147 | `TRK145` | fTracker |  | S | S |  |  |  |  |
| 148 | `TRK146` | fTracker |  | S | S |  |  |  |  |
| 149 | `TRK147` | fTracker |  | S | S |  |  |  |  |
| 150 | `TRK148` | fTracker |  | S | S |  |  |  |  |
| 151 | `TRK149` | fTracker |  | S | S |  |  |  |  |
| 152 | `TRK150` | fTracker |  | S | S |  |  |  |  |
| 153 | `TRK151` | fTracker |  | S | S |  |  |  |  |
| 154 | `TRK152` | fTracker |  | S | S |  |  |  |  |
| 155 | `TRK153` | fTracker |  | S | S |  |  |  |  |
| 156 | `TRK154` | fTracker |  | S | S |  |  |  |  |
| 157 | `TRK155` | fTracker |  | S | S |  |  |  |  |
| 158 | `TRK156` | fTracker |  | S | S |  |  |  |  |
| 159 | `TRK157` | fTracker |  | S | S |  |  |  |  |
| 160 | `TRK158` | fTracker |  | S | S |  |  |  |  |
| 161 | `TRK159` | fTracker |  | S | S |  |  |  |  |
| 162 | `TRK160` | fTracker |  | S | S |  |  |  |  |
| 163 | `TRK161` | fTracker |  | S | S |  |  |  |  |
| 164 | `TRK162` | fTracker |  | S | S |  |  |  |  |
| 165 | `TRK163` | fTracker |  | S | S |  |  |  |  |
| 166 | `TRK164` | fTracker |  | S | S |  |  |  |  |
| 167 | `TRK165` | fTracker |  | S | S |  |  |  |  |
| 168 | `TRK166` | fTracker |  | S | S |  |  |  |  |
| 169 | `TRK167` | fTracker |  | S | S |  |  |  |  |
| 170 | `TRK168` | fTracker |  | S | S |  |  |  |  |
| 171 | `TRK169` | fTracker |  | S | S |  |  |  |  |
| 172 | `TRK170` | fTracker |  | S | S |  |  |  |  |
| 173 | `TRK171` | fTracker |  | S | S |  |  |  |  |
| 174 | `TRK172` | fTracker |  | S | S |  |  |  |  |
| 175 | `TRK173` | fTracker |  | S | S |  |  |  |  |
| 176 | `TRK174` | fTracker |  | S | S |  |  |  |  |
| 177 | `TRK175` | fTracker |  | S | S |  |  |  |  |
| 178 | `TRK176` | fTracker |  | S | S |  |  |  |  |
| 179 | `TRK177` | fTracker |  | S | S |  |  |  |  |
| 180 | `TRK178` | fTracker |  | S | S |  |  |  |  |
| 181 | `TRK179` | fTracker |  | S | S |  |  |  |  |
| 182 | `TRK180` | fTracker |  | S | S |  |  |  |  |
| 183 | `TR-PYR01` | fTracker |  | S | S |  |  | Vincular com o Tracker que possui piranômetro |  |
| 184 | `TR-PYR02` | fTracker |  | S | S |  |  | Vincular com o Tracker que possui piranômetro |  |
| 185 | `TR-PYR03` | fTracker |  | S | S |  |  | Vincular com o Tracker que possui piranômetro |  |
| 186 | `TR-PYR04` | fTracker |  | S | S |  |  | Vincular com o Tracker que possui piranômetro |  |
| 187 | `medRSUVelVento` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 188 | `cmdModoManual` | fComando |  | S | S |  |  |  |  |
| 189 | `cmdModoAutomatico` | fComando |  | S | S |  |  |  |  |
| 190 | `cmdPosSegLimpeza` | fComando |  | S | S |  |  |  |  |
| 191 | `cmdPosSegVento` | fComando |  | S | S |  |  |  |  |
| 192 | `cmdPosSegNeve` | fComando |  | S | S |  |  |  |  |
| 193 | `cfgAlarmes` | Variant |  | S | S |  |  |  |  |
| 194 | `disStatus` | fMedidaDigital |  | S | S |  |  |  |  |
| 195 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 196 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fNCU.CustomConfig` (44 linhas)

<a id="fqgbt"></a>
### fQGBT

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {30255DC7-9BB6-4E1C-9683-889CF52FE52F} · `_IID` = {0E42E72B-50DB-41D2-9A13-BBE76BF8098A} · `_EVENTIID` = {CDDD359D-41FE-4C2A-86AA-FF07F37D3D33} · `IconPath` = imgQGBT · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="frsu"></a>
### fRSU

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {E7E4F58E-9CA4-4A4C-B319-0744AFC2F8D8} · `_IID` = {C59486DF-ABCF-4C47-ABD9-A4EC096F32BF} · `_EVENTIID` = {8597C9F6-8332-4EEF-97BD-BB4B0F7B524C} · `IconPath` = Sensors\SolarThermometer · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="fstringbox"></a>
### fStringBox

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {A1009488-84A1-46A5-AA0C-2CE9A1ED37AD} · `_IID` = {D61456B1-EEC5-444D-82FB-14322C41B5E7} · `_EVENTIID` = {494EFB76-4CF2-42E5-A281-898399677CB6} · `IconPath` = imgArray · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (8)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `CorrenteAtual` | Variant |  | S | S |  |  |  |  |
| 2 | `TensaoAtual` | Variant |  | S | S |  |  |  |  |
| 3 | `QtdModulos` | Variant |  | S | S |  |  |  |  |
| 4 | `CorrenteMaxima` | Variant |  | S | S |  |  |  |  |
| 5 | `linkGrupoAnalogicas` | fGrupoAnalogicas |  | S | S |  |  |  |  |
| 6 | `linkGrupoDigitais` | fGrupoDigitais |  | S | S |  |  |  |  |
| 7 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 8 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fStringBox.CustomConfig` (32 linhas)

<a id="fstring"></a>
### fString

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {9FAF32DD-C614-4B7F-ACE4-3951434938CB} · `_IID` = {839CC1D5-0A94-45C1-A0A3-8F32E0DFACDB} · `_EVENTIID` = {CA225A9D-3897-4CE0-950D-4497C7F2E72A} · `IconPath` = imgStringPV · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (8)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `anlCorrente` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 2 | `anlTensao` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 3 | `cfgQtdModulos` | Variant |  | S | S |  |  |  |  |
| 4 | `cfgImpp` | Variant |  | S | S |  |  | Corrente do ponto máximo de potência - Módulo |  |
| 5 | `cfgStringAtiva` | Boolean | Boolean `True` | S | S |  |  |  |  |
| 6 | `cfgIDStringConectada` | Variant |  | S | S |  |  | ID da String conectada |  |
| 7 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 8 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fString.CustomConfig` (26 linhas)

<a id="fsubestacao"></a>
### fSubestacao

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {1A5A8903-FCE2-4612-BDD5-4688424BA0ED} · `_IID` = {461F7A82-0CBD-4EFA-B9ED-16C38AF988D2} · `_EVENTIID` = {83152046-14E8-4B48-A86F-DCD373609C1C} · `IconPath` = imgSubstation · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="ftracker"></a>
### fTracker

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {22FA7AF1-96D4-43EA-888A-1B8AEFE33FDE} · `_IID` = {1E0E17FC-7720-4B66-9D8A-81C18592ED9E} · `_EVENTIID` = {08A6A8B8-3205-4D72-84BB-1279E54075D8} · `IconPath` = imgTracker · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (12)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `ID` | Variant |  | S | S |  |  | ID do Tracker |  |
| 2 | `UFV` | Variant |  | S | S |  |  | UFV pertencente |  |
| 3 | `Grupo` | Variant |  | S | S |  |  | Grupo de controle |  |
| 4 | `ANG_ALVO` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 5 | `ANG_ATUAL` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 6 | `linkGrupoAnalogicas` | fGrupoAnalogicas |  | S | S |  |  |  |  |
| 7 | `linkGrupoDigitais` | fGrupoDigitais |  | S | S |  |  |  |  |
| 8 | `Alarmes` | Variant |  | S | S |  |  |  |  |
| 9 | `cfgArray` | fArray |  | S | S |  |  |  |  |
| 10 | `linkCOMUNICACAO` | fMedidaDigital |  | S | S |  |  | Link com a COMUNICAÇÃO do Tracker |  |
| 11 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 12 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fTracker.CustomConfig` (484 linhas)

<a id="ftransformador"></a>
### fTransformador

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {7552346C-1A1C-4531-8BD1-150917570A30} · `_IID` = {B9FAA380-0544-467E-8468-73F3369CE111} · `_EVENTIID` = {C7DCF5D8-B5AD-4E6B-8600-3B176FCD1E32} · `IconPath` = imgTransformer · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (70)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `ID` | Variant | String `-` | S | S |  |  | Identificação do Trafo |  |
| 2 | `Primario` | Variant | String `-` | S | S |  |  | Relação de Transformação. Exemplo: 34,5kV/800V |  |
| 3 | `Capacidade` | Variant | Integer `0` | S | S |  |  | MVA |  |
| 4 | `Secundario` | Variant | String `-` | S | S |  |  | Relação de Transformação. Exemplo: 34,5kV/800V |  |
| 5 | `MedidaDigital01` | MedidaDigital |  | S | S |  |  |  |  |
| 6 | `MedidaDigital02` | MedidaDigital |  | S | S |  |  |  |  |
| 7 | `MedidaDigital03` | MedidaDigital |  | S | S |  |  |  |  |
| 8 | `MedidaDigital04` | MedidaDigital |  | S | S |  |  |  |  |
| 9 | `MedidaDigital05` | MedidaDigital |  | S | S |  |  |  |  |
| 10 | `MedidaDigital06` | MedidaDigital |  | S | S |  |  |  |  |
| 11 | `MedidaDigital07` | MedidaDigital |  | S | S |  |  |  |  |
| 12 | `MedidaDigital08` | MedidaDigital |  | S | S |  |  |  |  |
| 13 | `MedidaDigital09` | MedidaDigital |  | S | S |  |  |  |  |
| 14 | `MedidaDigital10` | MedidaDigital |  | S | S |  |  |  |  |
| 15 | `MedidaDigital11` | MedidaDigital |  | S | S |  |  |  |  |
| 16 | `MedidaDigital12` | MedidaDigital |  | S | S |  |  |  |  |
| 17 | `MedidaDigital13` | MedidaDigital |  | S | S |  |  |  |  |
| 18 | `MedidaDigital14` | MedidaDigital |  | S | S |  |  |  |  |
| 19 | `MedidaDigital15` | MedidaDigital |  | S | S |  |  |  |  |
| 20 | `MedidaDigital16` | MedidaDigital |  | S | S |  |  |  |  |
| 21 | `MedidaDigital17` | MedidaDigital |  | S | S |  |  |  |  |
| 22 | `MedidaDigital18` | MedidaDigital |  | S | S |  |  |  |  |
| 23 | `MedidaDigital19` | MedidaDigital |  | S | S |  |  |  |  |
| 24 | `MedidaDigital20` | MedidaDigital |  | S | S |  |  |  |  |
| 25 | `MedidaDigital21` | MedidaDigital |  | S | S |  |  |  |  |
| 26 | `MedidaDigital22` | MedidaDigital |  | S | S |  |  |  |  |
| 27 | `MedidaDigital23` | MedidaDigital |  | S | S |  |  |  |  |
| 28 | `MedidaDigital24` | MedidaDigital |  | S | S |  |  |  |  |
| 29 | `MedidaDigital25` | MedidaDigital |  | S | S |  |  |  |  |
| 30 | `MedidaDigital26` | MedidaDigital |  | S | S |  |  |  |  |
| 31 | `MedidaDigital27` | MedidaDigital |  | S | S |  |  |  |  |
| 32 | `MedidaDigital28` | MedidaDigital |  | S | S |  |  |  |  |
| 33 | `MedidaDigital29` | MedidaDigital |  | S | S |  |  |  |  |
| 34 | `MedidaDigital30` | MedidaDigital |  | S | S |  |  |  |  |
| 35 | `MedidaDigital31` | MedidaDigital |  | S | S |  |  |  |  |
| 36 | `MedidaAnalogica01` | MedidaAnalogica |  | S | S |  |  |  |  |
| 37 | `MedidaAnalogica02` | MedidaAnalogica |  | S | S |  |  |  |  |
| 38 | `MedidaAnalogica03` | MedidaAnalogica |  | S | S |  |  |  |  |
| 39 | `MedidaAnalogica04` | MedidaAnalogica |  | S | S |  |  |  |  |
| 40 | `MedidaAnalogica05` | MedidaAnalogica |  | S | S |  |  |  |  |
| 41 | `MedidaAnalogica06` | MedidaAnalogica |  | S | S |  |  |  |  |
| 42 | `MedidaAnalogica07` | MedidaAnalogica |  | S | S |  |  |  |  |
| 43 | `MedidaAnalogica08` | MedidaAnalogica |  | S | S |  |  |  |  |
| 44 | `MedidaAnalogica09` | MedidaAnalogica |  | S | S |  |  |  |  |
| 45 | `MedidaAnalogica10` | MedidaAnalogica |  | S | S |  |  |  |  |
| 46 | `MedidaAnalogica11` | MedidaAnalogica |  | S | S |  |  |  |  |
| 47 | `MedidaAnalogica12` | MedidaAnalogica |  | S | S |  |  |  |  |
| 48 | `Comando01` | Comando |  | S | S |  |  |  |  |
| 49 | `Comando02` | Comando |  | S | S |  |  |  |  |
| 50 | `Comando03` | Comando |  | S | S |  |  |  |  |
| 51 | `Comando04` | Comando |  | S | S |  |  |  |  |
| 52 | `Comando05` | Comando |  | S | S |  |  |  |  |
| 53 | `TrafoSE` | Boolean | Boolean `True` | S | S |  |  | Alterar para True caso o transformador seja para SE |  |
| 54 | `cmdLigarVF` | Comando |  | S | S |  |  | Vincular ao comando de Ligar VF |  |
| 55 | `cmdDesligarVF` | Comando |  | S | S |  |  | Vincular ao comando de DesligarvVF |  |
| 56 | `cmdSELECLigarVF` | Comando |  | S | S |  |  | Vincular ao comando de Seleção LigarvVF |  |
| 57 | `cmdSELECDesligarVF` | Comando |  | S | S |  |  | Vincular ao comando de Seleção Desligar VF |  |
| 58 | `cmdManualAutomaticoCSC` | Comando |  | S | S |  |  | Vincular ao comando de Manual/Automático CSC |  |
| 59 | `cmdSubirTap` | Comando |  | S | S |  |  | Vincular ao comando de Subir Tap |  |
| 60 | `cmdDescerTap` | Comando |  | S | S |  |  | Vincular ao comando de Descer Tap |  |
| 61 | `PosTap` | MedidaAnalogica |  | S | S |  |  | Vincular a Medida Analógica da Posição do Tap |  |
| 62 | `StatusVF` | MedidaDigital |  | S | S |  |  | Vincular a Medida Digital com o Status da VF |  |
| 63 | `StatusCDC_ManualAutomatico` | MedidaDigital |  | S | S |  |  | Vincular a Medida Digital com o Status DO CDC |  |
| 64 | `StatusCDC_LocalRemoto` | MedidaDigital |  | S | S |  |  | Vincular a Medida Digital com o Status DO CDC |  |
| 65 | `TrafoPV` | Boolean | Boolean `False` | S | S |  |  | Alterar para True caso o transformador seja para PV , padrão GD'S |  |
| 66 | `cmdLigarVF2` | Comando |  | S | S |  |  | Vincular ao comando de Ligar VF2 |  |
| 67 | `cmdDesligarVF2` | Comando |  | S | S |  |  | Vincular ao comando de DesligarvVF2 |  |
| 68 | `cmdSELECLigarVF2` | Comando |  | S | S |  |  | Vincular ao comando de Seleção LigarvVF2 |  |
| 69 | `cmdSELECDesligarVF2` | Comando |  | S | S |  |  | Vincular ao comando de Seleção Desligar VF2 |  |
| 70 | `StatusVF2` | MedidaDigital |  | S | S |  |  | Vincular a Medida Digital com o Status da VF2 |  |

<a id="farray"></a>
### fArray

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**  ·  Conjunto de Strings
- Metadados: `_CLSID` = {BEB188B2-AAF6-41A5-B11D-859CD6FD5235} · `_IID` = {4ECEAE51-7C57-43B5-9DB6-4F382CD57DA7} · `_EVENTIID` = {3999B3DE-A7F9-40F7-8263-DABBCB97937F} · `IconPath` = imgArray · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (10)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `STG-A1` | fString |  | S | S |  |  |  |  |
| 2 | `STG-A2` | fString |  | S | S |  |  |  |  |
| 3 | `STG-B1` | fString |  | S | S |  |  |  |  |
| 4 | `STG-B2` | fString |  | S | S |  |  |  |  |
| 5 | `STG-C1` | fString |  | S | S |  |  |  |  |
| 6 | `STG-C2` | fString |  | S | S |  |  |  |  |
| 7 | `Tracker` | fTracker |  | S | S |  |  | Vínculo com o Tracker do Array |  |
| 8 | `FiltroInversor01` | Variant | Boolean `False` | S | S |  |  | Associar ao Inversor 01 que esse Tracker Pertence |  |
| 9 | `FiltroInversor02` | Variant | Boolean `False` | S | S |  |  | Associar ao Inversor 02 que esse Tracker Pertence  |  |
| 10 | `FiltroInversor03` | Variant | Boolean `False` | S | S |  |  | Associar ao Inversor 03 que esse Tracker Pertence  |  |

<a id="fbarramento"></a>
### fBarramento

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {494966EC-BB9A-4BD9-99DE-D81FB9202F0E} · `_IID` = {BCBE0373-2860-4476-B036-8126AE1E37E9} · `_EVENTIID` = {14D39B61-53A8-4E24-BCF9-20A35A9B50CD} · `IconPath` = imgBar · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="fconector"></a>
### fConector

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {E746D781-2FBD-4C13-89D9-ED0E09A3F238} · `_IID` = {EF8B449F-820E-4FC2-ADF2-C56D2C1BBC52} · `_EVENTIID` = {85A10AAA-6161-4788-93C8-AD68A7CAAC7D} · `IconPath` = imgConnector · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="feletrocentro"></a>
### fEletrocentro

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {0DAC93B8-7A29-418F-81BF-299F868A6AC6} · `_IID` = {88212C4C-D920-4658-83BB-ACFC0B1AE55C} · `_EVENTIID` = {16FDEE4C-6714-4890-9B47-E8BA2F587190} · `IconPath` = imgEletrocentro · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (11)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Alarmes` | Variant | Integer `0` | S |  |  |  | Vinculação com os alarmes ativos no equipamento |  |
| 2 | `cmdStartStop` | Comando |  | S | S |  |  | Link comando START e STOP na pasta de Dados - BD |  |
| 3 | `StatusComunicacao` | Boolean | Boolean `False` | S | S |  |  | Vincular condição para que caso perca a comunicação, o resultado seja 'False'. |  |
| 4 | `anlPotenciaAtiva` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 5 | `anEnergiaDia` | fMedidaAnalogica |  | S | S |  |  |  |  |
| 6 | `anlInversoresAway` | InternalTag |  | S | S |  |  |  |  |
| 7 | `anlInversoresOperating` | InternalTag |  | S | S |  |  |  |  |
| 8 | `anlInversoresStandby` | InternalTag |  | S | S |  |  |  |  |
| 9 | `anlInversoresFail` | InternalTag |  | S | S |  |  |  |  |
| 10 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 11 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fEletrocentro.CustomConfig` (48 linhas)

<a id="fcircuito"></a>
### fCircuito

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {09CA5058-B28D-42B8-B55E-E9B8AD07C03A} · `_IID` = {8E38880D-9113-4CA5-8762-F063DA4B94A5} · `_EVENTIID` = {B7846001-FFED-4873-B80A-2C16AC3FD7EB} · `IconPath` = imgCircuito · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="fgerador"></a>
### fGerador

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {1AB55271-226F-4DC9-8C9D-BD8E54ED96B7} · `_IID` = {A2F522B7-7A78-4F97-9442-0789481F1EF2} · `_EVENTIID` = {0DD04DCB-C088-4E3E-9867-7D12D2765EB2} · `IconPath` = iconGerador · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (9)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgId` | String |  | S | S |  |  | Identificação Operativa |  |
| 2 | `cfgSupervisao` | Boolean | Boolean `False` | S | S | S |  | Se Valor = False, então o equipamento será considerado MANUAL, com tags internas, sem aquisição e sem controle. |  |
| 3 | `cfgPlanta` | Variant |  | S | S |  |  | Nome da Planta |  |
| 4 | `linkGrupoAnalogicas` | fGrupoAnalogicas |  | S | S |  |  | Vincular ao Grupo de Analógicas |  |
| 5 | `linkGrupoDigitais` | fGrupoDigitais |  | S | S |  |  | Vincular ao Grupo de Digitais |  |
| 6 | `cmdExecPartir` | fComando |  | S | S |  |  | Vincular ao comando de EXECUTE PARTIR \| PONTO SIMPLES |  |
| 7 | `cmdExecParar` | fComando |  | S | S |  |  | Vincular ao comando de EXECUTE PARAR \| PONTO SIMPLES |  |
| 8 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 9 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fGerador.CustomConfig` (8 linhas)

<a id="fcomcloud"></a>
### fComCloud

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {56C94DC2-A978-4A39-9823-6C6C817BD252} · `_IID` = {817B91AF-3A18-4395-8D16-AD437678B7A0} · `_EVENTIID` = {31AF72A7-31C3-4FCB-997B-09B646C092FA} · `IconPath` = imgComCloud · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |

<a id="fcomconnection"></a>
### fComConnection

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {2F7DE2D6-8DFE-477C-8DC7-54498A1FFE2F} · `_IID` = {615F9846-89EA-4FBE-A7C9-E189FD786CBB} · `_EVENTIID` = {AEA23613-DC1E-480E-976F-D53C54F70DC1} · `IconPath` = imgConnection · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="fcomconverter"></a>
### fComConverter

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {02AF20EA-58B1-4092-864E-BE9F9E0E14AC} · `_IID` = {057B93FE-BF2D-49BB-97E6-76749CFBA44C} · `_EVENTIID` = {A610E1F6-96F9-4A1B-8FA9-A238B1076CB9} · `IconPath` = imgComConverter · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (25)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIP` | Variant | String `0.0.0.0` | S | S |  |  |  |  |
| 2 | `cfgSerialType` | Integer | Integer `0` | S | S |  |  | 0 - N/A \| 1 - RS485 \| 2 - RS232 |  |
| 3 | `cfgConverterType` | Integer | Integer `0` | S | S |  |  | 0 - DIO \| 1 - SERIAL/ETH \| RS485-RS232 |  |
| 4 | `cfgPhysicalLayer01` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 5 | `cfgPhysicalLayer02` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 6 | `cfgProtocol` | Integer | Integer `0` | S | S |  |  | 0 - N/A \| 1 - Modbus TCP \| 2 - Modbus RTU \| 3 - IEC104 \| 4 - DNP3 \| 5 - MQTT |  |
| 7 | `linkFibra01` | Link |  | S | S |  |  | Infra |  |
| 8 | `linkFibra02` | Link |  | S | S |  |  | Infra |  |
| 9 | `linkFibra03` | Link |  | S | S |  |  | Infra |  |
| 10 | `linkFibra04` | Link |  | S | S |  |  | Infra |  |
| 11 | `linkFibra05` | Link |  | S | S |  |  | Infra |  |
| 12 | `linkFibra06` | Link |  | S | S |  |  | Infra |  |
| 13 | `linkEthernet01` | Link |  | S | S |  |  | Infra |  |
| 14 | `linkEthernet02` | Link |  | S | S |  |  | Infra |  |
| 15 | `linkEthernet03` | Link |  | S | S |  |  | Infra |  |
| 16 | `linkEthernet04` | Link |  | S | S |  |  | Infra |  |
| 17 | `linkEthernet05` | Link |  | S | S |  |  | Infra |  |
| 18 | `linkEthernet06` | Link |  | S | S |  |  | Infra |  |
| 19 | `linkSerial01` | Link |  | S | S |  |  | Infra |  |
| 20 | `linkSerial02` | Link |  | S | S |  |  | Infra |  |
| 21 | `linkSerial03` | Link |  | S | S |  |  | Infra |  |
| 22 | `linkSerial04` | Link |  | S | S |  |  | Infra |  |
| 23 | `linkSerial05` | Link |  | S | S |  |  | Infra |  |
| 24 | `linkSerial06` | Link |  | S | S |  |  | Infra |  |
| 25 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |

<a id="fcomfirewall"></a>
### fComFirewall

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {C8813547-AB2B-49CB-9D0E-E5AFFD0CE20E} · `_IID` = {8C90D4F8-6EC7-40A6-9B5E-B560F21473D6} · `_EVENTIID` = {6F02560B-4A00-4D5D-924B-BDAA6A626304} · `IconPath` = imgFirewall · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (15)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIP` | Variant | String `0.0.0.0` | S | S |  |  |  |  |
| 2 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |
| 3 | `linkStatusConexao` | IOTag |  | S | S |  |  | Vincular com a Tag de Verificação do Status de Conexão |  |
| 4 | `linkFibra01` | Link |  | S | S |  |  | Infra |  |
| 5 | `linkFibra02` | Link |  | S | S |  |  | Infra |  |
| 6 | `linkFibra03` | Link |  | S | S |  |  | Infra |  |
| 7 | `linkFibra04` | Link |  | S | S |  |  | Infra |  |
| 8 | `linkFibra05` | Link |  | S | S |  |  | Infra |  |
| 9 | `linkFibra06` | Link |  | S | S |  |  | Infra |  |
| 10 | `linkEthernet01` | Link |  | S | S |  |  | Infra |  |
| 11 | `linkEthernet02` | Link |  | S | S |  |  | Infra |  |
| 12 | `linkEthernet03` | Link |  | S | S |  |  | Infra |  |
| 13 | `linkEthernet04` | Link |  | S | S |  |  | Infra |  |
| 14 | `linkEthernet05` | Link |  | S | S |  |  | Infra |  |
| 15 | `linkEthernet06` | Link |  | S | S |  |  | Infra |  |

<a id="fcomied"></a>
### fComIED

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {3BF5C510-9FF3-4FFE-A0E1-1A7367666813} · `_IID` = {372F3D56-A39F-4059-AA92-3AC5F696FDFC} · `_EVENTIID` = {7C4E370E-3AC7-4C9E-A5EC-72DF706F54A4} · `IconPath` = imgIED · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (24)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIP` | Variant | String `0.0.0.0` | S | S |  |  |  |  |
| 2 | `cfgProtocol` | Integer | Integer `0` | S | S |  |  | 0 - N/A \| 1 - Modbus TCP \| 2 - Modbus RTU \| 3 - IEC104 \| 4 - DNP3 \| 5 - MQTT |  |
| 3 | `cfgPhysicalLayer01` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 4 | `cfgPhysicalLayer02` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 5 | `linkFibra01` | Link |  | S | S |  |  | Infra |  |
| 6 | `linkFibra02` | Link |  | S | S |  |  | Infra |  |
| 7 | `linkFibra03` | Link |  | S | S |  |  | Infra |  |
| 8 | `linkFibra04` | Link |  | S | S |  |  | Infra |  |
| 9 | `linkFibra05` | Link |  | S | S |  |  | Infra |  |
| 10 | `linkFibra06` | Link |  | S | S |  |  | Infra |  |
| 11 | `linkEthernet01` | Link |  | S | S |  |  | Infra |  |
| 12 | `linkEthernet02` | Link |  | S | S |  |  | Infra |  |
| 13 | `linkEthernet03` | Link |  | S | S |  |  | Infra |  |
| 14 | `linkEthernet04` | Link |  | S | S |  |  | Infra |  |
| 15 | `linkEthernet05` | Link |  | S | S |  |  | Infra |  |
| 16 | `linkEthernet06` | Link |  | S | S |  |  | Infra |  |
| 17 | `linkSerial01` | Link |  | S | S |  |  | Infra |  |
| 18 | `linkSerial02` | Link |  | S | S |  |  | Infra |  |
| 19 | `linkSerial03` | Link |  | S | S |  |  | Infra |  |
| 20 | `linkSerial04` | Link |  | S | S |  |  | Infra |  |
| 21 | `linkSerial05` | Link |  | S | S |  |  | Infra |  |
| 22 | `linkSerial06` | Link |  | S | S |  |  | Infra |  |
| 23 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |
| 24 | `linkStatusConexao` | IOTag |  | S | S |  |  | Vincular com a Tag de Verificação do Status de Conexão |  |

<a id="fcominternet"></a>
### fComInternet

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {7E6ADEB1-9835-48C6-9B40-AF4D3BB6EDF9} · `_IID` = {7DBEACCF-173D-453B-BBAF-E5864901BC1B} · `_EVENTIID` = {34621905-82FF-4D5A-83C9-02DE1E2641DE} · `IconPath` = imgWireless · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgProvider` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgPhysicalLayer01` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless \| 4 - Satélite \| 5 - Starlink \| 6 - Rádio |  |
| 3 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |

<a id="fcomrack"></a>
### fComRack

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {2937587B-CF49-41F0-9683-D851BC527745} · `_IID` = {E42DB4D3-D6AE-4AD9-BD2E-1FA38839C0F0} · `_EVENTIID` = {EDCC4273-B2E6-436E-9830-64EF2A570EFB} · `IconPath` = imgRack · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (12)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `linkFirewall` | fComFirewall |  | S | S |  |  |  |  |
| 2 | `linkServer` | fComServer |  | S | S |  |  |  |  |
| 3 | `linkIED01` | fComIED |  | S | S |  |  |  |  |
| 4 | `linkIED02` | fComIED |  | S | S |  |  |  |  |
| 5 | `linkIED03` | fComIED |  | S | S |  |  |  |  |
| 6 | `linkIED04` | fComIED |  | S | S |  |  |  |  |
| 7 | `linkIED05` | fComIED |  | S | S |  |  |  |  |
| 8 | `linkIED06` | fComIED |  | S | S |  |  |  |  |
| 9 | `linkIED07` | fComIED |  | S | S |  |  |  |  |
| 10 | `linkIED08` | fComIED |  | S | S |  |  |  |  |
| 11 | `linkIED09` | fComIED |  | S | S |  |  |  |  |
| 12 | `linkIED10` | fComIED |  | S | S |  |  |  |  |

<a id="fcomrouter"></a>
### fComRouter

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {523976FA-F5F3-4DE2-A1CE-0B8FE9DF7720} · `_IID` = {7F073A01-A14C-4847-9564-2069710AB375} · `_EVENTIID` = {FE08F15B-DB99-4226-8A58-61F3651C2AA0} · `IconPath` = imgRouter · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (15)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIP` | Variant | String `0.0.0.0` | S | S |  |  |  |  |
| 2 | `cfgPhysicalLayer01` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 3 | `linkFibra01` | Link |  | S | S |  |  | Infra |  |
| 4 | `linkFibra02` | Link |  | S | S |  |  | Infra |  |
| 5 | `linkFibra03` | Link |  | S | S |  |  | Infra |  |
| 6 | `linkFibra04` | Link |  | S | S |  |  | Infra |  |
| 7 | `linkFibra05` | Link |  | S | S |  |  | Infra |  |
| 8 | `linkFibra06` | Link |  | S | S |  |  | Infra |  |
| 9 | `linkEthernet01` | Link |  | S | S |  |  | Infra |  |
| 10 | `linkEthernet02` | Link |  | S | S |  |  | Infra |  |
| 11 | `linkEthernet03` | Link |  | S | S |  |  | Infra |  |
| 12 | `linkEthernet04` | Link |  | S | S |  |  | Infra |  |
| 13 | `linkEthernet05` | Link |  | S | S |  |  | Infra |  |
| 14 | `linkEthernet06` | Link |  | S | S |  |  | Infra |  |
| 15 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |

<a id="fcomrtu"></a>
### fComRTU

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {7FBB1A8E-8A0C-42DF-8BA5-EE2EC167DE4A} · `_IID` = {C83F06AA-A726-43A5-A373-EEA840E489E6} · `_EVENTIID` = {9827EA73-84EB-4283-82AA-73745C7FA4B9} · `IconPath` = imgRTU · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (24)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIP` | Variant | String `0.0.0.0` | S | S |  |  |  |  |
| 2 | `cfgProtocol` | Integer | Integer `0` | S | S |  |  | 0 - N/A \| 1 - Modbus TCP \| 2 - Modbus RTU \| 3 - IEC104 \| 4 - DNP3 \| 5 - MQTT |  |
| 3 | `cfgPhysicalLayer01` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 4 | `cfgPhysicalLayer02` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 5 | `linkFibra01` | Link |  | S | S |  |  | Infra |  |
| 6 | `linkFibra02` | Link |  | S | S |  |  | Infra |  |
| 7 | `linkFibra03` | Link |  | S | S |  |  | Infra |  |
| 8 | `linkFibra04` | Link |  | S | S |  |  | Infra |  |
| 9 | `linkFibra05` | Link |  | S | S |  |  | Infra |  |
| 10 | `linkFibra06` | Link |  | S | S |  |  | Infra |  |
| 11 | `linkEthernet01` | Link |  | S | S |  |  | Infra |  |
| 12 | `linkEthernet02` | Link |  | S | S |  |  | Infra |  |
| 13 | `linkEthernet03` | Link |  | S | S |  |  | Infra |  |
| 14 | `linkEthernet04` | Link |  | S | S |  |  | Infra |  |
| 15 | `linkEthernet05` | Link |  | S | S |  |  | Infra |  |
| 16 | `linkEthernet06` | Link |  | S | S |  |  | Infra |  |
| 17 | `linkSerial01` | Link |  | S | S |  |  | Infra |  |
| 18 | `linkSerial02` | Link |  | S | S |  |  | Infra |  |
| 19 | `linkSerial03` | Link |  | S | S |  |  | Infra |  |
| 20 | `linkSerial04` | Link |  | S | S |  |  | Infra |  |
| 21 | `linkSerial05` | Link |  | S | S |  |  | Infra |  |
| 22 | `linkSerial06` | Link |  | S | S |  |  | Infra |  |
| 23 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |
| 24 | `linkStatusConexao` | IOTag |  | S | S |  |  | Vincular com a Tag de Verificação do Status de Conexão |  |

<a id="fcomserver"></a>
### fComServer

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {E5E06D1B-16FF-4163-A290-A84048D4BAF8} · `_IID` = {750588FB-335D-43D5-A64F-E94F810AFECC} · `_EVENTIID` = {C0D23418-7CAD-4A17-9BBB-0DF527A1341C} · `IconPath` = imgServer · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (18)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIP` | Variant | String `0.0.0.0` | S | S |  |  |  |  |
| 2 | `cfgProtocol` | Integer | Integer `0` | S | S |  |  | 0 - N/A \| 1 - Modbus TCP \| 2 - Modbus RTU \| 3 - IEC104 \| 4 - DNP3 \| 5 - MQTT |  |
| 3 | `cfgPhysicalLayer01` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 4 | `cfgPhysicalLayer02` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 5 | `linkFibra01` | Link |  | S | S |  |  | Infra |  |
| 6 | `linkFibra02` | Link |  | S | S |  |  | Infra |  |
| 7 | `linkFibra03` | Link |  | S | S |  |  | Infra |  |
| 8 | `linkFibra04` | Link |  | S | S |  |  | Infra |  |
| 9 | `linkFibra05` | Link |  | S | S |  |  | Infra |  |
| 10 | `linkFibra06` | Link |  | S | S |  |  | Infra |  |
| 11 | `linkEthernet01` | Link |  | S | S |  |  | Infra |  |
| 12 | `linkEthernet02` | Link |  | S | S |  |  | Infra |  |
| 13 | `linkEthernet03` | Link |  | S | S |  |  | Infra |  |
| 14 | `linkEthernet04` | Link |  | S | S |  |  | Infra |  |
| 15 | `linkEthernet05` | Link |  | S | S |  |  | Infra |  |
| 16 | `linkEthernet06` | Link |  | S | S |  |  | Infra |  |
| 17 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |
| 18 | `linkStatusConexao` | IOTag |  | S | S |  |  | Vincular com a Tag de Verificação do Status de Conexão |  |

<a id="fcomswitch"></a>
### fComSwitch

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {C0DE088C-F128-4AFA-AF5A-AB53A53EAB0A} · `_IID` = {5D12D152-143E-4B66-AB2D-A2DCC0543A46} · `_EVENTIID` = {D5C12C32-6178-48D7-ACDD-BDF9898067E2} · `IconPath` = imgSwitchInfra · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (17)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIP` | Variant | String `0.0.0.0` | S | S |  |  |  |  |
| 2 | `cfgType` | Boolean | Boolean `False` | S | S |  |  | True - Transparente \| False - Gerenciável |  |
| 3 | `cfgPhysicalLayer01` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 4 | `cfgPhysicalLayer02` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet \| 1 - Serial \| 2 - Fibra \| 3 - Wireless |  |
| 5 | `linkFibra01` | Link |  | S | S |  |  | Infra |  |
| 6 | `linkFibra02` | Link |  | S | S |  |  | Infra |  |
| 7 | `linkFibra03` | Link |  | S | S |  |  | Infra |  |
| 8 | `linkFibra04` | Link |  | S | S |  |  | Infra |  |
| 9 | `linkFibra05` | Link |  | S | S |  |  | Infra |  |
| 10 | `linkFibra06` | Link |  | S | S |  |  | Infra |  |
| 11 | `linkEthernet01` | Link |  | S | S |  |  | Infra |  |
| 12 | `linkEthernet02` | Link |  | S | S |  |  | Infra |  |
| 13 | `linkEthernet03` | Link |  | S | S |  |  | Infra |  |
| 14 | `linkEthernet04` | Link |  | S | S |  |  | Infra |  |
| 15 | `linkEthernet05` | Link |  | S | S |  |  | Infra |  |
| 16 | `linkEthernet06` | Link |  | S | S |  |  | Infra |  |
| 17 | `anlLatencia` | Variant |  | S | S |  |  | Recebe o resultado do Script de ping |  |

<a id="fcomvpn"></a>
### fComVPN

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {BF319C68-6246-462C-8DD9-468409E664DF} · `_IID` = {643329A5-29AA-4F67-BAAF-F1B730C45BCA} · `_EVENTIID` = {5C25C620-F8B1-46CA-898A-9EE28E9E94A7} · `IconPath` = imgLock · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgName` | Variant |  | S | S |  |  |  |  |

<a id="fmppt"></a>
### fMPPT

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {1B1F0BC5-8DDE-4ECA-B2B0-39B3C394AB1C} · `_IID` = {69FA9087-E5FE-44BD-ABEB-2A0757CC0D3B} · `_EVENTIID` = {2939995A-9783-4B49-A62E-CEEEF6E57101} · `IconPath` = imgMPPT · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (9)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `CorrenteAtual` | Variant | Integer `0` | S | S |  |  |  |  |
| 2 | `TensaoMedia` | Variant | Integer `0` | S | S |  |  |  |  |
| 3 | `CorrenteMaxima` | Variant | Integer `0` | S | S |  |  | Corrente em Ponto de Máxima Potência |  |
| 4 | `STG01` | Strings |  | S | S |  |  | Link com a STG |  |
| 5 | `STG02` | Strings |  | S | S |  |  | Link com a STG |  |
| 6 | `STG03` | Strings |  | S | S |  |  | Link com a STG |  |
| 7 | `STG04` | Strings |  | S | S |  |  | Link com a STG |  |
| 8 | `STG05` | Strings |  | S | S |  |  | Link com a STG |  |
| 9 | `STG06` | Strings |  | S | S |  |  | Link com a STG |  |

**Eventos com script:** `fMPPT.CustomConfig` (18 linhas)

<a id="fmedidadigitalbit"></a>
### fMedidaDigitalBit

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {4B119ED4-BD3A-41C0-A9FA-9C58E715B2D3} · `_IID` = {95AFB110-7E0E-4BDA-9609-DDEC8984498C} · `_EVENTIID` = {2CADF48B-3FEB-44E6-82F2-9F72B8E81959} · `IconPath` = imgDiscrete · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

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

**Eventos com script:** `fMedidaDigitalBit.CustomConfig` (56 linhas)

<a id="fobjscadapowercontrol"></a>
### fObjScadaPowerControl

- Biblioteca: `matrixenergylibxfolderpv.lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {37943D0B-215E-456C-AB36-DA802578DF6B} · `_IID` = {02B79A48-1DA4-423E-990F-2EA72E22A2DA} · `_EVENTIID` = {3D0C3C4F-8508-458B-8AF5-B1ACADDB664D} · `IconPath` = imgSpc · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cmdSpActivePower` | fComando | String `Dados.Analog.[RETORNO-SETPOINT]` | S | S |  |  |  |  |
| 2 | `cmdControlMode` | fComando | String `Dados.Command.[MODO-CONTROLE]` | S | S |  |  |  |  |
| 3 | `disControlMode` | fMedidaDigital | String `Dados.Digital.[MODO-CONTROLE]` | S | S |  |  |  |  |
| 4 | `anlReturnSpActivePower` | fMedidaAnalogica | String `Dados.Analog.[RETORNO-SETPOINT]` | S | S |  |  |  |  |
| 5 | `cfgPotenciaAtivaMaxPlanta` | Double |  | S | S |  |  | em kW |  |

---

## Biblioteca `matrixenergylibxfolderse .lib`

<a id="fchave0se"></a>
### fChave0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {6729F72D-B0EA-4C87-A125-D81BFC25A5C4} · `_IID` = {3452366D-67B3-41D8-9429-A671EB822EE1} · `_EVENTIID` = {34E332B9-292E-4669-A401-43EDE7EE0B97} · `IconPath` = imgSwitch · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (16)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `disEstado` | fMedidaDigital0se | Boolean `True` | S | S |  |  |  |  |
| 2 | `IDOperativo` | String | String `` | S | S | S |  |  |  |
| 3 | `cfgSupervisao` | Integer | Integer `0` | S | S | S |  | 0 -> Manual \| 1 -> Supervisão \| 2 -> Supervisão e Controle |  |
| 4 | `cfgDefaultPositionType` | Integer | Integer `0` | S | S |  |  | 0 -> 2103 \| 1 -> 1203 \| 2-> 01 \| |  |
| 5 | `cmdPontoDuplo` | Boolean |  | S | S |  |  | Alterar para True em caso de Comando de Ponto Duplo (cmdSelect + cmdExecute) |  |
| 6 | `cmdTipoComando` | Boolean |  | S | S |  |  | False = Execute Only \| True = Select + Execute |  |
| 7 | `cmdSELECT` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT \| PONTO DUPLO |  |
| 8 | `cmdEXEC` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE \| PONTO DUPLO |  |
| 9 | `cmdRSTPROT` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 10 | `cmdSELECTRSTPROT` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 11 | `cmdABRIR` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE ABRIR \| PONTO SIMPLES |  |
| 12 | `cmdFECHAR` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE FECHAR \| PONTO SIMPLES |  |
| 13 | `cmdSELECTABRIR` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT ABRIR \| PONTO SIMPLES |  |
| 14 | `cmdSELECTFECHAR` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT FECHAR \| PONTO SIMPLES |  |
| 15 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 16 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fChave0se.CustomConfig` (27 linhas)

<a id="fcircuito0se"></a>
### fCircuito0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {F9E59293-53D2-4371-A0AD-462DFC5AC7B9} · `_IID` = {3A44A154-8DC5-4B34-BB44-7106DD6B59A4} · `_EVENTIID` = {A0EC9910-A87A-4ABE-AB6C-C28CC3E54ADF} · `IconPath` = imgCircuito · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgAlarmes` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 3 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fCircuito0se.CustomConfig` (3 linhas)

<a id="fcomando0se"></a>
### fComando0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {D867BB98-A7AC-4FE1-8E47-90872B5F1AF4} · `_IID` = {B6FE7351-8F25-4728-B8E0-CA2C76C8C656} · `_EVENTIID` = {34AA8B10-4B7A-4A88-91F5-F24B61FED843} · `IconPath` = imgCommandv2 · `CustomConfig` = Configurar Comando · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Variant |  | S | S |  |  |  |  |
| 2 | `ID` | Variant |  | S | S |  |  |  |  |
| 3 | `Fonte` | IOTag |  | S | S |  |  | Tag do Driver |  |
| 4 | `Event` | Variant |  | S | S |  |  |  |  |
| 5 | `TimeStamp` | Variant |  | S | S |  |  |  |  |

**Eventos com script:** `fComando.CustomConfig` (5 linhas)

<a id="ftransformador0se"></a>
### fTransformador0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {38329521-6346-472D-A53F-F26FCF316EC9} · `_IID` = {49E05723-4ADF-4A50-B8C8-A148BCDE67E8} · `_EVENTIID` = {CE7633CE-4D18-4EA1-9973-31C23F57DA9B} · `IconPath` = imgTransformer · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (29)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `ID` | String | String `-` | S | S |  |  | Identificação do Trafo |  |
| 2 | `Primario` | String | String `-` | S | S |  |  | Relação de Transformação. Exemplo: 34,5kV/800V |  |
| 3 | `Capacidade` | Double | Integer `0` | S | S |  |  | MVA |  |
| 4 | `Secundario` | String | String `-` | S | S |  |  | Relação de Transformação. Exemplo: 34,5kV/800V |  |
| 5 | `linkGrupoDigitais` | fGrupoDigitais0se |  | S | S |  |  |  |  |
| 6 | `linkGrupoAnalogicas` | fGrupoAnalogicas0se |  | S | S |  |  |  |  |
| 7 | `cmdVF1Start` | fComando0se |  | S | S |  |  | Vincular ao comando de Ligar Ventilação Forçada 1º Estágio |  |
| 8 | `cmdVF1Stop` | fComando0se |  | S | S |  |  | Vincular ao comando de Desligar Ventilação Forçada 1º Estágio |  |
| 9 | `cmdVF2Start` | fComando0se |  | S | S |  |  | Vincular ao comando de Ligar Ventilação Forçada 2º Estágio |  |
| 10 | `cmdVF2Stop` | fComando0se |  | S | S |  |  | Vincular ao comando de Desligar Ventilação Forçada 2º Estágio |  |
| 11 | `cmdVF1SelectStart` | fComando0se |  | S | S |  |  | Vincular ao comando de Ligar Ventilação Forçada 1º Estágio |  |
| 12 | `cmdVF2SelectStart` | fComando0se |  | S | S |  |  | Vincular ao comando de Ligar Ventilação Forçada 1º Estágio |  |
| 13 | `cmdVF1SelectStop` | fComando0se |  | S | S |  |  | Vincular ao comando de Ligar Ventilação Forçada 1º Estágio |  |
| 14 | `cmdVF2SelectStop` | fComando0se |  | S | S |  |  | Vincular ao comando de Ligar Ventilação Forçada 1º Estágio |  |
| 15 | `cmdTapUp` | fComando0se |  | S | S |  |  | Vincular ao comando de Subir Tap |  |
| 16 | `cmdTapDown` | fComando0se |  | S | S |  |  | Vincular ao comando de Descer Tap |  |
| 17 | `cmdTapAutomatico` | fComando0se |  | S | S |  |  | Vincular ao comando de Tap Automático |  |
| 18 | `cmdTapManual` | fComando0se |  | S | S |  |  | Vincular ao comando de Tap Manual |  |
| 19 | `cmdReset86` | fComando0se |  | S | S |  |  | Vincular ao comando de Rearme / Reset 86 |  |
| 20 | `cmdCdcManual` | fComando0se |  | S | S |  |  | Vincular ao comando CDC Manual |  |
| 21 | `cmdCdcAutomatico` | fComando0se |  | S | S |  |  | Vincular ao comando CDC Automatico |  |
| 22 | `anlPosTap` | fMedidaAnalogica0se |  | S | S |  |  | Vincular a Medida Analógica da Posição do Tap |  |
| 23 | `disStatusVF` | fMedidaDigital0se |  | S | S |  |  | Vincular a Medida Digital com o Status da VF |  |
| 24 | `disCdcManAut` | fMedidaDigital0se |  | S | S |  |  | Vincular a Medida Digital com o Status DO CDC - Manual ou Automático |  |
| 25 | `disCdcLocalRemoto` | fMedidaDigital0se |  | S | S |  |  | Vincular a Medida Digital com o Status DO CDC - Local ou Remoto |  |
| 26 | `cfgTipoTrafo` | Integer |  | S | S |  |  | 0 - Dyn \| 1 - Ddyn \| 2 - Dydn \| 3 - Dyyn |  |
| 27 | `cfgModoOperacao` | Integer | Integer `1` | S | S |  |  | 1 - Manual (Estático) \| 2 - Supervisionado \| 3 - Telecomandado |  |
| 28 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 29 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fTransformador0se.CustomConfig` (18 linhas)

<a id="fsubestacao0se"></a>
### fSubestacao0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {26ABA1F8-C2F3-4449-B3EC-668C8CA117FA} · `_IID` = {BE4F51EA-3A1E-4176-8B52-D2A4E1229444} · `_EVENTIID` = {92F9AEA0-68A9-4AD6-85CF-0EB6D7E8C259} · `IconPath` = imgSubstation · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTypeConfig` | Integer | Integer `0` | S | S |  |  | 0 - Desligado \| 1 - Configuração dos Equipamentos \| 2 - Configuração dos nomes baseado no cfgCaminhoArquivo \| 3 - Exporta Alarmes \| |  |
| 2 | `cfgCaminhoArquivo` | Variant |  | S | S |  |  |  |  |

**Eventos com script:** `fSubestacao0se.CustomConfig` (1521 linhas)

<a id="fprotection0se"></a>
### fProtection0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {5E916D38-8B7A-4A2D-BEB1-A706DA828341} · `_IID` = {82E5A4EE-94AB-4DD9-A18C-D6ADFD4A7477} · `_EVENTIID` = {B8C1F3D7-11FC-4C32-8CE2-E34E2F822697} · `IconPath` = imgProtection · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="fmedidadigital0se"></a>
### fMedidaDigital0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {C3697613-1C16-46F3-84A0-B347D2B024E0} · `_IID` = {E252A135-FD43-406F-9BBE-21AACEE7079F} · `_EVENTIID` = {55EFF036-02A6-4F23-A8FA-49FA72CA35C5} · `IconPath` = imgDiscrete · `CustomConfig` = Vincular Valores com Fonte · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (7)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Variant | Boolean `True` | S |  | S |  |  |  |
| 2 | `Quality` | Variant |  | S |  | S |  |  |  |
| 3 | `TimeStamp` | Variant |  | S |  | S |  |  |  |
| 4 | `Fonte` | IOTag |  | S | S |  |  | Tag do  Driver |  |
| 5 | `cfgDescritivoValores` | Variant |  | S |  | S |  | Configurar com conexão por tabela, onde deverá ser configurado o valor para cada status. Exemplo: 0 (False) = Desabilitado \| 1 (True) = Habilitado |  |
| 6 | `cfgTipoMedidaDigital` | Boolean | Boolean `True` | S | S | S |  | True -> Discreto (Fonte.Value) \| False -> Bit (Parent.Fonte.Bitxx) \| |  |
| 7 | `cfgVirtualMode` | Boolean | Boolean `False` | S | S | S |  | True -> Virtual Point \| False -> Acquisition Point |  |

**Eventos com script:** `fMedidaDigital0se.CustomConfig` (56 linhas)

<a id="fmedidaanalogica0se"></a>
### fMedidaAnalogica0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {CC9806EE-4B0D-4ACC-B0FE-2212973DE84F} · `_IID` = {C24E77AB-B73B-4B7C-BF53-80843D6C48CE} · `_EVENTIID` = {1909B46E-9987-42F0-8E06-92351B42BF7E} · `IconPath` = imgAnalog · `CustomConfig` = Vincular Valores com Fonte · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Format` | Format |  | S | S | S |  |  |  |
| 2 | `Fonte` | IOTag |  | S | S |  |  | IOTag vinculada \| Para acessar as propriedades, necessário realizar ponteiros corretamente. |  |
| 3 | `Value` | Variant |  | S |  | S |  | Vincular com o Valor da Fonte |  |
| 4 | `Quality` | Variant |  | S |  | S |  | Vincular com a Qualidade da Fonte. |  |
| 5 | `TimeStamp` | Variant |  | S |  | S |  | Vincular com o TimeStamp da Fonte. |  |

**Eventos com script:** `fMedidaAnalogica0se.CustomConfig` (5 linhas)

<a id="fied0se"></a>
### fIED0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {804056EB-1ACC-4EF3-93B5-F871DD076621} · `_IID` = {362AC7D7-1091-4E7A-A4AB-A38492EBDAEC} · `_EVENTIID` = {036C7F86-3959-4C15-918A-3292F7E0EDE9} · `IconPath` = imgIED · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (14)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgProtocol` | Integer | Integer `0` | S | S |  |  | 0 - N/A \| 1 - Modbus TCP \| 2 - Modbus RTU \| 3 - IEC104 \| 4 - DNP3 \| 5 - MQTT |  |
| 2 | `cfgFabricante` | Variant | String `-` | S | S |  |  |  |  |
| 3 | `cfgModelo` | Variant | String `-` | S | S |  |  |  |  |
| 4 | `linkComIED` | fComIED |  | S | S |  |  | Vínculo com o objeto de rede do IED |  |
| 5 | `linkGOOSE01` | fIED0se |  | S | S |  |  | Vínculo GOOSE |  |
| 6 | `linkGOOSE02` | fIED0se |  | S | S |  |  | Vínculo GOOSE |  |
| 7 | `linkGOOSE03` | fIED0se |  | S | S |  |  | Vínculo GOOSE |  |
| 8 | `linkGOOSE04` | fIED0se |  | S | S |  |  | Vínculo GOOSE |  |
| 9 | `linkGOOSE05` | fIED0se |  | S | S |  |  | Vínculo GOOSE |  |
| 10 | `linkGOOSE06` | fIED0se |  | S | S |  |  | Vínculo GOOSE |  |
| 11 | `linkAnalog` | fGrupoAnalogicas0se |  | S | S |  |  | Grupo de Analógicas |  |
| 12 | `linkDigital` | fGrupoDigitais0se |  | S | S |  |  | Grupo de Digitais |  |
| 13 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 14 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fIED0se.CustomConfig` (14 linhas)

<a id="fgrupodigitais0se"></a>
### fGrupoDigitais0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {BD9B8049-3751-4CEB-9FE3-CB88A76BF556} · `_IID` = {0FF5487E-14C8-4901-9599-704EFC712C6F} · `_EVENTIID` = {55157076-A49F-4271-A37D-8378701A7035} · `IconPath` = imgFolderDiscrete · `CustomConfig` = Configurar · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (70)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `medidaDigital01` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 2 | `medidaDigital02` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 3 | `medidaDigital03` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 4 | `medidaDigital04` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 5 | `medidaDigital05` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 6 | `medidaDigital06` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 7 | `medidaDigital07` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 8 | `medidaDigital08` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 9 | `medidaDigital09` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 10 | `medidaDigital10` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 11 | `medidaDigital11` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 12 | `medidaDigital12` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 13 | `medidaDigital13` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 14 | `medidaDigital14` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 15 | `medidaDigital15` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 16 | `medidaDigital16` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 17 | `medidaDigital17` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 18 | `medidaDigital18` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 19 | `medidaDigital19` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 20 | `medidaDigital20` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 21 | `medidaDigital21` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 22 | `medidaDigital22` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 23 | `medidaDigital23` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 24 | `medidaDigital24` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 25 | `medidaDigital25` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 26 | `medidaDigital26` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 27 | `medidaDigital27` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 28 | `medidaDigital28` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 29 | `medidaDigital29` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 30 | `medidaDigital30` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 31 | `medidaDigital31` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 32 | `medidaDigital32` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 33 | `medidaDigital33` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 34 | `medidaDigital34` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 35 | `medidaDigital35` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 36 | `medidaDigital36` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 37 | `medidaDigital37` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 38 | `medidaDigital38` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 39 | `medidaDigital39` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 40 | `medidaDigital40` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 41 | `medidaDigital41` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 42 | `medidaDigital42` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 43 | `medidaDigital43` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 44 | `medidaDigital44` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 45 | `medidaDigital45` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 46 | `medidaDigital46` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 47 | `medidaDigital47` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 48 | `medidaDigital48` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 49 | `medidaDigital49` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 50 | `medidaDigital50` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 51 | `medidaDigital51` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 52 | `medidaDigital52` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 53 | `medidaDigital53` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 54 | `medidaDigital54` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 55 | `medidaDigital55` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 56 | `medidaDigital56` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 57 | `medidaDigital57` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 58 | `medidaDigital58` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 59 | `medidaDigital59` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 60 | `medidaDigital60` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 61 | `medidaDigital61` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 62 | `medidaDigital62` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 63 | `medidaDigital63` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 64 | `medidaDigital64` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 65 | `medidaDigital65` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 66 | `medidaDigital66` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 67 | `medidaDigital67` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 68 | `medidaDigital68` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 69 | `medidaDigital69` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |
| 70 | `medidaDigital70` | fMedidaDigital0se |  | S | S |  |  | link com a medida digital desejada |  |

**Eventos com script:** `fGrupoDigitais0se.CustomConfig` (76 linhas)

<a id="fgrupocomandos0se"></a>
### fGrupoComandos0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {E1595C34-A816-45DE-BC09-098E5FF886F9} · `_IID` = {644CF778-673D-4651-BD0E-2BA9D780E796} · `_EVENTIID` = {426E8D54-705F-4422-857A-34EE2188E33D} · `IconPath` = imgFolderCommand · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Eventos com script:** `GrupoComandos.CustomConfig` (6 linhas)

<a id="fgrupoanalogicas0se"></a>
### fGrupoAnalogicas0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {401ABB45-26AB-47D3-91DC-2BFA4FDC503A} · `_IID` = {A8197D10-5AE2-425D-81BC-3213F56DD533} · `_EVENTIID` = {6218B5E6-F6AE-4F37-9176-8D9E0FCB49D2} · `IconPath` = imgFolderAnalog · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (70)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `medidaAnalogica01` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 2 | `medidaAnalogica02` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 3 | `medidaAnalogica03` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 4 | `medidaAnalogica04` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 5 | `medidaAnalogica05` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 6 | `medidaAnalogica06` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 7 | `medidaAnalogica07` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 8 | `medidaAnalogica08` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 9 | `medidaAnalogica09` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 10 | `medidaAnalogica10` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 11 | `medidaAnalogica11` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 12 | `medidaAnalogica12` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 13 | `medidaAnalogica13` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 14 | `medidaAnalogica14` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 15 | `medidaAnalogica15` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 16 | `medidaAnalogica16` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 17 | `medidaAnalogica17` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 18 | `medidaAnalogica18` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 19 | `medidaAnalogica19` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 20 | `medidaAnalogica20` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 21 | `medidaAnalogica21` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 22 | `medidaAnalogica22` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 23 | `medidaAnalogica23` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 24 | `medidaAnalogica24` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 25 | `medidaAnalogica25` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 26 | `medidaAnalogica26` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 27 | `medidaAnalogica27` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 28 | `medidaAnalogica28` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 29 | `medidaAnalogica29` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 30 | `medidaAnalogica30` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 31 | `medidaAnalogica31` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 32 | `medidaAnalogica32` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 33 | `medidaAnalogica33` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 34 | `medidaAnalogica34` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 35 | `medidaAnalogica35` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 36 | `medidaAnalogica36` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 37 | `medidaAnalogica37` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 38 | `medidaAnalogica38` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 39 | `medidaAnalogica39` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 40 | `medidaAnalogica40` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 41 | `medidaAnalogica41` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 42 | `medidaAnalogica42` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 43 | `medidaAnalogica43` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 44 | `medidaAnalogica44` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 45 | `medidaAnalogica45` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 46 | `medidaAnalogica46` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 47 | `medidaAnalogica47` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 48 | `medidaAnalogica48` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 49 | `medidaAnalogica49` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 50 | `medidaAnalogica50` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 51 | `medidaAnalogica51` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 52 | `medidaAnalogica52` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 53 | `medidaAnalogica53` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 54 | `medidaAnalogica54` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 55 | `medidaAnalogica55` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 56 | `medidaAnalogica56` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 57 | `medidaAnalogica57` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 58 | `medidaAnalogica58` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 59 | `medidaAnalogica59` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 60 | `medidaAnalogica60` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 61 | `medidaAnalogica61` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 62 | `medidaAnalogica62` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 63 | `medidaAnalogica63` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 64 | `medidaAnalogica64` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 65 | `medidaAnalogica65` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 66 | `medidaAnalogica66` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 67 | `medidaAnalogica67` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 68 | `medidaAnalogica68` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 69 | `medidaAnalogica69` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |
| 70 | `medidaAnalogica70` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida analógica desejada |  |

**Eventos com script:** `fGrupoAnalogicas0se.CustomConfig` (50 linhas)

<a id="felectricpanel0se"></a>
### fElectricPanel0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {1908CF7A-DB3F-40BA-9C7F-DA13DB4456F8} · `_IID` = {C404AE3A-6B80-44A5-968E-CB6F211B31CC} · `_EVENTIID` = {4548AF2A-10FC-44F0-936F-3EDA408FA2EA} · `IconPath` = imgQGBT · `FriendlyName` = Painel Elétrico · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `linkDisjuntor` | fDisjuntor0se |  | S | S |  |  |  |  |
| 2 | `linkSecEntrada` | fChave0se |  | S | S |  |  |  |  |
| 3 | `linkSecAterrEntrada` | fChave0se |  | S | S |  |  |  |  |
| 4 | `linkSecSaida` | fChave0se |  | S | S |  |  |  |  |
| 5 | `linkSecAterrSaida` | fChave0se |  | S | S |  |  |  |  |

<a id="fdados0se"></a>
### fDados0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {ED6A3F77-55BE-47B0-91DD-7C03C5BF1445} · `_IID` = {B5C36724-93D5-4AE4-9042-342FD089FE19} · `_EVENTIID` = {003A58D0-093D-412F-B423-C093D9E1C7FA} · `IconPath` = imgFolderMeasurement · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Eventos com script:** `Dados.CustomConfig` (2 linhas)

<a id="fdisjuntor0se"></a>
### fDisjuntor0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {A88832CC-409A-4990-971B-F4631877A219} · `_IID` = {70A7FA45-E70E-4D4A-BFD6-6E51107834F5} · `_EVENTIID` = {9335AE82-68DB-4E5D-B5AB-1B186F8624E0} · `IconPath` = imgCircuitBreaker · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (31)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgId` | String |  | S | S |  |  | Identificação Operativa |  |
| 2 | `cfgSupervisao` | Integer | Integer `2` | S | S | S |  | 0 -> Manual \| 1 -> Supervisão \| 2 -> Supervisão e Controle |  |
| 3 | `cfgFabricante` | Variant |  | S | S |  |  | Fabricante do Equipamento |  |
| 4 | `cfgModelo` | Variant |  | S | S |  |  | Modelo do Equipamento |  |
| 5 | `cfgPlanta` | Variant |  | S | S |  |  | Nome da Planta |  |
| 6 | `cfgAlarmes` | Variant |  | S | S |  |  | Vincular com os Alarmes ativos no equipamento |  |
| 7 | `cfgSelectBeforeOperate` | Boolean |  | S | S |  |  | Alterar para True em caso de Comando que precisa de Select antes de executar =>  cmdSelect + cmdExecute |  |
| 8 | `cfgTipoComando` | Boolean |  | S | S |  |  | [False] -> Single Command \| [True] -> Double Command |  |
| 9 | `cfgDefaultPositionType` | Integer | Integer `0` | S | S |  |  | 0 -> 2103 \| 1 -> 1203 \| 2 -> 01 \| |  |
| 10 | `cmdSelect` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT \| PONTO DUPLO |  |
| 11 | `cmdExecute` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE \| PONTO DUPLO |  |
| 12 | `cmdExecResetProt` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 13 | `cmdSelectResetProt` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT Reset de Proteções do DJ \| PONTO SIMPLES |  |
| 14 | `cmdExecAbrir` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE ABRIR \| PONTO SIMPLES |  |
| 15 | `cmdExecFechar` | fComando0se |  | S | S |  |  | Vincular ao comando de EXECUTE FECHAR \| PONTO SIMPLES |  |
| 16 | `cmdSelectAbrir` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT ABRIR \| PONTO SIMPLES |  |
| 17 | `cmdSelectFechar` | fComando0se |  | S | S |  |  | Vincular ao comando de SELECT FECHAR \| PONTO SIMPLES |  |
| 18 | `cmdHabilitaReligamento` | fComando0se |  | S | S |  |  |  |  |
| 19 | `cmdBloqueiaReligamento` | fComando0se |  | S | S |  |  |  |  |
| 20 | `disEstado` | fMedidaDigital0se | Integer `-4` | S | S |  |  | Vincular com o ponto EST do Relé. |  |
| 21 | `disDisjuntorInserido` | fMedidaDigital0se | Integer `1` | S | S |  |  | Status de Disjuntor Inserido |  |
| 22 | `disLocalRemoto` | fMedidaDigital0se |  | S | S |  |  | Vincular com o status LR \| Local = 1 \| Remoto = 0 |  |
| 23 | `linkGrupoAnalogicas` | fGrupoAnalogicas0se |  | S | S |  |  | Vincular ao Grupo de Analógicas |  |
| 24 | `linkGrupoDigitais` | fGrupoDigitais0se |  | S | S |  |  | Vincular ao Grupo de Digitais |  |
| 25 | `anlVMedia` | fMedidaAnalogica0se |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 26 | `anlIMedia` | fMedidaAnalogica0se |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 27 | `anlFP` | fMedidaAnalogica0se |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 28 | `anlPotenciaAtiva` | fMedidaAnalogica0se |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 29 | `anlPotenciaReativa` | fMedidaAnalogica0se |  | S | S |  |  | Vincular ao item analógico do equipamento. |  |
| 30 | `cfgNoteEnabled` | Boolean | Boolean `False` | S | S | S |  |  |  |
| 31 | `cfgNoteType` | Integer | Integer `0` | S | S | S |  |  |  |

**Eventos com script:** `fDisjuntor0se.CustomConfig` (60 linhas)

<a id="fretificador0se"></a>
### fRetificador0se

- Biblioteca: `matrixenergylibxfolderse .lib`  ·  tipo: **XFolder**
- Metadados: `_CLSID` = {663258F8-3CB6-449E-B23D-EEFC9D423462} · `_IID` = {E823BF6D-D2D5-4304-955C-01641B853443} · `_EVENTIID` = {3411B419-7332-40B0-9689-F109A545CDEF} · `IconPath` = imgInverter · `EnableTagBehavior` = False · `ValueMode` = 0 · `DefaultIsAlarmArea` = False
- Depende de: `Panel.e3`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `linkAnalog` | fGrupoAnalogicas0se |  | S | S |  |  |  |  |
| 2 | `linkDigital` | fGrupoDigitais0se |  | S | S |  |  |  |  |
| 3 | `disStatus` | fMedidaDigital0se |  | S | S |  |  |  |  |
| 4 | `cfgNoteEnabled` | Boolean | Boolean `False` | S |  | S |  |  |  |
| 5 | `cfgNoteType` | Integer | Integer `0` | S |  | S |  |  |  |

**Eventos com script:** `fRetificador0se.CustomConfig` (8 linhas)
