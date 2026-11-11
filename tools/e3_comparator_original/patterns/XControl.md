# XControl — classes das bibliotecas Matrix Energy e suas propriedades

Fonte: arquivos `.lib` em `C:\SCADA_Eng01\01_MatrixEnergy\02_Libraries`. **127 classes**, **225 propriedades/métodos próprios**.

XControl = **componente gráfico** de tela com propriedades próprias (prefixo `c`).

Formato de cada item: metadados da classe (`_CLSID`, `_IID`, `IconPath`…) → propriedades próprias (`XMethod`: tipo, padrão, flags) → tags internas → estrutura interna → associações → scripts → elementos gráficos.

## Propriedades base (herdadas por todas as classes XControl)

Valem para toda classe deste tipo, além das próprias (tabela de cada classe). "Gravado como" = nome no `.prj`; **derivada** = não existe no arquivo, é calculada pelo E3 em tempo de execução. Categorias provisórias (ver `e3base.py`).

| Categoria | Propriedade | Gravado como | Origem | Tipo | Descrição |
|---|---|---|---|---|---|
| Aparência / Gráfico | `Angle` | `Angle` | gravada | Long | Ângulo de rotação |
| Aparência / Gráfico | `Enabled` | `Enabled` | gravada | Boolean | Objeto habilitado |
| Aparência / Gráfico | `Height` | — | binária | Double | Altura = y2 − y1 |
| Aparência / Gráfico | `Layer` | `Layer` | gravada | Long | Camada (0xFFFFFFFF = todas) |
| Aparência / Gráfico | `TabStop` | `TabStop` | gravada | Boolean | Participa da ordem de tabulação |
| Aparência / Gráfico | `Tip` | `Tip` | gravada | String | Dica (tooltip) do objeto gráfico |
| Aparência / Gráfico | `Visible` | `Visible` | gravada | Boolean | Objeto visível |
| Aparência / Gráfico | `Width` | — | binária | Double | Largura = x2 − x1 |
| Aparência / Gráfico | `X` | — | binária | Double | Posição horizontal = x1 do retângulo gravado após o cabeçalho |
| Aparência / Gráfico | `Y` | — | binária | Double | Posição vertical = y1 do retângulo |
| Identificação | `DocString` | `DocString` | gravada | String | Texto de documentação do objeto |
| Identificação | `Name` | `Name` | gravada | String | Nome do objeto |
| Identificação | `PathContainer` | — | derivada | String | Nome completo da pasta/unidade que contém o objeto |
| Identificação | `PathName` | — | derivada | String | Caminho completo do objeto (ex.: Usinas.UFV_CSA.BD.UFV_CSA.SE01) |
| Identificação | `PathVolume` | — | derivada | String | Arquivo do volume (.PRJ/.LIB) onde o objeto está armazenado |

## Índice

| Biblioteca | Classes |
|---|---|
| `matrixenergylibxcontrolbtc.lib` | [cEquipInversorFreq](#cequipinversorfreq), [cEquipMineradorBtc](#cequipmineradorbtc), [cEquipVentilador](#cequipventilador), [cDashCardBtc](#cdashcardbtc), [cDadosContainerBtc](#cdadoscontainerbtc), [cDadosGrupoContainerBtc](#cdadosgrupocontainerbtc) |
| `matrixenergylibxcontrolpv.lib` | [cDashMeteorologicas](#cdashmeteorologicas), [cObjGauge](#cobjgauge), [cDashGauge](#cdashgauge), [cDashCardGeralUsinas](#cdashcardgeralusinas), [cObjLayoutGeral](#cobjlayoutgeral), [cObjMedidaAnalogicaLayout](#cobjmedidaanalogicalayout), [cPainelInversor](#cpainelinversor), [cPainelMedidasTela](#cpainelmedidastela), [cPainelMultimedidor](#cpainelmultimedidor), [cPainelStrings](#cpainelstrings), [cEquipCMB](#cequipcmb), [cEquipInversor](#cequipinversor), [cEquipMeteorologica](#cequipmeteorologica), [cEquipMultimedidor](#cequipmultimedidor), [cEquipPPC](#cequipppc), [cEquipString](#cequipstring), [cEquipStringLayout](#cequipstringlayout), [cEquipTracker](#cequiptracker), [cDetalhesUsina](#cdetalhesusina), [cNavegacaoScreensHeader](#cnavegacaoscreensheader), [cObjSetPoint](#cobjsetpoint), [cObjPosicaoDeBits16b](#cobjposicaodebits16b), [cObjMedidaDigitalLayout](#cobjmedidadigitallayout), [cObjMedidaAnalogicaTela](#cobjmedidaanalogicatela), [cObjHeader](#cobjheader), [cObjCheckBox](#cobjcheckbox), [cObjVideoWall](#cobjvideowall), [cIconeVento](#ciconevento), [cIconeUsuario](#ciconeusuario), [cIconeUmidade](#ciconeumidade), [cIconeTermometro](#ciconetermometro), [cIconeSol](#ciconesol), [cLibAlbedo](#clibalbedo), [cLibChuva](#clibchuva), [cLibGHI](#clibghi), [cLibLogout](#cliblogout), [cLibMapaBrasil](#clibmapabrasil), [cLibPOA](#clibpoa), [cLibTemperatura](#clibtemperatura), [cLibUmidade](#clibumidade), [cEquipArrayLayout](#cequiparraylayout), [cObjAlarme](#cobjalarme), [cPainelTracker](#cpaineltracker), [cEquipFiltro](#cequipfiltro), [cPainelNCU](#cpainelncu), [cEquipNCU](#cequipncu), [cTabularTRK](#ctabulartrk), [cObjBotaoHighPerformance](#cobjbotaohighperformance), [cObjBarGraph](#cobjbargraph), [cObjCardFundo](#cobjcardfundo), [cObjTexto](#cobjtexto), [cEquipStringPainel](#cequipstringpainel), [cTabularResumoUsinas](#ctabularresumousinas), [cDashBarGraph](#cdashbargraph), [cObjMedidaAnalogicaPaineis](#cobjmedidaanalogicapaineis), [cObjMedidaDigitalPaineis](#cobjmedidadigitalpaineis), [cPainelPPC](#cpainelppc), [cDashGaugePaineis](#cdashgaugepaineis), [cObjSelect](#cobjselect), [cIconeAntena01](#ciconeantena01), [cIconeAntena02](#ciconeantena02), [cIconeCFTV](#ciconecftv), [cIconeComputador](#ciconecomputador), [cIconeConversorRede](#ciconeconversorrede), [cIconeDesktop](#ciconedesktop), [cIconeFirewall](#ciconefirewall), [cIconeIED](#ciconeied), [cIconeMedidor](#ciconemedidor), [cIconeRoteador](#ciconeroteador), [cIconeRTU](#ciconertu), [cIconeServidorSimples](#ciconeservidorsimples), [cIconeServidorTriplo](#ciconeservidortriplo), [cIconeSwitchRede](#ciconeswitchrede), [cObjGraph](#cobjgraph), [cObjComConnection](#cobjcomconnection), [cObjElectricConnection](#cobjelectricconnection), [cIconeCloud](#ciconecloud), [cObjTextBox](#cobjtextbox), [cIconePainelSolar](#ciconepainelsolar), [cDashPizzaGraph](#cdashpizzagraph), [cHistPanel](#chistpanel), [cDetalhesAtivo](#cdetalhesativo), [0tempCreateObj](#0tempcreateobj), [cPainelCMB](#cpainelcmb), [cPainelMeteorologica](#cpainelmeteorologica), [cObjHist](#cobjhist), [cPainelResumedMeteo](#cpainelresumedmeteo), [cLibModuloPV](#clibmodulopv), [cObjTelaAlarmes](#cobjtelaalarmes), [cObjNotaOperativa](#cobjnotaoperativa), [cPainelNotaOperativa](#cpainelnotaoperativa), [cObjLogoSCADA](#cobjlogoscada), [cPainelScadaPowerControl](#cpainelscadapowercontrol), [cEquipScadaPowerControl](#cequipscadapowercontrol) |
| `matrixenergylibxcontrolse.lib` | [cPainelTransformadores0se](#cpaineltransformadores0se), [cPainelIED0se](#cpainelied0se), [cPainelDisjuntor0se](#cpaineldisjuntor0se), [cPainelChave0se](#cpainelchave0se), [cObjMedidaDigitalPaineis0se](#cobjmedidadigitalpaineis0se), [cObjMedidaAnalogicaPaineis0se](#cobjmedidaanalogicapaineis0se), [cObjHeader0se](#cobjheader0se), [cObjElectricConnection0se](#cobjelectricconnection0se), [cObjBotaoHighPerformance0se](#cobjbotaohighperformance0se), [cNavegacaoScreensHeader0se](#cnavegacaoscreensheader0se), [cEquipIED0se](#cequipied0se), [cEquipGerador0se](#cequipgerador0se), [cEquipDisjuntor0se](#cequipdisjuntor0se), [cEquipChave0se](#cequipchave0se), [cDashCardGeral0se](#cdashcardgeral0se), [cEquipTrafo0se](#cequiptrafo0se), [cObjCardFundo0se](#cobjcardfundo0se), [cDashBarGraph0se](#cdashbargraph0se), [cEquipRetificador0se](#cequipretificador0se), [cDashGauge0se](#cdashgauge0se), [cDashGaugePequeno0se](#cdashgaugepequeno0se), [cPainelRetificador0se](#cpainelretificador0se), [cEquipBateria0se](#cequipbateria0se), [cObjAnalogScreen0se](#cobjanalogscreen0se), [cObjGround0se](#cobjground0se), [cEquipCUB0se](#cequipcub0se), [cDashGaugePaineis0se](#cdashgaugepaineis0se) |

---

## Biblioteca `matrixenergylibxcontrolbtc.lib`

<a id="cequipinversorfreq"></a>
### cEquipInversorFreq

- Biblioteca: `matrixenergylibxcontrolbtc.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {D8B66B6A-5EAA-413E-99FB-B6409D42E037} · `_IID` = {0E843470-F626-437A-81BA-EB80BDEA2899} · `_EVENTIID` = {CCE8A864-4638-49E6-B403-14EEBE30D962} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `cObjCardFundo`, `TableBind`, `DrawArc`, `DrawLine`, `DrawRect`, `AnimationBind`, `DrawConnector`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fInversorFrequencia |  | S | S |  |  |  |  |
| 2 | `cfgHabilitarAcesso` | Variant | Boolean `True` | S | S |  |  | Habilita ou não o acesso ao painel do Inversor |  |
| 3 | `cfgEnableInfo` | Integer | Integer `1` | S | S |  |  | 1 -> Habilita Informações do Inversor: ID e Gráfico \| 0 -> Desabilita |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (falhaCom, Inversor)
  DrawString ×1 (falhaCom)
  cObjCardFundo ×1 (cObjCardFundo1)
DrawString ×1 (Id)
```

**Eventos com script:** `Corpo.Click` (9 linhas), `BackGround.Click` (9 linhas)

**Elementos gráficos:** DrawLine ×7, DrawGroup ×4, DrawString ×2, DrawArc ×2, DrawRect ×2, DrawConnector ×1

<a id="cequipmineradorbtc"></a>
### cEquipMineradorBtc

- Biblioteca: `matrixenergylibxcontrolbtc.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {368D20F9-864C-4625-A7C4-3B1B3D6FC542} · `_IID` = {7F5F2598-D795-4CEE-BD1A-0822675323CF} · `_EVENTIID` = {0143C365-9AF6-4ECE-ABF0-6FD7E2EFE208} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `cObjCardFundo`, `TableBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oMineradorBtc |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (miner)
  DrawString ×3 (Valor3, Valor2, Valor)
  cObjCardFundo ×1 (cObjCardFundo1)
```

**Elementos gráficos:** DrawString ×3, DrawGroup ×1

<a id="cequipventilador"></a>
### cEquipVentilador

- Biblioteca: `matrixenergylibxcontrolbtc.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {BE2BD0B3-FD24-41D7-8A7E-3830732FDFDE} · `_IID` = {3C594402-91DC-490C-8B25-039D2325216D} · `_EVENTIID` = {296FCFE8-665E-4F8D-9340-58E0BF5CE63E} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawCircle`, `DrawBezier`, `DrawConnector`, `DrawRect`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawCircle ×2 (Circulo1, Circulo2)
  DrawGroup ×1 (Grupo1)
    DrawBezier ×4 (Bezier3, Bezier4, Bezier1, …)
    DrawConnector ×4 (Conector5, Conector4, Conector2, …)
  DrawRect ×1 (Retangulo1)
```

**Elementos gráficos:** DrawBezier ×4, DrawConnector ×4, DrawGroup ×2, DrawCircle ×2, DrawRect ×1

<a id="cdashcardbtc"></a>
### cDashCardBtc

- Biblioteca: `matrixenergylibxcontrolbtc.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {E5E7BA24-954F-42D2-91F0-8914943DA71B} · `_IID` = {11BEDCE7-0197-46BB-A547-94A18E05723A} · `_EVENTIID` = {C31AD45D-1CB6-4B76-A80B-754333C90C4E} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `AnimationBind`, `DrawTank`, `cObjGauge`, `DrawString`, `TableBind`, `cObjCardFundo`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oConfigCardBtc |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Card)
  DrawTank ×2 (falhaCom, RoundRect1)
  cObjGauge ×2 (PowerDraw, HashRate)
  DrawGroup ×2 (header, miners)
    DrawString ×1 (nomePlanta)
    DrawTank ×1 (RoundRect2)
```

**Eventos com script:** `nomePlanta.Click` (38 linhas)

**Elementos gráficos:** DrawString ×9, DrawGroup ×3, DrawTank ×3

<a id="cdadoscontainerbtc"></a>
### cDadosContainerBtc

- Biblioteca: `matrixenergylibxcontrolbtc.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {EB2876FE-EC39-4F46-9E3C-9D7CDFE8EE02} · `_IID` = {B7687124-0F87-43D0-8DC5-4356CC995027} · `_EVENTIID` = {422A92F4-7B73-4853-A2B3-89CD10DA1732} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `cObjCardFundo`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fContainerMineracao |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Container)
  DrawString ×10 (textoMinersHashing, textoMinersOnline, textoTotalMiners, …)
  cObjCardFundo ×1 (back)
```

**Elementos gráficos:** DrawString ×10, DrawGroup ×1

<a id="cdadosgrupocontainerbtc"></a>
### cDadosGrupoContainerBtc

- Biblioteca: `matrixenergylibxcontrolbtc.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {3947E7F2-EE79-4888-B702-4C05740D3C05} · `_IID` = {EA0BD377-6135-4C67-8E0C-3C280451D2DA} · `_EVENTIID` = {224BBBDC-01F6-48D0-ABF9-F77F4AAB160D} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `cObjCardFundo`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDadosContainerBtc |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Container)
  DrawString ×13 (textoMinersHashing, textoMinersOnline, textoTotalMiners, …)
  cObjCardFundo ×1 (back)
```

**Elementos gráficos:** DrawString ×13, DrawGroup ×1

---

## Biblioteca `matrixenergylibxcontrolpv.lib`

<a id="cdashmeteorologicas"></a>
### cDashMeteorologicas

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {49E2805F-06B6-4EAB-9D1C-2E70F7E016C1} · `_IID` = {2E442D2E-5AAD-4267-9796-543AE2B49640} · `_EVENTIID` = {284208B7-3FFA-434C-87D0-8D9607DB8C33} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fEMET |  | S | S |  |  | Fabricante, Modelo, TemperaturaAr, TemperaturaModulos, Chuva, GHI_Regiao1, GHI_Regiao2, POA_Regiao1, POA_Regiao2, Albedo_Regiao1, Albedo_Regiao2, VelVento, DirVento |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
```

**Elementos gráficos:** DrawString ×1

<a id="cobjgauge"></a>
### cObjGauge

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {D6460B06-AA9C-43A0-BFD5-379BA4D0E201} · `_IID` = {55531177-A23D-4940-9F65-47461FC96E86} · `_EVENTIID` = {8985A08F-3EA8-451B-99F9-93D423A25EB1} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawCircle`, `DrawArc`, `AnalogBind`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `valorFiltrado` | Variant |  | S | S |  |  |  |  |
| 2 | `valorMaximo` | Variant |  | S | S |  |  |  |  |
| 3 | `Format` | Format |  | S | S |  |  |  |  |
| 4 | `unidadeMedida` | Format |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Medida, Valor)
DrawCircle ×1 (Centro)
DrawArc ×2 (BordaGrafico, Grafico)
```

**Elementos gráficos:** DrawString ×2, DrawArc ×2, DrawCircle ×1

<a id="cdashgauge"></a>
### cDashGauge

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {88FB0E29-F3A6-47C1-8A56-68A577D99BAC} · `_IID` = {3EC69AA3-8587-46F5-8178-FE27DB101F95} · `_EVENTIID` = {F189D9DB-4F09-4F86-8D8A-FA2BD26A28B1} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawCircle`, `DrawArc`, `AnalogBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigGauge |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×3 (Text1, Medida, Valor)
DrawCircle ×1 (Centro)
DrawArc ×3 (BordaGrafico, BordaGrafico2, Grafico)
```

**Elementos gráficos:** DrawString ×3, DrawArc ×3, DrawCircle ×1

<a id="cdashcardgeralusinas"></a>
### cDashCardGeralUsinas

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B851295B-DB15-4D68-A39C-97F79A7DE577} · `_IID` = {B8F1D535-3927-4106-954E-0BD9E1CC8658} · `_EVENTIID` = {E2CB7718-FF01-4B64-B389-FEF0892BD17D} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `TableBind`, `DrawString`, `cObjCardFundo`, `AnimationBind`, `DrawCircle`, `DrawTank`, `cDashBarGraph`, `cDashGaugePaineis`, `cObjMedidaAnalogicaTela`, `cEquipInversor`, `cLibGHI`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigCardGeralUsinas |  | S | S |  |  |  |  |
| 2 | `SE` | Integer | Integer `1` | S | S |  |  | SE Comissionada = 2 \| SE Não Comissionada = 1 \| Sem SE = 0 |  |
| 3 | `PV` | Integer | Integer `1` | S | S |  |  | PV Comissionada = 2 \| PV Não Comissionada = 1 \| Sem PV = 0 |  |
| 4 | `cfgManutSCADA` | Integer | Integer `0` | S | S |  |  | 0 -> UFV no COG \| 1 -> UFV em manutenção no SCADA |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (manutSCADA, Card)
  DrawString ×1 (Texto4)
  cObjCardFundo ×1 (cObjCardFundo1)
```

**Eventos com script:** `comissSE.Click` (8 linhas), `nomePlanta.Click` (39 linhas), `comissPV.Click` (8 linhas)

**Elementos gráficos:** DrawGroup ×8, DrawString ×8, DrawTank ×3, DrawCircle ×2

<a id="cobjlayoutgeral"></a>
### cObjLayoutGeral

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {D6115AEC-F4A7-41B6-8F80-666859276CF1} · `_IID` = {ECEA5926-E1FF-4AD6-BD6F-E0175125C62C} · `_EVENTIID` = {0FD9A5C6-0AD6-460B-9C3B-113132C8208F} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawTank`, `AnalogBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fInversor |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
DrawTank ×1 (RetanguloArr1)
```

**Elementos gráficos:** DrawString ×1, DrawTank ×1

<a id="cobjmedidaanalogicalayout"></a>
### cObjMedidaAnalogicaLayout

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {E7B2AE9F-3565-44A1-828C-D9EAF1306C9F} · `_IID` = {EF31B5ED-820E-47BE-85BC-31DD9A6CABE7} · `_EVENTIID` = {37D92850-6712-4010-B175-D1EC555C6018} · `FriendlyName` = MEDANALOG · `InstanceName` = textoAnalog0 · `CustomConfig` = Medida Analógica p/ Layout · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaAnalogica |  | S | S |  |  | Nome da Medida Analógica \| Max 22 caracteres |  |
| 2 | `Conversao` | Variant | Double `1` | S | S |  |  | Inserir a fórmula de conversão \| Por padrão, o valor está em 1 para que, em caso de não-utilização, mantenha o valor aquisitado |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Text2, Text1)
```

**Elementos gráficos:** DrawString ×2

<a id="cpainelinversor"></a>
### cPainelInversor

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {100382DC-E5A2-4419-8EF1-BD83AE1FB741} · `_IID` = {5CB1F460-436D-4D16-B08C-E2FD6DA222CA} · `_EVENTIID` = {9F32CA0A-F19B-4921-BB49-C29DBE4FFB99} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawString`, `AnalogBind`, `DrawGroup`, `cObjBotaoHighPerformance`, `cObjGauge`, `AnimationBind`, `cObjMedidaDigitalPaineis`, `cObjMedidaAnalogicaPaineis`, `cObjBarGraph`, `cObjCardFundo`, `TableBind`, `cPainelStrings`, `cEquipInversor`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fInversor |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×3 (anltemp, Id4, Id)
DrawGroup ×3 (Grupo1, Digital, Analog)
  DrawString ×2 (graus, Celcius)
