# Hierarquia dos objetos E3

Estrutura de contenção observada em **29 projetos** (Main, GC, SE, GD) e **9 libs** (XFolder/XControl/XObject), sem valores. `[XFolder]`/`[XControl]`/`[XObject]`/`[nativa]` = origem da classe. "Fontes" = em quantos arquivos a relação aparece.

## 1. Nível de projeto: pastas e nós

O projeto é uma árvore de **pastas organizadoras** (sem dados) e **nós**. Cada nó guarda um conjunto de objetos e é identificado pela **classe do objeto raiz**. Recursos (imagens/sons) são nós folha sem objetos.

> Linhas com pai `<projeto>` e filho XFolder/XControl/XObject/Recurso vêm dos arquivos `.lib` (cada classe da lib é um nó); as demais, dos `.prj`.

| Pai | Filho | Qtd | Fontes |
|---|---|---:|---:|
| Pasta | Screen [nativa] | 180 | 27 |
| <projeto> | XControl [nativa] | 127 | 3 |
| Pasta | Pasta | 106 | 29 |
| <projeto> | XFolder [nativa] | 68 | 3 |
| <projeto> | Recurso | 63 | 1 |
| Pasta | IODriver [nativa] | 57 | 29 |
| Pasta | DataServer [nativa] | 53 | 27 |
| <projeto> | Pasta | 32 | 29 |
| <projeto> | XObject [nativa] | 31 | 4 |
| Pasta | Recurso | 13 | 1 |
| Pasta | DBServer [nativa] | 3 | 1 |
| Pasta | Hist [nativa] | 3 | 2 |
| Pasta | Frame [nativa] | 3 | 1 |
| Pasta | UaDriver [nativa] | 2 | 1 |
| Pasta | AlarmServer [nativa] | 1 | 1 |
| Pasta | Viewer [nativa] | 1 | 1 |

### Classes raiz de nó

| Classe raiz | Nós | Fontes |
|---|---:|---:|
| Screen [nativa] | 180 | 27 |
| XControl [nativa] | 127 | 3 |
| XFolder [nativa] | 68 | 3 |
| IODriver [nativa] | 57 | 29 |
| DataServer [nativa] | 53 | 27 |
| XObject [nativa] | 31 | 4 |
| DBServer [nativa] | 3 | 1 |
| Hist [nativa] | 3 | 2 |
| Frame [nativa] | 3 | 1 |
| UaDriver [nativa] | 2 | 1 |
| AlarmServer [nativa] | 1 | 1 |
| Viewer [nativa] | 1 | 1 |

## 2. Estrutura dentro de cada tipo de nó

> **Contenção observada, não regra imposta:** as libs não definem onde cada classe pode ser criada (`Contexts` quase nunca é usado). As relações abaixo são o que **ocorre** nos projetos e libs; a árvore é a união de todas as variantes (GD, GC, SE, Main), por isso mistura caminhos que nunca coexistem num mesmo projeto. Para uma árvore concreta, veja a seção 5.

Árvore de contenção a partir de cada classe raiz (profundidade ≤ 5; `↻` = classe já exibida acima no mesmo ramo; filhos com ≤ 1 ocorrência em 1 fonte omitidos — veja a matriz da seção 3).

### Screen [nativa]

```
Screen [nativa]  (raiz de nó: 180 nós)
  cObjElectricConnection0se [XControl]  ×1410 (26)
  cEquipInversor [XControl]  ×622 (23)
  cEquipString [XControl]  ×622 (23)
  cEquipDisjuntor0se [XControl]  ×438 (25)
  cEquipChave0se [XControl]  ×432 (26)
  DrawGroup [nativa]  ×373 (25)
    cEquipArrayLayout [XControl]  ×5668 (21)
    cObjElectricConnection0se [XControl]  ×1456 (19)
    cEquipFiltro [XControl]  ×678 (21)
    DrawGroup [nativa] ↻  ×607 (23)
    cObjMedidaAnalogicaPaineis0se [XControl]  ×490 (2)
    cObjMedidaDigitalPaineis0se [XControl]  ×490 (2)
    DrawString [nativa]  ×400 (23)
    DrawLine [nativa]  ×275 (10)
    cObjMedidaDigitalPaineis [XControl]  ×267 (1)
    cTabularTRK [XControl]  ×184 (1)
    cObjBotaoHighPerformance0se [XControl]  ×134 (2)
    cObjMedidaAnalogicaPaineis [XControl]  ×112 (1)
    DrawConnector [nativa]  ×94 (6)
    DrawTank [nativa]  ×93 (12)
    cObjCardFundo [XControl]  ×91 (5)
    cObjBotaoHighPerformance [XControl]  ×81 (3)
    cEquipNCU [XControl]  ×68 (5)
    DrawCircle [nativa]  ×54 (18)
    DrawRect [nativa]  ×53 (18)
    cEquipIED0se [XControl]  ×50 (1)
    cEquipChave0se [XControl]  ×40 (4)
    cObjCardFundo0se [XControl]  ×35 (3)
    cEquipInversor [XControl]  ×34 (3)
    cEquipDisjuntor0se [XControl]  ×33 (2)
    cEquipString [XControl]  ×33 (2)
    cObjMedidaAnalogicaTela [XControl]  ×33 (1)
    cTabularResumoUsinas [XControl]  ×26 (1)
    DrawArc [nativa]  ×23 (4)
    cEquipStringLayout [XControl]  ×20 (1)
    cObjComConnection [XControl]  ×16 (1)
    cObjSelect [XControl]  ×10 (1)
    cPainelResumedMeteo [XControl]  ×9 (1)
    CheckBox [nativa]  ×9 (2)
    DrawBezier [nativa]  ×7 (2)
    E3Alarm [nativa]  ×6 (2)
    cIconeIED [XControl]  ×6 (1)
    cNavegacaoScreensHeader0se [XControl]  ×6 (1)
    cObjNotaOperativa [XControl]  ×4 (2)
    cEquipTracker [XControl]  ×4 (1)
    E3Browser [nativa]  ×2 (1)
      E3Query [nativa]  ×3 (2)
    ComboBox [nativa]  ×2 (2)
    cObjGauge [XControl]  ×2 (1)
    cDashGaugePaineis [XControl]  ×2 (1)
    cLibGHI [XControl]  ×2 (1)
    cObjAlarme [XControl]  ×2 (1)
    DynamicMove [nativa]  ×2 (1)
      DrawGroup [nativa] ↻  ×6 (2)
      DrawTank [nativa]  ×2 (1)
    cLibPOA [XControl]  ×2 (1)
    cDashBarGraph0se [XControl]  ×2 (1)
    cDashGaugePequeno0se [XControl]  ×2 (1)
  DrawString [nativa]  ×363 (27)
  cEquipArrayLayout [XControl]  ×98 (2)
  cEquipTrafo0se [XControl]  ×96 (26)
  cObjComConnection [XControl]  ×90 (2)
  DrawLine [nativa]  ×88 (26)
  cObjCardFundo [XControl]  ×76 (13)
  cObjBotaoHighPerformance0se [XControl]  ×56 (7)
  cEquipMultimedidor [XControl]  ×56 (22)
  DrawTank [nativa]  ×55 (20)
  cObjCardFundo0se [XControl]  ×50 (27)
  cDetalhesUsina [XControl]  ×41 (25)
  E3Alarm [nativa]  ×40 (26)
  cPainelMedidasTela [XControl]  ×40 (20)
  cEquipCMB [XControl]  ×36 (20)
  DrawRect [nativa]  ×35 (14)
  cObjAnalogScreen0se [XControl]  ×31 (3)
  cObjBotaoHighPerformance [XControl]  ×30 (3)
  E3Chart [nativa]  ×28 (1)
    E3Query [nativa]  ×2 (1)
  cObjHeader0se [XControl]  ×27 (27)
  cObjTelaAlarmes [XControl]  ×26 (26)
  cObjHist [XControl]  ×26 (26)
  cDashCardGeralUsinas [XControl]  ×25 (1)
  cIconeIED [XControl]  ×25 (2)
  cEquipGerador0se [XControl]  ×22 (5)
  cEquipPPC [XControl]  ×22 (5)
  cPainelResumedMeteo [XControl]  ×22 (4)
  cObjGround0se [XControl]  ×22 (2)
  DrawConnector [nativa]  ×20 (3)
  cEquipIED0se [XControl]  ×20 (2)
  cEquipMeteorologica [XControl]  ×20 (20)
  cEquipFiltro [XControl]  ×20 (2)
  cEquipCUB0se [XControl]  ×19 (2)
  cEquipNCU [XControl]  ×17 (14)
  DrawCircle [nativa]  ×13 (9)
  cDashGauge [XControl]  ×8 (4)
  cIconeCFTV [XControl]  ×7 (1)
  cIconeRTU [XControl]  ×7 (1)
  cDashPizzaGraph [XControl]  ×5 (1)
  cIconeConversorRede [XControl]  ×5 (1)
  cIconeServidorSimples [XControl]  ×5 (2)
  cIconeCloud [XControl]  ×4 (2)
  cEquipRetificador0se [XControl]  ×4 (2)
  cDashGauge0se [XControl]  ×4 (1)
  cIconeSwitchRede [XControl]  ×3 (1)
  DrawPicture [nativa]  ×2 (1)
  TimerTag [nativa]  ×2 (2)
  ListBox [nativa]  ×2 (1)
  cEquipBateria0se [XControl]  ×2 (1)
```

### XControl [nativa]