cObjBotaoHighPerformance ×5 (buttonSaveNote, callDigital, callAnalog, …)
cObjGauge ×2 (gaugeEnergiaDia, gaugePotenciaAtiva)
cObjMedidaDigitalPaineis ×1 (Discrete01)
cObjBarGraph ×1 (temperature)
cObjCardFundo ×5 (cObjCardFundo6, cObjCardFundo3, cObjCardFundo5, …)
cPainelStrings ×1 (cPainelStrings1)
cEquipInversor ×1 (objInversor)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `callDigital.CallChildVisible` (4 linhas), `callDigital03.CallChildVisible` (5 linhas), `callDigital02.CallChildVisible` (5 linhas), `callDigital01.CallChildVisible` (5 linhas), `callAnalog03.CallChildVisible` (5 linhas), `callAnalog02.CallChildVisible` (5 linhas), `callAnalog01.CallChildVisible` (5 linhas), `callAnalog.CallChildVisible` (4 linhas)

**Elementos gráficos:** DrawGroup ×9, DrawString ×5

<a id="cpainelmedidastela"></a>
### cPainelMedidasTela

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {30D7EC34-1DAD-4564-BE7B-0BF0F1DBBA73} · `_IID` = {50F96B51-B319-481A-B491-A8E475473C20} · `_EVENTIID` = {ED257F0F-0373-48F1-AF0B-28B49D8D287F} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgDJ` | fDisjuntor |  | S | S |  |  |  |  |
| 2 | `cfgMMD` | fMultimedidor |  | S | S |  |  |  |  |
| 3 | `Tipo` | Boolean |  | S | S |  |  | True = DJ \| False = MMD |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (DJ, MMD)
```

**Elementos gráficos:** DrawGroup ×2

<a id="cpainelmultimedidor"></a>
### cPainelMultimedidor

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {F3D66B90-A1DB-463F-9F26-3A5F765C7A5A} · `_IID` = {BE43B906-EBA7-4EE1-B561-657EAA69D7EC} · `_EVENTIID` = {03793611-8C3A-4295-98FC-3855EBCDBC65} · `FriendlyName` = painel Multimedidores · `InstanceName` = painelMultimedidores0 · `CustomConfig` = painelMultimedidores0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawString`, `DrawGroup`, `cObjBotaoHighPerformance0se`, `AnimationBind`, `cObjMedidaAnalogicaPaineis0se`, `cObjCardFundo0se`, `cObjMedidaDigitalPaineis0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fMultimedidor |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawString ×1 (ID_DJ)
DrawGroup ×1 (grupoMedidas)
  DrawGroup ×2 (grupoAnalog, grupoDigital)
    cObjBotaoHighPerformance0se ×6 (call06, call05, call04, …)
    DrawGroup ×6 (Analog01, Analog02, Analog03, …)
      cObjMedidaAnalogicaPaineis0se ×13 (Analog13, Analog12, Analog11, …)
  cObjBotaoHighPerformance0se ×2 (callAnalog, callDiscrete)
  cObjCardFundo0se ×1 (cObjCardFundo1)
cObjCardFundo0se ×1 (cObjCardFundo1)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `call06.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call01.CallChildVisible` (8 linhas), `callAnalog.CallChildVisible` (4 linhas), `callDiscrete.CallChildVisible` (4 linhas), `call05.CallChildVisible` (7 linhas), `call04.CallChildVisible` (7 linhas), `call03.CallChildVisible` (7 linhas), `call02.CallChildVisible` (7 linhas), `call01.CallChildVisible` (7 linhas)

**Elementos gráficos:** DrawGroup ×14, DrawString ×1

<a id="cpainelstrings"></a>
### cPainelStrings

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {E80E7D5B-3A6E-4E46-806B-7F1E763DE214} · `_IID` = {5706D202-B125-4576-A329-78E4719EA6C6} · `_EVENTIID` = {5B109F46-D15B-4D6A-BA6E-CD90F4D036C5} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawConnector`, `DrawString`, `cEquipStringPainel`, `cObjCardFundo`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fGrupoStrings |  | S | S |  |  |  |  |
| 2 | `cfgQuantidadeStrings` | Integer |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawConnector ×21 (Conector21, Conector20, Conector19, …)
DrawString ×1 (Texto1)
cEquipStringPainel ×22 (String22, String21, String20, …)
cObjCardFundo ×1 (cObjCardFundo3)
```

**Elementos gráficos:** DrawConnector ×21, DrawString ×1

<a id="cequipcmb"></a>
### cEquipCMB

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {C05D0112-01D1-44F3-82BA-F2C4DA3BA3EA} · `_IID` = {0F8E0797-2C02-4EA5-97FB-31D49CA9F2A6} · `_EVENTIID` = {9088D98D-B118-408B-9CE0-0F280215E255} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `DrawConnector`, `DrawString`, `DrawLine`, `DrawTank`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fCMB |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×1 (Group1)
  DrawConnector ×5 (Connector4, Connector5, Connector6, …)
  DrawString ×1 (Text1)
  DrawLine ×1 (Line1)
  DrawTank ×3 (RoundRect3, RoundRect2, RoundRect1)
```

**Eventos com script:** `RoundRect1.Click` (8 linhas)

**Elementos gráficos:** DrawConnector ×5, DrawTank ×3, DrawGroup ×1, DrawString ×1, DrawLine ×1

<a id="cequipinversor"></a>
### cEquipInversor

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {C06119E4-4346-42AF-B4F0-B56E231571D0} · `_IID` = {BEB4E4CF-56AC-4EC6-9F9B-42D884D83069} · `_EVENTIID` = {7EFE262C-FB2E-44ED-A815-C929DC17DA46} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `DrawString`, `cObjCardFundo`, `TableBind`, `DrawArc`, `DrawLine`, `DrawRect`, `AnimationBind`, `DrawConnector`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fInversor |  | S | S |  |  | Propriedades: MedidaAnalogica01 ~ 30 \| MedidaDigital01 ~ 05 \| Comando01 ~ 04 \| Modelo \| Fabricante \| Pot_Nominal \| Pot_Ativa \| StartStop \| SP-Pot-Ativa \| Status \| Eficiencia \| Alarmes \| Comunicacao |  |
| 2 | `cfgHabilitarAcesso` | Variant | Boolean `True` | S | S |  |  | Habilita ou não o acesso ao painel do Inversor |  |
| 3 | `cfgEnableInfo` | Integer | Integer `1` | S | S |  |  | 1 -> Habilita Informações do Inversor: ID e Gráfico \| 0 -> Desabilita \| 2 -> Habilita ID Reduzido (2 dígitos) |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×2 (falhaCom, Inversor)
  DrawString ×1 (falhaCom)
  cObjCardFundo ×1 (cObjCardFundo1)
DrawString ×2 (IdReduzido, Id)
DrawRect ×1 (Potencia)
```

**Eventos com script:** `Corpo.Click` (9 linhas), `BackGround.Click` (9 linhas)

**Elementos gráficos:** DrawGroup ×4, DrawString ×3, DrawRect ×3, DrawArc ×2, DrawLine ×2, DrawConnector ×1

<a id="cequipmeteorologica"></a>
### cEquipMeteorologica

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {E93AE166-2139-4B83-8145-BE037F810CAC} · `_IID` = {E5588247-B67A-44EA-8676-247CA0452487} · `_EVENTIID` = {6EF2EBB3-A1B2-4B09-A71A-5063FA26943A} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawString`, `DrawTank`, `AnimationBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fEMET |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawString ×2 (Identificador, Text1)
DrawTank ×2 (RoundRect2, RoundRect1)
```

**Eventos com script:** `RoundRect1.Click` (8 linhas)

**Elementos gráficos:** DrawString ×2, DrawTank ×2

<a id="cequipmultimedidor"></a>
### cEquipMultimedidor

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {48CC68E1-CD85-4333-A5DF-685DF08ED071} · `_IID` = {FDAF7B05-DD96-4867-96E0-73317A33431B} · `_EVENTIID` = {ADBAD0C9-A3A5-4532-9EB4-6EB14A916DF2} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawString`, `DrawTank`, `AnimationBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fMultimedidor |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawString ×2 (Identificador, Text1)
DrawTank ×2 (RoundRect2, RoundRect1)
```

**Eventos com script:** `RoundRect1.Click` (8 linhas)

**Elementos gráficos:** DrawString ×2, DrawTank ×2

<a id="cequipppc"></a>
### cEquipPPC

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {09A1C3D3-1315-43C3-A98F-AD6456E1A731} · `_IID` = {3C5C2EB4-4DC8-4AFD-B80D-90CC618D10A8} · `_EVENTIID` = {8E85B6A9-EEED-461E-8B27-0D37C742446E} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `DrawConnector`, `DrawString`, `DrawLine`, `DrawTank`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fPPC |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×1 (Group1)
  DrawConnector ×5 (Connector4, Connector5, Connector6, …)
  DrawString ×1 (Text1)
  DrawLine ×1 (Line1)
  DrawTank ×3 (RoundRect3, RoundRect2, RoundRect1)
```

**Eventos com script:** `RoundRect1.Click` (8 linhas)

**Elementos gráficos:** DrawConnector ×5, DrawTank ×3, DrawGroup ×1, DrawString ×1, DrawLine ×1

<a id="cequipstring"></a>
### cEquipString

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {C9A8C78D-A67B-43B5-8B23-635B1A8988BD} · `_IID` = {2B7FCB53-0FE1-4C04-BF3F-B92888061F23} · `_EVENTIID` = {55BA7968-74DE-4624-A559-9B200F10CB4D} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawConnector`, `DrawRect`, `DrawString`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fGrupoStrings |  | S | S |  |  | Vincular com Folder do tipo 'fGrupoStrings' |  |
| 2 | `CampoSolar` | fCampoSolar |  | S | S |  |  | Vincular com Folder do tipo 'fCampoSolar' |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Group1)
  DrawConnector ×2 (Connector2, Connector1)
  DrawRect ×2 (campoSolar, grupoStrings)
DrawString ×1 (Text1)
```

**Eventos com script:** `campoSolar.Click` (8 linhas), `grupoStrings.Click` (8 linhas)

**Elementos gráficos:** DrawConnector ×2, DrawRect ×2, DrawGroup ×1, DrawString ×1

<a id="cequipstringlayout"></a>
### cEquipStringLayout

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {8CEB67A2-5B8C-4A73-8148-0C95D09B5C28} · `_IID` = {8943F6A0-C5F8-4902-A727-BFBC2EAAD00C} · `_EVENTIID` = {BA5D3C45-D9B7-431E-943A-5F5BEA6200A0} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `DrawString`, `DrawTank`, `AnalogBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fString |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×1 (StringHorizontal)
  DrawString ×1 (Texto1)
  DrawTank ×1 (RetanguloArr1)
```

**Elementos gráficos:** DrawGroup ×1, DrawString ×1, DrawTank ×1

<a id="cequiptracker"></a>
### cEquipTracker

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {A6F844CC-C87A-410E-9D7E-3E82BDB5B45E} · `_IID` = {935E154C-8D3E-44A1-A1A2-88CEFF26409F} · `_EVENTIID` = {C2BF401C-E1CE-4F07-B84A-8275FE96D40D} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `cObjNotaOperativa`, `cObjAlarme`, `DynamicMove`, `DrawTank`, `TableBind`, `DrawString`, `AnimationBind`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fTracker |  | S | S |  |  | Herança do XFolder 'Trackers' |  |
| 2 | `Orientação` | Boolean |  | S | S |  |  | True = Vertical \| False = Horizontal |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (MovVert, MovHoriz)
  cObjNotaOperativa ×1 (cObjNotaOperativa1)
  cObjAlarme ×1 (Alarm01)
  DrawGroup ×1 (Grupo1)
    DynamicMove ×1 (DynamicMove1)
      DrawTank ×1 (RetanguloArr2)
    DrawTank ×1 (RetanguloArr1)
  DrawString ×1 (Texto1)
```

**Eventos com script:** `Texto1.Click` (8 linhas), `Texto1.Click` (8 linhas)

**Elementos gráficos:** DrawGroup ×4, DrawTank ×4, DynamicMove ×2, DrawString ×2

<a id="cdetalhesusina"></a>
### cDetalhesUsina

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B7B0C068-B43D-4AAF-9419-A4B9CEC30245} · `_IID` = {F258E2AC-A5F3-48AF-B102-337EBB20669C} · `_EVENTIID` = {5A18F3FD-B7D5-4B3C-95C2-D9D28A2ADC7F} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fUsinaPV |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×6 (CapacidadeInstalada2, InícioOperacao, CapacidadeInstalada, …)
```

**Elementos gráficos:** DrawString ×6

<a id="cnavegacaoscreensheader"></a>
### cNavegacaoScreensHeader

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {7A5BC93B-9A50-4647-A8DF-E712479E699C} · `_IID` = {68E0160C-F48F-4B09-8CFB-D547E52065DE} · `_EVENTIID` = {A82E7452-44D0-4E6E-81E0-E8B9156AF074} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `AnimationBind`, `DrawString`, `DrawRect`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oConfigNavegacaoScreens |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Group1)
  DrawString ×1 (Texto1)
  DrawRect ×1 (Rectangle1)
```