```
XControl [nativa]  (raiz de nó: 127 nós)
  DrawString [nativa]  ×135 (3)
  DrawGroup [nativa]  ×112 (3)
    cEquipArrayLayout [XControl]  ×5668 (21)
    cObjElectricConnection0se [XControl]  ×1456 (19)
    cEquipFiltro [XControl]  ×678 (21)
    DrawGroup [nativa] ↻  ×607 (23)
    cObjMedidaAnalogicaPaineis0se [XControl]  ×490 (2)
    cObjMedidaDigitalPaineis0se [XControl]  ×490 (2)
    DrawString [nativa]  ×400 (23)
    DrawLine [nativa]  ×275 (10)
    cObjMedidaDigitalPaineis [XControl]  ×267 (1)
    cTabularTRK [XControl]  ×184 (1)
    cObjBotaoHighPerformance0se [XControl]  ×134 (2)
    cObjMedidaAnalogicaPaineis [XControl]  ×112 (1)
    DrawConnector [nativa]  ×94 (6)
    DrawTank [nativa]  ×93 (12)
    cObjCardFundo [XControl]  ×91 (5)
    cObjBotaoHighPerformance [XControl]  ×81 (3)
    cEquipNCU [XControl]  ×68 (5)
    DrawCircle [nativa]  ×54 (18)
    DrawRect [nativa]  ×53 (18)
    cEquipIED0se [XControl]  ×50 (1)
    cEquipChave0se [XControl]  ×40 (4)
    cObjCardFundo0se [XControl]  ×35 (3)
    cEquipInversor [XControl]  ×34 (3)
    cEquipDisjuntor0se [XControl]  ×33 (2)
    cEquipString [XControl]  ×33 (2)
    cObjMedidaAnalogicaTela [XControl]  ×33 (1)
    cTabularResumoUsinas [XControl]  ×26 (1)
    DrawArc [nativa]  ×23 (4)
    cEquipStringLayout [XControl]  ×20 (1)
    cObjComConnection [XControl]  ×16 (1)
    cObjSelect [XControl]  ×10 (1)
    cPainelResumedMeteo [XControl]  ×9 (1)
    CheckBox [nativa]  ×9 (2)
    DrawBezier [nativa]  ×7 (2)
    E3Alarm [nativa]  ×6 (2)
    cIconeIED [XControl]  ×6 (1)
    cNavegacaoScreensHeader0se [XControl]  ×6 (1)
    cObjNotaOperativa [XControl]  ×4 (2)
    cEquipTracker [XControl]  ×4 (1)
    E3Browser [nativa]  ×2 (1)
      E3Query [nativa]  ×3 (2)
    ComboBox [nativa]  ×2 (2)
    cObjGauge [XControl]  ×2 (1)
    cDashGaugePaineis [XControl]  ×2 (1)
    cLibGHI [XControl]  ×2 (1)
    cObjAlarme [XControl]  ×2 (1)
    DynamicMove [nativa]  ×2 (1)
      DrawGroup [nativa] ↻  ×6 (2)
      DrawTank [nativa]  ×2 (1)
    cLibPOA [XControl]  ×2 (1)
    cDashBarGraph0se [XControl]  ×2 (1)
    cDashGaugePequeno0se [XControl]  ×2 (1)
  cObjCardFundo [XControl]  ×46 (2)
  DrawLine [nativa]  ×37 (2)
  cObjBotaoHighPerformance [XControl]  ×32 (2)
  DrawConnector [nativa]  ×28 (2)
  DrawArc [nativa]  ×23 (2)
  cEquipStringPainel [XControl]  ×22 (1)
  cObjCardFundo0se [XControl]  ×18 (2)
  CheckBox [nativa]  ×18 (1)
  DrawTank [nativa]  ×17 (2)
  cObjNotaOperativa [XControl]  ×13 (2)
  DrawCircle [nativa]  ×12 (2)
  DynamicMove [nativa]  ×7 (2)
    DrawGroup [nativa]  ×6 (2)
      cEquipArrayLayout [XControl]  ×5668 (21)
      cObjElectricConnection0se [XControl]  ×1456 (19)
      cEquipFiltro [XControl]  ×678 (21)
      DrawGroup [nativa] ↻  ×607 (23)
      cObjMedidaAnalogicaPaineis0se [XControl]  ×490 (2)
      cObjMedidaDigitalPaineis0se [XControl]  ×490 (2)
      DrawString [nativa]  ×400 (23)
      DrawLine [nativa]  ×275 (10)
      cObjMedidaDigitalPaineis [XControl]  ×267 (1)
      cTabularTRK [XControl]  ×184 (1)
      cObjBotaoHighPerformance0se [XControl]  ×134 (2)
      cObjMedidaAnalogicaPaineis [XControl]  ×112 (1)
      DrawConnector [nativa]  ×94 (6)
      DrawTank [nativa]  ×93 (12)
      cObjCardFundo [XControl]  ×91 (5)
      cObjBotaoHighPerformance [XControl]  ×81 (3)
      cEquipNCU [XControl]  ×68 (5)
      DrawCircle [nativa]  ×54 (18)
      DrawRect [nativa]  ×53 (18)
      cEquipIED0se [XControl]  ×50 (1)
      cEquipChave0se [XControl]  ×40 (4)
      cObjCardFundo0se [XControl]  ×35 (3)
      cEquipInversor [XControl]  ×34 (3)
      cEquipDisjuntor0se [XControl]  ×33 (2)
      cEquipString [XControl]  ×33 (2)
      cObjMedidaAnalogicaTela [XControl]  ×33 (1)
      cTabularResumoUsinas [XControl]  ×26 (1)
      DrawArc [nativa]  ×23 (4)
      cEquipStringLayout [XControl]  ×20 (1)
      cObjComConnection [XControl]  ×16 (1)
      cObjSelect [XControl]  ×10 (1)
      cPainelResumedMeteo [XControl]  ×9 (1)
      CheckBox [nativa]  ×9 (2)
      DrawBezier [nativa]  ×7 (2)
      E3Alarm [nativa]  ×6 (2)
      cIconeIED [XControl]  ×6 (1)
      cNavegacaoScreensHeader0se [XControl]  ×6 (1)
      cObjNotaOperativa [XControl]  ×4 (2)
      cEquipTracker [XControl]  ×4 (1)
      E3Browser [nativa]  ×2 (1)
        E3Query [nativa]  ×3 (2)
      ComboBox [nativa]  ×2 (2)
      cObjGauge [XControl]  ×2 (1)
      cDashGaugePaineis [XControl]  ×2 (1)
      cLibGHI [XControl]  ×2 (1)
      cObjAlarme [XControl]  ×2 (1)
      DynamicMove [nativa] ↻  ×2 (1)
      cLibPOA [XControl]  ×2 (1)
      cDashBarGraph0se [XControl]  ×2 (1)
      cDashGaugePequeno0se [XControl]  ×2 (1)
    DrawTank [nativa]  ×2 (1)
  DrawRect [nativa]  ×4 (2)
  cLibModuloPV [XControl]  ×3 (1)
  cObjGauge [XControl]  ×2 (1)
  cObjBarGraph [XControl]  ×2 (1)
  cObjMedidaAnalogicaTela [XControl]  ×2 (1)
  E3Browser [nativa]  ×2 (1)
    E3Query [nativa]  ×3 (2)
  cObjElectricConnection0se [XControl]  ×2 (1)
  DrawPicture [nativa]  ×2 (1)
```

### XFolder [nativa]

```
XFolder [nativa]  (raiz de nó: 68 nós)
```

### IODriver [nativa]

```
IODriver [nativa]  (raiz de nó: 57 nós)
  IOFolder [nativa]  ×266 (29)
    IOTag [nativa]  ×140206 (29)
      DiscreteAlarmSource [nativa]  ×2 (2)
    IOFolder [nativa] ↻  ×20551 (29)
    IOBlock [nativa]  ×86 (2)
      IOBlockElement [nativa]  ×344 (2)
  IOTag [nativa]  ×100 (16)
    DiscreteAlarmSource [nativa]  ×2 (2)
```

### DataServer [nativa]

```
DataServer [nativa]  (raiz de nó: 53 nós)
  DataFolder [nativa]  ×83 (27)
    oConfigNavegacaoScreens [XObject]  ×157 (26)
    InternalTag [nativa]  ×89 (25)
      DiscreteAlarmSource [nativa]  ×6 (2)
      DigitalAlarmSource [nativa]  ×3 (2)
    oDashConfigGauge [XObject]  ×54 (26)
    oConfigHeader [XObject]  ×25 (25)
    oDashConfigGauge0se [XObject]  ×6 (1)
    DataFolder [nativa] ↻  ×5 (1)
    oCalcSum [XObject]  ×4 (1)
    oConfigNavegacaoScreens0se [XObject]  ×3 (1)
    oConfigHeader0se [XObject]  ×2 (2)
  oDashConfigCardGeralUsinas [XObject]  ×25 (25)
  fUsinaPV [XFolder]  ×25 (25)
    fSubestacao0se [XFolder]  ×41 (24)
      fDisjuntor0se [XFolder]  ×43 (20)
        fDados [XFolder]  ×472 (24)
          fGrupoAnalogicas [XFolder]  ×37969 (25)
          fGrupoDigitais [XFolder]  ×8219 (25)
          fGrupoComandos [XFolder]  ×876 (25)
          InternalTag [nativa]  ×166 (1)
          oCalcSum [XObject]  ×115 (6)
          oCalcResumoInversores [XObject]  ×96 (25)
          fGrupoDigitais0se [XFolder]  ×69 (4)
          fIED0se [XFolder]  ×41 (1)
          fDados [XFolder] ↻  ×32 (6)
          oMedidaAnalogicaCalculada [XObject]  ×23 (5)
          fMedidaAnalogica [XFolder]  ×21 (1)
          fDados0se [XFolder]  ×20 (20)
          DigitalAlarmSource [nativa]  ×18 (5)
          fCMB [XFolder]  ×9 (1)
          oMedidaAnalogicaCalculada0se [XObject]  ×2 (1)
        fGrupoAnalogicas [XFolder]  ×120 (1)
          fMedidaAnalogica [XFolder]  ×114032 (25)
          oMedidaAnalogicaCalculada0se [XObject]  ×103 (22)
        DigitalAlarmSource [nativa]  ×44 (7)
        fDados0se [XFolder]  ×24 (2)
          oCalcSum [XObject]  ×128 (20)
          fGrupoDigitais0se [XFolder]  ×64 (5)
          fGrupoAnalogicas0se [XFolder]  ×53 (3)
          fGrupoComandos0se [XFolder]  ×46 (2)
          DigitalAlarmSource [nativa]  ×40 (20)
          InternalTag [nativa]  ×29 (2)
          oMedidaAnalogicaCalculada0se [XObject]  ×22 (13)
          oMedidaAnalogicaCalculada [XObject]  ×20 (20)
          fDados0se [XFolder] ↻  ×14 (2)
        fIED0se [XFolder]  ×2 (1)
          fDados [XFolder]  ×42 (1)
          fDados0se [XFolder]  ×24 (4)
          fChave0se [XFolder]  ×11 (1)
          fDisjuntor0se [XFolder] ↻  ×9 (1)
          fTransformador0se [XFolder]  ×2 (1)
        AnalogAlarmSource [nativa]  ×2 (1)
      fTransformador0se [XFolder]  ×34 (21)
        fDados [XFolder]  ×56 (5)
          fGrupoAnalogicas [XFolder]  ×37969 (25)
          fGrupoDigitais [XFolder]  ×8219 (25)
          fGrupoComandos [XFolder]  ×876 (25)
          InternalTag [nativa]  ×166 (1)
          oCalcSum [XObject]  ×115 (6)
          oCalcResumoInversores [XObject]  ×96 (25)
          fGrupoDigitais0se [XFolder]  ×69 (4)
          fIED0se [XFolder]  ×41 (1)
          fDados [XFolder] ↻  ×32 (6)
          oMedidaAnalogicaCalculada [XObject]  ×23 (5)
          fMedidaAnalogica [XFolder]  ×21 (1)
          fDados0se [XFolder]  ×20 (20)
          DigitalAlarmSource [nativa]  ×18 (5)
          fCMB [XFolder]  ×9 (1)
          oMedidaAnalogicaCalculada0se [XObject]  ×2 (1)
        fDados0se [XFolder]  ×2 (1)
          oCalcSum [XObject]  ×128 (20)
          fGrupoDigitais0se [XFolder]  ×64 (5)
          fGrupoAnalogicas0se [XFolder]  ×53 (3)
          fGrupoComandos0se [XFolder]  ×46 (2)
          DigitalAlarmSource [nativa]  ×40 (20)
          InternalTag [nativa]  ×29 (2)
          oMedidaAnalogicaCalculada0se [XObject]  ×22 (13)
          oMedidaAnalogicaCalculada [XObject]  ×20 (20)
          fDados0se [XFolder] ↻  ×14 (2)
      fCampoSolar [XFolder]  ×34 (19)
        fDisjuntor0se [XFolder]  ×300 (1)
          fDados [XFolder]  ×472 (24)
          fGrupoAnalogicas [XFolder]  ×120 (1)
          DigitalAlarmSource [nativa]  ×44 (7)
          fDados0se [XFolder]  ×24 (2)
          fIED0se [XFolder]  ×2 (1)
          AnalogAlarmSource [nativa]  ×2 (1)
        fInversor [XFolder]  ×296 (1)
          fDados [XFolder]  ×655 (25)
          fGrupoStrings [XFolder]  ×594 (21)
          fCampoSolar [XFolder] ↻  ×61 (4)
          fChave0se [XFolder]  ×2 (1)
          fDisjuntor0se [XFolder]  ×2 (1)
        fMPPT [XFolder]  ×61 (4)
          fStringBox [XFolder]  ×897 (4)
        fQGBT [XFolder]  ×36 (20)
          fDisjuntor0se [XFolder]  ×46 (20)
          fCMB [XFolder]  ×36 (20)
          fgrupoChaves [XFolder]  ×32 (17)
          fStringBox [XFolder]  ×10 (4)
        fDados [XFolder]  ×20 (1)
          fGrupoAnalogicas [XFolder]  ×37969 (25)
          fGrupoDigitais [XFolder]  ×8219 (25)
          fGrupoComandos [XFolder]  ×876 (25)
          InternalTag [nativa]  ×166 (1)
          oCalcSum [XObject]  ×115 (6)
          oCalcResumoInversores [XObject]  ×96 (25)
          fGrupoDigitais0se [XFolder]  ×69 (4)
          fIED0se [XFolder]  ×41 (1)
          fDados [XFolder] ↻  ×32 (6)
          oMedidaAnalogicaCalculada [XObject]  ×23 (5)
          fMedidaAnalogica [XFolder]  ×21 (1)
          fDados0se [XFolder]  ×20 (20)
          DigitalAlarmSource [nativa]  ×18 (5)
          fCMB [XFolder]  ×9 (1)
          oMedidaAnalogicaCalculada0se [XObject]  ×2 (1)
        fNCU [XFolder]  ×13 (11)
          fGrupoTrackers [XFolder]  ×58 (19)
          fDados [XFolder]  ×58 (19)
      fElectricPanel0se [XFolder]  ×31 (3)
        fChave0se [XFolder]  ×40 (3)
          fDados [XFolder]  ×462 (24)
          DigitalAlarmSource [nativa]  ×33 (3)
          fDados0se [XFolder]  ×16 (1)
        fDisjuntor0se [XFolder]  ×25 (3)
          fDados [XFolder]  ×472 (24)
          fGrupoAnalogicas [XFolder]  ×120 (1)
          DigitalAlarmSource [nativa]  ×44 (7)
          fDados0se [XFolder]  ×24 (2)
          fIED0se [XFolder]  ×2 (1)
          AnalogAlarmSource [nativa]  ×2 (1)
        fIED0se [XFolder]  ×23 (3)
          fDados [XFolder]  ×42 (1)
          fDados0se [XFolder]  ×24 (4)
          fChave0se [XFolder]  ×11 (1)
          fDisjuntor0se [XFolder]  ×9 (1)
          fTransformador0se [XFolder]  ×2 (1)
        fRetificador0se [XFolder]  ×3 (2)
          fDados0se [XFolder]  ×5 (3)
  … +1058 linhas
```