**Eventos com script:** `Group1.Click` (5 linhas)

**Elementos gráficos:** DrawGroup ×1, DrawString ×1, DrawRect ×1

<a id="cobjsetpoint"></a>
### cObjSetPoint

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {6A282978-C831-44ED-ABC5-AF718FF91123} · `_IID` = {A6E3C6E4-65B7-4C58-987B-A718CBD76469} · `_EVENTIID` = {326B284C-4F5B-4018-900C-0A634B658803} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="cobjposicaodebits16b"></a>
### cObjPosicaoDeBits16b

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {0DBAB191-C309-464C-8A5F-9C43F760B67C} · `_IID` = {2933D4AC-DD90-4F9D-9741-00B7298C04C3} · `_EVENTIID` = {CC5181E5-53B3-4796-BDA0-62FA223CBBDF} · `FriendlyName` = Posição de Bits - 16bits · `InstanceName` = pos16bit0 · `CustomConfig` = Posição de Bits - 16bits · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `CheckBox`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaDigital |  | S | S |  |  | Fonte.Value |  |

**Estrutura interna (classe ×qtd):**

```
CheckBox ×16 (Bit15, Bit14, Bit13, …)
```

**Elementos gráficos:** CheckBox ×16

<a id="cobjmedidadigitallayout"></a>
### cObjMedidaDigitalLayout

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {DBA0AA47-7257-42A7-AEFC-129235985910} · `_IID` = {329D2270-242B-444D-9046-6BE4301E44AF} · `_EVENTIID` = {5D0AE007-95B6-448F-8BCB-6FF19FD71767} · `FriendlyName` = textoMedidaDigital · `InstanceName` = textoDigital0 · `CustomConfig` = Medida Digital p/ Layout · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaDigital |  | S | S |  |  | Nome da Medida Analógica \| Max 22 caracteres |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Text2, Text1)
```

**Elementos gráficos:** DrawString ×2

<a id="cobjmedidaanalogicatela"></a>
### cObjMedidaAnalogicaTela

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {399CB43C-DD93-480B-AEC1-2191C71E18DD} · `_IID` = {52193290-155B-46AE-9E68-0A75D1F2591F} · `_EVENTIID` = {BD83085F-3E84-4A22-A9F5-1CA474D283CF} · `IconPath` = imgAnalog · `FriendlyName` = MedidaAnalogica · `InstanceName` = textoAnalog0 · `CustomConfig` = Medida Analógica p/ Tela · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`

**Propriedades / métodos próprios (6)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fMedidaAnalogica |  | S | S |  |  | Nome da Medida Analógica \| Max 22 caracteres |  |
| 2 | `Conversao` | Variant | Double `1` | S | S |  |  | Inserir a fórmula de conversão \| Por padrão, o valor está em 1 para que, em caso de não-utilização, mantenha o valor aquisitado |  |
| 3 | `setpointValue` | Variant |  | S | S |  |  |  |  |
| 4 | `cfgSetpoint` | Boolean | Boolean `False` | S | S |  |  | True = Setpoint |  |
| 5 | `cfgSpMaxLimit` | Variant |  | S | S |  |  | Limite máximo do Setpoint |  |
| 6 | `cfgSpMinLimit` | Variant |  | S | S |  |  | Limite mínimo do Setpoint |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (setpoint, analog)
```

**Elementos gráficos:** DrawString ×2

<a id="cobjheader"></a>
### cObjHeader

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {0A42A237-EE0D-486D-9157-3EC7D8F3BD4B} · `_IID` = {CE55AF0B-26EF-4E54-BB97-5F9F6BFA77FB} · `_EVENTIID` = {7B98B23D-9E8A-4739-B926-D1ED2300392B} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawRect`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oConfigHeader |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×4 (Usuario, Data, Horario, …)
DrawRect ×1 (fundoHeader)
```

**Eventos com script:** `Usuario.Click` (3 linhas)

**Elementos gráficos:** DrawString ×4, DrawRect ×1

<a id="cobjcheckbox"></a>
### cObjCheckBox

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {5199E960-7D1C-4EBD-BA3B-5EE381594E96} · `_IID` = {40F6B474-72AD-4A16-87D4-86D137C97BEB} · `_EVENTIID` = {4F9AC64B-E226-4910-BE7C-B151C5A66C2A} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `CheckBox`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Boolean |  | S | S |  |  |  |  |
| 2 | `Caption` | Variant |  | S | S |  |  |  |  |
| 3 | `Quality` | Variant |  | S | S |  |  | Vincular à qualidade do ponto |  |

**Estrutura interna (classe ×qtd):**

```
CheckBox ×1 (Bit00)
```

**Elementos gráficos:** CheckBox ×1

<a id="cobjvideowall"></a>
### cObjVideoWall

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {382430D0-00A1-4546-8BF2-493F2D09B63C} · `_IID` = {AB451D53-8A78-476E-BC99-D715FDE1DDFF} · `_EVENTIID` = {5EF9CD5E-1B84-45D2-B9BD-B2851E1F5903} · `FriendlyName` = VideoWall · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawGroup ×2 (ArcLight, ArcShadow)
    DrawLine ×4 (Linha12, Linha9, Linha6, …)
```

**Elementos gráficos:** DrawLine ×14, DrawGroup ×3

<a id="ciconevento"></a>
### cIconeVento

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {3EFB5296-6091-4844-9026-68D688D7B294} · `_IID` = {009ECC2E-442F-47DA-B334-39C012D4943D} · `_EVENTIID` = {D9BE3C56-FE68-4542-9E56-2677C7B2C087} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawBezier`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawBezier ×3 (Bezier3, Bezier2, Bezier1)
```

**Elementos gráficos:** DrawBezier ×3, DrawGroup ×1

<a id="ciconeusuario"></a>
### cIconeUsuario

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {EED597FB-5D82-4D9F-841F-F518F22C9405} · `_IID` = {BA5400B5-8A3E-4CD3-A867-4403DE96C2B4} · `_EVENTIID` = {15F58F98-FB3F-471E-BB36-46A1E44A2175} · `FriendlyName` = User · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawGroup ×1 (ArcShadow)
    DrawLine ×2 (Linha2, Linha1)
```

**Elementos gráficos:** DrawGroup ×2, DrawLine ×2

<a id="ciconeumidade"></a>
### cIconeUmidade

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {23D2B38B-283A-4776-A6AE-5AEA604C390C} · `_IID` = {FAF6D547-DEB4-49F4-B253-6F8F1601D826} · `_EVENTIID` = {31FA5974-BDB6-4791-82A5-0DB1579CCA73} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawArc`, `DrawConnector`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawArc ×2 (Arco2, Arco1)
  DrawConnector ×1 (Conector1)
```

**Elementos gráficos:** DrawArc ×2, DrawGroup ×1, DrawConnector ×1

<a id="ciconetermometro"></a>
### cIconeTermometro

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {D657FD91-E12E-473C-ABD5-66BE23765D2A} · `_IID` = {6B2967E0-83BA-4DED-8996-8DDC95E84F19} · `_EVENTIID` = {904D1161-1010-4BC6-B60D-6FC5D2C5D8C9} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawTank`, `DrawCircle`, `DrawArc`, `DrawConnector`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawTank ×1 (RetanguloArr1)
DrawCircle ×1 (Circulo1)
DrawArc ×2 (Arco2, Arco1)
DrawConnector ×2 (Conector2, Conector1)
```

**Elementos gráficos:** DrawArc ×2, DrawConnector ×2, DrawTank ×1, DrawCircle ×1

<a id="ciconesol"></a>
### cIconeSol

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {9E5AF1F1-975F-412A-B92D-B4C0508BCB3B} · `_IID` = {FCA82B92-7D13-4854-AD20-342A75D502F5} · `_EVENTIID` = {0B3AD516-20D4-477D-B438-6755CFE62970} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`, `DrawArc`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawLine ×7 (Linha8, Linha7, Linha6, …)
  DrawArc ×1 (Arco1)
```

**Elementos gráficos:** DrawLine ×7, DrawGroup ×1, DrawArc ×1

<a id="clibalbedo"></a>
### cLibAlbedo

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {8D7D1764-0174-4C8A-A155-402D6211CF06} · `_IID` = {E17E67EB-69BD-4195-AF5A-E8CC539683D5} · `_EVENTIID` = {13551036-CAC9-4E40-9263-460140A19D01} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cLibModuloPV`, `DrawGroup`, `DrawTank`, `DrawConnector`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
cLibModuloPV ×1 (cLibModuloPV1)
DrawGroup ×1 (Grupo1)
  DrawGroup ×2 (Grupo3, Grupo2)
    DrawTank ×6 (RetanguloArr6, RetanguloArr5, RetanguloArr2, …)
DrawConnector ×1 (Conector1)
```

**Elementos gráficos:** DrawTank ×12, DrawGroup ×3, DrawConnector ×1

<a id="clibchuva"></a>
### cLibChuva

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {16A5D778-263E-499B-82EE-F4A814E10F39} · `_IID` = {0E2E4A0C-E2DA-4EB7-8053-67BBA1197BCA} · `_EVENTIID` = {DB470F83-0AE7-4F29-A524-E31BD8E38859} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`, `DrawArc`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawGroup ×1 (Grupo1)
    DrawLine ×1 (Line1)
    DrawArc ×3 (Arc3, Arc2, Arc1)
  DrawLine ×3 (Line6, Line5, Line4)
```

**Elementos gráficos:** DrawLine ×4, DrawArc ×3, DrawGroup ×2

<a id="clibghi"></a>
### cLibGHI

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {43325B3C-8B0F-4161-A759-C9AFE312DC51} · `_IID` = {D0FC1936-842A-4D32-B1C8-E58EFB6F7BAE} · `_EVENTIID` = {FA682215-E1C6-4DA7-B2FA-618BD0AA8AD1} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cLibModuloPV`, `cIconeSol`, `DrawGroup`, `DrawTank`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
cLibModuloPV ×1 (cLibModuloPV1)
cIconeSol ×1 (cIconeSol1)
DrawGroup ×1 (Grupo1)
  DrawGroup ×1 (Grupo1)
    DrawTank ×3 (RetanguloArr4, RetanguloArr3, RetanguloArr1)
```

**Elementos gráficos:** DrawTank ×3, DrawGroup ×2

<a id="cliblogout"></a>
### cLibLogout

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {690DEA22-6C8A-4268-A971-92E2D1A5B2B4} · `_IID` = {44484765-222B-4FC3-BFAD-76E3AAAC4362} · `_EVENTIID` = {C8EE1FBC-2F78-46E3-98D6-10143BBAF364} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawLine`, `DrawArc`, `DrawConnector`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawLine ×6 (Line6, Line5, Line4, …)
DrawArc ×1 (Arc1)
DrawConnector ×2 (Connector2, Connector1)
```

**Elementos gráficos:** DrawLine ×6, DrawConnector ×2, DrawArc ×1

<a id="clibmapabrasil"></a>
### cLibMapaBrasil

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {5C7AC8A5-C8F0-450E-B6B6-1BE2F836413A} · `_IID` = {DA2C679B-326B-4272-9DA0-BEED06755765} · `_EVENTIID` = {AD7E5D2A-9712-4855-92D6-C211903D2034} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

<a id="clibpoa"></a>
### cLibPOA

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {A837B781-46F3-4B05-A397-8BB9DF4BC9FB} · `_IID` = {33254BD6-958C-4C3B-A418-AB7E82DF49B6} · `_EVENTIID` = {8364537D-F80B-4CC0-90D2-0E26DD1CB559} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cLibModuloPV`, `DrawGroup`, `DrawTank`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
cLibModuloPV ×1 (cLibModuloPV1)
DrawGroup ×1 (Grupo1)
  DrawGroup ×2 (Grupo2, Grupo1)
    DrawTank ×3 (RetanguloArr4, RetanguloArr3, RetanguloArr1)
```

**Elementos gráficos:** DrawTank ×6, DrawGroup ×3

<a id="clibtemperatura"></a>
### cLibTemperatura

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {3A8E7784-D684-4D68-86FC-FB0FF3095DEA} · `_IID` = {6CADAFA2-4B2E-4782-B224-E02B87BCC671} · `_EVENTIID` = {767D243C-38CF-451E-A76A-688E29557665} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawCircle`, `DrawString`, `DrawLine`, `DrawArc`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawCircle ×1 (Circle1)
DrawString ×1 (Text1)
DrawLine ×5 (Line5, Line4, Line3, …)
DrawArc ×2 (Arc2, Arc1)
```

**Elementos gráficos:** DrawLine ×5, DrawArc ×2, DrawCircle ×1, DrawString ×1

<a id="clibumidade"></a>
### cLibUmidade

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {ECC2A0EC-F541-428D-AE1E-8C9079C0B9A7} · `_IID` = {2A98BC32-C0BC-4942-892B-21020AC45127} · `_EVENTIID` = {6CE2F824-B99A-4E28-B1E7-3B01A9B5E07D} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawArc`, `DrawLine`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawArc ×2 (Arc2, Arc1)
DrawLine ×2 (Line2, Line1)
```

**Elementos gráficos:** DrawArc ×2, DrawLine ×2

<a id="cequiparraylayout"></a>
### cEquipArrayLayout

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {07CB35BE-2454-4641-BE28-D68197CF55C6} · `_IID` = {3E572BBB-E2CE-40AA-AD91-BF081CD3FBDF} · `_EVENTIID` = {336E2E35-6877-42FE-81A1-6F962E5F1422} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `cEquipTracker`, `cEquipStringLayout`, `DrawRect`, `AnimationBind`, `DrawTank`, `DrawCircle`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Orientação` | Boolean |  | S | S |  |  | False = Horizontal \| True = Vertical |  |
| 2 | `Settings` | fArray |  | S | S |  |  |  |  |
| 3 | `Arranjo` | Integer | Integer `0` | S | S |  |  | 0 - 2x2 \| 1 - 2x3 |  |
| 4 | `Estrutura` | Integer | Integer `0` | S | S |  |  | 0 - Tracker \| 1 - Fixa |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (2x2, 2x3)
  DrawGroup ×2 (Horizontal, Vertical)
    cEquipTracker ×1 (cEquipTracker1)
    cEquipStringLayout ×4 (STG-B1, STG-A1, STG-B2, …)
    DrawRect ×1 (Retangulo1)
    DrawGroup ×1 (Eixo)
      DrawTank ×1 (RetanguloArr1)
      DrawCircle ×1 (Circulo1)
```

**Elementos gráficos:** DrawGroup ×10, DrawTank ×10, DrawRect ×4, DrawCircle ×4

<a id="cobjalarme"></a>
### cObjAlarme

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B5071296-2B25-4A4D-9EDA-E5950ACCC772} · `_IID` = {FEE6992F-15DE-4D55-9CE1-547557598AB2} · `_EVENTIID` = {FB7B4B49-5A83-4547-985C-175662674A23} · `FriendlyName` = Alarme · `InstanceName` = Alarm0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `AlarmActive` | Integer |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawString ×1 (Texto1)
  DrawLine ×1 (Linha1)
```

**Elementos gráficos:** DrawGroup ×1, DrawString ×1, DrawLine ×1

<a id="cpaineltracker"></a>
### cPainelTracker

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {F0C13FFA-802E-427F-B3D9-1C180D8F93E7} · `_IID` = {55034A34-5BF3-4821-9FE6-304827495BA1} · `_EVENTIID` = {EED0E14F-19A3-45FC-B224-90ABE262BB57} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawGroup`, `AnimationBind`, `DrawString`, `cObjMedidaAnalogicaPaineis`, `cObjCardFundo`, `cObjMedidaAnalogicaTela`, `cEquipTracker`, `DrawLine`, `DrawTank`, `cObjMedidaDigitalPaineis`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fTracker |  | S | S |  |  | Herança do XFolder 'Trackers' |  |
| 2 | `String` | fString |  | S | S |  |  | Herança do XFolder 'Strings' |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×3 (buttonSaveNote, callStrings, callDigital)
DrawGroup ×3 (Strings, Id, Digital)
  cObjBotaoHighPerformance ×2 (callStrings01, callStrings02)
  DrawGroup ×2 (Strings01, Strings02)
    DrawGroup ×4 (Grupo4, Grupo3, Grupo2, …)
      DrawString ×1 (Texto3)
      cObjMedidaAnalogicaPaineis ×2 (Analog08, Analog07)
      cObjCardFundo ×1 (cObjCardFundo2)
cObjCardFundo ×3 (cObjCardFundo3, cObjCardFundo1, cObjCardFundo2)
DrawString ×2 (Texto6, Texto5)
cObjMedidaAnalogicaTela ×2 (textoAnalog04, textoAnalog03)
cEquipTracker ×1 (cEquipTracker1)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `callStrings01.CallChildVisible` (4 linhas), `callStrings02.CallChildVisible` (4 linhas), `callStrings.CallChildVisible` (4 linhas), `callDigital.CallChildVisible` (4 linhas), `callDigital01.CallChildVisible` (5 linhas)

**Elementos gráficos:** DrawString ×13, DrawGroup ×12, DrawLine ×1, DrawTank ×1

<a id="cequipfiltro"></a>
### cEquipFiltro

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {18C0865F-6D39-41FD-A5D2-52D0AC6CF31C} · `_IID` = {197F6724-2050-4FB3-BF11-3EB68A3F1784} · `_EVENTIID` = {207AA815-919F-4197-9B84-D16232F05765} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawRect`, `AnalogBind`, `AnimationBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fInversor |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto)
DrawRect ×1 (Retangulo1)
```

**Eventos com script:** `Texto.Click` (8 linhas)

**Elementos gráficos:** DrawString ×1, DrawRect ×1

<a id="cpainelncu"></a>
### cPainelNCU

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {3EDE53DD-FCF1-4792-A1FA-3AC9C99A07C4} · `_IID` = {68D7DEAD-1DF5-4527-8A4D-E942D5860D7B} · `_EVENTIID` = {BE2A2148-E59E-4E25-A6BB-FEE410611C1B} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawGroup`, `cObjBotaoHighPerformance0se`, `cObjSelect`, `DrawString`, `cObjCardFundo`, `cTabularTRK`, `AnimationBind`, `TableBind`, `DrawTank`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fNCU |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawGroup ×1 (Painel)
  DrawGroup ×3 (Comandos, Grupo1, Trackers)
    cObjBotaoHighPerformance0se ×5 (cmdNeve, cmdVento, cmdLimp, …)
    cObjSelect ×10 (cObjSelect10, cObjSelect9, cObjSelect8, …)
  DrawString ×4 (Texto5, Texto10, Texto9, …)
  cObjCardFundo ×5 (cObjCardFundo4, cObjCardFundo2, cObjCardFundo3, …)
```

**Eventos com script:** `cPainelNCU.OnStartRunning` (11 linhas), `buttonSaveNote.callNotes` (8 linhas), `call07.CallChildVisible` (11 linhas), `call08.CallChildVisible` (11 linhas), `call09.CallChildVisible` (11 linhas), `call04.CallChildVisible` (11 linhas), `call05.CallChildVisible` (11 linhas), `call06.CallChildVisible` (11 linhas), `call03.CallChildVisible` (11 linhas), `call02.CallChildVisible` (11 linhas), `call01.CallChildVisible` (11 linhas)

**Elementos gráficos:** DrawGroup ×13, DrawString ×5, DrawTank ×1

<a id="cequipncu"></a>
### cEquipNCU

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {7F5A35DD-C78F-4B57-950D-B119703215BA} · `_IID` = {9E7A0BE8-E9B5-464B-A124-8BB96BCDD59E} · `_EVENTIID` = {27DFE294-1E9A-4EB0-9622-0A5C42B8C011} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `DrawConnector`, `DrawString`, `DrawLine`, `DrawTank`, `AnimationBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fNCU |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×1 (Group1)
  DrawConnector ×5 (Connector4, Connector5, Connector6, …)
  DrawString ×1 (Text1)
  DrawLine ×1 (Line1)
  DrawTank ×3 (RoundRect3, RoundRect2, RoundRect1)
```

**Eventos com script:** `RoundRect1.Click` (3 linhas)

**Elementos gráficos:** DrawConnector ×5, DrawTank ×3, DrawGroup ×1, DrawString ×1, DrawLine ×1

<a id="ctabulartrk"></a>
### cTabularTRK

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {7EAFC845-5461-4E6B-8D91-571E68879A82} · `_IID` = {6BBDC1A3-61B1-49DD-B47F-5BA0ABFEBEDC} · `_EVENTIID` = {5F504BE4-024C-4013-935C-7ED4261116D8} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `DrawCircle`, `TableBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fTracker |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (TRK001)
  DrawString ×10 (Texto10, Texto9, Texto8, …)
  DrawCircle ×1 (Circulo1)
```

**Eventos com script:** `Texto1.Click` (8 linhas)

**Elementos gráficos:** DrawString ×10, DrawGroup ×1, DrawCircle ×1

<a id="cobjbotaohighperformance"></a>
### cObjBotaoHighPerformance

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {381A8228-3C9F-40E6-8E3C-3C5E91CA0D5C} · `_IID` = {2A7C2844-FC0A-4DB3-97DB-9DB3E78C5F62} · `_EVENTIID` = {EB111D4C-F6E4-475F-BC5F-555FAE536CC7} · `IconPath` = imgButton · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawTank`, `DrawString`, `MultiSourceBind`, `TableBind`, `AnimationBind`

**Propriedades / métodos próprios (14)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgCaption` | String |  | S | S |  |  |  |  |
| 2 | `cfgColorButton` | Color |  | S | S |  |  |  |  |
| 3 | `cfgColorButtonMouseOver` | Color |  | S | S |  |  |  |  |
| 4 | `cfgColorText` | Color |  | S | S |  |  |  |  |
| 5 | `cfgColorTextMouseOver` | Color |  | S | S |  |  |  |  |
| 6 | `cfgButtonType` | Integer | Integer `0` | S | S |  |  | 0 - Comando Simples \| 1 - call Group \| 2 - Comando Duplo (Select + Execute) \| 3 - Call PopUp \| 4 - call Screen |  |
| 7 | `cfgCommand` | fComando |  | S | S |  |  |  |  |
| 8 | `cfgSecondCommand` | fComando |  | S | S |  |  |  |  |
| 9 | `cfgCommandName` | Variant |  | S | S |  |  |  |  |
| 10 | `cfgCommandValue` | Variant |  | S | S |  |  |  |  |
| 11 | `cfgSecondCommandValue` | Variant |  | S | S |  |  |  |  |
| 12 | `cfgNavigateValue` | Boolean | Boolean `False` | S | S |  |  |  |  |
| 13 | `cfgTextSize` | Integer | Integer `0` | S | S |  |  | 0 - Low \| 1 - Medium \| 2 - High |  |
| 14 | `cfgPathMainScreen` | Variant |  | S | S |  |  | Inserir o PathName da Tela a ser aberta via comando de Call Popup (3) ou Call Screen. |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (botao)
  DrawTank ×4 (IndispCommand, Navigate, SingleCommand, …)
  DrawString ×3 (Size2, Size1, Size0)
```

**Eventos com script:** `Navigate.MouseUp` (3 linhas), `Navigate.Click` (23 linhas), `SingleCommand.Click` (31 linhas), `DoubleCommand.Click` (39 linhas)

**Elementos gráficos:** DrawTank ×4, DrawString ×3, DrawGroup ×1

<a id="cobjbargraph"></a>
### cObjBarGraph

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {8071E519-B540-4463-8B90-9CD4D7F094EA} · `_IID` = {B925EFC2-58DC-4629-80DC-D5FF5055B408} · `_EVENTIID` = {89CDB674-9923-400C-87FF-DF16CC68BA8A} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DynamicMove`, `DrawCircle`, `DrawTank`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `anlValue` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgValueMax` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DynamicMove ×1 (DynamicMove1)
  DrawCircle ×1 (Circulo1)
DrawTank ×1 (RetanguloArr1)
```

**Elementos gráficos:** DynamicMove ×1, DrawCircle ×1, DrawTank ×1

<a id="cobjcardfundo"></a>
### cObjCardFundo

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {0B25401F-4B61-4694-BF82-1561705954C5} · `_IID` = {C8BCF752-9F1F-4EE7-B43D-198A86AB6C71} · `_EVENTIID` = {3A1C3657-A4BB-4631-8AD3-F0A7C1328557} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawTank`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgCorPrincipal` | Color | Long `2368548` | S | S |  |  |  |  |
| 2 | `cfgCorBorda` | Color | Long `5530222` | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawTank ×1 (RetanguloArr3)
```

**Elementos gráficos:** DrawTank ×1

<a id="cobjtexto"></a>
### cObjTexto

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {58CDA0E8-2C61-4EF0-8A1A-086571E85AAC} · `_IID` = {4C0E6BF5-536C-4631-AB19-0A21FEEB307C} · `_EVENTIID` = {86D6B351-A80C-4ABD-9D95-441EC736061E} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `TableBind`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Variant | String `Texto` | S | S |  |  |  |  |
| 2 | `Format` | Format | Integer `0` | S | S |  |  |  |  |
| 3 | `FontColor` | Integer | Integer `0` | S | S |  |  | 0 - Normal \| 1 - Falha de Communication / Qualidade Ruim \| 2 - Atuado |  |
| 4 | `StretchText` | Boolean | Boolean `False` | S | S |  |  |  |  |
| 5 | `TextAlignment` | HorizontalAlignment |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Text)
```

**Elementos gráficos:** DrawString ×1

<a id="cequipstringpainel"></a>
### cEquipStringPainel

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {4C5CB145-334B-4C59-8613-383DD5DDAE57} · `_IID` = {72C92DCB-25A3-4620-9135-9DDC413CEDAE} · `_EVENTIID` = {7CC54197-0FEA-4EE3-9CAF-9EFE5BFA98A2} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawString`, `cObjBarGraph`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fString |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawString ×1 (Texto1)
cObjBarGraph ×1 (cObjBarGraph1)
```

**Elementos gráficos:** DrawString ×1

<a id="ctabularresumousinas"></a>
### cTabularResumoUsinas

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B698206C-EA68-4076-915E-2B46622F7497} · `_IID` = {D3B424F8-9525-4CB4-945D-F0EE1A612647} · `_EVENTIID` = {3B70EAB3-E789-4E99-AFCB-518E5A77E341} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `AnimationBind`, `DrawString`, `cObjCardFundo`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigCardGeralUsinas |  | S | S |  |  |  |  |
| 2 | `SE` | Integer | Integer `1` | S | S |  |  | SE Comissionada = 2 \| SE Não Comissionada = 1 \| Sem SE = 0 |  |
| 3 | `PV` | Integer | Integer `1` | S | S |  |  | PV Comissionada = 2 \| PV Não Comissionada = 1 \| Sem PV = 0 |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Card)
  DrawString ×1 (Text2)
  cObjCardFundo ×1 (cObjCardFundo1)
```

**Eventos com script:** `Text2.Click` (44 linhas)

**Elementos gráficos:** DrawGroup ×1, DrawString ×1

<a id="cdashbargraph"></a>
### cDashBarGraph

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {5A340E3C-94D3-475D-B32E-DAEC0F499A6A} · `_IID` = {495EF278-9839-447F-99A3-0006E3BBE325} · `_EVENTIID` = {D206E5ED-D966-450B-854F-96F7587BE7A4} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DynamicMove`, `DrawGroup`, `DrawLine`, `DrawConnector`, `DrawString`, `TableBind`, `AnimationBind`, `DrawTank`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Double |  | S | S |  |  | Valor Atual |  |
| 2 | `NominalValue` | Double |  | S | S |  |  | Valor nominal |  |
| 3 | `LowLimit` | Double | Integer `15` | S | S |  |  | Inserir o % em relação ao valor nominal |  |
| 4 | `HighLimit` | Double | Integer `15` | S | S |  |  | Inserir o % em relação ao valor nominal |  |
| 5 | `Format` | Format |  | S | S |  |  | Formato do Dado |  |

**Estrutura interna (classe ×qtd):**

```
DynamicMove ×3 (moveMedido, moveBaixo, moveAlto)
  DrawGroup ×1 (medido)
    DrawLine ×1 (valorMedido)
DrawConnector ×1 (Conector1)
DrawString ×1 (Texto1)
DrawTank ×1 (base)
```

**Elementos gráficos:** DynamicMove ×3, DrawGroup ×3, DrawLine ×3, DrawString ×3, DrawConnector ×1, DrawTank ×1

<a id="cobjmedidaanalogicapaineis"></a>
### cObjMedidaAnalogicaPaineis

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B909C423-AE76-4393-A8A3-6F39639F1A5C} · `_IID` = {0A711E68-6AAF-44E0-9536-AA1C134EF3FB} · `_EVENTIID` = {20984E06-5FBC-4EF0-A70D-C8023BFC63AB} · `FriendlyName` = MedidaAnalogicaPaineis · `InstanceName` = Analog0 · `CustomConfig` = Medida Analógica Painéis · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `cObjCardFundo0se`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaAnalogica |  | S | S |  |  | Nome da Medida Analógica \| Max 22 caracteres |  |
| 2 | `Conversao` | Variant | Double `1` | S | S |  |  | Inserir a fórmula de conversão \| Por padrão, o valor está em 1 para que, em caso de não-utilização, mantenha o valor aquisitado |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Text2, Text1)
cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**Elementos gráficos:** DrawString ×2

<a id="cobjmedidadigitalpaineis"></a>
### cObjMedidaDigitalPaineis

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {ECBACA60-8EA6-4DF5-A3A8-DAEA56DE12B5} · `_IID` = {A78C0597-13E8-4063-84F0-249A6F92DACE} · `_EVENTIID` = {4CF94C4F-2576-4FBF-B471-883C4BF530DD} · `FriendlyName` = MedidaDigitalPaineis · `InstanceName` = Discrete0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `TableBind`, `cObjCardFundo`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaDigital |  | S | S |  |  | Nome da Medida Analógica \| Max 22 caracteres |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawString ×1 (Text2)
  cObjCardFundo ×1 (cObjCardFundo1)
DrawString ×1 (Text1)
```

**Elementos gráficos:** DrawString ×2, DrawGroup ×1

<a id="cpainelppc"></a>
### cPainelPPC

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {6A9E98D8-4508-410D-90C0-29D3134071D4} · `_IID` = {63AE9974-97F9-47A8-A1B3-4879B8EC321A} · `_EVENTIID` = {D6D4890D-06A2-4B44-85CE-611ABA5C7EDE} · `FriendlyName` = painel PPC · `InstanceName` = painelPPC0 · `CustomConfig` = painelPPC0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawGroup`, `cObjCardFundo`, `DrawString`, `AnimationBind`, `TableBind`, `cObjMedidaAnalogicaTela`, `cObjMedidaAnalogicaPaineis`, `cObjMedidaDigitalPaineis`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fPPC |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawGroup ×2 (AUTOMA, WEG)
  cObjCardFundo ×6 (cObjCardFundo6, cObjCardFundo1, cObjCardFundo3, …)
  DrawGroup ×8 (modelPPC, statusCom, activeCLP, …)
    DrawString ×1 (Texto10)
    cObjCardFundo ×1 (cObjCardFundo8)
  cObjBotaoHighPerformance ×9 (cObjBotaoHighPerformance7, cObjBotaoHighPerformance8, callGraphs, …)
  DrawString ×2 (Texto2, Texto1)
cObjCardFundo ×2 (cObjCardFundo7, cObjCardFundo6)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `aplicaPotAtiva.CallChildVisible` (4 linhas), `callGraphs.CallChildVisible` (5 linhas), `callDig.CallChildVisible` (5 linhas), `callAnl.CallChildVisible` (5 linhas), `call02.CallChildVisible` (4 linhas), `call01.CallChildVisible` (4 linhas), `call01.CallChildVisible` (4 linhas), `call02.CallChildVisible` (4 linhas), `call01.CallChildVisible` (4 linhas), `call02.CallChildVisible` (4 linhas), `call01.CallChildVisible` (4 linhas), `call02.CallChildVisible` (4 linhas), `callDigPPC.CallChildVisible` (5 linhas), `callGraphs.CallChildVisible` (5 linhas), `callDig.CallChildVisible` (5 linhas), `callAnl.CallChildVisible` (5 linhas), `call01.CallChildVisible` (3 linhas), `call01.CallChildVisible` (4 linhas), `call02.CallChildVisible` (4 linhas), `call01.CallChildVisible` (4 linhas), `call02.CallChildVisible` (4 linhas), `call03.CallChildVisible` (5 linhas), `call01.CallChildVisible` (5 linhas), `call02.CallChildVisible` (5 linhas), `callDigDROOP.CallChildVisible` (5 linhas), `callDigAVR.CallChildVisible` (5 linhas), `callDigPPC.CallChildVisible` (5 linhas)

**Elementos gráficos:** DrawGroup ×44, DrawString ×25