### XObject [nativa]

```
XObject [nativa]  (raiz de nó: 31 nós)
  InternalTag [nativa]  ×70 (3)
    DiscreteAlarmSource [nativa]  ×6 (2)
    DigitalAlarmSource [nativa]  ×3 (2)
  fDados [XFolder]  ×5 (1)
    fGrupoAnalogicas [XFolder]  ×37969 (25)
      fMedidaAnalogica [XFolder]  ×114032 (25)
        DigitalAlarmSource [nativa]  ×23623 (24)
        fMedidaAnalogica [XFolder] ↻  ×888 (4)
        DiscreteAlarmSource [nativa]  ×187 (4)
      oMedidaAnalogicaCalculada0se [XObject]  ×103 (22)
    fGrupoDigitais [XFolder]  ×8219 (25)
      fMedidaDigital [XFolder]  ×27541 (25)
        oMedidaDigitalBit [XObject]  ×46880 (23)
        DigitalAlarmSource [nativa]  ×25883 (25)
        fMedidaDigital [XFolder] ↻  ×23669 (23)
        oStatusTrackers [XObject]  ×4119 (18)
        DiscreteAlarmSource [nativa]  ×3504 (26)
      oMedidaDigitalCalculada [XObject]  ×359 (24)
      oMedidaDigitalBit [XObject]  ×170 (1)
      oMedidaDigitalCalculada0se [XObject]  ×116 (21)
    fGrupoComandos [XFolder]  ×876 (25)
      fComando [XFolder]  ×2119 (25)
        DigitalAlarmSource [nativa]  ×2218 (25)
        fComando [XFolder] ↻  ×200 (1)
    InternalTag [nativa]  ×166 (1)
      DiscreteAlarmSource [nativa]  ×6 (2)
      DigitalAlarmSource [nativa]  ×3 (2)
    oCalcSum [XObject]  ×115 (6)
    oCalcResumoInversores [XObject]  ×96 (25)
    fGrupoDigitais0se [XFolder]  ×69 (4)
      fMedidaDigital0se [XFolder]  ×485 (2)
        DigitalAlarmSource [nativa]  ×449 (2)
        DiscreteAlarmSource [nativa]  ×31 (1)
      fMedidaDigital [XFolder]  ×362 (5)
        oMedidaDigitalBit [XObject]  ×46880 (23)
        DigitalAlarmSource [nativa]  ×25883 (25)
        fMedidaDigital [XFolder] ↻  ×23669 (23)
        oStatusTrackers [XObject]  ×4119 (18)
        DiscreteAlarmSource [nativa]  ×3504 (26)
      oMedidaDigitalCalculada0se [XObject]  ×23 (5)
    fIED0se [XFolder]  ×41 (1)
      fDados [XFolder] ↻  ×42 (1)
      fDados0se [XFolder]  ×24 (4)
        oCalcSum [XObject]  ×128 (20)
        fGrupoDigitais0se [XFolder]  ×64 (5)
          fMedidaDigital0se [XFolder]  ×485 (2)
          fMedidaDigital [XFolder]  ×362 (5)
          oMedidaDigitalCalculada0se [XObject]  ×23 (5)
        fGrupoAnalogicas0se [XFolder]  ×53 (3)
          fMedidaAnalogica0se [XFolder]  ×377 (2)
          fMedidaAnalogica [XFolder]  ×40 (2)
        fGrupoComandos0se [XFolder]  ×46 (2)
          fComando0se [XFolder]  ×55 (1)
          fComando [XFolder]  ×6 (1)
        DigitalAlarmSource [nativa]  ×40 (20)
        InternalTag [nativa]  ×29 (2)
          DiscreteAlarmSource [nativa]  ×6 (2)
          DigitalAlarmSource [nativa]  ×3 (2)
        oMedidaAnalogicaCalculada0se [XObject]  ×22 (13)
        oMedidaAnalogicaCalculada [XObject]  ×20 (20)
        fDados0se [XFolder] ↻  ×14 (2)
      fChave0se [XFolder]  ×11 (1)
        fDados [XFolder] ↻  ×462 (24)
        DigitalAlarmSource [nativa]  ×33 (3)
        fDados0se [XFolder]  ×16 (1)
          oCalcSum [XObject]  ×128 (20)
          fGrupoDigitais0se [XFolder]  ×64 (5)
          fGrupoAnalogicas0se [XFolder]  ×53 (3)
          fGrupoComandos0se [XFolder]  ×46 (2)
          DigitalAlarmSource [nativa]  ×40 (20)
          InternalTag [nativa]  ×29 (2)
          oMedidaAnalogicaCalculada0se [XObject]  ×22 (13)
          oMedidaAnalogicaCalculada [XObject]  ×20 (20)
          fDados0se [XFolder] ↻  ×14 (2)
      fDisjuntor0se [XFolder]  ×9 (1)
        fDados [XFolder] ↻  ×472 (24)
        fGrupoAnalogicas [XFolder]  ×120 (1)
          fMedidaAnalogica [XFolder]  ×114032 (25)
          oMedidaAnalogicaCalculada0se [XObject]  ×103 (22)
        DigitalAlarmSource [nativa]  ×44 (7)
        fDados0se [XFolder]  ×24 (2)
          oCalcSum [XObject]  ×128 (20)
          fGrupoDigitais0se [XFolder]  ×64 (5)
          fGrupoAnalogicas0se [XFolder]  ×53 (3)
          fGrupoComandos0se [XFolder]  ×46 (2)
          DigitalAlarmSource [nativa]  ×40 (20)
          InternalTag [nativa]  ×29 (2)
          oMedidaAnalogicaCalculada0se [XObject]  ×22 (13)
          oMedidaAnalogicaCalculada [XObject]  ×20 (20)
          fDados0se [XFolder] ↻  ×14 (2)
        fIED0se [XFolder] ↻  ×2 (1)
        AnalogAlarmSource [nativa]  ×2 (1)
      fTransformador0se [XFolder]  ×2 (1)
        fDados [XFolder] ↻  ×56 (5)
        fDados0se [XFolder]  ×2 (1)
          oCalcSum [XObject]  ×128 (20)
          fGrupoDigitais0se [XFolder]  ×64 (5)
          fGrupoAnalogicas0se [XFolder]  ×53 (3)
          fGrupoComandos0se [XFolder]  ×46 (2)
          DigitalAlarmSource [nativa]  ×40 (20)
          InternalTag [nativa]  ×29 (2)
          oMedidaAnalogicaCalculada0se [XObject]  ×22 (13)
          oMedidaAnalogicaCalculada [XObject]  ×20 (20)
          fDados0se [XFolder] ↻  ×14 (2)
    fDados [XFolder] ↻  ×32 (6)
    oMedidaAnalogicaCalculada [XObject]  ×23 (5)
    fMedidaAnalogica [XFolder]  ×21 (1)
      DigitalAlarmSource [nativa]  ×23623 (24)
      fMedidaAnalogica [XFolder] ↻  ×888 (4)
      DiscreteAlarmSource [nativa]  ×187 (4)
    fDados0se [XFolder]  ×20 (20)
      oCalcSum [XObject]  ×128 (20)
      fGrupoDigitais0se [XFolder]  ×64 (5)
        fMedidaDigital0se [XFolder]  ×485 (2)
          DigitalAlarmSource [nativa]  ×449 (2)
          DiscreteAlarmSource [nativa]  ×31 (1)
        fMedidaDigital [XFolder]  ×362 (5)
          oMedidaDigitalBit [XObject]  ×46880 (23)
          DigitalAlarmSource [nativa]  ×25883 (25)
          fMedidaDigital [XFolder] ↻  ×23669 (23)
          oStatusTrackers [XObject]  ×4119 (18)
          DiscreteAlarmSource [nativa]  ×3504 (26)
        oMedidaDigitalCalculada0se [XObject]  ×23 (5)
      fGrupoAnalogicas0se [XFolder]  ×53 (3)
        fMedidaAnalogica0se [XFolder]  ×377 (2)
          fMedidaAnalogica0se [XFolder] ↻  ×2 (1)
        fMedidaAnalogica [XFolder]  ×40 (2)
          DigitalAlarmSource [nativa]  ×23623 (24)
          fMedidaAnalogica [XFolder] ↻  ×888 (4)
          DiscreteAlarmSource [nativa]  ×187 (4)
      fGrupoComandos0se [XFolder]  ×46 (2)
        fComando0se [XFolder]  ×55 (1)
        fComando [XFolder]  ×6 (1)
          DigitalAlarmSource [nativa]  ×2218 (25)
          fComando [XFolder] ↻  ×200 (1)
      DigitalAlarmSource [nativa]  ×40 (20)
      InternalTag [nativa]  ×29 (2)
        DiscreteAlarmSource [nativa]  ×6 (2)
        DigitalAlarmSource [nativa]  ×3 (2)
      oMedidaAnalogicaCalculada0se [XObject]  ×22 (13)
  … +62 linhas
```