<a id="cdashgaugepaineis"></a>
### cDashGaugePaineis

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {38DF118C-7625-4E81-B1B2-BFC14D34487E} · `_IID` = {E87D4591-F463-4EA4-962E-AEF95CEAD3E0} · `_EVENTIID` = {C20569EE-3748-421B-B04C-B56DF0428F4D} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawCircle`, `DrawArc`, `AnalogBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigGauge |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Medida, Valor)
DrawCircle ×1 (Centro)
DrawArc ×3 (BordaGrafico, Grafico, graficoTarget)
```

**Elementos gráficos:** DrawArc ×3, DrawString ×2, DrawCircle ×1

<a id="cobjselect"></a>
### cObjSelect

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {828EF602-C487-45BA-9A5A-89CDA1C7DC45} · `_IID` = {BA196C9E-A111-43F0-9A9B-FD3F15DC4BFD} · `_EVENTIID` = {8034C566-DBBB-45B8-A898-E03240B5F267} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `CheckBox`, `AnimationBind`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgCaption` | Variant | String `-` | S | S |  |  | Nome do Ponto |  |
| 2 | `cfgBitPosition` | Integer | Integer `0` | S | S |  |  | Bit00 ~ Bit32 |  |
| 3 | `disValueInt` | Integer | Integer `0` | S | S |  |  | Valor em Inteiro |  |
| 4 | `disValueBool` | Boolean | Boolean `False` | S | S |  |  | Valor em Booleano |  |

**Estrutura interna (classe ×qtd):**

```
CheckBox ×1 (selectGroup01)
```

**Eventos com script:** `selectGroup01.Value` (16 linhas)

**Elementos gráficos:** CheckBox ×1

<a id="ciconeantena01"></a>
### cIconeAntena01

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {A99D5B8C-E3AD-4D12-823C-0763B76A6130} · `_IID` = {A7A3AB57-09D1-4848-AB4F-6C31B3E54C73} · `_EVENTIID` = {E6E50613-84CD-4BEB-981A-128FE66826B6} · `FriendlyName` = Antena 01 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawLine`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIdentificacao` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgIP` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawLine ×5 (Linha5, Linha4, Linha3, …)
```

**Elementos gráficos:** DrawLine ×5

<a id="ciconeantena02"></a>
### cIconeAntena02

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {2FA18D01-084F-4FD5-88D2-5F877DCB33F6} · `_IID` = {E3E246C9-D7D4-4F0A-960B-C00F05B3E3DB} · `_EVENTIID` = {9FC808E1-99B8-4998-8BB7-B65CBB30983A} · `FriendlyName` = Antena 02 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawLine`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIdentificacao` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgIP` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawLine ×6 (Linha6, Linha5, Linha4, …)
```

**Elementos gráficos:** DrawLine ×6

<a id="ciconecftv"></a>
### cIconeCFTV

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {4212D649-E58E-41C5-8E9E-AED57097D5D3} · `_IID` = {568E744D-97FD-4FA6-8023-FDACFACDF99B} · `_EVENTIID` = {8AF413D0-577D-40B0-B93E-F70E93EE9698} · `FriendlyName` = Camera CFTV · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComRTU |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawLine ×5 (Linha5, Linha4, Linha3, …)
```

**Elementos gráficos:** DrawLine ×5, DrawGroup ×1

<a id="ciconecomputador"></a>
### cIconeComputador

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {AA45C9F3-9D7F-4C19-8739-1903FF1DE8D7} · `_IID` = {DE2D0EB8-D390-453A-BBA2-4090A4525B68} · `_EVENTIID` = {2D2D0B83-FCF7-494C-93EC-3A0ABA82F9F5} · `FriendlyName` = Computador · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComIED |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawGroup ×2 (ArcLight, ArcShadow)
    DrawLine ×7 (Linha10, Linha9, Linha8, …)
```

**Elementos gráficos:** DrawLine ×9, DrawGroup ×3

<a id="ciconeconversorrede"></a>
### cIconeConversorRede

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {31B6BF53-F56C-42A7-94DC-5900F5767676} · `_IID` = {C522412D-F937-4DA0-93AA-8738E3549B55} · `_EVENTIID` = {BD1F2CCF-7E8F-4936-A88B-B8E8608A0D38} · `FriendlyName` = Redes - Conversor · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComConverter |  | S | S |  |  |  |  |
| 2 | `cfgOrientacao` | Boolean |  | S | S |  |  | False - Vertical \| True - Horizontal |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
DrawGroup ×2 (Horizontal, Vertical)
  DrawGroup ×1 (ArcLight)
    DrawLine ×2 (Linha4, Linha3)
  DrawLine ×1 (ArcShadow)
```

**Elementos gráficos:** DrawLine ×6, DrawGroup ×4, DrawString ×1

<a id="ciconedesktop"></a>
### cIconeDesktop

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {270021A7-9A84-4B27-B4F8-68F20EAA7E29} · `_IID` = {DEB0F728-10AF-4C59-9CCD-641B35A1D07F} · `_EVENTIID` = {D13C34B2-635D-4D89-A504-C3AAEEE42C34} · `FriendlyName` = Desktop · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComServer |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (ArcLight)
  DrawLine ×6 (Linha8, Linha7, Linha6, …)
DrawLine ×1 (ArcShadow)
```

**Elementos gráficos:** DrawLine ×7, DrawGroup ×1

<a id="ciconefirewall"></a>
### cIconeFirewall

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {07D07789-205B-48B6-B2B2-D4E3B191B3BD} · `_IID` = {71DE0307-AA20-4DBE-8331-006717595BEF} · `_EVENTIID` = {C27076CB-1199-41DB-80C5-D3AEBE75A1AD} · `FriendlyName` = Redes - Firewall · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComFirewall |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
DrawLine ×8 (Linha9, Linha8, Linha7, …)
```

**Elementos gráficos:** DrawLine ×8, DrawString ×1

<a id="ciconeied"></a>
### cIconeIED

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {68CEF4AC-4F1A-41D2-A827-CDDD2D013CDA} · `_IID` = {7C4071ED-0C75-45A6-8C9F-065845DB2CE9} · `_EVENTIID` = {CAC1EAB0-3728-46D4-BDEB-2B46953CCBDC} · `FriendlyName` = IED · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComIED |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
DrawGroup ×1 (Grupo1)
  DrawGroup ×1 (ArcLight)
    DrawLine ×4 (Linha6, Linha5, Linha4, …)
  DrawLine ×1 (ArcShadow)
```

**Elementos gráficos:** DrawLine ×5, DrawGroup ×2, DrawString ×1

<a id="ciconemedidor"></a>
### cIconeMedidor

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {921F8631-7D4D-4583-9D97-8E6295AD15C4} · `_IID` = {95A5CD9F-FEEF-4603-A72B-66CF8FF552D1} · `_EVENTIID` = {7F1D20EB-5BFE-4DB6-A6F8-B80323112D10} · `FriendlyName` = Medidor · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIdentificacao` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgIP` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (ArcLight)
  DrawLine ×7 (Linha8, Linha7, Linha6, …)
DrawLine ×1 (ArcShadow)
```

**Elementos gráficos:** DrawLine ×8, DrawGroup ×1

<a id="ciconeroteador"></a>
### cIconeRoteador

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {E21FBBDB-8CC3-4F69-B9E2-19E97E13ECEF} · `_IID` = {51609FA4-F161-4B15-8D36-FD25D22FBE36} · `_EVENTIID` = {3D567D0D-DAA3-4FCE-8692-946F65F37C0C} · `FriendlyName` = Redes - Roteador · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIdentificacao` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgIP` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawGroup ×1 (ArcLight)
    DrawLine ×8 (Linha10, Linha9, Linha8, …)
  DrawLine ×1 (ArcShadow)
```

**Elementos gráficos:** DrawLine ×9, DrawGroup ×2

<a id="ciconertu"></a>
### cIconeRTU

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {981B0412-40B6-46F0-BABE-941B2A6FB94B} · `_IID` = {555A9B2F-1122-4716-98F4-16D8BBB102BE} · `_EVENTIID` = {97DFC6F3-3669-417D-BBBD-780A7722C4F2} · `FriendlyName` = RTU · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComRTU |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
DrawGroup ×1 (Grupo1)
  DrawLine ×2 (ArcLight, ArcShadow)
```

**Elementos gráficos:** DrawLine ×2, DrawString ×1, DrawGroup ×1

<a id="ciconeservidorsimples"></a>
### cIconeServidorSimples

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {AB76DD93-1B17-4DB7-ACFF-EC9D4C50F09F} · `_IID` = {A6C653E4-80B2-4EC0-9388-15BA91561755} · `_EVENTIID` = {952627BB-D12C-4F03-9631-667358176ACF} · `FriendlyName` = Servidor Simples · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComServer |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
DrawGroup ×1 (Grupo1)
  DrawGroup ×2 (ArcLight, ArcShadow)
    DrawLine ×6 (Linha9, Linha8, Linha7, …)
```

**Elementos gráficos:** DrawLine ×8, DrawGroup ×3, DrawString ×1

<a id="ciconeservidortriplo"></a>
### cIconeServidorTriplo

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {8C211D57-BD1B-4BD8-B452-028B27F24E9C} · `_IID` = {D3B806CD-1EDA-4073-837D-C84CA978A660} · `_EVENTIID` = {6F3CB31C-75A2-4E22-AE3D-B5BE5348FDC0} · `FriendlyName` = Servidor Triplo · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComServer |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Texto1)
DrawGroup ×1 (Grupo1)
  DrawGroup ×2 (ArcLight, ArcShadow)
    DrawLine ×18 (Linha23, Linha22, Linha21, …)
```

**Elementos gráficos:** DrawLine ×22, DrawGroup ×3, DrawString ×1

<a id="ciconeswitchrede"></a>
### cIconeSwitchRede

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {9BF4E6C8-D784-45D8-9C9F-40F14444BA7B} · `_IID` = {B453FEB0-C179-4B53-A82A-A68B02DC93C4} · `_EVENTIID` = {6F37B62C-6F91-4057-99F2-C76D5E8D8772} · `FriendlyName` = Redes - Switch · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfg` | fComSwitch |  | S | S |  |  |  |  |
| 2 | `cfgOrientacao` | Boolean |  | S | S |  |  | False - Vertical \| True - Horizontal |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (Horizontal, Vertical)
  DrawGroup ×1 (ArcLight)
    DrawLine ×8 (Linha10, Linha9, Linha8, …)
  DrawLine ×1 (ArcShadow)
```

**Elementos gráficos:** DrawLine ×18, DrawGroup ×4

<a id="cobjgraph"></a>
### cObjGraph

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {4DF426D2-0C8E-4BDE-8499-1D8D88968B61} · `_IID` = {794C582D-EFE4-4DB4-9D87-A9DF0DFF633C} · `_EVENTIID` = {656A086D-B2DC-4E63-ABCD-B234382FD8E6} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `E3Chart.dll`, `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `E3Chart`, `cObjCardFundo`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTitle` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgShowBackground` | Boolean |  | S | S |  |  |  |  |
| 3 | `cfgGraph` | oCfgObjGraph |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
E3Chart ×1 (Graph)
cObjCardFundo ×1 (BackGround)
```

**Eventos com script:** `Graph.OnCursorChange` (5 linhas), `Graph.OnStartRunning` (6 linhas)

<a id="cobjcomconnection"></a>
### cObjComConnection

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {3F8FEE2A-0061-4E9A-998B-9D2DF766D285} · `_IID` = {9E792194-B920-4F66-8806-64DB10CDCA1B} · `_EVENTIID` = {B9B143A5-8A29-447F-B164-E53D189B6A59} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawTank`, `TableBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgPhysicalLayerType` | Integer | Integer `0` | S | S |  |  | 0 - EtherNet Geral \| 1 - EtherNet Crítica \| 2 - Fibra Single Mode \| 3 - Fibra Multi Mode \| 4 - Serial RS485 \| 5 - Serial RS232 \| 6 - Serial PLC \| 7 - Wireless |  |

**Estrutura interna (classe ×qtd):**

```
DrawTank ×1 (RetanguloArr3)
```

**Elementos gráficos:** DrawTank ×1

<a id="cobjelectricconnection"></a>
### cObjElectricConnection

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {F4F45CA9-6306-4DE8-8CC3-335B480DC7A0} · `_IID` = {C111C69C-B60D-47D6-8A17-235468C05371} · `_EVENTIID` = {3941966B-62D7-4C49-96E8-2787B8768ED4} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawTank`, `TableBind`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgStatus` | Integer | Integer `0` | S | S |  |  | 0 - Sem Energia \| 1 - Com Energia \| -1 -> Falha |  |
| 2 | `cfgHabilitaRound` | Integer | Integer `1` | S | S |  |  | 1 - Rounded \| 0 - Line |  |

**Estrutura interna (classe ×qtd):**

```
DrawTank ×1 (RetanguloArr3)
```

**Elementos gráficos:** DrawTank ×1

<a id="ciconecloud"></a>
### cIconeCloud

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {1A42DAE7-7582-4A8F-8EA5-1D3F5905DA49} · `_IID` = {49B1ADA4-FB15-4AF7-8966-95362A3D998A} · `_EVENTIID` = {61EBE780-9CFC-4968-84B7-A2D1B6C204A4} · `FriendlyName` = Redes - Cloud · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawLine`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgIdentificacao` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgIP` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawLine ×1 (Linha1)
```

**Elementos gráficos:** DrawLine ×1

<a id="cobjtextbox"></a>
### cObjTextBox

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B82E9C9E-48F0-40F3-ACEE-02367D75FA77} · `_IID` = {B77F83F0-DCB1-437C-8EF1-645B6612BC14} · `_EVENTIID` = {11B89DB4-88C8-48D4-AA02-AA584873D3C4} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (DataInicio)
```

**Eventos com script:** `DataInicio.AlteraValor` (9 linhas), `DataInicio.OnStartRunning` (4 linhas)

**Elementos gráficos:** DrawString ×1

<a id="ciconepainelsolar"></a>
### cIconePainelSolar

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {DE407B04-2980-4490-8DBB-6E77A4D4FC83} · `_IID` = {503B1AD4-4709-4694-BBD1-E45C62C40C3B} · `_EVENTIID` = {F5394393-2383-422D-9B3A-C066B84024D0} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawTank`, `DrawConnector`, `DrawArc`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawTank ×2 (RetanguloArr2, RetanguloArr1)
  DrawConnector ×10 (Conector10, Conector9, Conector8, …)
  DrawArc ×4 (Arco3, Arco4, Arco2, …)
```

**Elementos gráficos:** DrawConnector ×10, DrawArc ×4, DrawTank ×2, DrawGroup ×1

<a id="cdashpizzagraph"></a>
### cDashPizzaGraph

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {3F940E45-F907-4E49-931E-AAD868B4433E} · `_IID` = {859DF90F-05AF-4908-BD5E-C3FB2C9C9385} · `_EVENTIID` = {7D6F9747-7119-402A-BF54-62491666F2FB} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawCircle`, `DrawArc`

**Propriedades / métodos próprios (10)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgMaxValue` | Variant |  | S | S |  |  |  |  |
| 2 | `cfgValueGraph01` | Variant | Integer `0` | S | S |  |  |  |  |
| 3 | `cfgValueGraph02` | Variant | Integer `0` | S | S |  |  |  |  |
| 4 | `cfgValueGraph03` | Variant | Integer `0` | S | S |  |  |  |  |
| 5 | `cfgValueGraph04` | Variant | Integer `0` | S | S |  |  |  |  |
| 6 | `cfgDescriptionGraph01` | Variant |  | S | S |  |  |  |  |
| 7 | `cfgDescriptionGraph02` | Variant |  | S | S |  |  |  |  |
| 8 | `cfgDescriptionGraph03` | Variant |  | S | S |  |  |  |  |
| 9 | `cfgDescriptionGraph04` | Variant |  | S | S |  |  |  |  |
| 10 | `cfgDescriptionRemainGraph` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (TotalPerc)
DrawCircle ×2 (Circulo2, Sobra)
DrawArc ×4 (Graph01, Graph02, Graph03, …)
```

**Elementos gráficos:** DrawArc ×4, DrawCircle ×2, DrawString ×1