### DBServer [nativa]

```
DBServer [nativa]  (raiz de nó: 3 nós)
```

### Hist [nativa]

```
Hist [nativa]  (raiz de nó: 3 nós)
  HistFieldsCollection [nativa]  ×3 (2)
    HistField [nativa]  ×98 (2)
```

### Frame [nativa]

```
Frame [nativa]  (raiz de nó: 3 nós)
  FrameSet [nativa]  ×3 (1)
    FrameSet [nativa] ↻  ×10 (1)
```

### UaDriver [nativa]

```
UaDriver [nativa]  (raiz de nó: 2 nós)
```

### AlarmServer [nativa]

```
AlarmServer [nativa]  (raiz de nó: 1 nós)
```

### Viewer [nativa]

```
Viewer [nativa]  (raiz de nó: 1 nós)
```

## 3. Matriz pai → filhos (completa)

Para cada classe-pai, as classes-filhas observadas, com quantidade e número de fontes. `<raiz do nó>` = objeto raiz do nó.

**<raiz do nó>**

| Filho | Qtd | Fontes |
|---|---:|---:|
| Screen [nativa] | 180 | 27 |
| XControl [nativa] | 127 | 3 |
| XFolder [nativa] | 68 | 3 |
| IODriver [nativa] | 57 | 29 |
| DataServer [nativa] | 53 | 27 |
| XObject [nativa] | 31 | 4 |
| DBServer [nativa] | 3 | 1 |
| Hist [nativa] | 3 | 2 |
| Frame [nativa] | 3 | 1 |
| UaDriver [nativa] | 2 | 1 |
| AlarmServer [nativa] | 1 | 1 |
| Viewer [nativa] | 1 | 1 |