<a id="chistpanel"></a>
### cHistPanel

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {53C9C7DF-7479-48D6-ACF7-DA64FF7EB678} · `_IID` = {9FB46EA8-8FA3-4D2B-AA68-F5CC2AE481F2} · `_EVENTIID` = {CE9A279B-1494-4A7C-82CB-5E2D907AAB7B} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `E3Browse.dll`, `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `ComboBox`, `DrawString`, `AnimationBind`, `DrawCircle`, `E3Browser`, `cObjCardFundo`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgAtivo` | Variant |  | S | S |  |  |  |  |
| 2 | `linkDB` | DBServer |  | S | S |  |  |  |  |
| 3 | `linkQuery` | E3Query |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (cObjBotaoHighPerformance1)
ComboBox ×1 (ComboBox1)
DrawString ×18 (Texto9, StatusConexaoDB, Texto8, …)
DrawCircle ×1 (Circulo1)
E3Browser ×1 (E3Browser)
cObjCardFundo ×1 (cObjCardFundo1)
```

**Eventos com script:** `cObjBotaoHighPerformance1.Export` (30 linhas), `ComboBox1.AlteraValor` (19 linhas), `ComboBox1.OnStartRunning` (10 linhas), `Usuario.AlteraValor` (6 linhas), `Descritivo.AlteraValor` (6 linhas), `Equipamento.AlteraValor` (6 linhas), `Instalacao.AlteraValor` (6 linhas), `Bay.AlteraValor` (6 linhas), `Usina.AlteraValor` (6 linhas), `DataFinal.AlteraValor` (9 linhas), `DataFinal.Click` (6 linhas), `DataFinal.OnStartRunning` (4 linhas), `DataInicio.AlteraValor` (9 linhas), `DataInicio.Click` (6 linhas), `DataInicio.OnStartRunning` (4 linhas), `E3Browser.OnStartRunning` (21 linhas)

**Elementos gráficos:** DrawString ×18, ComboBox ×1, DrawCircle ×1

<a id="cdetalhesativo"></a>
### cDetalhesAtivo

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {1E5DACC9-ED4A-465E-A8BA-FFCC69F28FF4} · `_IID` = {620E84D4-C855-4F2A-B349-B69425B864F5} · `_EVENTIID` = {26A2459C-A315-4ACF-BE0B-4A168B61A6CB} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawString`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fAtivoBTC |  | S | S |  |  |  |  |
| 2 | `cfgType` | Integer |  | S | S |  |  | 0 -> Usina PV \| 1 -> Ativo Bitcoin \| 2 -> Subestação |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (ativoBTC, usinaPV)
  DrawString ×2 (Localidade, nomeAtivo)
```

**Elementos gráficos:** DrawString ×8, DrawGroup ×2

<a id="0tempcreateobj"></a>
### 0tempCreateObj

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {24009DB9-800B-4BC1-823E-86896FEF6B80} · `_IID` = {48330AC1-46FB-4A90-84E0-4982A8D6C99E} · `_EVENTIID` = {9DA9309A-67DF-4FE9-A86E-0CD338A15479} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `CommandButton`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
CommandButton ×1 (CommandButton1)
```

**Eventos com script:** `0tempCreateObj.CustomConfig` (40 linhas)

<a id="cpainelcmb"></a>
### cPainelCMB

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {11AFE874-49C8-4615-A299-236D9589282A} · `_IID` = {AAF24579-28EB-46A9-AE23-5C284441F51E} · `_EVENTIID` = {85F1CAE0-B8EC-4738-8E87-6EFA01755540} · `FriendlyName` = painel CMB · `InstanceName` = painelCMB0 · `CustomConfig` = painelCMB0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawString`, `DrawGroup`, `cObjMedidaAnalogicaTela`, `cObjBotaoHighPerformance0se`, `cObjCardFundo0se`, `cObjBotaoHighPerformance`, `AnimationBind`, `cObjMedidaAnalogicaPaineis0se`, `cObjMedidaDigitalPaineis0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fCMB |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (ID_DJ2, ID_DJ)
DrawGroup ×2 (grupoComandos, grupoMedidas)
  DrawGroup ×2 (comandoSetpoint, comandoInversores)
    cObjMedidaAnalogicaTela ×1 (spPotenciaAtiva)
    DrawString ×1 (Texto2)
    cObjBotaoHighPerformance0se ×1 (cmdAplicaSP)
    cObjCardFundo0se ×2 (background3, background2)
  cObjCardFundo0se ×1 (background)
cObjBotaoHighPerformance ×1 (buttonCallNotes)
cObjCardFundo0se ×2 (background, cObjCardFundo1)
```

**Eventos com script:** `cmdAplicaSP.CallChildVisible` (5 linhas), `callCommand2.CallChildVisible` (5 linhas), `callCommand.CallChildVisible` (5 linhas), `buttonCallNotes.callNotes` (8 linhas), `callAnalog.CallChildVisible` (4 linhas), `callDiscrete.CallChildVisible` (4 linhas), `call06.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call01.CallChildVisible` (8 linhas), `call05.CallChildVisible` (7 linhas), `call04.CallChildVisible` (7 linhas), `call03.CallChildVisible` (7 linhas), `call02.CallChildVisible` (7 linhas), `call01.CallChildVisible` (7 linhas)

**Elementos gráficos:** DrawGroup ×17, DrawString ×4

<a id="cpainelmeteorologica"></a>
### cPainelMeteorologica

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {CDC7AF99-C771-41AE-8125-809602BE76E7} · `_IID` = {1F3782B9-3049-4C33-A279-F6174E621BF4} · `_EVENTIID` = {37319550-B542-45D7-A23A-A6B2CB88A347} · `FriendlyName` = painel Meteo · `InstanceName` = painelMeteo0 · `CustomConfig` = painelMeteo · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawString`, `DrawGroup`, `cObjBotaoHighPerformance0se`, `AnimationBind`, `cObjMedidaAnalogicaPaineis0se`, `cObjCardFundo0se`, `cObjMedidaDigitalPaineis0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fMultimedidor |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawString ×1 (ID_DJ)
DrawGroup ×1 (grupoMedidas)
  DrawGroup ×2 (grupoAnalog, grupoDigital)
    cObjBotaoHighPerformance0se ×6 (call06, call05, call04, …)
    DrawGroup ×6 (Analog01, Analog02, Analog03, …)
      cObjMedidaAnalogicaPaineis0se ×13 (Analog13, Analog12, Analog11, …)
  cObjBotaoHighPerformance0se ×2 (callAnalog, callDiscrete)
  cObjCardFundo0se ×1 (cObjCardFundo1)
cObjCardFundo0se ×1 (cObjCardFundo1)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `call06.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call01.CallChildVisible` (8 linhas), `callAnalog.CallChildVisible` (4 linhas), `callDiscrete.CallChildVisible` (4 linhas), `call05.CallChildVisible` (7 linhas), `call04.CallChildVisible` (7 linhas), `call03.CallChildVisible` (7 linhas), `call02.CallChildVisible` (7 linhas), `call01.CallChildVisible` (7 linhas)

**Elementos gráficos:** DrawGroup ×14, DrawString ×1

<a id="cobjhist"></a>
### cObjHist

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B5FEA4C3-075A-4993-82CC-01AE7BE4B8C7} · `_IID` = {5387FE46-CA83-4C13-84D9-442214341F66} · `_EVENTIID` = {388322D4-3FF1-4204-9137-EF9A66CF5D53} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `E3Browse.dll`, `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawString`, `DrawGroup`, `ComboBox`, `cObjBotaoHighPerformance`, `AnimationBind`, `DrawCircle`, `E3Browser`, `E3Query`, `cObjCardFundo0se`, `cObjCardFundo`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgType` | Integer |  | S | S |  |  |  |  |
| 2 | `cfgAtivo` | Variant | String `%` | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×11 (maxRegistros, Texto9, StatusConexaoDB, …)
DrawGroup ×1 (stepsQuery)
  DrawString ×9 (TipoEvento, Usuario, Descritivo, …)
  ComboBox ×1 (Criticidade)
cObjBotaoHighPerformance ×2 (runQuery, buttonExport)
DrawCircle ×1 (Circulo1)
E3Browser ×1 (HistoricalData)
  E3Query ×1 (Consulta)
cObjCardFundo0se ×1 (cObjCardFundo0se1)
cObjCardFundo ×1 (cObjCardFundo1)
```

**Eventos com script:** `maxRegistros.Click` (11 linhas), `TipoEvento.Click` (11 linhas), `Criticidade.OnStartRunning` (11 linhas), `Bay.AlteraValor` (6 linhas), `DataFinal.Click` (6 linhas), `DataFinal.OnStartRunning` (4 linhas), `DataInicio.Click` (6 linhas), `DataInicio.OnStartRunning` (4 linhas), `runQuery.runQuery` (69 linhas), `HistoricalData.OnStartRunning` (56 linhas), `buttonExport.Export` (31 linhas)

**Elementos gráficos:** DrawString ×20, DrawGroup ×1, ComboBox ×1, DrawCircle ×1

<a id="cpainelresumedmeteo"></a>
### cPainelResumedMeteo

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B647ED81-20B5-4920-BB3A-DAEA265FBD15} · `_IID` = {2F291CF5-3CC8-4E3C-93D3-67AA2939999E} · `_EVENTIID` = {EBC7908F-8956-40E2-B277-A2FA62C836DB} · `FriendlyName` = painelResumedMeteo · `InstanceName` = painelResumedMeteo0 · `CustomConfig` = painelResumedMeteo · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance0se`, `DrawGroup`, `TableBind`, `cObjMedidaAnalogicaTela`, `cObjCardFundo`, `cLibAlbedo`, `cLibGHI`, `cLibPOA`, `cObjCardFundo0se`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fEMET |  | S | S |  |  |  |  |
| 2 | `cfgType` | Integer | Integer `0` | S | S |  |  | 0 - Completa [GHI, POA e Albedo] \| 1 - Simplificada [POA] |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance0se ×1 (cObjBotaoHighPerformance0se8)
DrawGroup ×2 (full, simplified)
  DrawGroup ×3 (ALBEDO, GHI, POA)
    DrawGroup ×1 (anlALBEDO)
      cObjMedidaAnalogicaTela ×1 (textoAnalog01)
      cObjCardFundo ×1 (cObjCardFundo2)
    cLibAlbedo ×1 (cLibAlbedo1)
  cObjCardFundo0se ×2 (cObjCardFundo3, cObjCardFundo1)
```

**Eventos com script:** `cObjBotaoHighPerformance0se8.ValueChange` (9 linhas)

**Elementos gráficos:** DrawGroup ×10

<a id="clibmodulopv"></a>
### cLibModuloPV

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {57DB543F-EED3-466B-83A1-B8E1BC477E10} · `_IID` = {D9F291F3-1B44-4953-B482-6A3BA4DACAD8} · `_EVENTIID` = {79F8CAF0-DB5A-4C82-8C0F-F545BEC27836} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawLine`, `DrawTank`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (PVModule)
  DrawGroup ×1 (modules)
    DrawLine ×8 (Linha5, Linha6, Linha7, …)
  DrawTank ×1 (axis)
```

**Elementos gráficos:** DrawLine ×8, DrawGroup ×2, DrawTank ×1

<a id="cobjtelaalarmes"></a>
### cObjTelaAlarmes

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {B235BF11-779F-48F5-967E-6132771E60D8} · `_IID` = {8F052240-198D-4CBE-BA53-809BDB747B77} · `_EVENTIID` = {F54CEB5B-B68C-4321-B07B-CD486CC7231D} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `E3Alarm.dll`, `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `AnimationBind`, `DrawGroup`, `CheckBox`, `E3Alarm`, `TableBind`, `DrawString`, `cObjCardFundo`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgPlantFilter` | Variant | String `*` | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×2 (callSegregado, callUnificado)
DrawGroup ×2 (modeloUnificado, modeloSegregado)
  CheckBox ×5 (showEvents, showLow, showMedium, …)
  E3Alarm ×1 (Alarmes)
cObjCardFundo ×2 (fundoContent, fundoHeader)
```

**Eventos com script:** `callSegregado.CallChildVisible` (4 linhas), `callUnificado.CallChildVisible` (4 linhas), `add.Valor` (12 linhas)

**Elementos gráficos:** DrawString ×9, DrawGroup ×5, CheckBox ×5

<a id="cobjnotaoperativa"></a>
### cObjNotaOperativa

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {4F323546-AE86-4D21-9038-AE1C3414B84A} · `_IID` = {F824E2A9-1771-4C65-8A56-E4B47582956B} · `_EVENTIID` = {CCDD2F2E-2104-4071-A004-4982C6D2867F} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawCircle`, `DrawLine`, `TableBind`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTargetPathName` | Variant |  | S |  |  |  |  |  |
| 2 | `cfgQtdNotas` | Variant |  | S |  |  |  |  |  |
| 3 | `cfgStatusResumo` | Variant |  | S |  |  |  |  |  |
| 4 | `disEnabled` | Boolean | Boolean `False` | S |  |  |  |  |  |
| 5 | `disType` | Integer | Integer `0` | S |  |  |  | 0 - Informativa \| 1 - Anomalia \| 2 - Restritiva \| 3 - Manutenção |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawCircle ×1 (Circulo1)
  DrawLine ×1 (Note)
```

**Eventos com script:** `Note.Click` (8 linhas)

**Elementos gráficos:** DrawGroup ×1, DrawCircle ×1, DrawLine ×1

<a id="cpainelnotaoperativa"></a>
### cPainelNotaOperativa

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {678558E4-F787-465B-B974-2920074A6A7E} · `_IID` = {1DC770E1-8F26-4700-A992-B86998C1BC7A} · `_EVENTIID` = {BF6A679F-350F-4138-9257-1CA1C64AEACE} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawGroup`, `DrawString`, `DrawCircle`, `cObjCardFundo`, `AnimationBind`, `TableBind`, `ListBox`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgTargetPathName` | Variant |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×7 (buttonClearFields, buttonDisableTag, buttonEnableTag, …)
DrawGroup ×7 (Grupo7, Grupo6, Grupo5, …)
  DrawString ×1 (Texto10)
  DrawCircle ×1 (backNumb)
DrawString ×23 (Texto5, Texto12, Texto11, …)
cObjCardFundo ×28 (cObjCardFundo20, cObjCardFundo15, cObjCardFundo12, …)
ListBox ×1 (lstNotas)
```

**Eventos com script:** `buttonClearFields.clearFields` (22 linhas), `txtStatus.Click` (20 linhas), `txtType.Click` (18 linhas), `txtArea.Click` (24 linhas), `buttonDisableTag.disableTag` (7 linhas), `buttonEnableTag.enableTag` (24 linhas), `buttonRemoveNote.saveEdition` (129 linhas), `buttonSaveEdition.saveEdition` (164 linhas), `buttonSaveNote.saveNote` (207 linhas), `lstNotas.carregaPath` (3 linhas), `lstNotas.Change` (110 linhas), `buttonQueryNotes.queryNotes` (188 linhas), `Texto3.mudaNome` (3 linhas)

**Elementos gráficos:** DrawString ×36, DrawGroup ×7, DrawCircle ×6, ListBox ×1

<a id="cobjlogoscada"></a>
### cObjLogoSCADA

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {15033B06-4323-4BE7-A072-2A8AFBFC1A26} · `_IID` = {2E9C081D-6492-40BE-981E-EC3E44C5EF44} · `_EVENTIID` = {111737C7-B640-4146-A1D7-5B57F2A46F53} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawConnector`, `DrawPicture`, `DrawString`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawGroup ×2 (Grupo2, Grupo1)
    DrawConnector ×4 (Conector5, Conector4, Conector3, …)
```

**Elementos gráficos:** DrawConnector ×4, DrawGroup ×3, DrawString ×2, DrawPicture ×1

<a id="cpainelscadapowercontrol"></a>
### cPainelScadaPowerControl

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {55A3E1AC-C379-486B-A3D9-5196B38F85AC} · `_IID` = {F7446691-02C6-40BB-8A7A-299835ADA1BB} · `_EVENTIID` = {53EA9107-0D8A-4205-B76E-04FE47CCF7B0} · `FriendlyName` = painel SPC · `InstanceName` = painelSPC0 · `CustomConfig` = painelSPC0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawGroup`, `cObjMedidaAnalogicaTela`, `DrawString`, `cObjCardFundo0se`, `cObjBotaoHighPerformance0se`, `cObjBotaoHighPerformance`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fObjScadaPowerControl |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (grupoComandos)
  DrawGroup ×3 (comandoSetpoint2, comandoSetpoint, comandoInversores)
    cObjMedidaAnalogicaTela ×1 (spPotenciaAtiva)
    DrawString ×1 (Texto2)
    cObjCardFundo0se ×2 (background3, background2)
  cObjCardFundo0se ×1 (background)
cObjBotaoHighPerformance ×1 (buttonCallNotes)
DrawString ×1 (ID_DJ)
cObjCardFundo0se ×2 (background, cObjCardFundo1)
```

**Eventos com script:** `cmdAplicaSP.CallChildVisible` (5 linhas), `cmdManual.CallChildVisible` (5 linhas), `cmdSemiAuto.CallChildVisible` (5 linhas), `cmdAuto.CallChildVisible` (5 linhas), `buttonCallNotes.callNotes` (8 linhas)

**Elementos gráficos:** DrawGroup ×4, DrawString ×4

<a id="cequipscadapowercontrol"></a>
### cEquipScadaPowerControl

- Biblioteca: `matrixenergylibxcontrolpv.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {2A1AD7C0-1D82-4686-AA62-413A3C5B7387} · `_IID` = {DBD11768-ECB7-489C-BA8E-5D7203B149A7} · `_EVENTIID` = {7C2A7E1F-E9D7-42B9-8666-771C7840B684} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `DrawConnector`, `DrawString`, `DrawTank`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fObjScadaPowerControl |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×1 (Group1)
  DrawGroup ×1 (Grupo1)
    DrawConnector ×5 (Conector5, Conector4, Conector3, …)
  DrawString ×1 (Texto1)
  DrawTank ×2 (RoundRect2, RoundRect1)
```

**Eventos com script:** `RoundRect1.Click` (8 linhas)

**Elementos gráficos:** DrawConnector ×5, DrawGroup ×2, DrawTank ×2, DrawString ×1

---

## Biblioteca `matrixenergylibxcontrolse.lib`

<a id="cpaineltransformadores0se"></a>
### cPainelTransformadores0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {934C5F3D-C947-4781-9741-DCA0E27942DE} · `_IID` = {6B539FA4-6731-4FBF-816A-708EB51F910E} · `_EVENTIID` = {615B08EE-234E-4DD6-87FA-2AE54700C24F} · `FriendlyName` = painel Transformadores · `InstanceName` = painelTransformadores0 · `CustomConfig` = painelTransformadores0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawGroup`, `DrawString`, `cObjCardFundo`, `cEquipTrafo0se`, `cObjMedidaAnalogicaPaineis0se`, `cObjBotaoHighPerformance0se`, `AnimationBind`, `cObjCardFundo0se`, `cObjMedidaDigitalPaineis0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fTransformador0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawGroup ×2 (comandos, grupoMedidas)
  DrawGroup ×4 (csc, vf01, vf02, …)
    DrawString ×1 (Texto4)
    cObjBotaoHighPerformance ×2 (cmdSingleCommandClose11, cmdSingleCommandClose12)
    cObjCardFundo ×1 (cObjCardFundo7)
  cObjBotaoHighPerformance ×1 (cmdRst86)
  cObjCardFundo ×1 (cObjCardFundo3)
cEquipTrafo0se ×1 (cEquipTrafo0se1)
cObjCardFundo ×2 (cObjCardFundo1, cObjCardFundo2)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `call01.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas), `call06.CallChildVisible` (8 linhas), `callAnalog.CallChildVisible` (4 linhas), `callDiscrete.CallChildVisible` (4 linhas), `call05.CallChildVisible` (7 linhas), `call04.CallChildVisible` (7 linhas), `call03.CallChildVisible` (7 linhas), `call02.CallChildVisible` (7 linhas), `call01.CallChildVisible` (7 linhas)

**Elementos gráficos:** DrawGroup ×19, DrawString ×4

<a id="cpainelied0se"></a>
### cPainelIED0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {06E0D5A0-959E-46CE-B7BF-5261907970FE} · `_IID` = {F0CAECF5-A14B-4E2F-A2C7-64211519C837} · `_EVENTIID` = {BE69F1B9-970A-474B-A80D-D9BAE4CF720F} · `FriendlyName` = painel IED · `InstanceName` = painelIED0 · `CustomConfig` = painelIED0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawString`, `DrawGroup`, `cObjBotaoHighPerformance0se`, `AnimationBind`, `cObjMedidaAnalogicaPaineis0se`, `cObjCardFundo0se`, `cObjMedidaDigitalPaineis0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fIED0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawString ×1 (ID_DJ)
DrawGroup ×1 (grupoMedidas)
  DrawGroup ×2 (grupoAnalog, grupoDigital)
    cObjBotaoHighPerformance0se ×6 (call06, call05, call04, …)
    DrawGroup ×6 (Analog01, Analog02, Analog03, …)
      cObjMedidaAnalogicaPaineis0se ×13 (Analog13, Analog12, Analog11, …)
  cObjBotaoHighPerformance0se ×2 (callAnalog, callDiscrete)
  cObjCardFundo0se ×1 (cObjCardFundo1)
cObjCardFundo0se ×1 (cObjCardFundo1)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `call06.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call01.CallChildVisible` (8 linhas), `callAnalog.CallChildVisible` (4 linhas), `callDiscrete.CallChildVisible` (4 linhas), `call05.CallChildVisible` (7 linhas), `call04.CallChildVisible` (7 linhas), `call03.CallChildVisible` (7 linhas), `call02.CallChildVisible` (7 linhas), `call01.CallChildVisible` (7 linhas)

**Elementos gráficos:** DrawGroup ×14, DrawString ×1

<a id="cpaineldisjuntor0se"></a>
### cPainelDisjuntor0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {653EF6E4-675F-40CD-9218-97F9905FA22D} · `_IID` = {FC882BEA-6EB0-4777-A732-1FA35E03E625} · `_EVENTIID` = {518DFE29-F2CE-4396-8FFB-D2ADDCEEF32C} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `AnimationBind`, `cEquipDisjuntor0se`, `cObjElectricConnection0se`, `DrawGroup`, `cObjBotaoHighPerformance0se`, `cObjMedidaAnalogicaPaineis0se`, `cObjCardFundo0se`, `cObjMedidaDigitalPaineis0se`, `TableBind`, `DrawString`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fDisjuntor0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×2 (buttonCallRelig, buttonSaveNote)
cEquipDisjuntor0se ×1 (cEquipDisjuntor0se1)
cObjElectricConnection0se ×2 (cObjElectricConnection0se2, cObjElectricConnection0se1)
DrawGroup ×2 (grupoMedidas, Command)
  cObjBotaoHighPerformance0se ×2 (callDiscrete, callAnalog)
  DrawGroup ×2 (grupoAnalog, grupoDigital)
    DrawGroup ×6 (Analog01, Analog02, Analog03, …)
      cObjMedidaAnalogicaPaineis0se ×13 (Analog13, Analog12, Analog11, …)
    cObjBotaoHighPerformance0se ×6 (call01, call02, call03, …)
  cObjCardFundo0se ×1 (cObjCardFundo1)
cObjCardFundo0se ×2 (cObjCardFundo1, cObjCardFundo0se1)
```

**Eventos com script:** `buttonCallRelig.callNotes` (8 linhas), `buttonSaveNote.callNotes` (8 linhas), `callDiscrete.CallChildVisible` (4 linhas), `call01.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas), `call06.CallChildVisible` (8 linhas), `callAnalog.CallChildVisible` (4 linhas), `call01.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas)

**Elementos gráficos:** DrawGroup ×20, DrawString ×5

<a id="cpainelchave0se"></a>
### cPainelChave0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {9CF18702-5352-4EB8-A94E-A8A0033A7A06} · `_IID` = {605DB7A0-4AC7-45BA-B9C2-35C88B0BB2E4} · `_EVENTIID` = {C89C738B-7294-4E69-8818-700391138268} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawGroup`, `TableBind`, `DrawCircle`, `DrawConnector`, `DrawString`, `cObjCardFundo0se`, `cObjBotaoHighPerformance0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fChave0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawGroup ×1 (Grupo1)
  DrawGroup ×3 (x1203, x2103, Command)
    DrawGroup ×1 (Grupo1)
      DrawCircle ×2 (Carga, Fonte)
      DrawConnector ×5 (Aberto, Connector2, Connector3, …)
      DrawString ×1 (Id)
    cObjCardFundo0se ×1 (cObjCardFundo1)
  cObjCardFundo0se ×1 (cObjCardFundo2)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas)

**Elementos gráficos:** DrawGroup ×10, DrawConnector ×10, DrawString ×6, DrawCircle ×4

<a id="cobjmedidadigitalpaineis0se"></a>
### cObjMedidaDigitalPaineis0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {BDB72935-3CCC-4BF0-ADBE-5B6453784EDF} · `_IID` = {49FFFFAF-872C-4457-8800-4944EDDC6F8C} · `_EVENTIID` = {5C4AA42F-57A5-498B-880D-97CB01D8EC4F} · `InstanceName` = Discrete0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `TableBind`, `cObjCardFundo0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaDigital0se |  | S | S |  |  | Nome da Medida Analógica \| Max 22 caracteres |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawString ×1 (Text2)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
DrawString ×1 (Text1)
```

**Elementos gráficos:** DrawString ×2, DrawGroup ×1

<a id="cobjmedidaanalogicapaineis0se"></a>
### cObjMedidaAnalogicaPaineis0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {4CDEF00C-4533-4A4D-8F72-F4A1C5D6511F} · `_IID` = {7AFF5D70-4C90-4AEF-9A29-4912B9A4BB06} · `_EVENTIID` = {3278878B-9BC4-4A03-B4A4-4A81369C2241} · `InstanceName` = Analog0 · `CustomConfig` = Medida Analógica Painéis · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `cObjCardFundo0se`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaAnalogica0se |  | S | S |  |  | Nome da Medida Analógica \| Max 22 caracteres |  |
| 2 | `Conversao` | Variant | Double `1` | S | S |  |  | Inserir a fórmula de conversão \| Por padrão, o valor está em 1 para que, em caso de não-utilização, mantenha o valor aquisitado |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Text2, Text1)
cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**Elementos gráficos:** DrawString ×2

<a id="cobjheader0se"></a>
### cObjHeader0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {97CD3ADF-3D81-4D98-AB8A-6817B3306A41} · `_IID` = {25519ABE-1BC5-4CD6-B6D8-87056A1B1D24} · `_EVENTIID` = {FDE40F9A-EDA2-4571-8116-61A80BD4DDC4} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjLogoSCADA`, `DrawString`, `AnimationBind`, `DrawGroup`, `cNavegacaoScreensHeader0se`, `DrawPicture`, `MultiSourceBind`, `cObjCardFundo0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oConfigHeader0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjLogoSCADA ×1 (cObjLogoSCADA1)
DrawString ×5 (versionSCADA, Usuario, Data, …)
DrawGroup ×1 (navegacao)
  cNavegacaoScreensHeader0se ×6 (cNavegacaoScreensHeader0se7, cNavegacaoScreensHeader0se6, cNavegacaoScreensHeader0se3, …)
DrawPicture ×2 (Figura1, ExitButton)
cObjCardFundo0se ×3 (fundoLogin, fundoNomePagina, fundoHeader)
```

**Eventos com script:** `versionSCADA.Click` (36 linhas), `ExitButton.Click` (3 linhas), `Usuario.Click` (12 linhas)

**Elementos gráficos:** DrawString ×5, DrawPicture ×2, DrawGroup ×1

<a id="cobjelectricconnection0se"></a>
### cObjElectricConnection0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {D990D851-695B-4EA4-A5FA-7FC7F518BEEA} · `_IID` = {47F73295-0A39-4B18-A0AA-60AB046000C0} · `_EVENTIID` = {98AC2AF5-9BB2-4871-9E00-28E2DA9BD0A4} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawTank`, `TableBind`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgStatus` | Integer | Integer `0` | S | S |  |  | 0 - Sem Energia \| 1 - Com Energia \| -1 -> Falha |  |
| 2 | `cfgHabilitaRound` | Integer | Integer `1` | S | S |  |  | 1 - Rounded \| 0 - Line |  |

**Estrutura interna (classe ×qtd):**

```
DrawTank ×1 (RetanguloArr3)
```

**Elementos gráficos:** DrawTank ×1

<a id="cobjbotaohighperformance0se"></a>
### cObjBotaoHighPerformance0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {D4508EF1-5C42-4ED8-B334-8193085D0804} · `_IID` = {5F25C7D4-D0EB-4859-960D-EE5185D29445} · `_EVENTIID` = {759E0606-8A59-4ED5-B175-51DA7737DAF8} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawTank`, `DrawString`, `MultiSourceBind`, `TableBind`, `AnimationBind`

**Propriedades / métodos próprios (14)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgCaption` | String |  | S | S |  |  |  |  |
| 2 | `cfgColorButton` | Color |  | S | S |  |  |  |  |
| 3 | `cfgColorButtonMouseOver` | Color |  | S | S |  |  |  |  |
| 4 | `cfgColorText` | Color |  | S | S |  |  |  |  |
| 5 | `cfgColorTextMouseOver` | Color |  | S | S |  |  |  |  |
| 6 | `cfgButtonType` | Integer | Integer `0` | S | S |  |  | 0 - Comando Simples \| 1 - Navigate (Group or Script) \| 2 - Comando Duplo (Select + Execute) \| 3 - Call PopUp \| 4 - call Screen |  |
| 7 | `cfgCommand` | fComando0se |  | S | S |  |  |  |  |
| 8 | `cfgSecondCommand` | fComando0se |  | S | S |  |  |  |  |
| 9 | `cfgCommandName` | Variant |  | S | S |  |  |  |  |
| 10 | `cfgCommandValue` | Variant |  | S | S |  |  |  |  |
| 11 | `cfgSecondCommandValue` | Variant |  | S | S |  |  |  |  |
| 12 | `cfgNavigateValue` | Boolean | Boolean `False` | S | S |  |  |  |  |
| 13 | `cfgTextSize` | Integer | Integer `0` | S | S |  |  | 0 - Low \| 1 - Medium \| 2 - High |  |
| 14 | `cfgPathMainScreen` | Variant |  | S | S |  |  | Inserir o PathName da Tela a ser aberta via comando de Call Popup (3) ou Call Screen. |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (botao)
  DrawTank ×4 (IndispCommand, Navigate, SingleCommand, …)
  DrawString ×3 (Size2, Size1, Size0)
```

**Eventos com script:** `Navigate.MouseUp` (3 linhas), `Navigate.Click` (23 linhas), `SingleCommand.Click` (31 linhas), `DoubleCommand.Click` (39 linhas)

**Elementos gráficos:** DrawTank ×4, DrawString ×3, DrawGroup ×1

<a id="cnavegacaoscreensheader0se"></a>
### cNavegacaoScreensHeader0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {F890921A-20A7-41E5-8968-3AC8DD47F8AA} · `_IID` = {1BDD35F1-36A9-458E-B89D-AD81423D2226} · `_EVENTIID` = {542C4178-0382-4044-A718-EF836FB0BE92} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `AnimationBind`, `DrawString`, `TableBind`, `DrawRect`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oConfigNavegacaoScreens0se |  | S | S |  |  |  |  |
| 2 | `settingsHeader` | oConfigHeader0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Group1)
  DrawString ×1 (Texto1)
  DrawRect ×1 (Rectangle1)
```

**Eventos com script:** `Group1.Click` (25 linhas)

**Elementos gráficos:** DrawGroup ×1, DrawString ×1, DrawRect ×1

<a id="cequipied0se"></a>
### cEquipIED0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {E8D537F4-D5DB-4148-B843-E1B417625E76} · `_IID` = {9B0AC708-9584-4310-9769-CAAB6DCEC381} · `_EVENTIID` = {65FD6EA4-C024-4F8F-805B-5C8A6043519B} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawString`, `DrawTank`, `AnimationBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fIED0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawString ×2 (Text2, Text1)
DrawTank ×2 (RoundRect2, RoundRect1)
```

**Eventos com script:** `RoundRect1.Click` (8 linhas)

**Elementos gráficos:** DrawString ×2, DrawTank ×2

<a id="cequipgerador0se"></a>
### cEquipGerador0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {74495A4D-E778-4B79-992B-6602D2280A93} · `_IID` = {E4586EC8-2BC2-46AE-9F6C-1BCFD2D7CBED} · `_EVENTIID` = {76077908-05F3-4D9D-BDB4-8355BFF93863} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawLine`, `TableBind`, `DrawCircle`

**Propriedades / métodos próprios (4)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgBackColor` | Color |  | S | S |  |  |  |  |
| 2 | `cfgMiddleColor` | Color |  | S | S |  |  |  |  |
| 3 | `cfgBorderColor` | Color |  | S | S |  |  |  |  |
| 4 | `cfgStatus` | Integer | Integer `0` | S | S |  |  | 0 - Desligado \| 1 - Em Standby \| 2 - Em Operação \| (-1) - Falha |  |

**Estrutura interna (classe ×qtd):**

```
DrawLine ×2 (Middle, Border)
DrawCircle ×1 (Back)
```

**Elementos gráficos:** DrawLine ×2, DrawCircle ×1

<a id="cequipdisjuntor0se"></a>
### cEquipDisjuntor0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {4B10393D-C055-4FA7-9BCD-9BE82CA94ECA} · `_IID` = {73AA9C48-3832-40C6-AFE9-00B7C1947B1F} · `_EVENTIID` = {12634981-E5D4-480B-A897-CBCB99EC63B1} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `DrawString`, `TableBind`, `DrawTank`, `cObjCardFundo`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fDisjuntor0se | String `xxxxxxxx` | S | S |  |  | PROPRIEDADES: cfgId, disEstado, cfgPlanta, cfgFabricante, cfgModelo, Alarmes     \| SCRIPTS:  \| |  |
| 2 | `cfgEnableInfo` | Integer | Integer `1` | S | S |  |  | Habilita ou desabilita as informações do DJ (ID e Modo) |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×3 (Type, SUPERVISIONADO, MANUAL)
  DrawString ×1 (TipoOperacao)
  DrawTank ×1 (RetanguloArr1)
```

**Eventos com script:** `RetanguloArr1.Click` (8 linhas), `RetanguloArr1.Click` (8 linhas), `RetanguloArr1.Click` (8 linhas)

**Elementos gráficos:** DrawGroup ×9, DrawString ×8, DrawTank ×6