**DataFolder [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| oConfigNavegacaoScreens [XObject] | 157 | 26 |
| InternalTag [nativa] | 89 | 25 |
| oDashConfigGauge [XObject] | 54 | 26 |
| oConfigHeader [XObject] | 25 | 25 |
| oDashConfigGauge0se [XObject] | 6 | 1 |
| DataFolder [nativa] | 5 | 1 |
| oCalcSum [XObject] | 4 | 1 |
| oConfigNavegacaoScreens0se [XObject] | 3 | 1 |
| oConfigHeader0se [XObject] | 2 | 2 |
| DemoTag [nativa] | 1 | 1 |
| oQueryPerformanceSQL [XObject] | 1 | 1 |
| temp [XObject] | 1 | 1 |

**DataServer [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DataFolder [nativa] | 83 | 27 |
| oDashConfigCardGeralUsinas [XObject] | 25 | 25 |
| fUsinaPV [XFolder] | 25 | 25 |
| fSubestacao0se [XFolder] | 1 | 1 |
| oDashConfigCardGeralUsinas0se [XObject] | 1 | 1 |
| InternalTag [nativa] | 1 | 1 |

**DBServer [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DigitalAlarmSource [nativa] | 1 | 1 |

**DrawGroup [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| cEquipArrayLayout [XControl] | 5668 | 21 |
| cObjElectricConnection0se [XControl] | 1456 | 19 |
| cEquipFiltro [XControl] | 678 | 21 |
| DrawGroup [nativa] | 607 | 23 |
| cObjMedidaAnalogicaPaineis0se [XControl] | 490 | 2 |
| cObjMedidaDigitalPaineis0se [XControl] | 490 | 2 |
| DrawString [nativa] | 400 | 23 |
| DrawLine [nativa] | 275 | 10 |
| cObjMedidaDigitalPaineis [XControl] | 267 | 1 |
| cTabularTRK [XControl] | 184 | 1 |
| cObjBotaoHighPerformance0se [XControl] | 134 | 2 |
| cObjMedidaAnalogicaPaineis [XControl] | 112 | 1 |
| DrawConnector [nativa] | 94 | 6 |
| DrawTank [nativa] | 93 | 12 |
| cObjCardFundo [XControl] | 91 | 5 |
| cObjBotaoHighPerformance [XControl] | 81 | 3 |
| cEquipNCU [XControl] | 68 | 5 |
| DrawCircle [nativa] | 54 | 18 |
| DrawRect [nativa] | 53 | 18 |
| cEquipIED0se [XControl] | 50 | 1 |
| cEquipChave0se [XControl] | 40 | 4 |
| cObjCardFundo0se [XControl] | 35 | 3 |
| cEquipInversor [XControl] | 34 | 3 |
| cEquipDisjuntor0se [XControl] | 33 | 2 |
| cEquipString [XControl] | 33 | 2 |
| cObjMedidaAnalogicaTela [XControl] | 33 | 1 |
| cTabularResumoUsinas [XControl] | 26 | 1 |
| DrawArc [nativa] | 23 | 4 |
| cEquipStringLayout [XControl] | 20 | 1 |
| cObjComConnection [XControl] | 16 | 1 |
| cObjSelect [XControl] | 10 | 1 |
| cPainelResumedMeteo [XControl] | 9 | 1 |
| CheckBox [nativa] | 9 | 2 |
| DrawBezier [nativa] | 7 | 2 |
| E3Alarm [nativa] | 6 | 2 |
| cIconeIED [XControl] | 6 | 1 |
| cNavegacaoScreensHeader0se [XControl] | 6 | 1 |
| cObjNotaOperativa [XControl] | 4 | 2 |
| cEquipTracker [XControl] | 4 | 1 |
| E3Browser [nativa] | 2 | 1 |
| ComboBox [nativa] | 2 | 2 |
| cObjGauge [XControl] | 2 | 1 |
| cDashGaugePaineis [XControl] | 2 | 1 |
| cLibGHI [XControl] | 2 | 1 |
| cObjAlarme [XControl] | 2 | 1 |
| DynamicMove [nativa] | 2 | 1 |
| cLibPOA [XControl] | 2 | 1 |
| cDashBarGraph0se [XControl] | 2 | 1 |
| cDashGaugePequeno0se [XControl] | 2 | 1 |
| cDashBarGraph [XControl] | 1 | 1 |
| cLibAlbedo [XControl] | 1 | 1 |
| DrawPicture [nativa] | 1 | 1 |

**DynamicMove [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DrawGroup [nativa] | 6 | 2 |
| DrawTank [nativa] | 2 | 1 |
| DrawCircle [nativa] | 1 | 1 |

**E3Browser [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| E3Query [nativa] | 3 | 2 |

**E3Chart [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| E3Query [nativa] | 2 | 1 |

**fCampoSolar [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDisjuntor0se [XFolder] | 300 | 1 |
| fInversor [XFolder] | 296 | 1 |
| fMPPT [XFolder] | 61 | 4 |
| fQGBT [XFolder] | 36 | 20 |
| fDados [XFolder] | 20 | 1 |
| fNCU [XFolder] | 13 | 11 |

**fChave0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 462 | 24 |
| DigitalAlarmSource [nativa] | 33 | 3 |
| fDados0se [XFolder] | 16 | 1 |

**fCircuito [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fChave0se [XFolder] | 2 | 1 |
| fCampoSolar [XFolder] | 2 | 1 |
| fTransformador0se [XFolder] | 1 | 1 |
| fDisjuntor0se [XFolder] | 1 | 1 |

**fCircuito0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fEletrocentro [XFolder] | 15 | 2 |
| fDisjuntor0se [XFolder] | 14 | 3 |
| fDados [XFolder] | 6 | 3 |
| fgrupoChaves [XFolder] | 5 | 2 |
| fTransformador0se [XFolder] | 3 | 3 |
| fRetificador0se [XFolder] | 2 | 1 |
| fEMET [XFolder] | 1 | 1 |
| fElectricPanel0se [XFolder] | 1 | 1 |
| fGerador [XFolder] | 1 | 1 |

**fCMB [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fInversor [XFolder] | 298 | 20 |
| fDados [XFolder] | 45 | 21 |
| DigitalAlarmSource [nativa] | 24 | 18 |

**fComando [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DigitalAlarmSource [nativa] | 2218 | 25 |
| fComando [XFolder] | 200 | 1 |

**fDados [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fGrupoAnalogicas [XFolder] | 37969 | 25 |
| fGrupoDigitais [XFolder] | 8219 | 25 |
| fGrupoComandos [XFolder] | 876 | 25 |
| InternalTag [nativa] | 166 | 1 |
| oCalcSum [XObject] | 115 | 6 |
| oCalcResumoInversores [XObject] | 96 | 25 |
| fGrupoDigitais0se [XFolder] | 69 | 4 |
| fIED0se [XFolder] | 41 | 1 |
| fDados [XFolder] | 32 | 6 |
| oMedidaAnalogicaCalculada [XObject] | 23 | 5 |
| fMedidaAnalogica [XFolder] | 21 | 1 |
| fDados0se [XFolder] | 20 | 20 |
| DigitalAlarmSource [nativa] | 18 | 5 |
| fCMB [XFolder] | 9 | 1 |
| oMedidaAnalogicaCalculada0se [XObject] | 2 | 1 |
| fMedidaDigital [XFolder] | 1 | 1 |

**fDados0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| oCalcSum [XObject] | 128 | 20 |
| fGrupoDigitais0se [XFolder] | 64 | 5 |
| fGrupoAnalogicas0se [XFolder] | 53 | 3 |
| fGrupoComandos0se [XFolder] | 46 | 2 |
| DigitalAlarmSource [nativa] | 40 | 20 |
| InternalTag [nativa] | 29 | 2 |
| oMedidaAnalogicaCalculada0se [XObject] | 22 | 13 |
| oMedidaAnalogicaCalculada [XObject] | 20 | 20 |
| fDados0se [XFolder] | 14 | 2 |

**fDisjuntor0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 472 | 24 |
| fGrupoAnalogicas [XFolder] | 120 | 1 |
| DigitalAlarmSource [nativa] | 44 | 7 |
| fDados0se [XFolder] | 24 | 2 |
| fIED0se [XFolder] | 2 | 1 |
| AnalogAlarmSource [nativa] | 2 | 1 |

**fElectricPanel0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fChave0se [XFolder] | 40 | 3 |
| fDisjuntor0se [XFolder] | 25 | 3 |
| fIED0se [XFolder] | 23 | 3 |
| fRetificador0se [XFolder] | 3 | 2 |
| fTransformador0se [XFolder] | 2 | 1 |
| fCircuito [XFolder] | 1 | 1 |
| fDados [XFolder] | 1 | 1 |
| fGerador [XFolder] | 1 | 1 |
| fCircuito0se [XFolder] | 1 | 1 |

**fEletrocentro [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fMultimedidor [XFolder] | 112 | 5 |
| fInversor [XFolder] | 61 | 4 |
| fTransformador0se [XFolder] | 51 | 5 |
| fDisjuntor0se [XFolder] | 47 | 3 |
| fDados [XFolder] | 41 | 5 |
| fNCU [XFolder] | 41 | 5 |
| fEMET [XFolder] | 36 | 5 |
| fCampoSolar [XFolder] | 20 | 1 |
| fgrupoChaves [XFolder] | 18 | 2 |

**fEMET [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 57 | 25 |
| DigitalAlarmSource [nativa] | 29 | 21 |

**fGerador [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados0se [XFolder] | 1 | 1 |
| fDados [XFolder] | 1 | 1 |

**fGrupoAnalogicas [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fMedidaAnalogica [XFolder] | 114032 | 25 |
| oMedidaAnalogicaCalculada0se [XObject] | 103 | 22 |

**fGrupoAnalogicas0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fMedidaAnalogica0se [XFolder] | 377 | 2 |
| fMedidaAnalogica [XFolder] | 40 | 2 |
| oMedidaAnalogicaCalculada0se [XObject] | 1 | 1 |

**fgrupoChaves [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fChave0se [XFolder] | 452 | 25 |

**fGrupoComandos [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fComando [XFolder] | 2119 | 25 |

**fGrupoComandos0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fComando0se [XFolder] | 55 | 1 |
| fComando [XFolder] | 6 | 1 |

**fGrupoDigitais [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fMedidaDigital [XFolder] | 27541 | 25 |
| oMedidaDigitalCalculada [XObject] | 359 | 24 |
| oMedidaDigitalBit [XObject] | 170 | 1 |
| oMedidaDigitalCalculada0se [XObject] | 116 | 21 |
| DigitalAlarmSource [nativa] | 1 | 1 |

**fGrupoDigitais0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fMedidaDigital0se [XFolder] | 485 | 2 |
| fMedidaDigital [XFolder] | 362 | 5 |
| oMedidaDigitalCalculada0se [XObject] | 23 | 5 |

**fGrupoStrings [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fString [XFolder] | 11922 | 21 |

**fGrupoTrackers [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fTracker [XFolder] | 5428 | 19 |

**fIED0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 42 | 1 |
| fDados0se [XFolder] | 24 | 4 |
| fChave0se [XFolder] | 11 | 1 |
| fDisjuntor0se [XFolder] | 9 | 1 |
| fTransformador0se [XFolder] | 2 | 1 |

**fInversor [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 655 | 25 |
| fGrupoStrings [XFolder] | 594 | 21 |
| fCampoSolar [XFolder] | 61 | 4 |
| fChave0se [XFolder] | 2 | 1 |
| fDisjuntor0se [XFolder] | 2 | 1 |

**fMedidaAnalogica [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DigitalAlarmSource [nativa] | 23623 | 24 |
| fMedidaAnalogica [XFolder] | 888 | 4 |
| DiscreteAlarmSource [nativa] | 187 | 4 |
| AnalogAlarmSource [nativa] | 1 | 1 |

**fMedidaAnalogica0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fMedidaAnalogica0se [XFolder] | 2 | 1 |
| TimerTag [nativa] | 1 | 1 |

**fMedidaDigital [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| oMedidaDigitalBit [XObject] | 46880 | 23 |
| DigitalAlarmSource [nativa] | 25883 | 25 |
| fMedidaDigital [XFolder] | 23669 | 23 |
| oStatusTrackers [XObject] | 4119 | 18 |
| DiscreteAlarmSource [nativa] | 3504 | 26 |

**fMedidaDigital0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DigitalAlarmSource [nativa] | 449 | 2 |
| DiscreteAlarmSource [nativa] | 31 | 1 |

**fMPPT [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fStringBox [XFolder] | 897 | 4 |

**fMultimedidor [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 155 | 23 |
| DigitalAlarmSource [nativa] | 24 | 16 |

**fNCU [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fGrupoTrackers [XFolder] | 58 | 19 |
| fDados [XFolder] | 58 | 19 |

**fObjScadaPowerControl [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 1 | 1 |

**fPPC [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fMultimedidor [XFolder] | 16 | 4 |
| fDados [XFolder] | 16 | 5 |

**fQGBT [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDisjuntor0se [XFolder] | 46 | 20 |
| fCMB [XFolder] | 36 | 20 |
| fgrupoChaves [XFolder] | 32 | 17 |
| fStringBox [XFolder] | 10 | 4 |

**Frame [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| FrameSet [nativa] | 3 | 1 |

**FrameSet [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| FrameSet [nativa] | 10 | 1 |

**fRetificador0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados0se [XFolder] | 5 | 3 |
| fDisjuntor0se [XFolder] | 4 | 1 |

**fString [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 30376 | 25 |

**fStringBox [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fString [XFolder] | 18454 | 4 |
| fDados [XFolder] | 897 | 4 |
| fArray [XFolder] | 387 | 4 |

**fSubestacao0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDisjuntor0se [XFolder] | 43 | 20 |
| fTransformador0se [XFolder] | 34 | 21 |
| fCampoSolar [XFolder] | 34 | 19 |
| fElectricPanel0se [XFolder] | 31 | 3 |
| fgrupoChaves [XFolder] | 29 | 12 |
| fMultimedidor [XFolder] | 23 | 15 |
| fEletrocentro [XFolder] | 16 | 2 |
| fCircuito0se [XFolder] | 7 | 3 |
| fDados [XFolder] | 5 | 2 |
| fSubestacao0se [XFolder] | 3 | 1 |
| fIED0se [XFolder] | 2 | 1 |
| fChave0se [XFolder] | 1 | 1 |
| DigitalAlarmSource [nativa] | 1 | 1 |

**fTracker [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fArray [XFolder] | 5428 | 19 |
| fDados [XFolder] | 5428 | 19 |

**fTransformador0se [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fDados [XFolder] | 56 | 5 |
| fDados0se [XFolder] | 2 | 1 |

**fUsinaPV [XFolder]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| fSubestacao0se [XFolder] | 41 | 24 |
| fDados [XFolder] | 25 | 25 |
| fEMET [XFolder] | 20 | 20 |
| fgrupoChaves [XFolder] | 16 | 16 |
| fEletrocentro [XFolder] | 10 | 1 |
| fPPC [XFolder] | 8 | 5 |
| fDisjuntor0se [XFolder] | 5 | 5 |
| fNCU [XFolder] | 4 | 3 |
| fMultimedidor [XFolder] | 4 | 4 |
| fUsinaPV [XFolder] | 3 | 1 |
| fTransformador0se [XFolder] | 3 | 3 |
| fCircuito [XFolder] | 2 | 1 |
| DigitalAlarmSource [nativa] | 1 | 1 |
| fObjScadaPowerControl [XFolder] | 1 | 1 |

**Hist [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| HistFieldsCollection [nativa] | 3 | 2 |
| HistPrimaryKey [nativa] | 1 | 1 |
| HistIndexesCollection [nativa] | 1 | 1 |

**HistFieldsCollection [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| HistField [nativa] | 98 | 2 |

**HistIndex [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| HistIndexField [nativa] | 5 | 1 |

**HistIndexesCollection [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| HistIndex [nativa] | 1 | 1 |

**InternalTag [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DiscreteAlarmSource [nativa] | 6 | 2 |
| DigitalAlarmSource [nativa] | 3 | 2 |

**IOBlock [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| IOBlockElement [nativa] | 344 | 2 |

**IODriver [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| IOFolder [nativa] | 266 | 29 |
| IOTag [nativa] | 100 | 16 |

**IOFolder [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| IOTag [nativa] | 140206 | 29 |
| IOFolder [nativa] | 20551 | 29 |
| IOBlock [nativa] | 86 | 2 |

**IOTag [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DiscreteAlarmSource [nativa] | 2 | 2 |

**Screen [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| cObjElectricConnection0se [XControl] | 1410 | 26 |
| cEquipInversor [XControl] | 622 | 23 |
| cEquipString [XControl] | 622 | 23 |
| cEquipDisjuntor0se [XControl] | 438 | 25 |
| cEquipChave0se [XControl] | 432 | 26 |
| DrawGroup [nativa] | 373 | 25 |
| DrawString [nativa] | 363 | 27 |
| cEquipArrayLayout [XControl] | 98 | 2 |
| cEquipTrafo0se [XControl] | 96 | 26 |
| cObjComConnection [XControl] | 90 | 2 |
| DrawLine [nativa] | 88 | 26 |
| cObjCardFundo [XControl] | 76 | 13 |
| cObjBotaoHighPerformance0se [XControl] | 56 | 7 |
| cEquipMultimedidor [XControl] | 56 | 22 |
| DrawTank [nativa] | 55 | 20 |
| cObjCardFundo0se [XControl] | 50 | 27 |
| cDetalhesUsina [XControl] | 41 | 25 |
| E3Alarm [nativa] | 40 | 26 |
| cPainelMedidasTela [XControl] | 40 | 20 |
| cEquipCMB [XControl] | 36 | 20 |
| DrawRect [nativa] | 35 | 14 |
| cObjAnalogScreen0se [XControl] | 31 | 3 |
| cObjBotaoHighPerformance [XControl] | 30 | 3 |
| E3Chart [nativa] | 28 | 1 |
| cObjHeader0se [XControl] | 27 | 27 |
| cObjTelaAlarmes [XControl] | 26 | 26 |
| cObjHist [XControl] | 26 | 26 |
| cDashCardGeralUsinas [XControl] | 25 | 1 |
| cIconeIED [XControl] | 25 | 2 |
| cEquipGerador0se [XControl] | 22 | 5 |
| cEquipPPC [XControl] | 22 | 5 |
| cPainelResumedMeteo [XControl] | 22 | 4 |
| cObjGround0se [XControl] | 22 | 2 |
| DrawConnector [nativa] | 20 | 3 |
| cEquipIED0se [XControl] | 20 | 2 |
| cEquipMeteorologica [XControl] | 20 | 20 |
| cEquipFiltro [XControl] | 20 | 2 |
| cEquipCUB0se [XControl] | 19 | 2 |
| cEquipNCU [XControl] | 17 | 14 |
| DrawCircle [nativa] | 13 | 9 |
| cDashGauge [XControl] | 8 | 4 |
| cIconeCFTV [XControl] | 7 | 1 |
| cIconeRTU [XControl] | 7 | 1 |
| cDashPizzaGraph [XControl] | 5 | 1 |
| cIconeConversorRede [XControl] | 5 | 1 |
| cIconeServidorSimples [XControl] | 5 | 2 |
| cIconeCloud [XControl] | 4 | 2 |
| cEquipRetificador0se [XControl] | 4 | 2 |
| cDashGauge0se [XControl] | 4 | 1 |
| cIconeSwitchRede [XControl] | 3 | 1 |
| DrawPicture [nativa] | 2 | 1 |
| TimerTag [nativa] | 2 | 2 |
| ListBox [nativa] | 2 | 1 |
| cEquipBateria0se [XControl] | 2 | 1 |
| cPainelDisjuntor0se [XControl] | 1 | 1 |
| cPainelChave0se [XControl] | 1 | 1 |
| cPainelInversor [XControl] | 1 | 1 |
| cPainelCMB [XControl] | 1 | 1 |
| cPainelStrings [XControl] | 1 | 1 |
| cPainelMultimedidor [XControl] | 1 | 1 |
| cPainelPPC [XControl] | 1 | 1 |
| cPainelTransformadores0se [XControl] | 1 | 1 |
| cPainelNCU [XControl] | 1 | 1 |
| cPainelTracker [XControl] | 1 | 1 |
| cPainelIED0se [XControl] | 1 | 1 |
| cPainelRetificador0se [XControl] | 1 | 1 |
| cPainelMeteorologica [XControl] | 1 | 1 |
| cPainelScadaPowerControl [XControl] | 1 | 1 |
| cDashCardBtc [XControl] | 1 | 1 |
| cDashCardGeral0se [XControl] | 1 | 1 |
| cPainelNotaOperativa [XControl] | 1 | 1 |
| cIconeRoteador [XControl] | 1 | 1 |
| CheckBox [nativa] | 1 | 1 |
| InternalTag [nativa] | 1 | 1 |
| cIconeComputador [XControl] | 1 | 1 |
| cIconeFirewall [XControl] | 1 | 1 |
| cDashBarGraph0se [XControl] | 1 | 1 |
| cEquipScadaPowerControl [XControl] | 1 | 1 |

**UaDriver [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| UaSubscription [nativa] | 1 | 1 |

**UaFolder [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| UaTag [nativa] | 48 | 1 |
| UaFolder [nativa] | 26 | 1 |

**UaSubscription [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| UaFolder [nativa] | 1 | 1 |

**UaTag [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DigitalAlarmSource [nativa] | 24 | 1 |
| DiscreteAlarmSource [nativa] | 24 | 1 |

**Viewer [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| FrameSet [nativa] | 1 | 1 |
| ViewerFolder [nativa] | 1 | 1 |

**ViewerFolder [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| InternalTag [nativa] | 8 | 1 |
| ViewerFolder [nativa] | 5 | 1 |
| E3Query [nativa] | 1 | 1 |
| DemoTag [nativa] | 1 | 1 |

**XControl [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| DrawString [nativa] | 135 | 3 |
| DrawGroup [nativa] | 112 | 3 |
| cObjCardFundo [XControl] | 46 | 2 |
| DrawLine [nativa] | 37 | 2 |
| cObjBotaoHighPerformance [XControl] | 32 | 2 |
| DrawConnector [nativa] | 28 | 2 |
| DrawArc [nativa] | 23 | 2 |
| cEquipStringPainel [XControl] | 22 | 1 |
| cObjCardFundo0se [XControl] | 18 | 2 |
| CheckBox [nativa] | 18 | 1 |
| DrawTank [nativa] | 17 | 2 |
| cObjNotaOperativa [XControl] | 13 | 2 |
| DrawCircle [nativa] | 12 | 2 |
| DynamicMove [nativa] | 7 | 2 |
| DrawRect [nativa] | 4 | 2 |
| cLibModuloPV [XControl] | 3 | 1 |
| cObjGauge [XControl] | 2 | 1 |
| cObjBarGraph [XControl] | 2 | 1 |
| cObjMedidaAnalogicaTela [XControl] | 2 | 1 |
| E3Browser [nativa] | 2 | 1 |
| cObjElectricConnection0se [XControl] | 2 | 1 |
| DrawPicture [nativa] | 2 | 1 |
| cObjMedidaDigitalPaineis [XControl] | 1 | 1 |
| cPainelStrings [XControl] | 1 | 1 |
| cEquipInversor [XControl] | 1 | 1 |
| cIconeSol [XControl] | 1 | 1 |
| cEquipTracker [XControl] | 1 | 1 |
| E3Chart [nativa] | 1 | 1 |
| ComboBox [nativa] | 1 | 1 |
| CommandButton [nativa] | 1 | 1 |
| cObjBotaoHighPerformance0se [XControl] | 1 | 1 |
| ListBox [nativa] | 1 | 1 |
| cEquipTrafo0se [XControl] | 1 | 1 |
| cEquipDisjuntor0se [XControl] | 1 | 1 |
| cObjLogoSCADA [XControl] | 1 | 1 |

**XObject [nativa]**

| Filho | Qtd | Fontes |
|---|---:|---:|
| InternalTag [nativa] | 70 | 3 |
| fDados [XFolder] | 5 | 1 |
| TimerTag [nativa] | 4 | 2 |
| fDados0se [XFolder] | 4 | 2 |
| DemoTag [nativa] | 1 | 1 |
| oCalcSum [XObject] | 1 | 1 |
| fMedidaDigital [XFolder] | 1 | 1 |

## 4. Componentes anexados a objetos

Componentes não são filhos na árvore: ficam **anexados** ao objeto dono (script de eventos, associação de propriedade, tabela de cores, animação).

| Dono | Componente | Qtd | Fontes |
|---|---|---:|---:|
| fMedidaAnalogica [XFolder] | AgSimple | 342932 | 25 |
| fMedidaDigital [XFolder] | AgSimple | 157878 | 26 |
| IOTag [nativa] | AgScript | 67755 | 16 |
| DigitalAlarmSource [nativa] | DigitalAlarm | 52416 | 29 |
| fMedidaDigital [XFolder] | TableBind | 51574 | 26 |
| oMedidaDigitalBit [XObject] | TableBind | 46790 | 22 |
| fMedidaAnalogica [XFolder] | AgScript | 46386 | 25 |
| fMedidaDigital [XFolder] | AgScript | 36413 | 25 |
| DigitalAlarmSource [nativa] | AgScript | 25809 | 29 |
| fDados [XFolder] | AgScript | 16258 | 26 |
| fGrupoAnalogicas [XFolder] | AgScript | 15549 | 25 |
| fString [XFolder] | AgScript | 12018 | 24 |
| IOFolder [nativa] | AgScript | 8604 | 16 |
| fComando [XFolder] | AgSimple | 6775 | 25 |
| fTracker [XFolder] | AgSimple | 6679 | 18 |
| fArray [XFolder] | AgSimple | 6256 | 23 |
| cEquipArrayLayout [XControl] | AgScript | 5766 | 23 |
| fGrupoDigitais [XFolder] | AgScript | 4025 | 25 |
| DiscreteAlarmSource [nativa] | DiscreteAlarm | 3754 | 30 |
| DiscreteAlarmSource [nativa] | AgScript | 3666 | 29 |
| cObjElectricConnection0se [XControl] | AgScript | 2868 | 27 |
| IOTag [nativa] | AgSimple | 2830 | 2 |
| fArray [XFolder] | AgScript | 2688 | 21 |
| fTracker [XFolder] | AgScript | 2318 | 17 |
| fComando [XFolder] | AgScript | 1921 | 25 |
| fInversor [XFolder] | AgSimple | 1905 | 25 |
| fMedidaDigital0se [XFolder] | AgSimple | 1455 | 2 |
| fMedidaAnalogica0se [XFolder] | AgSimple | 1135 | 2 |
| DrawGroup [nativa] | AgScript | 1080 | 28 |
| DigitalAlarmSource [nativa] | AgSimple | 969 | 26 |
| DrawString [nativa] | AgScript | 892 | 30 |
| fGrupoComandos [XFolder] | AgScript | 795 | 25 |
| cEquipFiltro [XControl] | AgScript | 698 | 23 |
| oMedidaDigitalBit [XObject] | AgScript | 693 | 3 |
| cEquipInversor [XControl] | AgScript | 657 | 26 |
| cEquipString [XControl] | AgScript | 655 | 25 |
| fInversor [XFolder] | AgScript | 631 | 25 |
| fGrupoStrings [XFolder] | AgScript | 594 | 21 |
| fChave0se [XFolder] | AgScript | 507 | 26 |
| fDisjuntor0se [XFolder] | AgScript | 493 | 25 |
| cObjMedidaAnalogicaPaineis0se [XControl] | AgScript | 490 | 2 |
| fMedidaDigital0se [XFolder] | AgScript | 485 | 2 |
| fMedidaDigital0se [XFolder] | TableBind | 485 | 2 |
| cEquipChave0se [XControl] | AgScript | 472 | 27 |
| cEquipDisjuntor0se [XControl] | AgScript | 465 | 26 |
| DrawLine [nativa] | AgScript | 398 | 30 |
| fMedidaAnalogica0se [XFolder] | AgScript | 379 | 2 |
| IOBlockElement [nativa] | AgScript | 344 | 2 |
| InternalTag [nativa] | AgScript | 279 | 10 |
| cObjMedidaDigitalPaineis0se [XControl] | AgScript | 270 | 2 |
| DrawString [nativa] | AgSimple | 227 | 4 |
| oCalcSum [XObject] | AgScript | 216 | 27 |
| cObjMedidaDigitalPaineis [XControl] | AgScript | 210 | 1 |
| InternalTag [nativa] | AgSimple | 206 | 27 |
| cObjCardFundo [XControl] | AgScript | 199 | 16 |
| oDashConfigCardGeralUsinas [XObject] | AgSimple | 194 | 25 |
| cObjBotaoHighPerformance0se [XControl] | AgScript | 185 | 9 |
| cTabularTRK [XControl] | AgScript | 184 | 1 |
| Screen [nativa] | AgScript | 180 | 27 |
| InternalTag [nativa] | TableBind | 175 | 3 |
| DrawTank [nativa] | AgScript | 167 | 25 |
| fComando0se [XFolder] | AgSimple | 165 | 1 |
| cObjBotaoHighPerformance0se [XControl] | AnimationBind | 155 | 9 |
| cObjBotaoHighPerformance [XControl] | AgScript | 143 | 5 |
| oMedidaDigitalCalculada0se [XObject] | AgScript | 139 | 24 |
| DrawConnector [nativa] | AgScript | 134 | 8 |
| fGrupoDigitais0se [XFolder] | AgScript | 129 | 6 |
| oMedidaAnalogicaCalculada0se [XObject] | AgScript | 127 | 24 |
| XControl [nativa] | XCoClass | 127 | 3 |
| XControl [nativa] | AgScript | 127 | 3 |
| fMultimedidor [XFolder] | AgScript | 122 | 23 |
| cObjMedidaAnalogicaPaineis [XControl] | AgScript | 112 | 1 |
| fDados0se [XFolder] | AgScript | 106 | 26 |
| fgrupoChaves [XFolder] | AgScript | 100 | 25 |
| HistField [nativa] | AgScript | 98 | 2 |
| cObjCardFundo0se [XControl] | AgScript | 98 | 29 |
| cEquipTrafo0se [XControl] | AgScript | 97 | 27 |
| DrawRect [nativa] | AgScript | 92 | 27 |
| fTransformador0se [XFolder] | AgScript | 89 | 26 |
| IOBlock [nativa] | AgScript | 86 | 2 |
| cEquipNCU [XControl] | AgScript | 85 | 19 |
| oDashConfigGauge [XObject] | AgSimple | 80 | 26 |
| fUsinaPV [XFolder] | AgSimple | 77 | 25 |
| DrawCircle [nativa] | AgScript | 76 | 27 |
| DataFolder [nativa] | AgScript | 73 | 27 |
| cObjBotaoHighPerformance0se [XControl] | AgSimple | 73 | 2 |
| fCampoSolar [XFolder] | AgScript | 72 | 25 |
| cEquipIED0se [XControl] | AgScript | 70 | 2 |
| DrawLine [nativa] | AnimationBind | 68 | 5 |
| fIED0se [XFolder] | AgScript | 68 | 4 |
| cObjNotaOperativa [XControl] | AgSimple | 68 | 2 |
| XFolder [nativa] | XCoClass | 68 | 3 |
| XFolder [nativa] | AgScript | 68 | 3 |
| DrawGroup [nativa] | TableBind | 64 | 2 |
| fMultimedidor [XFolder] | AgSimple | 63 | 23 |
| IODriver [nativa] | AgScript | 57 | 29 |
| fNCU [XFolder] | AgScript | 57 | 19 |
| cObjComConnection [XControl] | AgScript | 57 | 1 |
| cEquipMultimedidor [XControl] | AgScript | 56 | 22 |
| fComando0se [XFolder] | AgScript | 55 | 1 |
| DataServer [nativa] | AgScript | 53 | 27 |
| DrawTank [nativa] | AgSimple | 53 | 3 |
| fEMET [XFolder] | AgScript | 51 | 25 |
| DrawString [nativa] | AnimationBind | 50 | 5 |
| cObjBotaoHighPerformance [XControl] | AnimationBind | 50 | 2 |
| fGrupoAnalogicas0se [XFolder] | AgScript | 49 | 2 |
| UaTag [nativa] | AgScript | 48 | 1 |
| oStatusTrackers [XObject] | AgScript | 48 | 1 |
| DrawGroup [nativa] | AgSimple | 48 | 3 |
| E3Alarm [nativa] | AgSimple | 47 | 26 |
| E3Alarm [nativa] | AgScript | 46 | 27 |
| fStringBox [XFolder] | AgScript | 46 | 8 |
| DrawArc [nativa] | AgScript | 46 | 4 |
| fSubestacao0se [XFolder] | AgScript | 45 | 25 |
| fCMB [XFolder] | AgScript | 45 | 21 |
| fGrupoComandos0se [XFolder] | AgScript | 42 | 1 |
| fEletrocentro [XFolder] | AgScript | 41 | 5 |
| oConfigNavegacaoScreens [XObject] | AgScript | 40 | 24 |
| oDashConfigGauge [XObject] | AgScript | 40 | 26 |
| cDetalhesUsina [XControl] | AgScript | 40 | 25 |

## 5. Árvore real do projeto modelo (`ufv_gsii`, GC)

Ao contrário das seções 2–3 (união de todas as variantes), aqui está **uma árvore concreta**: nós do projeto e, em cada nó, os objetos agrupados por classe (`×n`; filhos mostrados para o 1º exemplar de cada grupo).

```
Usinas
  UFV_GSII
    Communication
      IEC104M_PV  [Driver de Comunicação · IODriver · 49144 objetos]
      IEC104M_SE  [Driver de Comunicação · IODriver · 1255 objetos]
    Settings  [Servidor de Dados · DataServer · 31 objetos]
    Screens
      Header  [Tela · Screen · 4 objetos]
      GS01_TS01  [Tela · Screen · 496 objetos]
      TelaRede  [Tela · Screen · 188 objetos]
      SE  [Tela · Screen · 162 objetos]
      GS01_TS02  [Tela · Screen · 493 objetos]
      GS01_TS03  [Tela · Screen · 496 objetos]
      GS02_TS01  [Tela · Screen · 496 objetos]
      GS02_TS02  [Tela · Screen · 493 objetos]
      GS02_TS03  [Tela · Screen · 496 objetos]
      GS03_TS01  [Tela · Screen · 503 objetos]
      GS03_TS02  [Tela · Screen · 502 objetos]
      GS03_TS03  [Tela · Screen · 505 objetos]
      GS03_TS04  [Tela · Screen · 456 objetos]
      PSA  [Tela · Screen · 78 objetos]
      Meteo  [Tela · Screen · 44 objetos]
      Alarms  [Tela · Screen · 4 objetos]
      Hist  [Tela · Screen · 4 objetos]
      Layout
        LayoutGeral  [Tela · Screen · 3549 objetos]
        NovaPasta
    BD  [Servidor de Dados · DataServer · 436805 objetos]
```

**`Usinas/UFV_GSII/Communication/IEC104M_PV`**

```
IODriver ×1 (IEC104M_PV)
  IOTag ×3 (IO.PhysicalLayerStatus, Ativo, C_IC_NA_1)
  IOFolder ×1 (GSII)
    IOFolder ×5 (UFV01, UFV02, UFV03, …)
      IOFolder ×3 (ELC01, ELC02, ELC03)
        IOFolder ×4 (Dados, EMET01-01, NCU01-01, …)
          IOFolder ×5 (Digital, Analog, Command, …)
```

**`Usinas/UFV_GSII/Communication/IEC104M_SE`**

```
IODriver ×1 (IEC104M_SE)
  IOTag ×3 (IO.PhysicalLayerStatus, Ativo, C_IC_NA_1)
  IOFolder ×1 (GSII)
    IOFolder ×14 (UAD, 1K4, 1H4, …)
      IOFolder ×1 (Dados)
        IOFolder ×3 (Digital, Analog, Command)
          IOTag ×127 (GSII_SE_UAD_L1TP-MCB1X, GSII_SE_UAD_INCENDIO-ALM, GSII_SE_UAD_INCENDIO-DEF, …)
```

**`Usinas/UFV_GSII/Settings`**

```
DataServer ×1 (Settings)
  DataFolder ×2 (Dashboards, Navigation)
    oDashConfigGauge ×2 (PotenciaAtivaTotal, Energia)
  oDashConfigCardGeralUsinas ×1 (cardGSII)
```

**`Usinas/UFV_GSII/Screens/Header`**

```
Screen ×1 (Header)
  cObjHeader0se ×1 (cObjHeader0se1)
```

**`Usinas/UFV_GSII/Screens/GS01_TS01`**

```
Screen ×1 (GS01_TS01)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×8 (Grupo8, Grupo1, Grupo3, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×3 (cObjBotaoHighPerformance0se7, cObjBotaoHighPerformance0se6, cObjBotaoHighPerformance0se3)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×33 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipInversor ×30 (equipInversor28, equipInversor27, equipInversor26, …)
  E3Alarm ×1 (Alarmes_GSII)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/TelaRede`**

```
Screen ×1 (TelaRede)
  DrawString ×39 (Texto34, Texto41, Texto40, …)
  cIconeCFTV ×7 (cIconeCFTV7, cIconeCFTV6, cIconeCFTV5, …)
  cIconeIED ×17 (cIconeIED4, cIconeIED3, cIconeIED7, …)
  cObjComConnection ×49 (cObjComConnection30, cObjComConnection29, cObjComConnection28, …)
  cIconeSwitchRede ×3 (cIconeSwitchRede2, cIconeSwitchRede3, cIconeSwitchRede1)
  cIconeConversorRede ×5 (cIconeConversorRede4, cIconeConversorRede3, cIconeConversorRede5, …)
  cIconeRTU ×7 (cIconeRTU5, cIconeRTU7, cIconeRTU6, …)
  cIconeServidorSimples ×1 (cIconeServidorSimples1)
  cIconeRoteador ×1 (cIconeRoteador1)
  cIconeCloud ×3 (cIconeCloud2, cIconeCloud1, cIconeCloud3)
  cObjCardFundo ×14 (Fundo2, Fundo3, Fundo14, …)
```

**`Usinas/UFV_GSII/Screens/SE`**

```
Screen ×1 (SE)
  cEquipIED0se ×8 (cEquipIED0se8, cEquipIED0se5, cEquipIED0se6, …)
  cObjBotaoHighPerformance0se ×9 (cObjBotaoHighPerformance0se10, cObjBotaoHighPerformance0se9, cObjBotaoHighPerformance0se8, …)
  cEquipPPC ×4 (cEquipPPC4, cEquipPPC3, cEquipPPC2, …)
  E3Alarm ×1 (Alarmes_GSII)
  DrawString ×8 (Text7, Text8, Text5, …)
  cEquipCUB0se ×8 (CUB08, CUB07, CUB06, …)
  cEquipGerador0se ×6 (cEquipGerador0se6, cEquipGerador0se5, cEquipGerador0se4, …)
  cObjElectricConnection0se ×23 (cObjElectricConnection0se21, cObjElectricConnection0se22, cObjElectricConnection0se23, …)
  cEquipTrafo0se ×1 (cEquipTrafo0se1)
  cEquipDisjuntor0se ×1 (cEquipDisjuntor0se1)
  cEquipChave0se ×2 (cEquipChave0se2, cEquipChave0se1)
  cObjGround0se ×1 (cObjGround0se1)
  DrawLine ×1 (Line1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS01_TS02`**

```
Screen ×1 (GS01_TS02)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×8 (Grupo8, Grupo1, Grupo3, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×2 (cObjBotaoHighPerformance0se6, cObjBotaoHighPerformance0se3)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×33 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipInversor ×30 (equipInversor28, equipInversor27, equipInversor26, …)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS01_TS03`**

```
Screen ×1 (GS01_TS03)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×8 (Grupo8, Grupo1, Grupo3, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×3 (cObjBotaoHighPerformance0se6, cObjBotaoHighPerformance0se4, cObjBotaoHighPerformance0se3)
  cEquipInversor ×30 (equipInversor7, equipInversor15, equipInversor30, …)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×33 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS02_TS01`**

```
Screen ×1 (GS02_TS01)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×8 (Grupo8, Grupo1, Grupo3, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipInversor ×30 (equipInversor28, equipInversor27, equipInversor26, …)
  cObjBotaoHighPerformance0se ×3 (cObjBotaoHighPerformance0se7, cObjBotaoHighPerformance0se6, cObjBotaoHighPerformance0se3)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×33 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS02_TS02`**

```
Screen ×1 (GS02_TS02)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×8 (Grupo8, Grupo1, Grupo3, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×2 (cObjBotaoHighPerformance0se6, cObjBotaoHighPerformance0se3)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×33 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipInversor ×30 (equipInversor28, equipInversor27, equipInversor26, …)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS02_TS03`**

```
Screen ×1 (GS02_TS03)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×8 (Grupo8, Grupo1, Grupo3, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cEquipDisjuntor0se ×33 (equipDisjuntor54, equipDisjuntor52, equipDisjuntor51, …)
  cObjBotaoHighPerformance0se ×3 (cObjBotaoHighPerformance0se6, cObjBotaoHighPerformance0se4, cObjBotaoHighPerformance0se3)
  cEquipInversor ×30 (equipInversor7, equipInversor15, equipInversor30, …)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS03_TS01`**

```
Screen ×1 (GS03_TS01)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×8 (Grupo8, Grupo1, Grupo3, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×4 (cObjBotaoHighPerformance0se8, cObjBotaoHighPerformance0se7, cObjBotaoHighPerformance0se6, …)
  DrawLine ×2 (Line1, Line3)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  cEquipDisjuntor0se ×33 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipInversor ×30 (equipInversor28, equipInversor27, equipInversor26, …)
  DrawTank ×2 (CardAlarmes, CardUnifilar)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS03_TS02`**

```
Screen ×1 (GS03_TS02)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×9 (Grupo9, Grupo8, Grupo1, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×3 (cObjBotaoHighPerformance0se8, cObjBotaoHighPerformance0se7, cObjBotaoHighPerformance0se3)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×18 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  cEquipInversor ×30 (equipInversor28, equipInversor27, equipInversor26, …)
  DrawTank ×2 (CardAlarmes, CardUnifilar)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS03_TS03`**

```
Screen ×1 (GS03_TS03)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×21 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×9 (Grupo9, Grupo8, Grupo1, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×4 (cObjBotaoHighPerformance0se8, cObjBotaoHighPerformance0se7, cObjBotaoHighPerformance0se6, …)
  cEquipInversor ×30 (equipInversor7, equipInversor15, equipInversor30, …)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×18 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×30 (equipString29, equipString27, equipString26, …)
  DrawTank ×2 (CardAlarmes, CardUnifilar)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/GS03_TS04`**

```
Screen ×1 (GS03_TS04)
  cObjBotaoHighPerformance ×2 (cObjBotaoHighPerformance2, cObjBotaoHighPerformance1)
  E3Alarm ×1 (Alarmes_GSII)
  cObjGround0se ×2 (cObjGround0se2, cObjGround0se1)
  cEquipChave0se ×4 (equipChave46, equipChave45, equipChave43, …)
  cObjElectricConnection0se ×73 (cObjElectricConnection0se17, cObjElectricConnection0se18, cObjElectricConnection0se16, …)
  DrawGroup ×4 (Grupo8, Grupo1, Grupo4, …)
    cEquipIED0se ×5 (cEquipIED9, cEquipIED8, cEquipIED7, …)
  cObjBotaoHighPerformance0se ×3 (cObjBotaoHighPerformance0se8, cObjBotaoHighPerformance0se7, cObjBotaoHighPerformance0se3)
  DrawString ×5 (Text6, Text5, Text4, …)
  cEquipTrafo0se ×2 (trafo2sec03, trafo2sec02)
  DrawLine ×2 (Line3, Line1)
  cEquipDisjuntor0se ×33 (equipDisjuntor17, equipDisjuntor36, equipDisjuntor37, …)
  cEquipString ×26 (equipString29, equipString27, equipString26, …)
  cEquipInversor ×26 (equipInversor28, equipInversor27, equipInversor26, …)
  cEquipMultimedidor ×2 (equipMultimedidor4, equipMultimedidor3)
  cEquipPPC ×1 (equipPPC1)
  cDetalhesUsina ×1 (DetalhesUsina1)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/PSA`**

```
Screen ×1 (PSA)
  DrawGroup ×3 (Grupo3, Grupo2, Grupo1)
    cObjElectricConnection0se ×1 (cObjElectricConnection0se19)
    DrawString ×1 (Text7)
    DrawLine ×1 (Line1)
  cEquipDisjuntor0se ×5 (cEquipDisjuntor0se10, cEquipDisjuntor0se7, cEquipDisjuntor0se8, …)
  DrawString ×4 (Text9, Text6, Text5, …)
  cEquipTrafo0se ×1 (cEquipTrafo0se1)
  cObjElectricConnection0se ×12 (cObjElectricConnection0se20, cObjElectricConnection0se18, cObjElectricConnection0se5, …)
  DrawLine ×1 (Line3)
  cEquipRetificador0se ×2 (cEquipRetificador0se2, cEquipRetificador0se1)
  cEquipGerador0se ×1 (cEquipGerador0se1)
  cObjCardFundo0se ×2 (cObjCardFundo0se2, cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/Screens/Meteo`**

```
Screen ×1 (Meteo)
  DrawGroup ×3 (UFV03, UFV02, UFV01)
    cPainelResumedMeteo ×3 (painelResumedMeteo05, painelResumedMeteo04, painelResumedMeteo01)
    DrawString ×1 (Text1)
    cObjCardFundo ×2 (cObjCardFundo2, cObjCardFundo1)
```

**`Usinas/UFV_GSII/Screens/Alarms`**

```
Screen ×1 (Alarms)
  cObjTelaAlarmes ×1 (cObjTelaAlarmes1)
```

**`Usinas/UFV_GSII/Screens/Hist`**

```
Screen ×1 (Hist)
  cObjHist ×1 (cObjHist1)
```

**`Usinas/UFV_GSII/Screens/Layout/LayoutGeral`**

```
Screen ×1 (LayoutGeral)
  DrawGroup ×22 (NavegacaoGSII, CS5.1, Grupo5, …)
    DrawLine ×20 (CS10.2, CS9.2, CS7.2, …)
    DrawString ×1 (nameCS)
  CheckBox ×1 (habilitaRolagem)
  InternalTag ×1 (valorRolagem)
  TimerTag ×1 (timerRolagem)
  cObjCardFundo0se ×1 (cObjCardFundo0se1)
```

**`Usinas/UFV_GSII/BD`**

```
DataServer ×1 (BD)
  fUsinaPV ×1 (UFV_GSII)
    fSubestacao0se ×1 (SE)
      fTransformador0se ×1 (T1)
        fDados ×1 (Dados)
          fGrupoDigitais ×1 (Digital)
          fGrupoAnalogicas ×1 (Analog)
          fGrupoComandos ×1 (Command)
      fIED0se ×2 (3KTP-MF, UAD)
        fDados0se ×1 (Dados)
          fGrupoAnalogicas0se ×1 (Analog)
      fElectricPanel0se ×9 (1K, 1H, 2H, …)
        fChave0se ×2 (1K5, 1K5T)
          fDados ×1 (Dados)
        fDisjuntor0se ×1 (1K4)
          fDados ×1 (Dados)
        fIED0se ×2 (L187LP, L187LS)
          fDados0se ×1 (Dados)
    fUsinaPV ×3 (UFV01, UFV02, UFV03)
      fEletrocentro ×3 (ELC01, ELC02, ELC03)
        fCampoSolar ×2 (CBTA, CBTB)
          fInversor ×15 (INV01-15, INV01-16, INV01-17, …)
          fDisjuntor0se ×15 (DJ-CBTA-QA1, DJ-CBTA-QA2, DJ-CBTA-QA3, …)
          fDados ×1 (Dados)
        fMultimedidor ×2 (MMD01-01, MMD01-02)
          fDados ×1 (Dados)
        fEMET ×1 (EMET01-01)
          fDados ×1 (Dados)
          DigitalAlarmSource ×1 (FalhaCom)
        fDisjuntor0se ×3 (DJ-52, DJ-52-A, DJ-52-B)
          fDados ×1 (Dados)
          DigitalAlarmSource ×1 (FalhaCom)
        fTransformador0se ×2 (TRE-1, TS0A1)
          fDados ×1 (Dados)
        fNCU ×1 (NCU01-01)
          fDados ×1 (Dados)
          fGrupoTrackers ×1 (Trackers)
        fDados ×1 (Dados)
          fIED0se ×5 (LV-ROOM, MV-ROOM, LV-A, …)
          oCalcSum ×4 (SOMA-INVERSORES-AWAY, SOMA-INVERSORES-OPERATING, SOMA-INVERSORES-STANDBY, …)
        fgrupoChaves ×1 (SECCIONADORAS)
          fChave0se ×4 (89-2, 89-3, 57-2, …)
      fPPC ×1 (PPC01)
        fDados ×1 (Dados)
          fGrupoDigitais ×1 (Digital)
          fGrupoAnalogicas ×1 (Analog)
          fGrupoComandos ×1 (Command)
    fPPC ×1 (PPC01)
      fDados ×1 (Dados)
        fGrupoDigitais ×1 (Digital)
          fMedidaDigital ×13 (COM, CLP-ATIVO, NIVEL-CTRL, …)
        fGrupoAnalogicas ×1 (Analog)
          fMedidaAnalogica ×21 (POTENCIA-ATIVA, POTENCIA-REATIVA, TENSAO-MEDIA, …)
        fGrupoComandos ×1 (Command)
          fComando ×18 (NIVEL-CTRL, ACION-COMPLEXO, CTRL-POT-ATIVA, …)
    fDados ×1 (Dados)
      fDados ×2 (Alarms, Calcs)
        DigitalAlarmSource ×2 (FalhaComGTW_PV, FalhaComGTW_SE)
```