<a id="cequipchave0se"></a>
### cEquipChave0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {821B9454-FC16-43CC-AD89-B30ECA8944C8} · `_IID` = {BB481626-7387-422A-BE80-BECD344F73F1} · `_EVENTIID` = {531786A2-0312-43B2-BAD2-E487EB1BAB25} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `DrawGroup`, `TableBind`, `cObjNotaOperativa`, `DrawString`, `AnimationBind`, `DrawTank`, `DrawCircle`, `DrawLine`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fChave0se |  | S | S |  |  |  |  |
| 2 | `Orientacao` | Boolean | Boolean `True` | S | S |  |  | True = Vertical \| False = Horizontal |  |
| 3 | `PosAbertura` | Boolean | Boolean `False` | S | S |  |  | True = Lado Fonte \| False = Lado Carga |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×2 (Vertical, Horizontal)
  cObjNotaOperativa ×1 (cObjNotaOperativa1)
  DrawString ×2 (falhaCom, id)
  DrawGroup ×2 (Grupo2, Grupo1)
    DrawString ×1 (Tipo)
    DrawTank ×1 (RetanguloArr1)
```

**Eventos com script:** `falhaCom.Click` (8 linhas), `Chave.Click` (8 linhas), `id.Click` (8 linhas), `falhaCom.Click` (8 linhas), `Chave.Click` (8 linhas), `id.Click` (8 linhas)

**Elementos gráficos:** DrawGroup ×14, DrawLine ×12, DrawString ×6, DrawCircle ×4, DrawTank ×2

<a id="cdashcardgeral0se"></a>
### cDashCardGeral0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {7A2116ED-D99B-4E06-9E5C-47E3C4E62185} · `_IID` = {D02A35C5-8FDC-43A2-B2D3-81BC31C863BA} · `_EVENTIID` = {96077FFC-614A-47E7-85D1-09F6D5238D23} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `TableBind`, `DrawTank`, `AnimationBind`, `cDashBarGraph0se`, `cDashGaugePequeno0se`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigCardGeralUsinas0se |  | S | S |  |  |  |  |
| 2 | `SE` | Integer | Integer `1` | S | S |  |  | SE Comissionada = 2 \| SE Não Comissionada = 1 \| Sem SE = 0 |  |
| 3 | `PV` | Integer | Integer `1` | S | S |  |  | PV Comissionada = 2 \| PV Não Comissionada = 1 \| Sem PV = 0 |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Card)
  DrawGroup ×2 (header, Grupo4)
    DrawString ×1 (nomePlanta)
    DrawTank ×1 (RoundRect2)
  DrawTank ×2 (falhaCom, RoundRect1)
  cDashBarGraph0se ×2 (cDashBarGraph0se2, cDashBarGraph0se1)
  cDashGaugePequeno0se ×2 (cDashGaugePequeno0se2, cDashGaugePequeno0se1)
```

**Eventos com script:** `nomePlanta.Click` (37 linhas)

**Elementos gráficos:** DrawGroup ×3, DrawString ×3, DrawTank ×3

<a id="cequiptrafo0se"></a>
### cEquipTrafo0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {3C826D55-4031-4957-A22A-597183560464} · `_IID` = {587CCD50-D449-46FF-A916-212CD205147F} · `_EVENTIID` = {7A042001-FB27-460C-8B8D-C6ECF992A94F} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `TableBind`, `DrawCircle`, `DrawLine`, `DrawConnector`, `DrawString`, `DrawTank`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fTransformador0se |  | S | S |  |  |  |  |
| 2 | `cfgTipoTrafo` | Integer | Integer `0` | S | S |  |  | 0 - Dyn (Alta - Delta / Baixa - Estrela) \| 1 - Ddyn (Alta - Delta / Baixa01 - delta \| Baixa 02 - Estrela) \| 2 - Dydn (Alta - Delta / Baixa01 - Estrela) / Baixa02 - delta ) \| 3 - Dyyn (Alta - Delta / Baixa01 - Estrela) / Baixa02 - Estrela) \| 4 - Dyn Invertido (Alta - Delta / Baixa - Estrela) |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×4 (1sec, 2sec, Descritivo, …)
  DrawGroup ×2 (Bordas, Fundo)
    DrawCircle ×2 (Alta, Baixa)
    DrawLine ×1 (Delta)
    DrawGroup ×1 (Estrela)
      DrawConnector ×3 (Connector3, Connector2, Connector1)
```

**Eventos com script:** `cEquipTrafo0se.CustomConfig` (3 linhas), `Fundo.Click` (8 linhas), `Fundo.Click` (8 linhas), `Fundo.Click` (8 linhas)

**Elementos gráficos:** DrawGroup ×17, DrawCircle ×14, DrawConnector ×12, DrawLine ×5, DrawString ×5, DrawTank ×1

<a id="cobjcardfundo0se"></a>
### cObjCardFundo0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {C4B17DE1-CC1F-4497-B48E-60BA4D19FE8D} · `_IID` = {03E39789-5820-4016-9F93-6912471CB2E2} · `_EVENTIID` = {CDFD428F-785B-4A2B-81DD-E005618C4877} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawTank`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgCorPrincipal` | Color | Long `2368548` | S | S |  |  |  |  |
| 2 | `cfgCorBorda` | Color | Long `5530222` | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawTank ×1 (RetanguloArr3)
```

**Elementos gráficos:** DrawTank ×1

<a id="cdashbargraph0se"></a>
### cDashBarGraph0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {E1C92EC8-EA54-45C4-B94B-C26930463FD8} · `_IID` = {0A5C350E-8126-4B28-A9A5-13BEA03C7175} · `_EVENTIID` = {3E16AECE-EC55-4494-8FB0-259927C43FE4} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DynamicMove`, `DrawGroup`, `DrawLine`, `DrawConnector`, `DrawString`, `TableBind`, `AnimationBind`, `DrawTank`

**Propriedades / métodos próprios (5)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Value` | Double |  | S | S |  |  | Valor Atual |  |
| 2 | `NominalValue` | Double |  | S | S |  |  | Valor nominal |  |
| 3 | `LowLimit` | Double | Integer `15` | S | S |  |  | Inserir o % em relação ao valor nominal |  |
| 4 | `HighLimit` | Double | Integer `15` | S | S |  |  | Inserir o % em relação ao valor nominal |  |
| 5 | `Format` | Format |  | S | S |  |  | Formato do Dado |  |

**Estrutura interna (classe ×qtd):**

```
DynamicMove ×3 (moveMedido, moveBaixo, moveAlto)
  DrawGroup ×1 (medido)
    DrawLine ×1 (valorMedido)
DrawConnector ×1 (Conector1)
DrawString ×1 (Texto1)
DrawTank ×1 (base)
```

**Elementos gráficos:** DynamicMove ×3, DrawGroup ×3, DrawLine ×3, DrawString ×3, DrawConnector ×1, DrawTank ×1

<a id="cequipretificador0se"></a>
### cEquipRetificador0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {063D74EF-C394-4631-A6C2-F11F247701B5} · `_IID` = {3B3D6D7A-4938-49CA-AA42-74C00B531124} · `_EVENTIID` = {A1045AD0-7BD7-4C25-9235-DCC5929D787B} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`
- Classes que usa internamente: `cObjNotaOperativa`, `DrawGroup`, `TableBind`, `DrawString`, `cObjCardFundo`, `DrawLine`, `DrawArc`, `DrawConnector`, `DrawRect`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fRetificador0se |  | S | S |  |  | Propriedades: |  |
| 2 | `cfgHabilitarAcesso` | Boolean | Boolean `True` | S | S |  |  | Habilita ou não o acesso ao painel do Retificador |  |
| 3 | `cfgRetificador` | Boolean | Boolean `False` | S | S |  |  | Se True = Retificador \| Se False = Retificador |  |

**Estrutura interna (classe ×qtd):**

```
cObjNotaOperativa ×1 (cObjNotaOperativa1)
DrawGroup ×2 (falhaCom, Group1)
  DrawString ×1 (falhaCom)
  cObjCardFundo ×1 (cObjCardFundo1)
DrawString ×1 (Text1)
```

**Eventos com script:** `Corpo.Click` (8 linhas)

**Elementos gráficos:** DrawGroup ×2, DrawString ×2, DrawLine ×2, DrawArc ×2, DrawConnector ×1, DrawRect ×1

<a id="cdashgauge0se"></a>
### cDashGauge0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {18AB3F08-6EFF-41A4-B8F7-36E8EE95586D} · `_IID` = {BF3CD1B0-776F-4BF8-956B-4E5769DC3123} · `_EVENTIID` = {EB0A90D1-FDE7-469C-856F-47368E51196F} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawGroup`, `DrawString`, `DrawCircle`, `DrawArc`, `AnalogBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigGauge0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (Grupo1)
  DrawString ×2 (Medida, Valor)
  DrawCircle ×1 (Centro)
  DrawArc ×3 (BordaGrafico, BordaGrafico2, Grafico)
DrawString ×1 (Text1)
```

**Elementos gráficos:** DrawString ×3, DrawArc ×3, DrawGroup ×1, DrawCircle ×1

<a id="cdashgaugepequeno0se"></a>
### cDashGaugePequeno0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {F7CBD322-953B-4496-985D-6D07E198991E} · `_IID` = {D1D2B0F6-0F39-4B16-BFF7-6D6070F4C6A9} · `_EVENTIID` = {CD9AEAF3-ADFB-44CC-8436-F553640F0021} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawCircle`, `DrawArc`, `AnalogBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigGauge0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Medida, Valor)
DrawCircle ×1 (Centro)
DrawArc ×2 (BordaGrafico, Grafico)
```

**Elementos gráficos:** DrawString ×2, DrawArc ×2, DrawCircle ×1

<a id="cpainelretificador0se"></a>
### cPainelRetificador0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {D1A534F2-0EEE-43B7-A7B1-DAF1D0535AFF} · `_IID` = {C69DA450-33ED-4BE6-9B66-BDD23A4ADC93} · `_EVENTIID` = {61FE5709-3DF6-47F9-BB62-369CF3597023} · `FriendlyName` = painel Retificador · `InstanceName` = painelRetificador0 · `CustomConfig` = painelRetificador0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolpv.lib`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `cObjBotaoHighPerformance`, `DrawString`, `DrawGroup`, `cObjBotaoHighPerformance0se`, `AnimationBind`, `cObjMedidaAnalogicaPaineis0se`, `cObjCardFundo0se`, `cObjMedidaDigitalPaineis0se`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fRetificador0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
cObjBotaoHighPerformance ×1 (buttonSaveNote)
DrawString ×1 (ID)
DrawGroup ×1 (grupoMedidas)
  DrawGroup ×2 (grupoAnalog, grupoDigital)
    cObjBotaoHighPerformance0se ×6 (call06, call05, call04, …)
    DrawGroup ×6 (Analog01, Analog02, Analog03, …)
      cObjMedidaAnalogicaPaineis0se ×13 (Analog13, Analog12, Analog11, …)
  cObjBotaoHighPerformance0se ×2 (callAnalog, callDiscrete)
  cObjCardFundo0se ×1 (cObjCardFundo1)
cObjCardFundo0se ×1 (cObjCardFundo1)
```

**Eventos com script:** `buttonSaveNote.callNotes` (8 linhas), `call06.CallChildVisible` (8 linhas), `call05.CallChildVisible` (8 linhas), `call04.CallChildVisible` (8 linhas), `call03.CallChildVisible` (8 linhas), `call02.CallChildVisible` (8 linhas), `call01.CallChildVisible` (8 linhas), `callAnalog.CallChildVisible` (4 linhas), `callDiscrete.CallChildVisible` (4 linhas), `call05.CallChildVisible` (7 linhas), `call04.CallChildVisible` (7 linhas), `call03.CallChildVisible` (7 linhas), `call02.CallChildVisible` (7 linhas), `call01.CallChildVisible` (7 linhas)

**Elementos gráficos:** DrawGroup ×14, DrawString ×1

<a id="cequipbateria0se"></a>
### cEquipBateria0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {4A66ABC1-E576-44C2-8F58-19D1899094CF} · `_IID` = {64C24901-2971-4EBF-BBC5-37F5DB1DFACD} · `_EVENTIID` = {8922A61E-5F0C-4989-89F1-DD07CF0B4080} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawTank`

_Sem propriedades próprias definidas em `XCoClass.Methods`._

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Texto2, Texto1)
DrawTank ×1 (RetanguloArr3)
```

**Elementos gráficos:** DrawString ×2, DrawTank ×1

<a id="cobjanalogscreen0se"></a>
### cObjAnalogScreen0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {FFF11FF7-CF0D-404C-95CC-AA1C232A53B7} · `_IID` = {A09C189F-4B8C-4FA4-B604-F81522B67BB3} · `_EVENTIID` = {B6F71844-1879-40EB-8A6B-B2D67C5B3C10} · `InstanceName` = AnlScreen0 · `CustomConfig` = Medida Analógica Screens · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawString`, `AnimationBind`, `cObjCardFundo0se`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Config` | fMedidaAnalogica0se |  | S | S |  |  | link com a medida |  |
| 2 | `Conversao` | Variant | Double `1` | S | S |  |  | Inserir a fórmula de conversão \| Por padrão, o valor está em 1 para que, em caso de não-utilização, mantenha o valor aquisitado |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×1 (Text2)
cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**Elementos gráficos:** DrawString ×1

<a id="cobjground0se"></a>
### cObjGround0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {C4E5BD32-2D10-4A35-BB14-21F0978A154E} · `_IID` = {27F07FF8-16B5-4C08-947B-2A1425E7ACE3} · `_EVENTIID` = {1747757F-7EC4-441F-A564-014B3B9323E0} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawGroup`, `TableBind`, `cObjElectricConnection0se`

**Propriedades / métodos próprios (2)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `cfgStatus` | Integer |  | S | S |  |  | 0 - Sem energização \| 1 - Energizado \| -1 - Em Falha |  |
| 2 | `cfgOrientacao` | Integer |  | S | S |  |  | 0 - Vertical \| 1 - Horizontal |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×1 (pos)
  DrawGroup ×2 (vertical, Horizontal)
    cObjElectricConnection0se ×3 (cObjElectricConnection0se81, cObjElectricConnection0se80, cObjElectricConnection0se79)
```

**Elementos gráficos:** DrawGroup ×3

<a id="cequipcub0se"></a>
### cEquipCUB0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {563A871B-0278-414E-99C6-68DD32DF6F6B} · `_IID` = {9A100AA2-C74E-4CDA-9AEA-E385A0B5DC31} · `_EVENTIID` = {BB4CA0C2-1C15-43B7-BAE9-5EC07998D6F9} · `InstanceName` = CUB0 · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`, `matrixenergylibxcontrolse.lib`
- Classes que usa internamente: `DrawGroup`, `TableBind`, `cEquipChave0se`, `cEquipDisjuntor0se`, `cObjElectricConnection0se`, `DrawConnector`, `DrawString`, `DrawRect`, `cObjCardFundo0se`

**Propriedades / métodos próprios (3)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | fElectricPanel0se |  | S | S |  |  |  |  |
| 2 | `cfgType` | Integer |  | S | S |  |  | 0: {1 Sec Entrada + 1 Sec Aterr Entrada + DJ }\| 1:{DJ + 1 Sec Saída } \| 2: 1 SEC Entrada -> 1 DJ -> 1 SEC Saída \| 3: 1 SEC Entrada |  |
| 3 | `cfgEnableBox` | Boolean | Boolean `True` | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawGroup ×4 (1SecEnt, 1secEnt1dj1secSaida, 1dj1secSaida, …)
  cEquipChave0se ×1 (secEntr)
DrawString ×1 (Id)
DrawRect ×1 (boxPontilhada)
cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**Elementos gráficos:** DrawGroup ×7, DrawConnector ×3, DrawString ×1, DrawRect ×1

<a id="cdashgaugepaineis0se"></a>
### cDashGaugePaineis0se

- Biblioteca: `matrixenergylibxcontrolse.lib`  ·  tipo: **XControl**
- Metadados: `_CLSID` = {09512768-435C-4054-B1B2-7F550FA3CA18} · `_IID` = {F2AA2971-66F1-4CA3-B6E8-8BD65B64F9C1} · `_EVENTIID` = {995AB924-D19A-4F56-8A8E-032405FFF5A6} · `EnableTagBehavior` = False · `ValueMode` = 0
- Depende de: `Panel.e3`
- Classes que usa internamente: `DrawString`, `DrawCircle`, `DrawArc`, `AnalogBind`

**Propriedades / métodos próprios (1)** — definidos em `XCoClass.Methods`:

| # | Nome | Tipo | Padrão | Público | Persistível | Retentivo | Expose | Descrição | Script |
|--:|---|---|---|:--:|:--:|:--:|:--:|---|---|
| 1 | `Settings` | oDashConfigGauge0se |  | S | S |  |  |  |  |

**Estrutura interna (classe ×qtd):**

```
DrawString ×2 (Medida, Valor)
DrawCircle ×1 (Centro)
DrawArc ×2 (BordaGrafico, Grafico)
```

**Elementos gráficos:** DrawString ×2, DrawArc ×2, DrawCircle ×1
