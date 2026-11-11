# E3 Pattern — itens nativos do Elipse E3 e suas propriedades

Catálogo de **propriedades existentes** por classe (esquema, **sem valores**). Fontes: type libraries do E3 instalado (`C:\Program Files\Elipse Software\Elipse E3\Bin`), nomes gravados nos `.prj` (Main, GC, SE, GD) e decodificação do bloco binário de geometria. Total: **178 classes**, **2779 propriedades**.

Colunas — **Acesso:** `R` leitura, `W` escrita · **Origem:** `type lib` (type library), `base gráfica` (propriedades comuns a todo objeto de tela, ausentes da type lib), `cabeçalho`/`framework` (propriedades comuns a todo objeto E3 gravadas no `.prj`), `gravada no .prj` (nome do arquivo sem equivalente na type lib) · **Nome no .prj:** nome com que a propriedade é gravada (`apelido inferido` = pareamento automático por similaridade de nome, a confirmar) · **Persistência:** `nomeada` (gravada com nome no `.prj`), `binária` (gravada em bloco binário), `não gravada nomeada` (existe na type lib, mas não aparece nomeada no arquivo: runtime, binária ou sempre padrão).

## Geometria dos objetos de tela (X, Y, Width, Height, Angle)

Todo objeto gráfico (`Draw*`, `Screen`, XControls, ActiveX, `E3Chart`…) grava, logo após o cabeçalho de propriedades nomeadas (146 bytes: `Tip`, `Angle`, `Layer`, `Visible`, `Enabled`, `TabStop`), 1 byte de tag e **4 doubles (little-endian) = retângulo `x1, y1, x2, y2`**. Daí: `X = x1`, `Y = y1`, `Width = x2 − x1`, `Height = y2 − y1`. `Angle` é a propriedade nomeada `Angle` (ULong, graus).

Evidência: em 101 dos 164 `DrawGroup` das libs XControl o retângulo é exatamente a união dos filhos; em todos os objetos de tela dos projetos o retângulo é válido (x2 ≥ x1, y2 ≥ y1). Coerente com `Screen`: `(0, 0, 50800, 25876,25)` = largura × altura da tela. Unidade = unidade interna do E3.

> **Propriedades de framework** (não constam na type lib, comuns a todos os objetos): `Name`, `DocString`, `Expose`, `Inherit#`, `_EventCount`, `_Event#.*` (eventos/scripts), `_LayerCount`/`_Layer#.*`.

## Índice

| Biblioteca | Arquivo | Classes | Enums |
|---|---|---:|---:|
| [Panel](#panel) | Panel.e3 | 70 | 62 |
| [DB](#db) | DB.e3 | 24 | 14 |
| [IODrv](#iodrv) | IODrv.e3 | 17 | 14 |
| [E3Alarm](#e3alarm) | E3Alarm.dll | 2 | 8 |
| [E3Chart](#e3chart) | E3Chart.dll | 1 | 19 |
| [E3Browser](#e3browser) | E3Browse.dll | 1 | 6 |
| [E3Sys](#e3sys) | E3Sys.dll | 63 | 25 |

---

## Panel

Arquivo `Panel.e3` · versão 1.1 · LIBID `{CBEB1BC0-2391-11D4-8E8A-525400E657A3}` · E3 Panel Library 1.1

Classes: [AgScript](#panel-agscript), [CounterTag](#panel-countertag), [DataFolder](#panel-datafolder), [DataServer](#panel-dataserver), [DemoTag](#panel-demotag), [DrawArc](#panel-drawarc), [DrawBezier](#panel-drawbezier), [DrawCircle](#panel-drawcircle), [DrawConnector](#panel-drawconnector), [DrawConnectorPoint](#panel-drawconnectorpoint), [DrawConnectorPoints](#panel-drawconnectorpoints), [DrawGroup](#panel-drawgroup), [DrawLine](#panel-drawline), [DrawLinePoint](#panel-drawlinepoint), [DrawLinePoints](#panel-drawlinepoints), [DrawPicture](#panel-drawpicture), [DrawRect](#panel-drawrect), [DrawScale](#panel-drawscale), [DrawString](#panel-drawstring), [DrawTank](#panel-drawtank), [DynamicMove](#panel-dynamicmove), [DynamicRotate](#panel-dynamicrotate), [E3SectionReport](#panel-e3sectionreport), [Frame](#panel-frame), [FrameSet](#panel-frameset), [InternalTag](#panel-internaltag), [PickDoModal](#panel-pickdomodal), [PickLaunchApp](#panel-picklaunchapp), [PickOpenScreen](#panel-pickopenscreen), [PickPrintReport](#panel-pickprintreport), [PickSetValue](#panel-picksetvalue), [PickToggleValue](#panel-picktogglevalue), [PowerExplorerObject](#panel-powerexplorerobject), [Report](#panel-report), [Screen](#panel-screen), [SectionDetail](#panel-sectiondetail), [SectionGroupFooter](#panel-sectiongroupfooter), [SectionGroupHeader](#panel-sectiongroupheader), [SectionPageFooter](#panel-sectionpagefooter), [SectionPageHeader](#panel-sectionpageheader), [SectionReport](#panel-sectionreport), [SectionReportBarcode](#panel-sectionreportbarcode), [SectionReportCheckbox](#panel-sectionreportcheckbox), [SectionReportControlBase](#panel-sectionreportcontrolbase), [SectionReportExportFilter](#panel-sectionreportexportfilter), [SectionReportExportFilterExcel](#panel-sectionreportexportfilterexcel), [SectionReportExportFilterHTML](#panel-sectionreportexportfilterhtml), [SectionReportExportFilterPDF](#panel-sectionreportexportfilterpdf), [SectionReportExportFilterText](#panel-sectionreportexportfiltertext), [SectionReportExportFilterWord](#panel-sectionreportexportfilterword), [SectionReportField](#panel-sectionreportfield), [SectionReportFooter](#panel-sectionreportfooter), [SectionReportHeader](#panel-sectionreportheader), [SectionReportLine](#panel-sectionreportline), [SectionReportPagebreak](#panel-sectionreportpagebreak), [SectionReportPicture](#panel-sectionreportpicture), [SectionReportSectionBase](#panel-sectionreportsectionbase), [SectionReportShape](#panel-sectionreportshape), [SectionReportText](#panel-sectionreporttext), [TimerTag](#panel-timertag), [TrendAnalysisObject](#panel-trendanalysisobject), [Viewer](#panel-viewer), [ViewerFolder](#panel-viewerfolder), [WaterExplorerObject](#panel-waterexplorerobject), [XCoClass](#panel-xcoclass), [XControl](#panel-xcontrol), [XFolder](#panel-xfolder), [XInterface](#panel-xinterface), [XMethod](#panel-xmethod), [XObject](#panel-xobject)

<a id="panel-agscript"></a>
### AgScript

- CLSID `{1CC935C2-4C20-2233-8E8A-525400E657A3}` · interface `IAgScript`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 269045 instâncias em 39 arquivo(s)
- Script Aggregate Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `_EventCount` | ULong | RW | framework | _EventCount | nomeada | — | Quantidade de eventos com script |
| `_Event#.*` | vários | RW | framework | _Event#.* | nomeada | — | Evento com script: Name, EventType, PickCount, Pick#Id/Data/Code, Link… (família) |

<a id="panel-countertag"></a>
### CounterTag

- CLSID `{77040846-D1CE-4DC0-A9C8-9D2F157FEFFC}` · interface `ICounterTag` · eventos `DCounterTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- CounterTag

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Enabled` | Boolean | RW | type lib | — | — | — | Starts or stops the counter. If True, the counting is started, otherwise it is stopped. |
| `CounterType` | CounterTypeFlags | RW | type lib | — | — | — | Defines the counter's behavior. Possible values for this property are 0 - Preset: The counting is stopped when the value set in the Preset property is reached (default) or 1 - Infinite: The counting goes on indefinitely |
| `AutoRestart` | Boolean | RW | type lib | — | — | — | Indicates that the counting must restart from zero after it reaches the value established in the Preset property. This property is only valid when the CounterType property is set to 0 - Preset. |
| `Preset` | Long | RW | type lib | — | — | — | Limit to be reached by the counter, in seconds. In case the value of this property is not a multiple of the value of the Increment property, the Tag reaches this value before the next increment. |
| `ResetCounterWhenEnabled` | Boolean | RW | type lib | — | — | — | Enables restarting the counting (from zero) each time the value of the Enabled property returns to True. When disabled, the counter restarts counting from the point it was previously interrupted. |
| `Increment` | Long | RW | type lib | — | — | — | Defines the update interval of the Value property. In case the value of this property is modified while the counting is on, this modification is only effective when the counter is stopped and restarted. |
| `Value` | Long | R | type lib | — | — | — | Displays the counting of the counter, in seconds. This is a read-only property. This property gets values multiples of the value of the Increment property, except when the Enabled property is set to False. In this case, the value is the one when the Tag was disabled. When restarting the counting, th… |

**Eventos:** `OnPreset()`

<a id="panel-datafolder"></a>
### DataFolder

- CLSID `{803F8CC7-F7DE-4120-A8E2-B2AECFF2620C}` · interface `IDataFolder`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 88 instâncias em 27 arquivo(s)
- DataFolder Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Expose` | ULong | RW | framework | Expose | nomeada | — | Expõe o objeto (flag de framework) |

<a id="panel-dataserver"></a>
### DataServer

- CLSID `{803F8CC4-F7DE-4120-A8E2-B2AECFF2620C}` · interface `IDataServer`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 53 instâncias em 27 arquivo(s)
- Data Server control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Expose` | ULong | RW | framework | Expose | nomeada | — | Expõe o objeto (flag de framework) |

<a id="panel-demotag"></a>
### DemoTag

- CLSID `{1EED2462-30A0-11D4-8E8A-525400E657A3}` · interface `IDemoTag`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 2 arquivo(s)
- DemoTag class

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | — | não gravada nomeada | the server's current date | This property varies according to the type of a Demo Tag's waveform, established in the Type property. This is a read-only property. When the Type property is equal to 3 (three, CurrentTime), the data type of this property is Date. In this case, the default value is the server's current date and tim… ⚠ manual: somente leitura |
| `TimeStamp` | Date | R | type lib | — | não gravada nomeada | 00:00:00 | This property is updated whenever a change in the value or state occurs in the Value or Quality properties. It informs what is the date and time associated to the value of a Demo Tag, as well as to its quality. This is a read-only property. The default value of this property is 00:00:00. |
| `Minimum` | Double | RW | type lib | — | não gravada nomeada | 0 (zero) | This property determines the minimum value of a Demo Tag. The default value of this property is 0 (zero). |
| `Maximum` | Double | RW | type lib | — | não gravada nomeada | 100 | This property determines the maximum value of a Demo Tag. The default value of this property is 100. |
| `Period` | Long | RW | type lib | — | não gravada nomeada | 10,000 ms | Defines the length of a waveform, in milliseconds. It does not apply when the Type property is set to either 0 - Random or 3 - CurrentTime. The default value of this property is 10,000 ms. |
| `Type` | DemoType | RW | type lib | Type | nomeada | — | Determines the type of a Demo Tag's waveform. Change this property according to the next table. When this property is set to 3 (three, CurrentTime), the Value property contains the server's current date and time. Available options for the Type property VALUE WAVEFORM 0 Random 286 Server Objects VALU… |
| `Scan` | Long | RW | type lib | Scan | nomeada | 1,000 | This property defines the time interval, in milliseconds, between two variations of the Value property. Use this property if users want a greater or smaller amount of data generated by a Demo Tag. The default value of this property is 1,000. The scan value must be greater than 0 (zero). |
| `Enabled` | Boolean | RW | type lib | Enabled | nomeada | True | This property enables or disables a variation in a Demo Tag. If this property is set to False, variation is disabled. Otherwise, a Demo Tag updates its Value property according to the settings in the Period and the Scan properties. The default value of this property is True. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Max` | Double |  | gravada no .prj | Max | nomeada | — | sem equivalente na type lib |
| `Min` | Double |  | gravada no .prj | Min | nomeada | — | sem equivalente na type lib |
| `Phase` | ULong |  | gravada no .prj | Phase | nomeada | — | sem equivalente na type lib |

**Métodos:** `Reset()`

<a id="panel-drawarc"></a>
### DrawArc

- CLSID `{429CD9A5-935B-4897-B629-ED6903C555E5}` · interface `IDrawArc` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 46 instâncias em 4 arquivo(s)
- DrawArc control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's horizontal area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how that fill is performed. The default value of this property is 100. |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's vertical area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which indicates how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's horizontal fill. This property works along with the HorizontalPercentFill property, which informs the percentage of an object must be filled. These two properties allow a simulation of a level fill in an object, such as a tank level. Available options for the HorizontalFillStyle … |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's vertical fill. This property works along with the VerticalPercentFill property, which informs the percentage of an object to fill. These two properties allow a simulation of a level fill on an object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fill p… |
| `FillStyle` | FillStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for Screen objects. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 1 - Hollow There is no fill style 2 - Horizontal Fill style contains horizontal strip… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for an object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, and also set the FillStyle property with values between 2 (two) and 8 (eight). This allows the remaining area to us… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen object. This property is only used when the value of the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color c… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a color for an object's background. This color is used when the BackgroundStyle property is configured to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties contains a value different from 100. Another use of this color is when the FillStyl… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `ArcStyle` | ArcStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a border or line style for this object. This border is drawn according to a defined style, using a color specified by the BorderColor property and a width specified by the BorderWidth property. The available options for this property are described on the next table. Available… |
| `ArcBeginAngle` | Int | RW | type lib | — | não gravada nomeada | 0 (zero) | This property configures an initial angle for this object's arc, in degrees. The accepted interval for this property ranges from 0 (zero) to 359. Arc's style and shape also depend on the ArcEndAngle and ArcStyle properties. The default value of this property is 0 (zero). The next script contains an … |
| `ArcEndAngle` | Int | RW | type lib | — | não gravada nomeada | 270 | This property configures a final angle for this object's arc, in degrees. The accepted interval for this property ranges from 0 (zero) to 359. Arc's style and shape also depend on the ArcBeginAngle and ArcStyle properties. The default value of this property is 270. The next script contains an exampl… |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawbezier"></a>
### DrawBezier

- CLSID `{2BE6FCB2-8CDB-4166-9D89-43A42DFD91D1}` · interface `IDrawBezier` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 7 instâncias em 2 arquivo(s)
- DrawBezier control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's horizontal area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how that fill is performed. The default value of this property is 100. |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's vertical area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which indicates how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's horizontal fill. This property works along with the HorizontalPercentFill property, which informs the percentage of an object must be filled. These two properties allow a simulation of a level fill in an object, such as a tank level. Available options for the HorizontalFillStyle … |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's vertical fill. This property works along with the VerticalPercentFill property, which informs the percentage of an object to fill. These two properties allow a simulation of a level fill on an object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fill p… |
| `FillStyle` | FillStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for Screen objects. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 1 - Hollow There is no fill style 2 - Horizontal Fill style contains horizontal strip… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for an object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, and also set the FillStyle property with values between 2 (two) and 8 (eight). This allows the remaining area to us… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen object. This property is only used when the value of the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color c… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a color for an object's background. This color is used when the BackgroundStyle property is configured to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties contains a value different from 100. Another use of this color is when the FillStyl… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `PolygonFill` | PolygonFillMode | RW | type lib | — | não gravada nomeada | — | This property configures the fill mode of this object's area. To determine whether this area must be filled or not, a line is drawn starting at a p point towards infinity without crossing any vertexes. Possible values for this property are the following: 0 - Alternate: If the drawn line crosses an o… |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawcircle"></a>
### DrawCircle

- CLSID `{C44E8392-FE8D-11D3-8E8A-525400E657A3}` · interface `IDrawCircle` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 80 instâncias em 27 arquivo(s)
- DrawCircle control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's horizontal area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how that fill is performed. The default value of this property is 100. |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's vertical area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which indicates how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's horizontal fill. This property works along with the HorizontalPercentFill property, which informs the percentage of an object must be filled. These two properties allow a simulation of a level fill in an object, such as a tank level. Available options for the HorizontalFillStyle … |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's vertical fill. This property works along with the VerticalPercentFill property, which informs the percentage of an object to fill. These two properties allow a simulation of a level fill on an object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fill p… |
| `FillStyle` | FillStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for Screen objects. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 1 - Hollow There is no fill style 2 - Horizontal Fill style contains horizontal strip… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for an object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, and also set the FillStyle property with values between 2 (two) and 8 (eight). This allows the remaining area to us… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen object. This property is only used when the value of the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color c… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a color for an object's background. This color is used when the BackgroundStyle property is configured to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties contains a value different from 100. Another use of this color is when the FillStyl… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawconnector"></a>
### DrawConnector

- CLSID `{C6E7C991-C47C-4749-A759-3C440D329483}` · interface `IDrawConnector`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 142 instâncias em 8 arquivo(s)
- DrawConnector control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `Points` | IDrawConnectorPoints | R | type lib | — | não gravada nomeada | — | Returns a Collection of Connector Points object in a Connector. The Collection of Connector Points object is used to insert, remove, or access the available Connector Points in a Connector. This is a read-only property. |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `ConnectionInfoCount` | ULong |  | gravada no .prj | ConnectionInfoCount | nomeada | — | sem equivalente na type lib |
| `SlotRef_0_PlugName` | String |  | gravada no .prj | SlotRef_0_PlugName | nomeada | — | sem equivalente na type lib |
| `SlotRef_0_SlotId` | String |  | gravada no .prj | SlotRef_0_SlotId | nomeada | — | sem equivalente na type lib |
| `SlotRef_0_SlotName` | String |  | gravada no .prj | SlotRef_0_SlotName | nomeada | — | sem equivalente na type lib |
| `SlotRef_1_PlugName` | String |  | gravada no .prj | SlotRef_1_PlugName | nomeada | — | sem equivalente na type lib |
| `SlotRef_1_SlotId` | String |  | gravada no .prj | SlotRef_1_SlotId | nomeada | — | sem equivalente na type lib |
| `SlotRef_1_SlotName` | String |  | gravada no .prj | SlotRef_1_SlotName | nomeada | — | sem equivalente na type lib |

<a id="panel-drawconnectorpoint"></a>
### DrawConnectorPoint

- CLSID `{11DE8162-20A9-4DF2-A320-313BCE3AD399}` · interface `IDrawConnectorPoint`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DrawConnectorPoint object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `X` | Double | RW | type lib | — | — | — | X Indicates the horizontal coordinate of this Connector Point relative to a Screen's left border, in Himetric units. |
| `Y` | Double | RW | type lib | — | — | — | Y Indicates the vertical coordinate of this Connector Point relative to a Screen's upper border, in Himetric units. |
| `Name` | String | R | type lib | — | — | — | Name Returns the name of this Connector Point. This is a read-only property. NOTES The name of a Connector Point may change after inserting or removing Connector Points from a Collection of Connector Points. The first and last Connector Point in the Collection of Connector Points are named, respecti… |
| `IsConnected` | Boolean | R | type lib | — | — | — | IsConnected Indicates whether this Connector Point is connected or not to any Screen object. If it is connected, the X and Y properties can be read but cannot be changed. |

**Métodos:** `ConnectTo(Object Object, SlotNameIndex Variant)`; `Disconnect(X Variant, Y Variant)`; `Delete()`

<a id="panel-drawconnectorpoints"></a>
### DrawConnectorPoints

- CLSID `{22E799DD-3015-4FEC-8164-BDF4DC7A93FF}` · interface `IDrawConnectorPoints`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DrawConnectorPoints collection object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Count` | Long | R | type lib | — | — | — | Count Contains the number of Connector Points in a Collection of Connector Points. This is a read-only property. |

**Métodos:** `Item(NameIndex Variant)`; `AddPoint(X Double, Y Double, lIndexAt Long)`; `DeletePoint(NameIndex Variant)`

<a id="panel-drawgroup"></a>
### DrawGroup

- CLSID `{C44E8382-FE8D-11D3-8E8A-525400E657A3}` · interface `IDrawGroup` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 1098 instâncias em 28 arquivo(s)
- DrawGroup control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `OverrideFillMode` | EnumFillOverrideMode | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for objects in a Group. It changes the original image's fill mode without changing original object's fill settings. Available options for the OverrideFillMode property 0 - NoOverride Object's original fill (default) 1 - Wireframe Objects are not filled, they draw … |
| `EnableOverrideLineColor` | Boolean | RW | type lib | — | não gravada nomeada | False | This property enables or disables a Group object to override original colors of lines on objects contained in that Group. If this property is enabled, original colors of lines on objects in that Group are replaced by the color defined in the OverrideLineColor property. Otherwise, each object contain… |
| `OverrideFillColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | red (RGB(255, 0, 0)) | When the OverrideFillMode property is set to 2 (two) or 3 (three), this property is used to define a color to use when filling adjacent objects in a Group, instead of their original colors. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this pr… |
| `OverrideLineColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | red (RGB(255, 0, 0)) | When the EnableOverrideLineColor property is set to True, this property is used to define a color to use on object's line of a Group, instead of their original colors. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is red (RGB(255… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawline"></a>
### DrawLine

- CLSID `{C44E83B2-FE8D-11D3-8E8A-525400E657A3}` · interface `IDrawLine` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 400 instâncias em 30 arquivo(s)
- DrawLine control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's horizontal area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how that fill is performed. The default value of this property is 100. |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's vertical area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which indicates how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's horizontal fill. This property works along with the HorizontalPercentFill property, which informs the percentage of an object must be filled. These two properties allow a simulation of a level fill in an object, such as a tank level. Available options for the HorizontalFillStyle … |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's vertical fill. This property works along with the VerticalPercentFill property, which informs the percentage of an object to fill. These two properties allow a simulation of a level fill on an object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fill p… |
| `FillStyle` | FillStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for Screen objects. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 1 - Hollow There is no fill style 2 - Horizontal Fill style contains horizontal strip… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for an object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, and also set the FillStyle property with values between 2 (two) and 8 (eight). This allows the remaining area to us… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen object. This property is only used when the value of the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color c… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a color for an object's background. This color is used when the BackgroundStyle property is configured to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties contains a value different from 100. Another use of this color is when the FillStyl… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `PolygonFill` | PolygonFillMode | RW | type lib | — | não gravada nomeada | — | This property configures the fill mode of this object's area. To determine whether this area must be filled or not, a line is drawn starting at a p point towards infinity without crossing any vertexes. Possible values for this property are the following: 0 - Alternate: If the drawn line crosses an o… |
| `Points` | IDrawLinePoints | R | type lib | — | não gravada nomeada | — | Returns a Collection of Polygon Points object inside this object. The Collection of Polygon Points object is used to insert, remove, or access the available Polygon Points inside this object. This is a read-only property. |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawlinepoint"></a>
### DrawLinePoint

- CLSID `{BB0BCC31-AEE9-4D4A-8476-BD34D975B3E2}` · interface `IDrawLinePoint`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DrawLinePoint object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `X` | Double | RW | type lib | — | — | — | X Indicates the horizontal coordinate of this Polygon Point relative to a Screen's left border, in Himetric units. |
| `Y` | Double | RW | type lib | — | — | — | Y Indicates the vertical coordinate of this Polygon Point relative to a Screen's upper border, in Himetric units. |

**Métodos:** `Delete()`

<a id="panel-drawlinepoints"></a>
### DrawLinePoints

- CLSID `{CC09069A-E766-4A4E-85CE-C0ACEE0EDEAA}` · interface `IDrawLinePoints`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DrawLinePoints collection object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Count` | Long | R | type lib | — | — | — | Count Contains the number of Polygon Points in the Collection of Polygon Points. This is a read-only property. |

**Métodos:** `Item(Index Long)`; `AddPoint(X Double, Y Double, lIndexAt Long)`; `DeletePoint(lIndex Long)`

<a id="panel-drawpicture"></a>
### DrawPicture

- CLSID `{C44E83C2-FE8D-11D3-8E8A-525400E657A3}` · interface `IDrawPicture` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 5 instâncias em 3 arquivo(s)
- DrawPicture control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of this object's horizontal area to fill. Acceptable values for this property range from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how this fill occurs. The default value of this property is 100. The next… |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of this object's vertical area to fill. Acceptable values for this property range from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which informs how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines a horizontal fill for this object. This property works along with the HorizontalPercentFill property, which informs a percentage of this object that must be filled. These two properties allow simulating a level fill in this object, such as a tank level, for example. Available options for the… |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines a vertical fill for this object. This property works along with the VerticalPercentFill property, which informs a percentage of this object to fill. These two properties allow simulating a level fill in this object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fil… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect in this object. If set to True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines a vertical coordinate to the left of this object's shadow, in Himetric units. This shadow is always relative to this object's X property. Positive values indicate that this shadow is on this object's right side, and negative values on this object's left side. The default value of this proper… |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines an upper horizontal coordinate for this object's shadow, in Himetric units. This shadow is always relative to this object's Y property. Positive values indicate that this shadow is under this object, and negative values that it is above this object. The default value of this property is 200.… |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | light gray (RGB(128, 128, 128)) | Specifies a fill color for this object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is light gray (RGB(128, 128, 128)). The next script contains an example of… |
| `OverrideFillMode` | EnumFillOverrideMode | RW | type lib | FillOverrideMode (apelido confirmado) | nomeada | — | This property specifies a fill mode for this object's picture, when displaying a Windows Metafile. It changes the picture's original fill mode without changing the file defined in the Filename property. The available options for this property are described on the next table. Available options for th… |
| `EnableOverrideLineColor` | Boolean | RW | type lib | OverrideLineColorEnabled (apelido confirmado) | nomeada | — | This property enables or disables this object to overwrite the original color of a picture's line by the color defined in the OverrideLineColor property. If this property is enabled, it allows modifying the original color of this object's line by the color of the OverrideLineColor property. Otherwis… |
| `OverrideFillColor` | ECO_COLOR | RW | type lib | OverrideFillColor | nomeada | red (RGB(255, 0, 0)) | When the OverrideFillMode property is set to 2 (two) or 3 (three), this property is used to define a color to fill a picture, instead of its original color. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is red (RGB(255, 0, 0)). T… |
| `OverrideLineColor` | ECO_COLOR | RW | type lib | OverrideLineColor | nomeada | red (RGB(255, 0, 0)) | When the EnableOverrideLineColor property is set to True, this property is used to define a color to use as a picture's line, instead of its original color. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is red (RGB(255, 0, 0)). T… |
| `Filename` | BSTRPICTURE | RW | type lib | Filename | nomeada | empty | Defines a picture's file name linked to this object. This file's path can be a full file path on disk, as well as a path relative to an application, when this picture file is inserted as an application Resource. The default value of this property is empty. The next table contains all supported file … |
| `Convert` | Long | RW | type lib | Convert | nomeada | 0 (zero) | This property allows converting a picture. If this property is set to 0 (zero), users can view that conversion. Otherwise, users cannot view that conversion. This property only accepts values 0 (zero) and 1 (one). The default value of this property is 0 (zero). |
| `TransparentMode` | EnumTransparentMode | RW | type lib | TransparentMode | nomeada | — | This property specifies a transparency effect mode for this picture. The available options for this property are described on the next table. Available options for the TransparentMode property 0 - Disabled No transparency is performed (default) 1 - ByColor Transparency uses a color defined in the Tr… |
| `TransparentColor` | ECO_COLOR | RW | type lib | TransparentColor | nomeada | white (RGB(255, 255, 255)) | When the TransparentMode property is set to 1 (one), this property defines which color on this picture is not drawn, and that picture remains transparent in these areas. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is white (RGB… |
| `TransparentPercent` | Long | RW | type lib | TransparentPercent | nomeada | — | When the TransparentMode property is set to 2 (two), this property defines how transparent a picture is displayed, ranging from 0 (zero, fully transparent) to 100 (opaque or solid). The next script contains an example of using this property. Sub DrawPicture1_Click() ' Leaves this picture transparent… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for this object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, allowing that the remaining area uses the color configured in the BackgroundColor property as its fill. The avail… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a fill color for this object's background. This color is used when the BackgroundStyle property is set to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties is different from 100. In scripts, use VBScript's RGB method to build a color to li… |
| `IgnoreFlipHorizontal` | Boolean | RW | type lib | — | não gravada nomeada | False | This property forces the image loaded in this object to keep the original orientation relative to the horizontal axis, regardless of the configuration of the FlipHorizontal property, common to all Screen objects. The default value of this property is False. NOTES This property is only effective if t… |
| `IgnoreFlipVertical` | Boolean | RW | type lib | — | não gravada nomeada | False | This property forces the image loaded in this object to keep the original orientation relative to the vertical axis, regardless of the configuration of the FlipVertical property, common to all Screen objects. The default value of this property is False. NOTES This property is only effective if this … |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `FlipSupport` | Boolean |  | gravada no .prj | FlipSupport | nomeada | — | sem equivalente na type lib |

**Métodos:** `ScaleImage(PercX Double, PercY Double, AnchorType PicturePositionConstants)`

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawrect"></a>
### DrawRect

- CLSID `{C44E83A2-FE8D-11D3-8E8A-525400E657A3}` · interface `IDrawRect` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 92 instâncias em 27 arquivo(s)
- DrawRect control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's horizontal area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how that fill is performed. The default value of this property is 100. |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's vertical area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which indicates how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's horizontal fill. This property works along with the HorizontalPercentFill property, which informs the percentage of an object must be filled. These two properties allow a simulation of a level fill in an object, such as a tank level. Available options for the HorizontalFillStyle … |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's vertical fill. This property works along with the VerticalPercentFill property, which informs the percentage of an object to fill. These two properties allow a simulation of a level fill on an object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fill p… |
| `FillStyle` | FillStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for Screen objects. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 1 - Hollow There is no fill style 2 - Horizontal Fill style contains horizontal strip… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for an object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, and also set the FillStyle property with values between 2 (two) and 8 (eight). This allows the remaining area to us… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen object. This property is only used when the value of the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color c… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a color for an object's background. This color is used when the BackgroundStyle property is configured to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties contains a value different from 100. Another use of this color is when the FillStyl… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawscale"></a>
### DrawScale

- CLSID `{6E28EBA8-17F5-4374-8045-7016C7D343C6}` · interface `IDrawScale` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DrawScale control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | — | white (RGB(255, 255, 255)) | This property determines a border color to apply to this object. With this property, users can apply a default color or customize that color by editing it. The default value of this property is white (RGB(255, 255, 255)). The next script contains an example of using this property. Sub Scale1_Click()… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | — | — | This property determines a border style applied to this object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border on scale's vertical grid 1 - Dash Applies a dashed-line border on this scale 2 - D… |
| `BorderWidth` | Long | RW | type lib | — | — | 0 (zero) | This property determines a border width, in pixels, of this object. By using this property, users can configure a border width, without changing its structure. The default value of this property is 0 (zero). |
| `FillStyle` | FillStyleConstants | RW | type lib | — | — | — | Returns/sets the fill style of object |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | — | — | Returns/sets the gradient style of object |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | — | blue (RGB(0, 0, 255)) | This property specifies a fill color for this object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (R… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | — | gray (RGB(192, 192, 192)) | This property specifies a fill color for this object's background. This color is used when the BackgroundStyle property is set to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties have a value different from 100. Another usage of this color is when the FillStyle … |
| `MinimumValue` | Double | RW | type lib | — | — | 0 (zero) | This property determines the minimum value reached by this object. The default value of this property is 0 (zero). The next script contains an example of using this property. Sub CommandButton1_Click() ' When clicking this button, opens a MessageBox ' indicating the minimum value for this property M… |
| `MaximumValue` | Double | RW | type lib | — | — | 100 | This property determines the maximum value reached by this object. The default value of this property is 100. The next script contains an example of using this property. Sub CommandButton_Click() ' When clicking this button, opens a MessageBox ' indicating the maximum value for this property MsgBox … |
| `LineColor` | ECO_COLOR | RW | type lib | — | — | black (RGB(0, 0, 0)) | Determines a line color for this object's ticks and minor ticks. To determine a legend color with this object's numbers, use the TextColor property. The default value of this property is black (RGB(0, 0, 0)). |
| `Ticks` | Long | RW | type lib | — | — | 5 (five) | Determines the number of ticks on this object. The default value of this property is 5 (five). |
| `TicksPercentSize` | Double | RW | type lib | — | — | 20 | Determines the size of lines that divide this object. According to the value specified in this property, the default divider line of this object appears smaller or bigger. The default value of this property is 20. |
| `MinorTicks` | Long | RW | type lib | — | — | 3 (three) | This property determines the amount of minor ticks on this object. The default value of this property is 3 (three). The next script contains an example of using this property. Sub CommandButton1_Click() ' Displays the total amount ' of minor ticks on a scale MsgBox CStr(Screen.Item("Scale1").MinorTi… |
| `MinorTicksPercentSize` | Double | RW | type lib | — | — | 10 | This property determines the size of minor ticks subdividing each measurement of this object. The default value of this property is 10. |
| `ScaleAlignment` | ScaleAlignmentStyle | RW | type lib | — | — | — | This property determines a type of alignment for this object. Possible values for this property are 0 - RightSide: To the right (default) or 1 - LeftSide: To the left. |
| `TextFont` | Font | RW | type lib | — | — | — | This property determines a font to apply to this object. The selected font is applied to the whole object. This property cannot be used in Links. Please check topic Font for more information about the sub-properties of this property. |
| `TextColor` | ECO_COLOR | RW | type lib | — | — | black (RGB(0, 0, 0)) | Determines a font color applied on this object's numbered legend. To determine a line color with this object's ticks and minor ticks, use the LineColor property. The default value of this property is black (RGB(0, 0, 0)). |
| `ShowText` | Boolean | RW | type lib | — | — | True | This property determines text visibility on this object's legend. If this property is set to True, text is displayed. Otherwise, this object only displays scale lines and minor ticks. The default value of this property is True. |
| `TextAlignment` | ShowFontAlignment | RW | type lib | — | — | — | This property determines this object's text alignment. The available options for this property are described on the next table. Available options for the TextAlignment property 0 - LeftAlignment Text alignment is on the left (default) 1 - CenterAlignment Text alignment is centered 2 - RightAlignment… |
| `StretchText` | Boolean | RW | type lib | — | — | False | This property determines the application of a stretch to this object's text. If this object's width or height change, text follows that change. If this property is enabled, this object follows width and height variations as it is transformed. Otherwise, text maintains its original settings. The defa… |
| `Format` | BSTRFORMAT | RW | type lib | — | — | — | This property specifies a format type to attribute to this object. It allows changing the way data is displayed without changing their values. This property can be edited manually or configured using a format window. Its usage is similar to formats used on spreadsheets, following the same syntax. Th… |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-drawstring"></a>
### DrawString

- CLSID `{A9B49EC2-3C94-11D4-8E73-00C0DFB1AC67}` · interface `IDrawString` · eventos `DDrawStringEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 898 instâncias em 30 arquivo(s)
- DrawString control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's horizontal area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how that fill is performed. The default value of this property is 100. |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's vertical area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which indicates how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's horizontal fill. This property works along with the HorizontalPercentFill property, which informs the percentage of an object must be filled. These two properties allow a simulation of a level fill in an object, such as a tank level. Available options for the HorizontalFillStyle … |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's vertical fill. This property works along with the VerticalPercentFill property, which informs the percentage of an object to fill. These two properties allow a simulation of a level fill on an object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fill p… |
| `FillStyle` | FillStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for Screen objects. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 1 - Hollow There is no fill style 2 - Horizontal Fill style contains horizontal strip… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for an object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, and also set the FillStyle property with values between 2 (two) and 8 (eight). This allows the remaining area to us… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen object. This property is only used when the value of the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color c… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a color for an object's background. This color is used when the BackgroundStyle property is configured to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties contains a value different from 100. Another use of this color is when the FillStyl… |
| `Value` | Variant | RW | type lib | Value | nomeada | — | This property is a Variant, which may assume any and every type of value displayed by this object. Usually this property contains a text, because it is automatically filled in when creating a new object. The IsSetPoint property is used to determine whether this object has the same behavior of a SetP… |
| `TextAlignment` | ShowFontAlignment | RW | type lib | — | não gravada nomeada | — | This property specifies a horizontal alignment for a text displayed in this object. The available options for this property are described on the next table. Available options for the TextAlignment property 0 - LeftAlignment Text's horizontal alignment is on the left 1 - CenterAlignment Text's horizo… |
| `VertTextAlignment` | VerticalAlignment | RW | type lib | — | não gravada nomeada | — | Determines a vertical alignment for this object's text. The available options for this property are described on the next table. Available options for the VertTextAlignment property 0 - TopAlignment Text's vertical alignment is on top of this object 1 - MidAlignment Text's vertical alignment is cent… |
| `TextFont` | Font | RW | type lib | — | não gravada nomeada | — | Defines information about a font used in this object. This property cannot be used in Links and all its sub-properties can be checked on topic Font. |
| `StretchText` | Boolean | RW | type lib | — | não gravada nomeada | — | Resizes this object's type. When enabling this property, this object automatically resizes its text font size, so that the area occupied by it always remains the same. Otherwise, if this property is set to False, no resizing is performed. 162 View |
| `WordWrap` | Boolean | RW | type lib | — | não gravada nomeada | — | Enables or disables a line break in this text, if the available area for this text overrides the limits defined by this object. For this property to work, the Multiline property must be set to True. |
| `Format` | BSTRFORMAT | RW | type lib | Format | nomeada | — | This property specifies a format type to attribute to this object. It allows changing the way data is displayed without changing its value. This property can be edited manually or configured using a format window. Its usage is similar to formats used on spreadsheets, following the same syntax. The n… |
| `TextColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | This property specifies a color for a text font to display. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is black (RGB(0, 0, 0)). |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `IsSetPoint` | Boolean | RW | type lib | IsSetPoint | nomeada | True | This property is used to determine whether this object behaves as a SetPoint, that is, if it allows editing its Value property. The Value property is a Variant, which may assume any and every type of value. This property is a Boolean and if it is equal to True, it allows edition. If it is equal to F… |
| `Multiline` | Boolean | RW | type lib | Multiline | nomeada | False | This property indicates whether the text contains multiple lines (True) or it is a simple text box (False). This behavior can be viewed when Elipse E3 Viewer is executing. The default value of this property is False. |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `SetPointDataType` | stDataType | RW | type lib | SetPointDataType | nomeada | — | Determines a type of value that is sent from this object to a Tag. The available options for this property are described on the next table. The available options for this property are described on the next table. 0 - stCurrentType Maintains current value type in this object (default, please check ne… |
| `EnableLimits` | Boolean | RW | type lib | EnableLimits | nomeada | — | Indicates if there is a check on text limits. When this property is equal to True, and users insert a non-number value or a value outside the limits defined in the MinLimit and MaxLimit properties, an error message is displayed (the IsSetPoint property must be equal to True). The next script contain… |
| `MinLimit` | Double | RW | type lib | MinLimit | nomeada | — | Contains the minimum allowed value for this object (the EnableLimits property must be equal to True). The next script contains an example of using this property. Sub CommandButton2_Click() Screen.Item("Text1").MinLimit = Screen.Item("Text5").Value |
| `MaxLimit` | Double | RW | type lib | MaxLimit | nomeada | — | Contains the maximum allowed value for this object (the EnableLimits property must be equal to True). The next script contains an example of using this property. Sub CommandButton3_Click() Screen.Item("Text1").MaxLimit = Screen.Item("Text6").Value |
| `KeepFormatWhenEditing` | kfKeepFormat | RW | type lib | KeepFormat (apelido confirmado) | nomeada | — | Allows the object's value to be edited with or without format. Possible values for this property are 0 - kfNever: Value is always edited without format (default) or 1 - kfAutomatic: Allows a value to be edited in the formatted value, if Elipse E3 detects that the formatted text can be interpreted as… |
| `MaxCharacters` | Long | RW | type lib | MaxCharacters | nomeada | — | This property establishes a limit of characters that users can type, when in edition mode, in this object. The following restrictions apply to this property: Configuring this property to 0 (zero) does not limit the number of characters when editing this object, and also configures the RemainingChara… |
| `RemainingCharacters` | Long | R | type lib | — | não gravada nomeada | — | This property indicates the number of characters that users still can type in this object, if the MaxCharacters property is configured with a value greater than 0 (zero). This is a read-only property and is only available at run time. |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `Validate(Cancel Variant, NewValue Variant)`

<a id="panel-drawtank"></a>
### DrawTank

- CLSID `{C44E83D2-FE8D-11D3-8E8A-525400E657A3}` · interface `IDrawTank` · eventos `DDrawObjectEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 167 instâncias em 25 arquivo(s)
- DrawTank control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `BorderColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)), except for Display | Specifies a color for an object's border or line. This property is only used when the BorderStyle property is not configured to 5 (five, Null), where an object does not have a border. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property… |
| `BorderStyle` | BorderStyleConstants | RW | type lib | — | não gravada nomeada | — | This property determines a border style to apply to an object. The available options for this property are described on the next table. Available options for the BorderStyle property 0 - Normal Applies a solid border to an object (default) 1 - Dash Applies a dashed border to an object 2 - Dot Applie… |
| `BorderWidth` | Long | RW | type lib | — | não gravada nomeada | 0 (zero) | Defines the width, in Himetric units, of an object's border or line. It is only used if the BorderStyle property is not configured to 5 (five, Null). The default value of this property is 0 (zero). This is an exception in Elipse E3's measuring system, because when its value is equal to 0 (zero), the… |
| `HorizontalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's horizontal area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the HorizontalFillStyle property, which informs how that fill is performed. The default value of this property is 100. |
| `VerticalPercentFill` | Single | RW | type lib | — | não gravada nomeada | 100 | Use this property to specify a percentage of an object's vertical area to fill. Acceptable values for this property vary from 0 (zero) to 100. This property works along with the VerticalFillStyle property, which indicates how this fill occurs. The default value of this property is 100. |
| `HorizontalFillStyle` | HorizontalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's horizontal fill. This property works along with the HorizontalPercentFill property, which informs the percentage of an object must be filled. These two properties allow a simulation of a level fill in an object, such as a tank level. Available options for the HorizontalFillStyle … |
| `VerticalFillStyle` | VerticalFillPercentStyle | RW | type lib | — | não gravada nomeada | — | Defines an object's vertical fill. This property works along with the VerticalPercentFill property, which informs the percentage of an object to fill. These two properties allow a simulation of a level fill on an object. Available options for the VerticalFillStyle property 0 - FillBottomToTop Fill p… |
| `FillStyle` | FillStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for Screen objects. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 1 - Hollow There is no fill style 2 - Horizontal Fill style contains horizontal strip… |
| `BackgroundStyle` | BackgroundStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for an object's background. This property enables using the VerticalPercentFill and HorizontalPercentFill properties with values different from 100, and also set the FillStyle property with values between 2 (two) and 8 (eight). This allows the remaining area to us… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen object. This property is only used when the value of the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color c… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | blue (RGB(0, 0, 255)), except for Display | This property specifies a color for an object's foreground. This color is used when the FillStyle property is set to 0 (zero, solid) or between 2 (two) and 9 (nine). In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is blue (RGB(0, 0… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | This property specifies a color for an object's background. This color is used when the BackgroundStyle property is configured to 1 (one, opaque) and one of the VerticalPercentFill or HorizontalPercentFill properties contains a value different from 100. Another use of this color is when the FillStyl… |
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `Effect3D` | Effect3DStyleConstants | RW | type lib | — | não gravada nomeada | — | Applies a 3D effect to the selected object. The available options for this property are described on the next table. Available options for the Effect3D property 0 - No3D Transparent (default) 1 - Raised Applies a raised 3D effect 2 - Sunken Applies a sunken 3D effect |
| `Effect3D_X` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's horizontal axis (X axis). The default value of this property is 30. |
| `Effect3D_Y` | Double | RW | type lib | — | não gravada nomeada | 30 | Specifies the dimension of a 3D effect on an object's vertical axis (Y axis). The default value of this property is 30. |
| `Effect3DColorBase` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Determines a color for an object's 3D base effect. The default value of this property is black (RGB(0, 0, 0)). |
| `Effect3DColorTop` | ECO_COLOR | RW | type lib | — | não gravada nomeada | white (RGB(255, 255, 255)) | Determines a color for an object's 3D top effect. The default value of this property is white (RGB(255, 255, 255)). |
| `RoundAspectX` | Double | RW | type lib | — | não gravada nomeada | — | This property defines the dimension of the sizes of this object on the horizontal axis. Thus, according to the value defined on this property, this object's corners change their shape, from a rectangle to an ellipse. This property may vary its value from 0,1 to 1,0. The next script contains an examp… |
| `RoundAspectY` | Double | RW | type lib | — | não gravada nomeada | — | This property defines the dimension of the height of this object on the vertical axis. Thus, according to the value defined on this property, this object's corners change their shape, from a rectangle to an ellipse. This property may vary its value from 0,1 to 1,0. The next script contains an exampl… |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`

<a id="panel-dynamicmove"></a>
### DynamicMove

- CLSID `{33CDEDBE-A66B-49EB-AB53-A7773D97D0F9}` · interface `IDynamicMove`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 9 instâncias em 2 arquivo(s)
- DynamicMove control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Shadow` | Boolean | RW | type lib | — | não gravada nomeada | False | Indicates the presence of a shadow effect on an object. If configured as True, this object has a shadow, whose coordinates are established by the ShadowX and ShadowY properties. Otherwise, this object does not have a shadow effect. The default value of this property is False. |
| `ShadowX` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the left vertical coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's X property. Positive values indicate that this shadow is on the right side of an object, and negative ones on the left side. The default value of this property is 200. |
| `ShadowY` | Double | RW | type lib | — | não gravada nomeada | 200 | Defines the upper horizontal coordinate of an object's shadow, in Himetric units. This shadow is always relative to the object's Y property. Positive values indicate that this shadow is below an object, and negative ones above. The default value of this property is 200. |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | dark gray (RGB(128, 128, 128)) | Specifies a fill color for an object's shadow. This color is used when the Shadow property is set to True. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is dark gray (RGB(128, 128, 128)). 100 View |
| `OverrideFillMode` | EnumFillOverrideMode | RW | type lib | — | não gravada nomeada | — | This property specifies a fill mode for moving objects. It changes the original fill mode of an image without changing objects' original fill settings. The available options for this property are described on the next table. 104 View Available options for the OverrideFillMode property 0 - NoOverride… |
| `EnableOverrideLineColor` | Boolean | RW | type lib | — | não gravada nomeada | False | This property enables or disables this object to override the original color of its image's line by the color defined in the OverrideLineColor property. If this property is enabled, this allows users to modify the original color of this object's line by the color of the OverrideLineColor property. O… |
| `OverrideFillColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | red (RGB(255, 0, 0)) | When the OverrideFillMode property is set to 2 (two) or 3 (three), this property is used to define a color to use when filling moving objects, instead of their original color. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is red … |
| `OverrideLineColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | red (RGB(255, 0, 0)) | When the EnableOverrideLineColor property is set to True, this property is used to define a color to use on the line color of moving objects, instead of their original color. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is red (… |
| `RangeMin` | Double | RW | type lib | — | não gravada nomeada | — | This property determines the minimum range of this object's linear sliding. |
| `RangeMax` | Double | RW | type lib | — | não gravada nomeada | — | This property determines the maximum range of this object's linear sliding. |
| `Value` | Double | RW | type lib | — | não gravada nomeada | — | Indicates the initial value of this object's movement. This must be a value between the values defined in the RangeMax and RangeMin properties. |
| `EnableSlider` | Boolean | RW | type lib | — | não gravada nomeada | — | This property enables a slider in this object's movement. If this property is enabled, a movement slider is enabled. Otherwise, it does not occur. |
| `Detents` | Int | RW | type lib | — | não gravada nomeada | — | This property determines the number of steps of this object's movement. |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

<a id="panel-dynamicrotate"></a>
### DynamicRotate

- CLSID `{0BCCD9B6-ADEA-4455-B908-4D8EB73D620B}` · interface `IDynamicRotate`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DynamicRotate control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Shadow` | Boolean | RW | type lib | — | — | — | True if shadow is visible |
| `ShadowX` | Double | RW | type lib | — | — | — | Returns/sets the horizontal shadow offset |
| `ShadowY` | Double | RW | type lib | — | — | — | Returns/sets the vertical shadow offset |
| `ShadowColor` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets the shadow color |
| `OverrideFillMode` | EnumFillOverrideMode | RW | type lib | — | — | — | This property specifies a fill mode for moving objects. It changes the original fill mode of an image without changing objects' original fill settings. The available options for this property are described on the next table. Available options for the OverrideFillMode property 0 - NoOverride Original… |
| `EnableOverrideLineColor` | Boolean | RW | type lib | — | — | False | This property enables or disables this object to override the original color of its image's line by the color defined in the OverrideLineColor property. If this property is enabled, this allows users to modify the original color of this object's line by the color of the OverrideLineColor property. O… |
| `OverrideFillColor` | ECO_COLOR | RW | type lib | — | — | red (RGB(255, 0, 0)) | When the OverrideFillMode property is set to 2 (two) or 3 (three), this property is used to define a color to use when filling moving objects, instead of their original color. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is red … |
| `OverrideLineColor` | ECO_COLOR | RW | type lib | — | — | red (RGB(255, 0, 0)) | When the EnableOverrideLineColor property is set to True, this property is used to define a color to use on the line color of moving objects, instead of their original color. In scripts, use VBScript's RGB method to create a color to link to this property. The default value of this property is red (… |
| `RangeMin` | Double | RW | type lib | — | — | — | This property determines the minimum range of this object's rotational movement. |
| `RangeMax` | Double | RW | type lib | — | — | — | This property determines the maximum range of this object's rotational movement. |
| `Value` | Double | RW | type lib | — | — | — | Indicates the initial value of this object's movement. This must be a value between the values defined in the RangeMax and RangeMin properties. |
| `EnableSlider` | Boolean | RW | type lib | — | — | — | This property enables a slider in this object's movement. |
| `Detents` | Int | RW | type lib | — | — | — | This property determines the number of steps of this object's movement. |
| `RotationAngle` | Int | RW | type lib | — | — | — | This property determines the rotational angle of this object's movement. |
| `RotationDirection` | RotationDirectionStyle | RW | type lib | — | — | — | This property determines the direction of the rotational angle of this object's movement. The available options for this property are described on the next table. Available options for the RotationDirection property 0 - Clockwise Sets this object's rotational angle to the right (default) 1 - Counter… |

<a id="panel-e3sectionreport"></a>
### E3SectionReport

- CLSID `{AC6703B0-769D-4791-B9C5-B48C45ADA22D}` · interface `IE3SectionReport`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- E3SectionReport Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Caption` | String | RW | type lib | — | — | an empty String | Contains the title of a Section Report that appears on the toolbar of the preview window. The default value of this property is an empty String. |
| `ShowSidebar` | Boolean | RW | type lib | — | — | False | Shows or hides the sidebar of the preview mode of a Section Report. The default value of this property is False. |
| `PreviewViewType` | ReportPreviewViewType | RW | type lib | — | — | — | Indicates how pages of a Section Report are displayed in preview mode. Possible values for this property are 0 - rv2SinglePage: Displays one page at a time in the preview area (default), 1 - rv2Multipage: Displays one or more pages in the preview area, according to the configuration of the Multipage… |
| `ZoomLevel` | Single | RW | type lib | — | — | 100% | Represents the level of zoom in which a Section Report is open in preview mode, as a percentage. The value of this property ranges between 10% and 800%. This property can be configured to the value -1 (minus one) so that the preview mode fits the width of a Section Report or -2 (minus two) so that t… |
| `MultipageCols` | Integer | RW | type lib | — | — | — | Indicates the number of columns of a page of a Section Report in preview mode. The value of this property ranges between 1 (one, default) and 5 (five). This property is only available when the PreviewViewType property is configured with the value 1 (one, rv2Multipage). |
| `MultipageRows` | Integer | RW | type lib | — | — | — | Indicates the number of rows of a page of a Section Report in preview mode. The value of this property ranges between 1 (one, default) and 4 (four). This property is only available when the PreviewViewType property is configured with the value 1 (one, rv2Multipage). |
| `DisablePrintButton` | Boolean | RW | type lib | — | — | False | Shows or hides the Print option of the printing preview window of a Section Report at run time. The default value of this property is False. |

**Métodos:** `Query()`; `PrintPreview(Left Variant, Top Variant, Width Variant, Height Variant)`; `Print(vbShowPrintDialog Boolean)`; `Export(ExportFormat Variant, ExportFileName Variant, bShowSaveDlg Boolean)`; `GetExportFilter(bstrFilter String)`

<a id="panel-frame"></a>
### Frame

- CLSID `{CBC31D3B-1DA4-4D6A-A284-D63B7C3FA537}` · interface `IFrame`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 1 arquivo(s)
- Frame control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Caption` | String | RW | type lib | Caption | nomeada | — |  |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

<a id="panel-frameset"></a>
### FrameSet

- CLSID `{CAD32D3B-1DA4-4D6A-A284-D63B7C3FA537}` · interface `IFrameSet`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 14 instâncias em 1 arquivo(s)
- FrameSet class

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `IsHTML` | Boolean | R | type lib | — | não gravada nomeada | — | Returns True if this frame has HTML content |
| `SplitLink` | BSTRSPLITLINK | RW | type lib | SplitLink | nomeada | — | Returns/sets the split link |
| `SplitValue` | Variant | RW | type lib | Value (apelido inferido) | nomeada | — | Returns/sets the value of split |
| `SplitDockPosition` | SplitDockPosition | RW | type lib | SplitDockPosition | nomeada | — | Returns/sets the position where the split is docked |
| `SplitResizable` | Boolean | RW | type lib | SplitResizable | nomeada | — | True if split is resizable |
| `SplitBorder` | Boolean | RW | type lib | SplitBorder | nomeada | — | True if split border is visible |
| `Screen` | Object | R | type lib | Screen | nomeada | — | Child Screen object |
| `NavigateHistCount` | Long | R | type lib | — | não gravada nomeada | — | Returns size of open Screen History for this frame |
| `NavigateCanGoBack` | Boolean | R | type lib | — | não gravada nomeada | — | Returns True if there is a previous Screen in the Screen History for this frame |
| `NavigateCanGoForward` | Boolean | R | type lib | — | não gravada nomeada | — | Returns True if there is a next Screen in the Screen History for this frame |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `FirstAlignment` | ULong |  | gravada no .prj | FirstAlignment | nomeada | — | sem equivalente na type lib |
| `FormatValue` | Byte |  | gravada no .prj | FormatValue | nomeada | — | sem equivalente na type lib |
| `Scroll` | ULong |  | gravada no .prj | Scroll | nomeada | — | sem equivalente na type lib |
| `Zoom` | ULong |  | gravada no .prj | Zoom | nomeada | — | sem equivalente na type lib |

**Métodos:** `ShowScreen(Screen Object, Zoom Long, Scrollbars Boolean, Arg Variant, Alignment Variant)`; `OpenScreen(ScreenName String, Arg Variant)`; `SetForegroundWnd()`; `FlashWindow(Number ULong, Time ULong)`; `MinimizeFrame()`; `MaximizeFrame()`; `RestoreFrame()`; `BringToFront()`; `Close(Code Long)`; `Refresh(Force Boolean)`; `MoveFrame(PosX Variant, PosY Variant, SizeX Variant, SizeY Variant, InternalSize Boolean)`; `SetFrameOptions(Title String, Flags Long)`; `CaptureScreen(Filename String)`; `SetDisableTaskSwitching(Disable Boolean)`; `NavigateBack()`; `NavigateForward()`; `NavigateHistReset()`

<a id="panel-internaltag"></a>
### InternalTag

- CLSID `{C36D5658-E3C4-4657-B704-451381FA3C34}` · interface `IInternalTag`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 364 instâncias em 30 arquivo(s)
- InternalTag class

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | Value | nomeada | empty | This is a Variant-type property, which allows storing values of any type, from an Integer to an object pointer, according to the next example. Use it to store values in a Viewer or in a Server, and to exchange data among several points in an application. The default value of this property is empty. … |
| `Retentive` | Boolean | RW | type lib | Retentive | nomeada | — | This property determines whether the Internal Tag's value must be stored automatically or not, if the active Domain is stopped. This guarantees that the Tag's value is synchronized with the standby server. Thus, when the server starts running, the Tag's value is the same as the server that was stopp… |
| `TimeStamp` | Date | RW | type lib | TimeStamp | nomeada | — | This property informs the date and time associated to the value in the Value property. This is a read-write property, but whenever an Internal Tag value is modified, by script or by a Link, it is updated as well. |
| `Quality` | Long | RW | type lib | Quality | nomeada | — | Informs the value's quality in the Value property. This is a read-write property, but whenever the Internal Tag value is modified, by script or by a Link, it is updated as well. The next script contains an example of using this property. Sub CommandButton1_Click() MsgBox Application.GetObject("Data.… |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Métodos:** `WriteEx(NewValue Variant, NewTimestamp Variant, NewQuality UShort)`

<a id="panel-pickdomodal"></a>
### PickDoModal

- CLSID `{28266827-0F18-46D4-85E0-5E88CFD1B5B2}` · interface `IPickDoModal`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DoModal Pick Action

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ScreenName` | String | RW | type lib | — | — | — |  |
| `ScreenTitle` | String | RW | type lib | — | — | — |  |
| `ScreenPosX` | String | RW | type lib | — | — | — |  |
| `ScreenPosY` | String | RW | type lib | — | — | — |  |
| `ScreenSizeX` | String | RW | type lib | — | — | — |  |
| `ScreenSizeY` | String | RW | type lib | — | — | — |  |
| `Zoom` | Long | RW | type lib | — | — | — |  |
| `Alignment` | EPanelAlignment | RW | type lib | — | — | — |  |
| `Scroll` | Boolean | RW | type lib | — | — | — |  |
| `Argument` | Variant | RW | type lib | — | — | — |  |
| `WindowOptions` | Long | RW | type lib | — | — | — |  |
| `Caption` | String | RW | type lib | — | — | — |  |

<a id="panel-picklaunchapp"></a>
### PickLaunchApp

- CLSID `{1E2D8F16-3570-4335-B289-62A99B9A9515}` · interface `IPickLaunchApp`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Launch Application Pick Action

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `AppPath` | String | RW | type lib | — | — | — |  |
| `Arguments` | String | RW | type lib | — | — | — |  |
| `InitialDir` | String | RW | type lib | — | — | — |  |
| `CmdShow` | Long | RW | type lib | — | — | — |  |

<a id="panel-pickopenscreen"></a>
### PickOpenScreen

- CLSID `{E320B25B-D7FA-400B-BA7E-DDDA4D096AA8}` · interface `IPickOpenScreen`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Open Screen Pick Action

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ScreenName` | String | RW | type lib | — | — | — |  |
| `FrameName` | String | RW | type lib | — | — | — |  |
| `Zoom` | Long | RW | type lib | — | — | — |  |
| `Alignment` | EPanelAlignment | RW | type lib | — | — | — |  |
| `Scroll` | Boolean | RW | type lib | — | — | — |  |
| `Argument` | Variant | RW | type lib | — | — | — |  |
| `WindowOptions` | Long | RW | type lib | — | — | — |  |
| `Caption` | String | RW | type lib | — | — | — |  |
| `ScreenPosX` | String | RW | type lib | — | — | — |  |
| `ScreenPosY` | String | RW | type lib | — | — | — |  |
| `ScreenSizeX` | String | RW | type lib | — | — | — |  |
| `ScreenSizeY` | String | RW | type lib | — | — | — |  |
| `InternalSize` | Boolean | RW | type lib | — | — | — |  |

<a id="panel-pickprintreport"></a>
### PickPrintReport

- CLSID `{399725E8-F62F-4D88-926C-297E08359B9D}` · interface `IPickPrintReport`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Print Report Pick Action

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ReportName` | String | RW | type lib | — | — | — |  |
| `Output` | Long | RW | type lib | — | — | — |  |
| `ScreenPosX` | String | RW | type lib | — | — | — |  |
| `ScreenPosY` | String | RW | type lib | — | — | — |  |
| `ScreenSizeX` | String | RW | type lib | — | — | — |  |
| `ScreenSizeY` | String | RW | type lib | — | — | — |  |

<a id="panel-picksetvalue"></a>
### PickSetValue

- CLSID `{9614E20C-8A3F-4764-95F5-FB34D24E146F}` · interface `IPickSetValue`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Set Value Pick Action

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | — | — | — |  |
| `TagName` | String | RW | type lib | — | — | — |  |

<a id="panel-picktogglevalue"></a>
### PickToggleValue

- CLSID `{11185CE7-306A-4975-9D86-F2EFE7FB4B74}` · interface `IPickToggleValue`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Toggle Value Pick Action

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `TagName` | String | RW | type lib | — | — | — |  |
| `Value1` | Variant | RW | type lib | — | — | — |  |
| `Value2` | Variant | RW | type lib | — | — | — |  |

<a id="panel-powerexplorerobject"></a>
### PowerExplorerObject

- CLSID `{2550519A-29A7-4265-9DCB-3BA7901BE2E2}` · interface `IPowerExplorerObject`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- PowerExplorer Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ReadOnly` | Boolean | RW | type lib | — | — | — | True if Explorer dialog does not allow writing values |
| `Title` | String | RW | type lib | — | — | — | Returns/sets title of Explorer dialog |
| `ScreenObject` | Object | RW | type lib | — | — | — | Returns/sets the Screen object associated with Explorer |
| `DisplayBkColor` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets background color of displays in Explorer dialog |
| `IsOpened` | Boolean | R | type lib | — | — | — | True if Explorer dialog is opened |
| `CommandInterlockMode` | CommandInterlockModeConstants | RW | type lib | — | — | — | Returns/sets the commands interlock behavior |
| `ShowMeasurementTimestamp` | Boolean | RW | type lib | — | — | — | True if Explorer measurement tabs show timestamp column |
| `TabsEnabled` | Long | RW | type lib | — | — | — | Returns/sets the mask of visible tabs in Explorer |
| `ActiveTab` | String | RW | type lib | — | — | — | Returns/sets the active tab in Explorer |
| `CommandConfirm` | CommandConfirmationConstants | RW | type lib | — | — | — | Returns/sets if the command needs to be confirmed in Explorer |
| `SelectionColor` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets background color of selected displays in Explorer dialog |
| `SelectionColorInactive` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets background color of inactive selected displays in Explorer dialog |
| `AnalogInputMode` | AnalogInputModeConstants | RW | type lib | — | — | — | Returns/sets the analog measurements input behavior |
| `SortMode` | SortModeConstants | RW | type lib | — | — | — | Returns/sets the sort mode used in Explorer tabs |
| `ShowObjectHierarchy` | Boolean | RW | type lib | — | — | — | True if Explorer shows object hierarchy on the left |

**Métodos:** `Show()`; `Close()`; `SetWindowPlacement(PosX Variant, PosY Variant, SizeX Variant, SizeY Variant)`; `CenterWindow()`; `InsertScreenTab(TabName String, TabTitle String, ScreenPath String, Arg Variant)`; `RemoveScreenTab(TabName String)`; `GetScreenTabFrame(TabName String)`

<a id="panel-report"></a>
### Report

- CLSID `{A9C7CED3-49EA-4C4E-9205-23C2749D078E}` · interface `IReport`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Report Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Caption` | String | RW | type lib | — | — | — | Title of the report preview window |

**Métodos:** `Query()`; `PrintPreview(Left Variant, Top Variant, Width Variant, Height Variant)`; `Print()`; `Export(ExportFilter Variant, ExportFileName Variant)`; `GetExportFilter(FilterName String)`

<a id="panel-screen"></a>
### Screen

- CLSID `{DF17C782-A66D-11D3-8E89-525400E657A3}` · interface `IScreen` · eventos `DScreenEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 180 instâncias em 27 arquivo(s)
- Screen control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `FillStyle` | ScreenStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a fill style for a Screen. The available options for this property are described on the next table. Available options for the FillStyle property 0 - Solid Fill style is solid (default) 2 - Horizontal Fill style contains horizontal stripes 3 - Vertical Fill style contains vert… |
| `GradientStyle` | GradientStyleConstants | RW | type lib | — | não gravada nomeada | — | This property specifies a gradient fill style for a Screen. This property is only used when the FillStyle property is set to 8 (eight, Gradient). Gradients consider a color change as starting from the color configured in the ForegroundColor property and moving towards the color configured in the Bac… |
| `ForegroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | black (RGB(0, 0, 0)) | Specifies a Screen's foreground color. In scripts, use VBScript's RGB method to gather a color to associate to this property. The default value of this property is black (RGB(0, 0, 0)). Applications previous to the introduction of this property have this property and the BackgroundColor property set… |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | não gravada nomeada | gray (RGB(192, 192, 192)) | Specifies a Screen's background filling color. In scripts, use VBScript's RGB method to gather a color to associate to this property. The default value of this property is gray (RGB(192, 192, 192)). |
| `Caption` | String | RW | type lib | Caption | nomeada | — | This property defines the title of a Screen to display on Elipse E3 Viewer's title bar. |
| `PictureFile` | BSTRPICTURE | RW | type lib | PictureFile | nomeada | an empty String | Contains a picture's filename used as a Screen's background. It can be any format supported by Elipse E3 on DrawPicture objects (*.bmp, *.gif, *.jpg, *.cur, *.ico, *.emf, *.wmf, *.png, and *.tif). The default value of this property is an empty String. This property is only valid if the FillStyle pro… |
| `PicturePosition` | PicturePositionConstants | RW | type lib | PicturePosition | nomeada | — | Indicates the position of the selected picture on a Screen's PictureFile property. This property is only valid if the FillStyle property is set to 12 - Picture. The available options for this property are described on the next table. Available options for the PicturePosition property 0 - Center Pict… |
| `RenderQuality` | ERenderQuality | RW | type lib | RenderQuality | nomeada | — | Controls a Screen's drawing quality. Possible values for this property are the following: 0 - rqDefault: Screen's drawing quality uses the value defined in Viewer's RenderQuality property. This is the default value of this property, even in applications created on versions earlier than version 4.0 1… |
| `ScreenAlignment` | EPanelAlignment | RW | type lib | PanelAlignment (apelido confirmado) | nomeada | — | Controls the alignment of a Screen relative to the visible area. Possible values for this property are the following: 0 - paDefault: Adjusts the Screen to follow the value configured in Viewer's ScreenAlignment property. It corresponds to the Use Default option of a Screen's Alignment (This Screen) … |
| `AllowZoomChange` | EPropPermission | RW | type lib | ZoomChangePermission (apelido confirmado) | nomeada | True | This property enables displaying or not the options to change zoom level on a Screen's contextual menu. The default value of this property is True. |
| `AllowContextMenu` | EPropPermission | RW | type lib | ContextMenuPermission (apelido confirmado) | nomeada | True | If configured to True, this property enables displaying a Screen's contextual menu by right-clicking it at run time, except when a script is configured with a different information on the MouseDown or MouseUp events. Otherwise, this contextual menu is not displayed. The default value of this propert… |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_LayerCount` | UShort | RW | framework | _LayerCount | nomeada | — | Quantidade de camadas da tela |
| `_NewLayerZoom` | Double | RW | framework | _NewLayerZoom | nomeada | — | Zoom de nova camada |
| `HasGradStyle` | Boolean |  | gravada no .prj | HasGradStyle | nomeada | — | sem equivalente na type lib |

**Métodos:** `Close(Code Long)`; `ToPixelX(XHimetric Double)`; `ToPixelY(YHimetric Double)`; `FromPixelX(XPixel Long)`; `FromPixelY(YPixel Long)`

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, ShiftState Integer, MouseX OLE_XPOS_PIXELS, MouseY OLE_YPOS_PIXELS)`; `OnPreShow(Arg Variant)`; `OnShow()`; `OnHide()`

<a id="panel-sectiondetail"></a>
### SectionDetail

- CLSID `{3C7EEA24-2226-460B-A5A2-3064B2599EE1}` · interface `ISECTIONDETAIL`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONDETAIL

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `ColumnCount` | Long | RW | type lib | — | — | — | Gets/sets the number of columns in the report |
| `ColumnSpacing` | Single | RW | type lib | — | — | — | Gets/sets the space between columns in multi-column report |
| `NewColumn` | ReportNewPageColumn | RW | type lib | — | — | — | Gets/sets whether a new column should be started before and/or after printing the section |
| `NewPage` | ReportNewPageColumn | RW | type lib | — | — | — | Gets/sets whether a new page should be inserted before and/or after printing the section |
| `ColumnDirection` | ReportColumnDirection | RW | type lib | — | — | — | Gets/sets how to print the detail section in a multi-column report |
| `RepeatToFill` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section's formatting should print to fill the page when there is not enough data to fill it |
| `KeepTogether` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should be printed on a single page |

<a id="panel-sectiongroupfooter"></a>
### SectionGroupFooter

- CLSID `{96583020-D40F-401E-8795-79D1A3FEBF3E}` · interface `ISECTIONGROUPFOOTER`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONGROUPFOOTER

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `NewColumn` | ReportNewPageColumn | RW | type lib | — | — | — | Gets/sets whether a new column should be started before and/or after printing the section |
| `NewPage` | ReportNewPageColumn | RW | type lib | — | — | — | Gets/sets whether a new page should be inserted before and/or after printing the section |
| `KeepTogether` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should be printed on a single page |
| `PrintAtBottom` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should be printed at the bottom of the page immediatly before any page footer section |
| `ColumnLayout` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should use the same column layout as its detail section |

<a id="panel-sectiongroupheader"></a>
### SectionGroupHeader

- CLSID `{05BFB7FD-A62E-4485-8B52-8A954F004ADB}` · interface `ISECTIONGROUPHEADER`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONGROUPHEADER

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `NewColumn` | ReportNewPageColumn | RW | type lib | — | — | — | Gets/sets whether a new column should be started before and/or after printing the section |
| `NewPage` | ReportNewPageColumn | RW | type lib | — | — | — | Gets/sets whether a new page should be inserted before and/or after printing the section |
| `ColumnLayout` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should use the same columnlayout as its detail section |
| `KeepTogether` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should be printed on a single page |
| `ColumnGroupKeepTogether` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section and its footer will print as a single block on the same column |
| `GroupKeepTogether` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section and its footer will print as a single block on the same page |
| `UnderlayNext` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should print underneath the following section |
| `RepeatStyle` | ReportRepeatStyle | RW | type lib | — | — | — | Gets/sets whether the section should print underneath the following section |
| `DataField` | String | RW | type lib | — | — | — | Gets/sets the object Data Field |

<a id="panel-sectionpagefooter"></a>
### SectionPageFooter

- CLSID `{B0B36465-584A-44AE-B167-81061158991B}` · interface `ISECTIONPAGEFOOTER`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONPAGEFOOTER

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |

<a id="panel-sectionpageheader"></a>
### SectionPageHeader

- CLSID `{E6F842C6-D689-4700-9DF4-D817F499901E}` · interface `ISECTIONPAGEHEADER`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONPAGEHEADER

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |

<a id="panel-sectionreport"></a>
### SectionReport

- CLSID `{9409CC76-300B-44A2-8919-5311F6FA77F3}` · interface `ISectionReport`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReport

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `MaxPages` | Long | RW | type lib | — | — | 0 (zero), that is, no limit of pages | Established the maximum number of pages for a Section Report. When this number is reached, Elipse E3 stops processing a document. The default value of this property is 0 (zero), that is, no limit of pages. |
| `PrintWidth` | Single | RW | type lib | — | — | 6.5 inches | Determines the width of a Section Report's printing area, in inches. If a Section Report's size changes at run time, its printing width must also be adjusted, to ensure that this Section Report uses the whole printing area. The size of the printing area must also include the width of margins, so tha… |
| `Watermark` | BSTRPICTURE | RW | type lib | — | — | empty, that is, no text or image | Adds a background image, or a watermark, to a Section Report. Watermarks are texts or images displayed under a document's text. Usually, these texts or images turn a document visually more interesting. Example of a watermark The default value of this property is empty, that is, no text or image. |
| `WatermarkAlignment` | ReportPictureAlignment | RW | type lib | — | — | — | Determines the watermark's alignment in a Section Report. Possible values for this property are described on the next table. Available options for the WatermarkAlignment property 0 - rv2PicTopLeft Aligns the image to the top and left 1 - rv2PicTopRight Aligns the image to the top and right 2 - rv2Pi… |
| `WatermarkPrintOnPages` | String | RW | type lib | — | — | — | Indicates the number of pages of a Section Report that receive a watermark. The syntax used may include a single page, a range of pages, or even a combination of both, such as "1, 5-8, 9, 10-15". |
| `WatermarkSizeMode` | ReportSizeMode | RW | type lib | — | — | — | Configures the effect of a watermark's size on a page of a Section Report. Possible values for this property are described on the next table. 228 View Available options for the WatermarkSizeMode property 0 - rv2Clip Watermark is displayed on a Section Report in its original size 1 - rv2Stretch Water… |

<a id="panel-sectionreportbarcode"></a>
### SectionReportBarcode

- CLSID `{6A6F0B08-D59A-4DD4-88E5-6D4464609D28}` · interface `ISECTIONREPORTBARCODE`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- BARCODE

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Defines whether the background of this object is opaque or not. Possible values for this property are 0 - rv2Opaque: Opaque background or 1 - rv2Transparent: Transparent (default). |
| `DataField` | String | RW | type lib | — | — | an empty String | Configures or returns the data linked to a Bar Code. This linked data can be a field on a database table provided by a Query object, a mathematical expression with Query fields or a Tag or property from Elipse E3. In this case, the current value of the variable is shown when printing. The default va… |
| `Text` | String | RW | type lib | — | — | an empty String | Defines the text shown on a Bar Code. The default value of this property is an empty String. 236 View |
| `ForeColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the foreground color of the object |
| `Style` | ReportBarcodeStyle | RW | type lib | — | — | — | Determines the style of the bar code. Possible values for this property are described on the next table. Available options for the Style property 0 - rv2NoBarcode Default bar code style 1 - rv2Ansi39 ANSI 3 of 9 (Code 39) bar code style. Uses letters, numbers, -, *, $, /, +, and %, among others 2 - … |
| `BarHeight` | Single | RW | type lib | — | — | 0 (zero) | Indicates the height of a bar code, in inches. The default value of this property is 0 (zero). If a bar code's height exceeds the control's height, this property is ignored. |
| `CaptionGrouping` | Boolean | RW | type lib | — | — | — | Indicates whether spaces must be added between groups of characters on the legend of this control to turn large numbers easier to read. This property is only available on some bar code styles. |
| `CaptionPosition` | ReportBarcodeCaptionPosition | RW | type lib | — | — | — | Specifies the position of the text indicated in the Text property. Possible values for this property are 0 - rv2NoCaption: Text appears on the Bar Code (default), 1 - rv2Above: Text appears above the Bar Code, or 2 - rv2Below: Text appears below the Bar Code. |
| `NarrowBarWidth` | Single | RW | type lib | — | — | 0 (zero) | Indicates the width of the narrowest part of a bar code, in pixels. The default value of this property is 0 (zero). |
| `AutoSize` | Boolean | RW | type lib | — | — | — | Indicates whether a bar code automatically fits the size of this control (True, default) or does not fit the size of this control (False). |
| `CheckSumEnabled` | Boolean | RW | type lib | — | — | — | Enables (default) or disables reading the checksum value (character of a Bar Code). If this property is configured to False, only codes with checksum are affected. |
| `Alignment` | ReportBarcodeTextAlignment | RW | type lib | — | — | — | Determines the text alignment on a Bar Code. Possible values for this property are 0 - rv2Left: Text aligned to the left (default), 1 - rv2Center: Text aligned to center, 2 - rv2Right: Text aligned to the right, or 3 - rv2Justify: Justified alignment. |

<a id="panel-sectionreportcheckbox"></a>
### SectionReportCheckbox

- CLSID `{1767F42A-2794-4E41-9D6B-9EDF08414E2E}` · interface `ISECTIONREPORTCHECKBOX`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- CHECKBOX

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `Text` | String | RW | type lib | — | — | — | Defines the text shown on a Check Box. |
| `ForeColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the foreground color of the object |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Defines whether the background of this object is opaque or not. Possible values for this property are 0 - rv2Opaque: Opaque background or 1 - rv2Transparent: Transparent (default). |
| `WrapMode` | ReportObjWordWrap | RW | type lib | — | — | — | Defines the text wrap mode shown on a Check Box. Possible values for this property are 0 - rv2NoWrap: No text wrap, 1 - rv2WordWrap: Text wraps only on whole words (default), or 2 - rv2CharWrap: Text wraps only on characters. |
| `Font` | Font | RW | type lib | — | — | an empty String | This property determines the text font on the Check Box object. The default value of this property is an empty String. This property cannot be used in scripts or Links and it is configured only via Elipse E3 Studio. Please check topic Font for more information about this property's sub-properties. |
| `Checked` | Boolean | RW | type lib | — | — | — | Indicates whether this Check Box is selected or not. |
| `CheckAlignment` | ReportCheckboxAlignment | RW | type lib | — | — | — | Determines the positioning of the check box relative to the area of this object. Possible values for this property are 1- rv2TopLeft: Aligned top and left, 2 - rv2TopCenter: Aligned top and center, 4 - rv2TopRight: Aligned top and right, 16 - rv2MIddleLeft: Aligned top and left (default), 32 - rv2Mi… |

<a id="panel-sectionreportcontrolbase"></a>
### SectionReportControlBase

- CLSID `{7DBEBE71-C1A2-467E-A5D0-70F081AE0C1B}` · interface `ISectionReportControlBase`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReportControlBase

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |

<a id="panel-sectionreportexportfilter"></a>
### SectionReportExportFilter

- CLSID `{0873380F-A8CE-4BA2-B3EC-E8AF102082BD}` · interface `ISectionReportExportFilter`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReportExportFilter

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ExportFilterType` | ULong | R | type lib | — | — | — | Returns the type of export filter of a Section Report. This is a read-only property. Possible values for this property are Excel (Excel spreadsheet), HTML (File in HTML format), PDF (File in PDF format), RTF (File in RTF format), or Text (File in Text format). |

<a id="panel-sectionreportexportfilterexcel"></a>
### SectionReportExportFilterExcel

- CLSID `{DF8352BE-295A-4F3F-A5A6-648FBEE7A24E}` · interface `ISectionReportExportFilterExcel`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReportExportFilterExcel

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ExportFilterType` | ULong | R | type lib | — | — | — | Gets the export filter type |
| `WritePassword` | String | RW | type lib | — | — | — | Defines a password for writing to the exported Excel file. |
| `Password` | String | RW | type lib | — | — | — | Defines a password to open the exported Excel file. |
| `XLSFileFormat` | SectionReportExportXLSFormat | RW | type lib | — | — | — | Format of the file to export. Possible values for this property are 0 - rv2XLSFormat97Plus: Format used by Excel 97, with extension .xls, 1 - rv2XLSFormat95: Format used by Excel 95, with extension .xls, or 2 - rv2XLSFormatXLSX: Format used by Excel 2007 or later, with extension .xlsx (default). |
| `AutoRowHeight` | Boolean | RW | type lib | — | — | — | Calculate the height of rows (False, default) or let the height of rows to be automatically calculated by Excel (True). |
| `DisplayGridLines` | Boolean | RW | type lib | — | — | — | Defines whether grid lines must be displayed (True, default) or not (False) in Excel. |
| `MinColumnWidth` | Single | RW | type lib | — | — | 0.1 | Minimum width of columns, in inches. The default value of this property is 0.1. |
| `MinRowHeight` | Single | RW | type lib | — | — | 0.1 | Minimum height of rows, in inches. The default value of this property is 0.1. |
| `MultiSheet` | Boolean | RW | type lib | — | — | — | Defines whether a page per table must be exported (True) or all pages to a single table (False, default). |
| `TrimVerticalSpace` | Boolean | RW | type lib | — | — | — | Defines whether the vertical blank space must be removed (True) or not (False, default). |
| `CellMerging` | Boolean | RW | type lib | — | — | — | Defines whether cells must be merged (True) or not (False, default), when applicable. |

<a id="panel-sectionreportexportfilterhtml"></a>
### SectionReportExportFilterHTML

- CLSID `{6B7A279B-5764-406A-9101-2CE40601DA4F}` · interface `ISectionReportExportFilterHTML`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReportExportFilterHTML

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ExportFilterType` | ULong | R | type lib | — | — | — | Gets the export filter type |
| `Title` | String | RW | type lib | — | — | — | Defines the title of the HTML page. |
| `Multipage` | Boolean | RW | type lib | — | — | — | Defines whether a Section Report must be exported into several HTML pages (True) or into a single HTML page (False, default). |
| `TrimVerticalSpace` | Boolean | RW | type lib | — | — | — | Defines whether the vertical blank space must be removed (True) or not (False, default). |

<a id="panel-sectionreportexportfilterpdf"></a>
### SectionReportExportFilterPDF

- CLSID `{B76BEBC7-4148-4800-B888-4DBB8731F41E}` · interface `ISectionReportExportFilterPDF`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReportExportFilterPDF

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ExportFilterType` | ULong | R | type lib | — | — | — | Gets the export filter type |
| `OwnerPassword` | String | RW | type lib | — | — | — | Defines a password for the owner of the exported PDF file. |
| `UserPassword` | String | RW | type lib | — | — | — | Defines a password for a user of the exported PDF file. 226 View |
| `UserPermissions` | SectionReportExportPermissionsPDF | RW | type lib | — | — | that a user has all permissions, that is, the su… | Allows specifying permissions for a user of the exported PDF file. Possible values for this property are 0 - rv2PermissionNone: No permission, 4 - rv2PermissionPrint: Permission to only print a file, 8 - rv2PermissionModifyContents: Permission to change the content of a file, 16 - rv2PermissionCopy:… |

<a id="panel-sectionreportexportfiltertext"></a>
### SectionReportExportFilterText

- CLSID `{3847CF92-BC86-4439-8422-12E83521A36D}` · interface `ISectionReportExportFilterText`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReportExportFilterText

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ExportFilterType` | ULong | R | type lib | — | — | — | Gets the export filter type |
| `TextDelimiter` | String | RW | type lib | — | — | — | Defines a text as a separator of fields. |
| `TrimVerticalSpace` | Boolean | RW | type lib | — | — | — | Defines whether the vertical blank space must be removed (True) or not (False, default). |
| `PageDelimiter` | String | RW | type lib | — | — | — | Defines a text as a separator of pages. |

<a id="panel-sectionreportexportfilterword"></a>
### SectionReportExportFilterWord

- CLSID `{AABAF68E-88C7-4859-877C-8B4FCE8DCAA9}` · interface `ISectionReportExportFilterWord`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SectionReportExportFilterWord

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ExportFilterType` | ULong | R | type lib | — | — | — | Gets the export filter type |
| `Pagination` | Boolean | RW | type lib | — | — | — | Indicates whether the exported document must contain pagination (True, default) or not (False). |
| `EnableShapes` | Boolean | RW | type lib | — | — | — | Allows exporting (True) or not (False, default) lines and shapes in RTF (Rich Text Format) format. |

<a id="panel-sectionreportfield"></a>
### SectionReportField

- CLSID `{F0F153BD-6C56-4F2B-A502-D2AEC5000D12}` · interface `ISECTIONREPORTFIELD`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- FIELD

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `DataField` | String | RW | type lib | — | — | empty | Configures or returns the data linked to a Field object. This linked data can be a field on a database table provided by a Query object, a mathematical expression with Query fields or a Tag or property from Elipse E3. In this case, the current value of the variable is shown when printing. The defaul… |
| `Text` | String | RW | type lib | — | — | — | Defines the text shown on a Field. |
| `Alignment` | ReportObjTextAlignment | RW | type lib | — | — | — | Determines the text alignment on a Field. Possible values for this property are 0 - rv2Left: Text aligned to the left (default), 1 - rv2Center: Text aligned to center, 2 - rv2Right: Text aligned to the right, or 3 - rv2Justify: Justified alignment. |
| `CanGrow` | Boolean | RW | type lib | — | — | True | Indicates whether this object can increase its height based on its content. The default value of this property is True. |
| `CanShrink` | Boolean | RW | type lib | — | — | False | Indicates whether this object can shrink its height based on its content. The default value of this property is False. |
| `Multiline` | Boolean | RW | type lib | — | — | True | This property indicates whether the text of a Field contains multiple lines (True) or is a simple text box (False). This behavior can be viewed when an Elipse E3 Viewer is executing. The default value of this property is True. |
| `RightToLeft` | Boolean | RW | type lib | — | — | — | Indicates whether the text of a Field aligns from right to left (False, default) or from left to right (True). |
| `ShrinkToFit` | Boolean | RW | type lib | — | — | — | Indicates whether the text font of a Field can shrink to fit its content (False, default) or cannot shrink (True). |
| `VerticalText` | Boolean | RW | type lib | — | — | — | Indicates whether the text of a Field must be drawn vertically (True) or horizontally (False, default). |
| `VerticalAlignment` | ReportObjVertAlignment | RW | type lib | — | — | — | Determines the vertical alignment of a Field. Possible values for this property are 0 - rv2Top: Aligns by the top (default), 1 - rv2Middle: Aligns by the center, or 2 - rv2Bottom: Aligns by the bottom. |
| `WrapMode` | ReportObjWordWrap | RW | type lib | — | — | — | Defines the text wrap mode shown on a Field. Possible values for this property are 0 - rv2NoWrap: No text wrap, 1 - rv2WordWrap: Text wraps only on whole words (default), or 2 - rv2CharWrap: Text wraps only on characters. |
| `Font` | Font | RW | type lib | — | — | an empty String | This property determines the text font on the Field object. The default value of this property is an empty String. This property cannot be used in scripts or Links and it is configured only via Elipse E3 Studio. Please check topic Font for more information about this property's sub-properties. |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Defines whether the background of this object is opaque or not. Possible values for this property are 0 - rv2Opaque: Opaque background or 1 - rv2Transparent: Transparent (default). |
| `ForeColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the foreground color of the object |
| `SummaryFunc` | ReportSummaryFunc | RW | type lib | — | — | — | Determines the type of function used to process values from the field specified in the DataField, property, as listed on the next table. This property is only valid when the SummaryType property is different from 0 (zero). Available options for the SummaryFunc property 0 - rv2Sum Calculates the sum … |
| `SummaryRunning` | ReportSummaryRunning | RW | type lib | — | — | — | Determines whether a sum of accumulated total is performed. Possible values for this property are 0 - rv2NoSR: Does not perform a total calculation (default), 1 - rv2Group: Calculates accumulated totals for each specified interval of totals, or 2 - rv2All: Calculates the accumulated total for all va… |
| `SummaryType` | ReportSummaryType | RW | type lib | — | — | — | Determines the type or level of summary to generate. Possible values for this property are described on the next table. Available options for the SummaryType property 0 - rv2NoST Do not generate a summary (default) 1 - rv2GrandTotal Specifies that the whole content of a Section Report is summarized … |
| `SummaryGroup` | String | RW | type lib | — | — | — | This property is only valid when the SummaryType property is equal to 3 - SubTotal. This property indicates the name of a GroupHeader Section used to control subtotals, that is, at each change of value on the GroupHeader, the sum restarts. When this property is used, the CanShrink and CanGrow proper… |
| `DistinctField` | String | RW | type lib | — | — | — | Determines the name of the field used by the function selected in the SummaryFunc property. This property is only valid if the function defined in SummaryFunc is from the group of functions Distinct Summary, which covers functions from 9 (nine) to 15, and when the SummaryType property is different f… |
| `CountNullValues` | Boolean | RW | type lib | — | — | False | Determines whether null values must be included as 0 (zero) in sum fields. The default value of this property is False. |
| `Hyperlink` | String | RW | type lib | — | — | — | This property determines the link set to the text of a Field. |
| `CharacterSpacing` | Single | RW | type lib | — | — | 0 (zero) | Indicates the spacing between characters of this object, in points. The default value of this property is 0 (zero). 230 View |
| `LineSpacing` | Single | RW | type lib | — | — | 0 (zero) | Indicates the spacing between lines of this object, in points. The default value of this property is 0 (zero). |
| `OutputFormat` | BSTRFORMAT | RW | type lib | — | — | an empty String, that is, the value is displayed… | Configures the format used to display the value of a Field. The default value of this property is an empty String, that is, the value is displayed without formatting. |

<a id="panel-sectionreportfooter"></a>
### SectionReportFooter

- CLSID `{3456C3A5-AD79-4EFA-812D-F676B726FDEE}` · interface `ISECTIONREPORTFOOTER`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONREPORTFOOTER

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `KeepTogether` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should be printed on a single page |
| `PrintAtBottom` | Boolean | RW | type lib | — | — | — | Gets/sets whether the section should be printed at the bottom of the page immediatly before any page footer section |

<a id="panel-sectionreportheader"></a>
### SectionReportHeader

- CLSID `{6484D276-4AA2-476F-B13F-545D945F6E13}` · interface `ISECTIONREPORTHEADER`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONREPORTHEADER

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `NewPage` | ReportNewPageColumn | RW | type lib | — | — | — | Gets/sets whether a new page should be inserted before and/or after printing the section |

<a id="panel-sectionreportline"></a>
### SectionReportLine

- CLSID `{DF9EEB54-F748-4F78-951E-92674B453D47}` · interface `ISECTIONREPORTLINE`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- LINE

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `LineColor` | ECO_COLOR | RW | type lib | — | — | black (RGB(0, 0, 0)) | Specifies the line color of a Line object. The default value of this property is black (RGB(0, 0, 0)). |
| `LineWeight` | Single | RW | type lib | — | — | 1 (one) | Specifies the line width of a Line object. Configuring the width to 1 (one), the object's line expands up to 15 points. Configuring the width to 2 (two), line is expanded up to 30 points, and so on. The greater the number configured in this property, the greater the object's width. The default value… |
| `LineStyle` | ReportObjBorderStyle | RW | type lib | — | — | — | Determines the line style of a Line. Possible values for this property are described on the next table. Available options for the LineStyle property 0 - rv2NoBorder Line remains transparent 1 - rv2Solid Line appears solid (default) 2 - rv2Dashed Line appears dashed 3 - rv2Dot Line appears dotted 4 -… |
| `AnchorBottom` | Boolean | RW | type lib | — | — | — | Indicates whether a Line is anchored on the bottom of the Section containing it (True) or not (False, default). |

<a id="panel-sectionreportpagebreak"></a>
### SectionReportPagebreak

- CLSID `{F16AEE9D-5A21-44E6-BE27-C9C7B8E9AF43}` · interface `ISECTIONREPORTPAGEBREAK`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- PAGEBREAK

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Top` | Single | RW | type lib | — | — | — | Specifies the vertical position of a Page Break. |
| `Enabled` | Boolean | RW | type lib | — | — | — | Gets/sets whether the control is enabled |

<a id="panel-sectionreportpicture"></a>
### SectionReportPicture

- CLSID `{FC1E91F7-0F06-4A87-9D1B-BA853428F08F}` · interface `ISECTIONREPORTPICTURE`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- PICTURE

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `Image` | BSTRPICTURE | RW | type lib | — | — | an empty String | Specifies an image file for a Picture object. Allowed extensions are .bmp, .cur, .emf, .gif, .ico, .jpg, .png, .tif, or .wmf. The default value of this property is an empty String. |
| `PictureAlignment` | ReportPictureAlignment | RW | type lib | — | — | — | Determines the alignment of an image on a Picture. Possible values for this property are described on the next table. Available options for the PictureAlignment property 0 - rv2PicTopLeft Aligns the image to object's top left 1 - rv2PicTopRight Aligns the image to object's top right 2 - rv2PicCenter… |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Defines whether the background of this object is opaque or not. Possible values for this property are 0 - rv2Opaque: Opaque background or 1 - rv2Transparent: Transparent (default). |
| `LineColor` | ECO_COLOR | RW | type lib | — | — | white (RGB(255, 255, 255)) | Specifies the line color of a Picture object. The default value of this property is white (RGB(255, 255, 255)). |
| `LineWeight` | Single | RW | type lib | — | — | 0 (zero) | Specifies the line width of a Picture object. Configuring the width to 1 (one), the object's line expands up to 15 points. Configuring the width to 2 (two), line is expanded up to 30 points, and so on. The greater the number configured in this property, the greater the object's width. The default va… |
| `LineStyle` | ReportObjBorderStyle | RW | type lib | — | — | — | Determines the line style of a Picture. Possible values for this property are described on the next table. Available options for the LineStyle property 0 - rv2NoBorder Line remains transparent (default) 1 - rv2Solid Line appears solid 2 - rv2Dashed Line appears dashed 238 View 3 - rv2Dot Line appear… |
| `SizeMode` | ReportSizeMode | RW | type lib | — | — | — | Specifies the size of a Picture. Possible values for this property are described on the next table. Available options for the SizeMode property 0 - rv2Clip Shows a Picture in the current size (default) 1 - rv2Stretch Stretches a Picture according to its area 2 - rv2Zoom Sets the height or width of t… |

<a id="panel-sectionreportsectionbase"></a>
### SectionReportSectionBase

- CLSID `{3D37B4DB-040C-465D-BC8D-FD25988F502F}` · interface `ISECTIONREPORTSECTIONBASE`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SECTIONREPORTSECTIONBASE

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `CanGrow` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can increase size to fit content |
| `CanShrink` | Boolean | RW | type lib | — | — | — | Gets/sets whether object can shrink size to fit content |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Gets/sets the background opacity of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |

<a id="panel-sectionreportshape"></a>
### SectionReportShape

- CLSID `{0BB766D3-C78A-45CD-BCF6-630C2917F532}` · interface `ISECTIONREPORTSHAPE`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SHAPE

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `LineWeight` | Single | RW | type lib | — | — | 1 (one) | Specifies the line width of Ellipse, Rectangle, and Rounded Rectangle objects. Configuring the width to 1 (one), the object's line expands up to 15 points. Configuring the width to 2 (two), line is expanded up to 30 points, and so on. The greater the number configured in this property, the greater t… |
| `LineStyle` | ReportObjBorderStyle | RW | type lib | — | — | — | Determines the line style of Ellipse, Rectangle, and Rounded Rectangle objects. Possible values for this property are described on the next table. Available options for the LineStyle property 0 - rv2NoBorder Line remains transparent 1 - rv2Solid Line appears solid (default) 2 - rv2Dashed Line appear… |
| `Style` | ShapeStyle | RW | type lib | — | — | — | Determines which shape to draw. The available options for this property are described on the next table. Available options for the Style property 0 - rv2Rectangle Rectangle shape 1 - rv2Ellipse Elliptical or circular shape 2 - rv2RoundRect Rounded rectangle shape |
| `LineColor` | ECO_COLOR | RW | type lib | — | — | black (RGB(0, 0, 0)) | Specifies the line color of Elipse, Rectangle,and Rounded Rectangle objects. The default value of this property is black (RGB(0, 0, 0)). |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | white (RGB(255, 255, 255)) | Specifies the color used when the BackOpacity property is equal to 0 - rv2Opaque. The default value of this property is white (RGB(255, 255, 255)). |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Defines whether the background of this object is opaque or not. Possible values for this property are 0 - rv2Opaque: Opaque background or 1 - rv2Transparent: Transparent (default). |
| `RoundingRadius` | Single | RW | type lib | — | — | 10 (ten percent) | Specifies a radius for each corner of a Rounded Rectangle, as a percentage. The default value of this property is 10 (ten percent). |
| `BackColor2` | ECO_COLOR | RW | type lib | — | — | black (RGB(0, 0, 0)) | Specifies the color used when the BackOpacity2 is equal to 0 - rv2Opaque. The default value of this property is black (RGB(0, 0, 0)). |
| `BackOpacity2` | ReportObjBackOpacity | RW | type lib | — | — | — | Defines whether the background of this object is opaque or not. Possible values for this property are 0 - rv2Opaque: Opaque background or 1 - rv2Transparent: Transparent (default). |
| `BackgroundStyle` | ReportBackgroundStyle | RW | type lib | — | — | — | Determines the background style of Ellipse, Rectangle, and Rounded Rectangle objects. Possible values for this property are described on the next table. Available options for the BackgroundStyle property 0 - rv2BackSolid Solid background style, uses the color indicated in the BackColor property 1 - … |

<a id="panel-sectionreporttext"></a>
### SectionReportText

- CLSID `{C0EFF240-82DA-4001-A3E5-E230CB416E41}` · interface `ISECTIONREPORTTEXT`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- TEXT

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Gets/sets the name of the object |
| `Left` | Single | RW | type lib | — | — | — | Gets/sets the vertical position of the object |
| `Top` | Single | RW | type lib | — | — | — | Gets/sets the horizontal position of the object |
| `Height` | Single | RW | type lib | — | — | — | Gets/sets the height of the object |
| `Width` | Single | RW | type lib | — | — | — | Gets/sets the width of the object |
| `Visible` | Boolean | RW | type lib | — | — | — | Gets/sets whether object is visible |
| `Text` | String | RW | type lib | — | — | — | Defines the text shown on a Text. |
| `Alignment` | ReportObjTextAlignment | RW | type lib | — | — | — | Determines the text alignment on a Text. Possible values for this property are 0 - rv2Left: Text aligned to the left (default), 1 - rv2Center: Text aligned to center, 2 - rv2Right: Text aligned to the right, or 3 - rv2Justify: Justified alignment. |
| `Font` | Font | RW | type lib | — | — | an empty String | This property determines the text font on the Text object. The default value of this property is an empty String. This property cannot be used in scripts or Links and it is configured only via Elipse E3 Studio. Please check topic Font for more information about this property's sub-properties. |
| `VerticalAlignment` | ReportObjVertAlignment | RW | type lib | — | — | — | Determines the vertical alignment of a Text. Possible values for this property are 0 - rv2Top: Aligns by the top (default), 1 - rv2Middle: Aligns by the center, or 2 - rv2Bottom: Aligns by the bottom. |
| `Multiline` | Boolean | RW | type lib | — | — | True | This property indicates whether the text of a Text object contains multiple lines (True) or is a simple text box (False). This behavior can be viewed when an Elipse E3 Viewer is executing. The default value of this property is True. |
| `WrapMode` | ReportObjWordWrap | RW | type lib | — | — | — | Defines the text wrap mode shown on a Text. Possible values for this property are 0 - rv2NoWrap: No text wrap, 1 - rv2WordWrap: Text wraps only on whole words (default), or 2 - rv2CharWrap: Text wraps only on characters. |
| `BackColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the background color of the object |
| `ForeColor` | ECO_COLOR | RW | type lib | — | — | — | Gets/sets the foreground color of the object |
| `BackOpacity` | ReportObjBackOpacity | RW | type lib | — | — | — | Defines whether the background of this object is opaque or not. Possible values for this property are 0 - rv2Opaque: Opaque background or 1 - rv2Transparent: Transparent (default). |
| `Hyperlink` | String | RW | type lib | — | — | — | This property determines the link set to the text of a Text. |
| `CharacterSpacing` | Single | RW | type lib | — | — | 0 (zero) | Indicates the spacing between characters of this object, in points. The default value of this property is 0 (zero). 240 View |
| `LineSpacing` | Single | RW | type lib | — | — | 0 (zero) | Indicates the spacing between lines of this object, in points. The default value of this property is 0 (zero). |
| `Angle` | Long | RW | type lib | — | — | 0 (zero) | Indicates the inclination angle of a Text's text. The default value of this property is 0 (zero). |
| `RightToLeft` | Boolean | RW | type lib | — | — | — | Indicates whether the text of a Text aligns from right to left (False, default) or from left to right (True). |
| `ShrinkToFit` | Boolean | RW | type lib | — | — | — | Indicates whether the text font of a Text can shrink to fit its content (False, default) or cannot shrink (True). |

<a id="panel-timertag"></a>
### TimerTag

- CLSID `{700E51D7-70A1-4FD1-ADFF-99B1118D6FBB}` · interface `ITimerTag` · eventos `DTimerTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 7 instâncias em 4 arquivo(s)
- TimerTag class

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Enabled` | Boolean | RW | type lib | Enabled | nomeada | True | Enables or disables the Timer Tag. The default value of this property is True. |
| `TriggerType` | TriggerTypeFlags | RW | type lib | TriggerType | nomeada | — | This is the Timer Tag's trigger type. Possible values for this property are described on the next table. Available options for the TriggerType property 0 - ttSingle Single trigger 1 - ttContinuous Continuous trigger (default) 2 - ttDaily Daily-based trigger 3 - ttMonthly Monthly-based trigger |
| `StartTime` | Date | RW | type lib | StartTime | nomeada | the local date | Initial Timer Tag's date and time. For the TriggerType property with value 0 - ttSingle, this is the triggering date and time itself. For other values, it is the moment when the Timer Tag triggers. The default value of this property is the local date and time. 300 Server Objects |
| `RepeatInterval` | Date | RW | type lib | RepeatInterval | nomeada | — | This property indicates a time interval for the repetition of an action. This property is only available if the TriggerType property is set to value 1 - ttContinuous. Possible values for this property are in the range between 00:00:01 (one second, default value) and 23:59:59. |
| `NextExecTime` | Date | R | type lib | — | não gravada nomeada | — | Displays the next triggering time. This is a read-only property. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Eventos:** `OnPreset()`

<a id="panel-trendanalysisobject"></a>
### TrendAnalysisObject

- CLSID `{CE4B1099-2770-47FE-BE50-FC6656054ED8}` · interface `ITrendAnalysisObject`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- TrendAnalysis Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Title` | String | R | type lib | — | — | — | Returns the title of a TrendAnalysis window. This is a read-only property. CHAPTER |
| `IsOpened` | Boolean | R | type lib | — | — | — | Informs whether there is an open TrendAnalysis window or not. This is a read-only property. |

**Métodos:** `Show()`; `Close()`; `SetWindowPlacement(PosX Variant, PosY Variant, SizeX Variant, SizeY Variant)`; `CenterWindow()`; `Load(Configuration String, ConfigStatus Variant, ErrorDetails Variant)`; `Save()`; `AddDisplay(Title String, DisplayPosition TrendAnalysisDisplayPosition)`; `AddPlotArea()`; `AddPen(PenPath String, ErrorDetails Variant)`

<a id="panel-viewer"></a>
### Viewer

- CLSID `{CBC51E2B-1DA5-4D6A-A284-D63B7C3FA537}` · interface `IViewer` · eventos `DViewerEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 1 instâncias em 1 arquivo(s)
- Viewer Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ProductVersionMajor` | Long | R | type lib | — | não gravada nomeada | — | This property returns the major number of the installed version of Elipse E3 Viewer. For example, if the installed version is 6.9.312, this property returns the value 6. This is a read-only property. |
| `ProductVersionMinor` | Long | R | type lib | — | não gravada nomeada | — | This method returns the minor number of the installed version of Elipse E3 Viewer. For example, if the installed version is 6.9.312, this property returns the value 9. This is a read-only property. |
| `ProductVersionBuild` | Long | R | type lib | — | não gravada nomeada | — | This property returns the build number of the installed version of Elipse E3 Viewer. For example, if the installed version is 6.9.312, this property returns the value 312. This is a read-only property. 76 View |
| `ProductString` | String | R | type lib | — | não gravada nomeada | — | This property returns a String containing the product's name and the installed version of Elipse E3 Viewer, such as "Elipse E3 6.9.312". This is a read-only property. Notice that an Elipse E3 Viewer can access an object in a Server and retrieve this property of that Server, according to the next exa… |
| `Caption` | String | RW | type lib | Caption | nomeada | an empty String | Determines the name of the application that is using Elipse E3 Viewer. The default value of this property is an empty String. |
| `InitialScreen` | BSTRSPLITLINK | RW | type lib | InitialScreen | nomeada | "InitialScreen" | Indicates an initial Screen or Frame to display when Elipse E3 Viewer is opened. By using the WindowStyle property, users can determine whether this window must start maximized, windowed, or minimized. The default value of this property is "InitialScreen". To use this property in scripts, please che… |
| `User` | String | R | type lib | — | não gravada nomeada | — | Contains the name of the user currently using Elipse E3 Viewer. This is a read-only property. |
| `IsReadOnly` | Boolean | R | type lib | — | não gravada nomeada | — | If set to True, indicates that Elipse E3 Viewer is in Read-Only mode (restricted access). This is a read-only property. |
| `WindowStyle` | WindowStyleConstants | RW | type lib | WindowStyle | nomeada | — | Defines an initial style for Elipse E3 Viewer's window. Possible values for this property are 0 - Maximized: Elipse E3 Viewer starts maximized (default), 1 - Windowed: Elipse E3 Viewer starts windowed, or 2 - Minimized: Elipse E3 Viewer starts minimized. |
| `WindowWidth` | Long | RW | type lib | WindowWidth | nomeada | 400 | Determines the width of Elipse E3 Viewer's window, in pixels. The default value of this property is 400. |
| `WindowHeight` | Long | RW | type lib | WindowHeight | nomeada | 300 | Determines the height of Elipse E3 Viewer's window, in pixels. The default value of this property is 300. |
| `CenterWindow` | Boolean | RW | type lib | CenterWindow | nomeada | True | When enabled, determines that Viewer's window must start centered. Otherwise, default settings are used. The default value of this property is True. |
| `TitleBar` | Boolean | RW | type lib | TitleBar | nomeada | True | If this property is enabled, Elipse E3 Viewer's title bar is displayed, according to the Caption property. Otherwise, it is hidden. The default value of this property is True. |
| `MinimizeButton` | Boolean | RW | type lib | MinimizeButton | nomeada | True | If this property is set to True, a Minimize button is enabled on Elipse E3 Viewer and this button can be used. Otherwise, this button does not display on that window. The default value of this property is True. |
| `MaximizeButton` | Boolean | RW | type lib | MaximizeButton | nomeada | True | If this property is set to True, a Maximize button is enabled on Elipse E3 Viewer and this button can be used. Otherwise, this button does not display on that window. The default value of this property is True. |
| `CloseButton` | Boolean | RW | type lib | CloseButton | nomeada | True | If this option is set to True, a Close button is enabled on Viewer, and it can be used. Otherwise, this button does not display on its window. The default value of this property is True. |
| `CacheEnable` | Boolean | RW | type lib | CacheEnable | nomeada | — | Keeps in memory all Screens already opened and instantiated on an Elipse E3 Viewer, allowing a quick switching among them. If this property is enabled, then Screen's cache is also enabled. |
| `DisableTaskSwitching` | Boolean | RW | type lib | DisableTaskSwitching | nomeada | False | If it is set to True, disables window switching on Elipse E3 Viewer. Otherwise, window switching is enabled. The default value of this property is False. This property can be changed at run time by using the SetDisableTaskSwitching method. |
| `EnableInactivity` | Boolean | RW | type lib | EnableInactivity | nomeada | False | Enables or disables checking user's inactivity period. For more information, please check Viewer's OnInactive event. The default value of this property is False. This property cannot be changed while this object is active. |
| `InactivityTime` | Long | RW | type lib | InactivityTime | nomeada | 5 (five) minutes | Defines a maximum waiting time for a mouse or keyboard event before an inactivity period, in minutes. For more information, please check Viewer's OnInactive event. The default value of this property is 5 (five) minutes. The next code contains a usage example of this property. Sub CommandButton3_Clic… |
| `EnableCommError` | Boolean | RW | type lib | EnableCommError | nomeada | True | Enables or disables viewing communication errors. For example, if there is a SetPoint on a Screen that is linked to an I/O Tag, and communication between Elipse E3 and this Tag fails, the text configured in the CommErrorText property is displayed in that SetPoint, with a color configured in the Comm… |
| `CommErrorText` | String | RW | type lib | CommErrorText | nomeada | "???" | Property used to define an alert message when a Link or Connection fails. The default value of this property is "???". Please check the EnableCommError property for more information. This property cannot be changed at run time, even if Elipse E3 Viewer is inactive. |
| `CommErrorTextColor` | ECO_COLOR | RW | type lib | CommErrorTextColor | nomeada | yellow (RGB(255, 255, 0)) | Property used to define a text color for a SetPoint when a Link or Connection fails. The default value of this property is yellow (RGB(255, 255, 0)). Please check the EnableCommError property for more information. This property cannot be changed at run time, even if Elipse E3 Viewer is inactive. |
| `CommErrorBkColor` | ECO_COLOR | RW | type lib | CommErrorBkColor | nomeada | red (RGB(255, 0, 0)) | Property used to define a background color for a SetPoint when a Link or Connection fails. The default value of this property is red (RGB(255, 0, 0)). Please check the EnableCommError property for more information. This property 74 View cannot be changed at run time, even if Elipse E3 Viewer is inac… |
| `ReconnectDialogDelaySec` | Long | RW | type lib | ReconnectDialogDelaySec | nomeada | — | Indicates the number of seconds that an Elipse E3 Viewer waits during a possible reconnection to a server, before displaying a message warning users about this action (this property does not affect the first connection). If it is equal to 0 (zero), a reconnection message is always displayed. To avoi… |
| `EnableHeartbeat` | Boolean | RW | type lib | EnableHeartbeat | nomeada | False | Enables or disables sending a heartbeat message (sent at fixed intervals, which indicates that the server is active) between an Elipse E3 Viewer and a server. In case Elipse E3 Viewer stops receiving heartbeat messages, this means that a problem occurred, therefore connection must be aborted. The de… |
| `HeartbeatPeriodMs` | Long | RW | type lib | HeartbeatPeriodMs | nomeada | 2000 (two seconds) | Indicates an interval, in milliseconds, between heartbeat messages sent by a Server. A heartbeat message is always sent when a server remains a period indicated by this property without sending messages for an Elipse E3 Viewer. The default value of this property is 2000 (two seconds). |
| `HeartbeatTimeoutMs` | Long | RW | type lib | HeartbeatTimeoutMs | nomeada | 5000 (five seconds) | Indicates a time, in milliseconds, that an Elipse E3 Viewer waits without receiving messages from a Server. If this time passes and no message is received, Elipse E3 Viewer assumes that connection was lost and starts the reconnection process. This time must be greater than the time set in the Heartb… |
| `LoginRetries` | Long | RW | type lib | LoginRetries | nomeada | 2 (two) | Specifies the number of Elipse E3 Viewer's login retries, that is, how many times the login dialog box is displayed besides the first time. The default value of this property is 2 (two). |
| `BlinkTime` | Long | RW | type lib | BlinkTime | nomeada | 200 ms | Defines a time, in milliseconds, between each status change when an object must blink, that is, each time an object has a Link and the Blink option is selected. The default value of this property is 200 ms. The minimum time to refresh a Screen is 55 ms. Therefore, if this property is set with a time… |
| `Params[ParamName String]` | String | R | type lib | — | não gravada nomeada | — | This property is a vector of key-value pairs, which returns parameters passed to Elipse E3 Viewer through the - params command prompt option. All values are returned as Strings. For example, if Elipse E3 Viewer's command prompt contains the following parameters: Viewer -params Language=ENU Users can… ⚠ type lib: somente leitura |
| `TargetResolutionX` | Long | RW | type lib | TargetResolutionX | nomeada | -1 (minus one), | Defines Screen's horizontal resolution for which this application is designed to, in pixels. The default value of this property is -1 (minus one), which assumes the current computer's resolution. This property cannot be changed at run time, even if Elipse E3 Viewer is inactive. |
| `TargetResolutionY` | Long | RW | type lib | TargetResolutionY | nomeada | -1 (minus one), | Defines Screen's vertical resolution for which this application is designed to, in pixels. The default value of this property is -1 (minus one), which assumes the current computer's resolution. This property cannot be changed at run time, even if Elipse E3 Viewer is inactive. |
| `TargetMarginX` | Long | RW | type lib | TargetMarginX | nomeada | -1 (minus one), | Defines the number of pixels that must be discounted from Screen's horizontal resolution (Elipse E3 Viewer's working area). The default value of this property is -1 (minus one), which assumes Elipse E3 Viewer's window configuration (with or without a title bar, with or without a border) together wit… |
| `TargetMarginY` | Long | RW | type lib | TargetMarginY | nomeada | -1 (minus one), | Defines the number of pixels that must be discounted from Screen's vertical resolution (Elipse E3 Viewer's working area). The default value of this property is -1 (minus one), which assumes Elipse E3 Viewer's window configuration (with or without a title bar, with or without a border) together with … |
| `TargetDPIX` | Long | RW | type lib | TargetDPIX | nomeada | -1 (minus one), | Defines a dots-per-inch value, horizontally, of the destination computer's monitor. The default value of this property is -1 (minus one), which means that the current computer's value is assumed. This property cannot be changed at run time, even if Elipse E3 Viewer is inactive. |
| `TargetDPIY` | Long | RW | type lib | TargetDPIY | nomeada | -1 (minus one), | Defines a dots-per-inch value, vertically, of the destination computer's monitor. The default value of this property is -1 (minus one), which means that the current computer's value is assumed. This property cannot be changed at run time, even if Elipse E3 Viewer is inactive. |
| `ShowKeyPadOnEdit` | Boolean | RW | type lib | ShowKeyPadOnEdit | nomeada | — | This property automatically enables displaying Elipse KeyPad, whenever a Screen object that allows edition receives the focus. |
| `WindowBorder` | Boolean | RW | type lib | WindowBorder | nomeada | True | Enables or disables a border around Elipse E3 Viewer's window. The default value of this property is True. This is a read-write property, but changing its value at run time does not change settings for an already opened Elipse E3 Viewer, only for windows opened using Elipse E3 Viewer's settings. |
| `WindowResizable` | Boolean | RW | type lib | WindowResizable | nomeada | True | Indicates whether a window can be resized. This property is effective only if the WindowBorder property is set to True. The default value of this property is True. This is a read-write property, but changing its value at run time does not change settings for an already opened Elipse E3 Viewer, only … |
| `WindowMovable` | Boolean | RW | type lib | WindowMovable | nomeada | True | Indicates whether this window can be moved. The default value of this property is True. This is a read-write property, but changing its value at run time does not change settings for an already opened Elipse E3 Viewer, only for windows opened using Elipse E3 Viewer's settings. 80 View |
| `WindowStayOnTop` | Boolean | RW | type lib | WindowStayOnTop | nomeada | False | Indicates whether Elipse E3 Viewer's window must always be on top of other windows. The default value of this property is False. This is a read-write property, but changing its value at run time does not change settings for an already opened Elipse E3 Viewer, only for windows opened using Elipse E3 … |
| `WindowSmallTitle` | Boolean | RW | type lib | WindowSmallTitle | nomeada | False | Indicates whether Elipse E3 Viewer's window must have a small title bar. This property is effective only if the TitleBar property is True. The default value of this property is False. This is a read-write property, but changing its value at run time does not change settings for an already opened Eli… |
| `ViewerLanguageId` | Long | R | type lib | — | não gravada nomeada | — | Returns the current Elipse E3 Viewer's language code. Possible values for this property are described on the next table. This is a read-only property. Available values for the ViewerLanguageId property DECIMAL HEXADECIMAL LANGUAGE 4 0x0004 Chinese Simplified 1031 0x0407 German 1033 0x0409 English (U… |
| `RenderQuality` | ERenderQuality | RW | type lib | RenderQuality | nomeada | — | Controls the drawing quality of all Screens, only if the value of RenderQuality property of all Screens is equal to 0 - rqDefault. Possible values for this property are: 0 - rqDefault: Uses the normal quality mode, GDI (Graphics Device Interface). Corresponds to the Use Default item on Viewer's Qual… |
| `AllowZoomChange` | Boolean | RW | type lib | ZoomChangePermission (apelido confirmado) | nomeada | True | This property enables displaying or not the options to change zoom levels on Screen's contextual menu. The default value of this property is True. |
| `AllowContextMenu` | Boolean | RW | type lib | — | não gravada nomeada | True | If configured to True, this property enables displaying Screen's contextual menu by right-clicking them at run time, except when a script is configured with a different information on the MouseDown or MouseUp events. Otherwise, the contextual menu is not displayed. The default value of this property… |
| `ScreenAlignment` | EPanelAlignment | RW | type lib | PanelAlignment (apelido confirmado) | nomeada | — | Controls the alignment, given by Elipse E3 Viewer, of all Screens that do not specify a value different from default. Possible values for this property are: 1 - paTopLeft: Adjusts the Screen to the top left corner relative to the visible area. It corresponds to the Force Top/Left option of a Screen'… |
| `IsWebView2Enabled` | Boolean | R | type lib | — | não gravada nomeada | — | Indicates whether using Microsoft Edge's WebView2 control is enabled or not as the rendering engine to display Internet content. This is a read-only property. |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `EnableZoomMenu` | Byte |  | gravada no .prj | EnableZoomMenu | nomeada | — | sem equivalente na type lib |
| `FrameChildExist` | Byte |  | gravada no .prj | FrameChildExist | nomeada | — | sem equivalente na type lib |
| `HideKeyPadOnEnter` | Byte |  | gravada no .prj | HideKeyPadOnEnter | nomeada | — | sem equivalente na type lib |
| `HideKeyPadOnEsc` | Byte |  | gravada no .prj | HideKeyPadOnEsc | nomeada | — | sem equivalente na type lib |

**Métodos:** `GetObject(ObjectPath String)`; `Trace(MessageText String, LogTimeStamp Boolean, BreakLine Boolean)`; `GetFrame(FrameName Variant, CreateNew Boolean)`; `SelectMenu(Menu String, Left Variant, Top Variant)`; `DoModal(Screen String, Title Variant, Left Variant, Top Variant, Width Variant, Height Variant, Arg Variant, Flags Long)`; `SetValue(TagName String, NewVal Variant)`; `GetValue(TagName String)`; `ToggleValue(TagName String, ValA Variant, ValB Variant)`; `LoadFormulaDlg(FormulaName String, UnitName Variant, ValueName Variant)`; `LoadFormulaValues(FormulaName String, UnitName String, ValueName String)`; `LoadFormulaValuesQuiet(FormulaName String, UnitName String, ValueName String)`; `GetFormulaUnitDataObj(FormulaName String)`; `GetFormulaValueDataObj(FormulaName String)`; `Exit()`; `Playsound(Filename String)`; `Stopsound()`; `ExecuteExternalApp(AppPath String, Arguments String, InitialDir String, CmdShow Long, ProcessId Variant)`; `IsAppRunning(ProcessId Long)`; `IsUserMemberOfGroup(GroupName String, UserName String)`; `GetFullUserName()`; `IsWebViewer()`; `Login(Mode Boolean, PosX Variant, PosY Variant, WindowsShowLastCredentials Boolean)`; `LoginUser(UserName String, UserPassword String, OpStatus Variant, WarnDaysToExpire Variant)`; `LoginWindowsUser(UserName String, UserPassword String, OpStatus Variant)`; `Logout(Mode Boolean)`; `PasswordConfirm(Mode Boolean, PosX Variant, PosY Variant)`; `ChangePassword(PosX Variant, PosY Variant)`; `ChangeUserPassword(UserName String, PasswordOld String, PasswordNew String, OpStatus Variant)`; `UserAdministration(PosX Variant, PosY Variant, ShowMergeErrorsOnExit Boolean, MergeDetails Variant)`; `LoadReport(ReportName String)`; `CaptureScreen(Filename String)`; `ShowFilePicker(Open Boolean, Filename Variant, Extension String, Flags Long, Filter String)`; `ShowDatePicker(DateValue Variant, Left Variant, Top Variant, DefaultDate Variant)`; `ShowPickColor(ColorValue Variant, Color Int, Left Variant, Top Variant)`; `TrackEvent(EventMessage String, Comment String, EventTimestamp Date)`; `ESign(ObjName String, Description Variant, Action String, From Variant, To Variant, User Variant, Comment Variant)`; `GetMouseX()`; `GetMouseY()`; `GetKeyPad()`; `ShowTrendAnalysis(Title String, Left Variant, Top Variant, Configuration String, ConfigStatus Variant, ErrorDetails Variant)`; `GetTrendAnalysis(Title String)`; `GetScreen(ScreenName String)`

**Eventos:** `OnLogin()`; `OnLogout()`; `OnInactive()`

<a id="panel-viewerfolder"></a>
### ViewerFolder

- CLSID `{BB53DC74-3C61-4040-A517-16823E17695B}` · interface `IViewerFolder`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 6 instâncias em 1 arquivo(s)
- ViewerFolder Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

<a id="panel-waterexplorerobject"></a>
### WaterExplorerObject

- CLSID `{55DBA82E-E041-483F-9A03-7F02F157F497}` · interface `IWaterExplorerObject`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- WaterExplorer Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ReadOnly` | Boolean | RW | type lib | — | — | — | True if Explorer dialog does not allow writing values |
| `Title` | String | RW | type lib | — | — | — | Returns/sets title of Explorer dialog |
| `ScreenObject` | Object | RW | type lib | — | — | — | Returns/sets the Screen object associated with Explorer |
| `DisplayBkColor` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets background color of displays in Explorer dialog |
| `IsOpened` | Boolean | R | type lib | — | — | — | True if Explorer dialog is opened |
| `CommandInterlockMode` | CommandInterlockModeConstants | RW | type lib | — | — | — | Returns/sets the commands interlock behavior |
| `ShowMeasurementTimestamp` | Boolean | RW | type lib | — | — | — | True if Explorer measurement tabs show timestamp column |
| `TabsEnabled` | Long | RW | type lib | — | — | — | Returns/sets the mask of visible tabs in Explorer |
| `ActiveTab` | String | RW | type lib | — | — | — | Returns/sets the active tab in Explorer |
| `CommandConfirm` | CommandConfirmationConstants | RW | type lib | — | — | — | Returns/sets if the command needs to be confirmed in Explorer |
| `SelectionColor` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets background color of selected displays in Explorer dialog |
| `SelectionColorInactive` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets background color of inactive selected displays in Explorer dialog |
| `AnalogInputMode` | AnalogInputModeConstants | RW | type lib | — | — | — | Returns/sets the analog measurements input behavior |
| `SortMode` | SortModeConstants | RW | type lib | — | — | — | Returns/sets the sort mode used in Explorer tabs |
| `ShowObjectHierarchy` | Boolean | RW | type lib | — | — | — | True if Explorer shows object hierarchy on the left |

**Métodos:** `Show()`; `Close()`; `SetWindowPlacement(PosX Variant, PosY Variant, SizeX Variant, SizeY Variant)`; `CenterWindow()`; `InsertScreenTab(TabName String, TabTitle String, ScreenPath String, Arg Variant)`; `RemoveScreenTab(TabName String)`; `GetScreenTabFrame(TabName String)`

<a id="panel-xcoclass"></a>
### XCoClass

- CLSID `{370A3C85-93AD-4E41-98CA-1FDD82424C18}` · interface `IXCoClass`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 226 instâncias em 10 arquivo(s)
- CoClass Declaration Aggregate

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Methods` | String |  | gravada no .prj | Methods | nomeada | — | sem equivalente na type lib |

**Métodos:** `Methods()`

<a id="panel-xcontrol"></a>
### XControl

- CLSID `{93F1CB22-52A7-11D4-8E8A-525400E657A3}` · interface `IXControl` · eventos `DElipseXEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 127 instâncias em 3 arquivo(s)
- XControl control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `CustomConfigText` | String | RW | type lib | CustomConfig (apelido confirmado) | nomeada | — |  |
| `FriendlyName` | String | RW | type lib | FriendlyName | nomeada | — |  |
| `InstanceName` | String | RW | type lib | InstanceName | nomeada | — |  |
| `Contexts` | String | RW | type lib | Contexts | nomeada | — |  |
| `IconPath` | BSTRPICTURE | RW | type lib | IconPath | nomeada | — |  |
| `EnableTagBehavior` | Boolean | RW | type lib | EnableTagBehavior | nomeada | — |  |
| `ValueMode` | EValueMode | RW | type lib | ValueMode | nomeada | — |  |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_CLSID` | String |  | gravada no .prj | _CLSID | nomeada | — | sem equivalente na type lib |
| `_EVENTIID` | String |  | gravada no .prj | _EVENTIID | nomeada | — | sem equivalente na type lib |
| `_IID` | String |  | gravada no .prj | _IID | nomeada | — | sem equivalente na type lib |
| `ConnectionInfoCount` | ULong |  | gravada no .prj | ConnectionInfoCount | nomeada | — | sem equivalente na type lib |
| `SlotRef_#_IsAnchorPoint` | Boolean |  | gravada no .prj | SlotRef_#_IsAnchorPoint | nomeada | — | sem equivalente na type lib (família: 6) |
| `SlotRef_#_PlugName` | String |  | gravada no .prj | SlotRef_#_PlugName | nomeada | — | sem equivalente na type lib (família: 6) |
| `SlotRef_#_SlotId` | String |  | gravada no .prj | SlotRef_#_SlotId | nomeada | — | sem equivalente na type lib (família: 6) |
| `SlotRef_#_SlotName` | String |  | gravada no .prj | SlotRef_#_SlotName | nomeada | — | sem equivalente na type lib (família: 6) |
| `SlotRef_#_XPosition` | Double |  | gravada no .prj | SlotRef_#_XPosition | nomeada | — | sem equivalente na type lib (família: 6) |
| `SlotRef_#_YPosition` | Double |  | gravada no .prj | SlotRef_#_YPosition | nomeada | — | sem equivalente na type lib (família: 6) |

**Eventos:** `Constructor()`; `CustomConfig()`

<a id="panel-xfolder"></a>
### XFolder

- CLSID `{9549A4AE-0BB5-46EF-B042-BDDAB2D791AF}` · interface `IXFolder` · eventos `DElipseXEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 68 instâncias em 3 arquivo(s)
- XFolder Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `CustomConfigText` | String | RW | type lib | CustomConfig (apelido confirmado) | nomeada | — |  |
| `FriendlyName` | String | RW | type lib | FriendlyName | nomeada | — |  |
| `InstanceName` | String | RW | type lib | InstanceName | nomeada | — |  |
| `Contexts` | String | RW | type lib | Contexts | nomeada | — |  |
| `IconPath` | BSTRPICTURE | RW | type lib | IconPath | nomeada | — |  |
| `DefaultIsAlarmArea` | Boolean | RW | type lib | DefaultIsAlarmArea | nomeada | — |  |
| `EnableTagBehavior` | Boolean | RW | type lib | EnableTagBehavior | nomeada | — |  |
| `ValueMode` | EValueMode | RW | type lib | ValueMode | nomeada | — |  |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_CLSID` | String |  | gravada no .prj | _CLSID | nomeada | — | sem equivalente na type lib |
| `_EVENTIID` | String |  | gravada no .prj | _EVENTIID | nomeada | — | sem equivalente na type lib |
| `_IID` | String |  | gravada no .prj | _IID | nomeada | — | sem equivalente na type lib |

**Eventos:** `Constructor()`; `CustomConfig()`

<a id="panel-xinterface"></a>
### XInterface

- CLSID `{370A3C88-93AD-4E41-98CA-1FDD82424C18}` · interface `IXInterface`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Interface Object

<a id="panel-xmethod"></a>
### XMethod

- CLSID `{370A3C8B-93AD-4E41-98CA-1FDD82424C18}` · interface `IXMethod` · eventos `DXMethodEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Method Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `HelpString` | String | RW | type lib | — | — | an empty String | Text containing the Property Definition's description. This text is displayed at the bottom of the Property List in Elipse E3 Studio when the Property Definition is selected. The default value of this property is an empty String. |
| `Public` | Boolean | RW | type lib | — | — | True | When a Property Definition is public (True), it is visible outside the Library. Otherwise, the Property Definition is internal and only visible to the object. The default value of this property is True. A public Property Definition is represented by the icon . |
| `Type` | String | RW | type lib | — | — | — | Determines the type of values accepted by a Property Definition, such as Boolean, Double, Integer, or Variant, among others. When specifying an object as a type, such as DemoTag, IOTag, or XObject, among others, this property has the following behavior: In case the ElipseX is inactive: This property… |
| `DefaultValue` | Variant | RW | type lib | — | — | empty | Defines an initial value for a Property Definition when a new instance of the object is created. If the Property Definition is configured as retentive, then it is initialized with this value every time the object is loaded. The default value of this property is empty. |
| `Retentive` | Boolean | RW | type lib | — | — | — | Indicates whether the current Property Definition's value at run time is persisted in the Domain file (True), while the Domain is loaded. A retentive Property Definition is represented by the icon . Retentive Property Definitions have the following behavior: Propagate their value to the Standby serv… |
| `Persistable` | Boolean | RW | type lib | — | — | True | Indicates whether a Property Definition is saved in the project file (True) or it is available only at run time (False). The default value of this property is True. If this property is configured as False, the Property Definition cannot be edited in Elipse E3 Studio anymore, saved, nor read from the… |
| `ExposableToOpc` | EExposableToOpc | RW | type lib | — | — | — | Indicates how a Property Definition is exposed on an OPC UA Server. Possible values for this property are 0 - eDontExpose: This Property Definition is not exposed on an OPC UA Server (default), 1 - eExpose: This Property Definition is exposed on an OPC UA Server for reading and writing, or 2 - eExpo… |

**Eventos:** `OnPropertyChanged()`

<a id="panel-xobject"></a>
### XObject

- CLSID `{45DE3043-56EA-4721-B558-AFE48339ACCB}` · interface `IXObject` · eventos `DElipseXEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 31 instâncias em 4 arquivo(s)
- XObject control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `CustomConfigText` | String | RW | type lib | CustomConfig (apelido confirmado) | nomeada | — |  |
| `FriendlyName` | String | RW | type lib | FriendlyName | nomeada | — |  |
| `InstanceName` | String | RW | type lib | InstanceName | nomeada | — |  |
| `Contexts` | String | RW | type lib | Contexts | nomeada | — |  |
| `IconPath` | BSTRPICTURE | RW | type lib | IconPath | nomeada | — |  |
| `DefaultIsAlarmArea` | Boolean | RW | type lib | DefaultIsAlarmArea | nomeada | — |  |
| `EnableTagBehavior` | Boolean | RW | type lib | EnableTagBehavior | nomeada | — |  |
| `ValueMode` | EValueMode | RW | type lib | ValueMode | nomeada | — |  |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_CLSID` | String |  | gravada no .prj | _CLSID | nomeada | — | sem equivalente na type lib |
| `_EVENTIID` | String |  | gravada no .prj | _EVENTIID | nomeada | — | sem equivalente na type lib |
| `_IID` | String |  | gravada no .prj | _IID | nomeada | — | sem equivalente na type lib |

**Eventos:** `Constructor()`; `CustomConfig()`

### Enumerações de Panel

- **AnalogInputModeConstants**: aimGuessType=0, aimKeepType=1
- **ArcStyleConstants**: arc=0, chord=1, pie=2
- **BackgroundStyleConstants**: Transparent=0, Opaque=1
- **BorderStyleConstants**: Normal=0, Dash=1, Dot=2, DashDot=3, DashDotDot=4, Null=5
- **CommandConfirmationConstants**: ccNever=-1, ccAlways=0
- **CommandInterlockModeConstants**: cimDoNothing=0, cimWarning=1, cimBlockCommand=2
- **CounterTypeFlags**: Preset=0, Infinite=1
- **DemoType**: Random=0, Sine=1, Square=2, CurrentTime=3, RampUp=4, RampDown=5, RampUpDown=6
- **EExposableToOpc**: eDontExpose=0, eExpose=1, eExposeAsReadOnly=2
- **Effect3DStyleConstants**: No3D=0, Raised=1, Sunken=2
- **EnumFillOverrideMode**: NoOverride=0, Wireframe=1, SolidFill=2, ByBrightness=3
- **EnumTransparentMode**: Disabled=0, ByColor=1, ByPercent=2
- **EPanelAlignment**: paDefault=0, paTopLeft=1, paCenter=2
- **EPropPermission**: ppDefault=0, ppAllow=1, ppBlock=2
- **ERenderQuality**: rqDefault=0, rqNormal=1, rqHighQuality=2
- **EValueMode**: vmUndefined=0, vmAnalog=1, vmDiscrete=2
- **FillStyleConstants**: Solid=0, Hollow=1, Horizontal=2, Vertical=3, Downward=4, Upward=5, Cross=6, DiagonalCross=7, Gradient=8, SemiTransparent=9, MouseArea=10, Background=11
- **FrameSetOptionFlags**: foDontChange=-1, foTitleBar=1, foClose=2, foMinimize=4, foMaximize=8, foBorder=16, foResize=32, foMove=64, foPopup=128, foStayOnTop=256, foSmallTitle=512, foNoButtons=1024, foCenter=2048
- **GradientStyleConstants**: LeftToRight=0, RightToLeft=1, VertToCenter=2, VertFromCenter=3, TopDown=4, BottomUp=5, HorzToCenter=6, HorzFromCenter=7, DiagDownRight=8, DiagUpLeft=9, DiagUpToCenter=10, DiagUpFromCenter=11, DiagDownLeft=12, DiagUpRight=13, DiagDownToCenter=14, DiagDownFromCenter=15, SpotBottomRight=16, SpotBottomLeft=17, SpotTopLeft=18, SpotTopRight=19, SpotFromCenter=20, SpotToCenter=21
- **HorizontalFillPercentStyle**: FillLeftToRight=0, FillRightToLeft=1, FillCenterToEdgesH=2
- **kfKeepFormat**: kfNever=0, kfAutomatic=1
- **PicturePositionConstants**: Center=0, Tile=1, Stretch=2, TopLeft=3, BottomLeft=4, BottomRight=5, TopRight=6
- **PolygonFillMode**: Alternate=0, Winding=1
- **ReportBackgroundStyle**: rv2BackSolid=0, rv2Gradient=1, rv2Pattern=2
- **ReportBarcodeCaptionPosition**: rv2NoCaption=0, rv2Above=1, rv2Below=2
- **ReportBarcodeRotation**: rv2NoRotation=0, rv2Rotate180Degrees=1, rv2Rotate90Degrees=2, rv2Rotate270Degrees=3
- **ReportBarcodeStyle**: rv2NoBarcode=0, rv2Ansi39=1, rv2Ansi39x=2, rv2Code_2_of_5=3, rv2Code25intlv=4, rv2Code25mat=5, rv2Matrix_2_of_5=5, rv2Code39=6, rv2Code39x=7, rv2Code_128_A=8, rv2Code_128_B=9, rv2Code_128_C=10, rv2Code_128auto=11, rv2Code_93=12, rv2Code93x=13, rv2MSI=14, rv2PostNet=15, rv2Codabar=16, rv2EAN_8=17, rv2EAN_13=18, rv2UPC_A=19, rv2UPC_E0=20, rv2UPC_E1=21, rv2RM4SCC=22, rv2UCCEAN128=23, rv2QRCode=24, rv2Code49=25, rv2JapanesePostal=26, rv2Pdf417=27, rv2EAN128FNC1=28, rv2RSS14=29, rv2RSS14Truncated=30, rv2RSS14Stacked=31, rv2RSS14StackedOmnidirectional=32, rv2RSSExpanded=33, rv2RSSExpandedStacked=34, rv2RSSLimited=35, rv2DataMatrix=36, rv2MicroPDF417=37, rv2MicroQRCode=38, rv2MaxiCode=39, rv2GS1QRCode=40, rv2GS1DataMatrix=41, rv2Aztec=42, rv2IntelligentMail=64, rv2ITF14=65, rv2Code_11=66, rv2SSCC_18=67, rv2Telepen=68, rv2Pharmacode=69, rv2PZN=70, rv2HIBCCode128=71, rv2HIBCCode39=72, rv2ISBN=73, rv2ISSN=74, rv2ISMN=75, rv2IATA_2_of_5=76, rv2BC412=77, rv2Plessey=78, rv2IntelligentMailPackage=79
- **ReportBarcodeTextAlignment**: rv2Near=0, rv2Centered=1, rv2Far=2
- **ReportCheckboxAlignment**: rv2TopLeft=1, rv2TopCenter=2, rv2TopRight=4, rv2MiddleLeft=16, rv2MiddleCenter=32, rv2MiddleRight=64, rv2BottomLeft=256, rv2BottomCenter=512, rv2BottomRight=1024
- **ReportColumnDirection**: rv2DownAcross=0, rv2AcrossDown=1
- **ReportNewPageColumn**: rv2NoNew=0, rv2Before=1, rv2After=2, rv2BeforeAfter=3
- **ReportObjBackOpacity**: rv2Opaque=0, rv2Transparent=1
- **ReportObjBorderStyle**: rv2NoBorder=0, rv2Solid=1, rv2Dashed=2, rv2Dot=3, rv2DashDot=4, rv2DashDotDot=5, rv2Double=6
- **ReportObjTextAlignment**: rv2Left=0, rv2Center=1, rv2Right=2, rv2Justify=3
- **ReportObjVertAlignment**: rv2Top=0, rv2Middle=1, rv2Bottom=2
- **ReportObjWordWrap**: rv2NoWrap=0, rv2WordWrap=1, rv2CharWrap=2
- **ReportPictureAlignment**: rv2PicTopLeft=0, rv2PicTopRight=1, rv2PicCenter=2, rv2PicBottomLeft=3, rv2PicBottomRight=4
- **ReportPreviewViewType**: rv2SinglePage=0, rv2Multipage=1, rv2Continuous=2
- **ReportRepeatStyle**: rv2NoRepeat=0, rv2OnPage=1, rv2OnColumn=2, rv2RepeatAll=3, rv2OnPageIncludeNoDetail=4
- **ReportSizeMode**: rv2Clip=0, rv2Stretch=1, rv2Zoom=2
- **ReportSummaryFunc**: rv2Sum=0, rv2Avg=1, rv2Count=2, rv2Min=3, rv2Max=4, rv2Var=5, rv2VarP=6, rv2StdDev=7, rv2StdDevP=8, rv2DSum=9, rv2DAvg=10, rv2DCount=11, rv2DVar=12, rv2DVarP=13, rv2DStdDev=14, rv2DStdDevP=15
- **ReportSummaryRunning**: rv2NoSR=0, rv2Group=1, rv2All=2
- **ReportSummaryType**: rv2NoST=0, rv2GrandTotal=1, rv2PageTotal=2, rv2SubTotal=3, rv2PageCount=4
- **RotationDirectionStyle**: Clockwise=0, Counterclockwise=1
- **ScaleAlignmentStyle**: RightSide=0, LeftSide=1
- **ScaleOrientationStyle**: HorizontalScale=0, VerticalScale=1
- **ScreenStyleConstants**: bkSolid=0, bkHorizontal=2, bkVertical=3, bkDownward=4, bkUpward=5, bkCross=6, bkDiagonalCross=7, bkGradient=8, bkBackground=11, bkPicture=12
- **SectionReportExportPermissionsPDF**: rv2PermissionNone=0, rv2PermissionPrint=4, rv2PermissionModifyContents=8, rv2PermissionCopy=16, rv2PermissionModifyAnnotation=32, rv2PermissionFillIn=256, rv2PermissionAccessibleReaders=512, rv2PermissionAssembly=1024
- **SectionReportExportXLSFormat**: rv2XLSFormat97Plus=0, rv2XLSFormat95=1, rv2XLSFormatXLSX=2
- **ShapeStyle**: rv2Rectangle=0, rv2Ellipse=1, rv2RoundRect=2
- **ShowFontAlignment**: LeftAlignment=0, CenterAlignment=1, RightAlignment=2
- **SortModeConstants**: smNoSort=-1, smAlphabetic=0, smTypeSorting=1
- **SplitDockPosition**: dockRemaining=0, dockTop=1, dockBottom=2, dockLeft=3, dockRight=4
- **SplitType**: SplitInvalid=-1, SplitNone=0, SplitHorizontal=1, SplitVertical=2
- **SplitUnit**: UnitPercent=0, UnitPixel=1, UnitHimetric=2
- **stDataType**: stCurrentType=0, stChar=1, stByte=2, stWord=3, stInteger=4, stLong=5, stDWord=6, stSingle=7, stDouble=8, stDateTime=9, stString=10
- **TrendAnalysisConfigStatus**: tacsSucceeded=0, tacsFailed=1, tacsInvalidContent=2, tacsNewerVersionRequired=3
- **TrendAnalysisDisplayPosition**: tadpDefault=-1, tadpLeft=0, tadpRight=1, tadpTop=2, tadpBottom=3
- **TriggerTypeFlags**: ttSingle=0, ttContinuous=1, ttDaily=2, ttMonthly=3
- **VerticalAlignment**: TopAlignment=0, MidAlignment=1, BottomAlignment=2
- **VerticalFillPercentStyle**: FillBottomToTop=0, FillTopToBottom=1, FillCenterToEdgesV=2
- **WindowStyleConstants**: maximized=0, windowed=1, minimized=2

---

## DB

Arquivo `DB.e3` · versão 1.1 · LIBID `{11317AA8-1BB4-4837-B3B2-58EAC732B5BF}` · E3 DB Library 1.1

Classes: [AlarmConfig](#db-alarmconfig), [AlarmServer](#db-alarmserver), [AlarmSource](#db-alarmsource), [AnalogLevelAlarm](#db-analoglevelalarm), [Area](#db-area), [DBServer](#db-dbserver), [DeadBandAlarm](#db-deadbandalarm), [DigitalAlarm](#db-digitalalarm), [DiscreteAlarm](#db-discretealarm), [Formula](#db-formula), [Hist](#db-hist), [HistField](#db-histfield), [HistFieldsCollection](#db-histfieldscollection), [HistIndex](#db-histindex), [HistIndexesCollection](#db-histindexescollection), [HistIndexField](#db-histindexfield), [Historian](#db-historian), [HistPrimaryKey](#db-histprimarykey), [HistPrimaryKeyField](#db-histprimarykeyfield), [HistServer](#db-histserver), [IStorageField](#db-istoragefield), [IStorageFieldsCollection](#db-istoragefieldscollection), [ROCAlarm](#db-rocalarm), [StorageSession](#db-storagesession)

<a id="db-alarmconfig"></a>
### AlarmConfig

- CLSID `{1ECEB9A4-515A-4202-B449-EEAD6CA81CF7}` · interface `IAlarmConfig`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Alarm Config Object

<a id="db-alarmserver"></a>
### AlarmServer

- CLSID `{DB951898-8F58-486B-B85B-B41F458764FF}` · interface `IAlarmServer`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 1 instâncias em 1 arquivo(s)
- Alarm Server control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Logging` | Boolean | RW | type lib | — | não gravada nomeada | False | Creates a record with information about Alarms on a Database specified by the DataSource property. If set to False, this record is not created. Otherwise, this record is created. The default value of this property is False. |
| `DataSource` | BSTRDBLINK | RW | type lib | DataSource | nomeada | an empty String, that is, there is no Database t… | Defines a Database object to use for storing Alarm data. The default value of this property is an empty String, that is, there is no Database to store Alarm data. |
| `EnableDiscard` | Boolean | RW | type lib | EnableDiscard | nomeada | False | Indicates Alarm's data discard after a certain time. If set to False, data is stored indefinitely on a table. Otherwise, it is discarded after a certain time. The default value of this property is False. |
| `DiscardInterval` | Long | RW | type lib | DiscardUnits (apelido confirmado) | nomeada | 1 (one time unit indicated by the 256 Server Obj… | This property works with the DiscardTimeUnit property and indicates a time interval in which Alarm data is stored on a database table, until it is discarded. The default value of this property is 1 (one time unit indicated by the 256 Server Objects DiscardTimeUnit property). If this property is conf… |
| `DiscardTimeUnit` | DBTimeUnit | RW | type lib | DiscardTimeUnit | nomeada | — | This property works with the DiscardInterval property and indicates a time unit in which Alarm data remains stored until it is discarded. Possible values for this property are 0: dtHour (hours), 1: dtDay (days), 2: dtMonth (months, default), or 3: dtMinute (minutes). |
| `VerificationInterval` | Long | RW | type lib | VerificationInterval | nomeada | 1 (one time unit indicated by the VerificationUn… | This property works with the VerificationUnit property to control the time interval that Elipse E3 checks if Alarm data is old, and then discard it. The default value of this property is 1 (one time unit indicated by the VerificationUnit property). |
| `VerificationUnit` | DBTimeUnit | RW | type lib | VerificationUnit | nomeada | — | This property works with the VerificationInterval property and indicates a time unit to perform a verification to discard Alarm data. Possible values for this property are 0: dtHour (hours), 1: dtDay (days), 2: dtMonth (months, default), or 3: dtMinute (minutes). |
| `EnableBackupTable` | Boolean | RW | type lib | EnableBackupTable | nomeada | True | Creates a backup table where discarded Alarm data is stored for security reasons. If set to True, this table is created. Otherwise, there is no backup table. The default value of this property is True. |
| `BackupDiscardInterval` | Long | RW | type lib | BackupDiscardUnits (apelido confirmado) | nomeada | 12 (twelve time units indicated by the BackupDis… | Indicates a maximum time interval, in minutes, hours, days, or months, for Alarm data on the backup table until it is discarded, regardless of the time data remains on the main table. For example, to keep data for 24 months on the main table and six more months on the backup table, this option's val… |
| `BackupDiscardTimeUnit` | DBTimeUnit | RW | type lib | BackupDiscardTimeUnit | nomeada | — | This property indicates a time unit in which Alarm's backup data remains stored until they are discarded. Possible values for this property are 0: dtHour (hours), 1: dtDay (days), 2: dtMonth (months, default), or 3: dtMinute (minutes). This property works with the BackupDiscardInterval property. |
| `ActiveNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms in an application, active or not. This is a read-only property. |
| `ActiveCritNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a Critical severity in an application. This is a read-only property. |
| `ActiveHighNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a High severity in an application. This is a read-only property. |
| `ActiveMedNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a Medium severity in an application. This is a read-only property. |
| `ActiveLowNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a Low severity in an application. This is a read-only property. |
| `ActiveAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of active Alarms in an application. This is a read-only property. Server Objects 255 |
| `ActiveCritAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a Critical severity in an application. This is a read-only property. |
| `ActiveHighAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a High severity in an application. This is a read-only property. |
| `ActiveMedAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a Medium severity in an application. This is a read-only property. |
| `ActiveLowAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a Low severity in an application. This is a read-only property. |
| `InactiveNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of inactive and unacknowledged Alarms in an application. This is a read-only property. |
| `InactiveCritNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a Critical severity in an application. This is a read- only property. |
| `InactiveHighNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a High severity in an application. This is a read- only property. |
| `InactiveMedNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a Medium severity in an application. This is a read-only property. |
| `InactiveLowNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a Low severity in an application. This is a read-only property. |
| `TableName` | String | RW | type lib | TableName | nomeada | "Alarms" | Defines a name for an Alarms table. The default value of this property is "Alarms". |
| `ExcludeSuppressedAlarmsOnCounters` | Boolean | RW | type lib | ExcludeSuppressedCounters (apelido confirmado) | nomeada | False | When configured to True, ignores Alarms suppressed using the Shelving type or using the By Design type on Alarm's general counters. The default value of this property is False. |
| `SuppressedAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of Alarms suppressed in an application, both using the Shelving type and using the By Design type. This is a read-only property. Server Objects 257 |
| `ShelvedAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of Alarms or Events suppressed using the Shelving type in an application. This is a read-only property. |
| `SuppressedByDesignAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of Alarms suppressed using the By Design type in an application. This is a read-only property. |
| `OutOfServiceAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of Alarms suppressed using the Out-of-Service type in an application. This is a read-only property. |
| `SuppressedAlarmsLogging` | Boolean | RW | type lib | LoggingAlarmsSuppressed (apelido confirmado) | nomeada | True, that is, Alarms are updated on the databas… | Indicates whether Alarms are updated or not on a database while suppressed using the Shelving type or using the Out-of-Service type. The default value of this property is True, that is, Alarms are updated on the database. When configuring this property as False, an Alarm entering or leaving the supp… |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `CustomName0` | String |  | gravada no .prj | CustomName0 | nomeada | — | sem equivalente na type lib |
| `CustomSize0` | ULong |  | gravada no .prj | CustomSize0 | nomeada | — | sem equivalente na type lib |
| `CustomSizeCount` | ULong |  | gravada no .prj | CustomSizeCount | nomeada | — | sem equivalente na type lib |
| `SelCount` | ULong |  | gravada no .prj | SelCount | nomeada | — | sem equivalente na type lib |
| `StoreOnDisk` | Byte |  | gravada no .prj | StoreOnDisk | nomeada | — | sem equivalente na type lib |
| `StrSel#` | String |  | gravada no .prj | StrSel# | nomeada | — | sem equivalente na type lib (família: 28) |
| `Tables` | ULong |  | gravada no .prj | Tables | nomeada | — | sem equivalente na type lib |
| `Units` | ULong |  | gravada no .prj | Units | nomeada | — | sem equivalente na type lib |
| `UnitType` | Byte |  | gravada no .prj | UnitType | nomeada | — | sem equivalente na type lib |
| `UserFieldCount` | ULong |  | gravada no .prj | UserFieldCount | nomeada | — | sem equivalente na type lib |
| `UserFieldLink#` | String |  | gravada no .prj | UserFieldLink# | nomeada | — | sem equivalente na type lib (família: 11) |
| `UserFieldName#` | String |  | gravada no .prj | UserFieldName# | nomeada | — | sem equivalente na type lib (família: 11) |
| `UserFieldPropagate#` | UShort |  | gravada no .prj | UserFieldPropagate# | nomeada | — | sem equivalente na type lib (família: 11) |
| `UserFieldSize#` | UShort |  | gravada no .prj | UserFieldSize# | nomeada | — | sem equivalente na type lib (família: 11) |
| `UserFieldType#` | ULong |  | gravada no .prj | UserFieldType# | nomeada | — | sem equivalente na type lib (família: 11) |

**Métodos:** `AckArea(Area String, ActorID Variant)`; `AckAllAlarms(ActorID Variant)`; `LogTrackingEvent(Message String, ActorID Variant, Area String, Severity EAlarmSeverity, EventTime Variant, Source String, EventCategory String, EventType Variant, UserFields Variant, AlarmSourceName String, FullAlarmSourceName String)`

<a id="db-alarmsource"></a>
### AlarmSource

- CLSID `{18FBE4D6-8D7D-4E50-AE6A-3B52C290B044}` · interface `IAlarmSource`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Alarm Source Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Source` | BSTRSIMPLELINK | RW | type lib | — | — | — | Defines alarm data source |
| `AlarmVerify` | Boolean | RW | type lib | — | — | — | Enables/disables alarm checking |
| `Alarm` | Boolean | R | type lib | — | — | — | Alarm current status |
| `ActiveNACKAlarm` | Boolean | R | type lib | — | — | — | Alarm current acknowledge status |
| `Value` | Variant | RW | type lib | — | — | — | Value from tag linked to alarm source |
| `CurrentSubConditionName` | String | R | type lib | — | — | — | Current alarm sub-condition name |
| `CurrentSeverity` | EAlarmSeverity | R | type lib | — | — | — | Current alarm severity |
| `FormattedValue` | String | R | type lib | — | — | — | Current formatted value |
| `Format` | BSTRFORMAT | RW | type lib | — | — | — | Specifies the format applied to alarm values |
| `RawAlarm` | Boolean | R | type lib | — | — | — | Tells if the alarm should be active or inactive, even if it's using delayed activation/deactivation |
| `Event` | Boolean | RW | type lib | — | — | — | Defines if this alarm must be treated as an event |
| `DoubleAckRequired` | Boolean | RW | type lib | — | — | — | Defines if this alarm requires double-acknowledgement |
| `AreaNameOverride` | String | RW | type lib | — | — | — | Defines an alternate area name for this alarm source |
| `UserFields` | IAlarmUserFieldsCollection | R | type lib | — | — | — | Retrieves the collection of user fields |
| `ExcludeSuppressedOnAreaCounters` | Boolean | RW | type lib | — | — | — | Exclude suppressed alarms on area counters |
| `SuppressedAlarmsConfigured` | Boolean | R | type lib | — | — | — | True if this alarm is configured to allow suppression |
| `SuppressCondition` | BSTRSIMPLELINK | RW | type lib | — | — | — | Defines data source for design alarm suppression |
| `SuppressedAsEvent` | Boolean | RW | type lib | — | — | — | Defines if alarm suppressed by design will be treated as an event |
| `Shelved` | Boolean | R | type lib | — | — | — | Alarm current shelved status |
| `ShelveMaxDuration` | Long | RW | type lib | — | — | — | Defines the maximum duration this alarm can be shelved, when it's not active |
| `OutOfService` | Boolean | R | type lib | — | — | — | True if this alarm is placed out of service |

**Métodos:** `Ack(ActorID Variant)`; `GetAlarm()`; `Shelve(Duration ULong, Reason String, ActorID Variant)`; `Unshelve(ActorID Variant)`; `RemoveFromService(Reason String, ActorID Variant)`; `ReturnToService(ActorID Variant)`

<a id="db-analoglevelalarm"></a>
### AnalogLevelAlarm

- CLSID `{5088EF42-1652-4525-8D59-0A08A3DD9BEE}` · interface `IAnalogLevelAlarm`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 2 arquivo(s)
- Analog Level Alarm Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | Name | nomeada | — | Name assigned to the condition |
| `ConditionName` | String | R | type lib | — | não gravada nomeada | — | Name assigned to the condition |
| `Delay` | Long | RW | type lib | Delay | nomeada | — | Delay in ms before entering/leaving alarm condition |
| `LevelDeadBand` | Double | RW | type lib | DeadBand (apelido confirmado) | nomeada | — | Dead band for Alarm level limits. |
| `LevelReturnMessageText` | String | RW | type lib | LevelReturnMessageText | nomeada | — | Sets a returning message for Alarm's level. |
| `LoLo` | Boolean | RW | type lib | LoLo.Enabled (apelido confirmado) | nomeada | — | Enables or disables a check on LoLo-type Alarms. |
| `LoLoLimit` | Double | RW | type lib | LoLo.Limit (apelido confirmado) | nomeada | — | Indicates the level in which a LoLo-type Alarm is activated. |
| `LoLoMessageText` | String | RW | type lib | LoLo.Message (apelido confirmado) | nomeada | — | Sets a text message for a LoLo-type Alarm's limit. |
| `LoLoSeverity` | EAlarmSeverity | RW | type lib | LoLo.Severity (apelido confirmado) | nomeada | — | Indicates the level of importance of a LoLo-type Alarm. Possible values for this property are -2: Critical, 0: High, 1: Medium, or 2: Low. |
| `LoLoAckRequired` | Boolean | RW | type lib | LoLo.Ack (apelido confirmado) | nomeada | — | Indicates whether a LoLo-type Alarm requires acknowledgment or not. |
| `LoLoEvent` | Boolean | RW | type lib | LoLo.Event (apelido confirmado) | nomeada | — | Defines whether an Alarm's LoLo subcondition must be treated as an Event. If the Event property, common to all Alarm Sources, is set to True, this property cannot be modified, and its value always remains in True. This property cannot be changed while this object is active. |
| `LoLoAllowShelving` | Boolean | RW | type lib | LoLo.AllowShelving (apelido confirmado) | nomeada | True | Indicates whether a LoLo-type Alarm or Event can be shelved. The default value of this property is True. |
| `LoLoShelveMaxDuration` | Long | RW | type lib | LoLo.ShelveMaxDuration (apelido confirmado) | nomeada | 60 (one hour) | Defines a maximum duration, in minutes, for shelving this LoLo-type Alarm or Event. The default value of this property is 60 (one hour). |
| `LoLoShelveMaxCount` | Long | RW | type lib | LoLo.ShelveMaxCount (apelido confirmado) | nomeada | 0 (zero), that is, no limits for shelving | Defines how many times a LoLo-type Alarm or Event can be shelved. The default value of this property is 0 (zero), that is, no limits for shelving. |
| `Lo` | Boolean | RW | type lib | Lo.Enabled (apelido confirmado) | nomeada | — | Enables or disables a check on Lo-type Alarms. |
| `LoLimit` | Double | RW | type lib | Lo.Limit (apelido confirmado) | nomeada | — | Indicates the level in which a Lo-type Alarm is activated. |
| `LoMessageText` | String | RW | type lib | Lo.Message (apelido confirmado) | nomeada | — | Sets a text message for a Lo-type Alarm's limit. |
| `LoSeverity` | EAlarmSeverity | RW | type lib | Lo.Severity (apelido confirmado) | nomeada | — | Indicates the level of importance of a Lo-type Alarm. Possible values for this property are -2: Critical, 0: High, 1: Medium, 2: Low. |
| `LoAckRequired` | Boolean | RW | type lib | Lo.Ack (apelido confirmado) | nomeada | — | Indicates whether a Lo-type Alarm requires acknowledgment or not. 266 Server Objects |
| `LoEvent` | Boolean | RW | type lib | Lo.Event (apelido confirmado) | nomeada | — | Defines whether an Alarm's Lo subcondition must be treated as an Event. If the Event property, common to all Alarm Sources, is set to True, this property cannot be modified, and its value always remains in True. This property cannot be changed while this object is active. |
| `LoAllowShelving` | Boolean | RW | type lib | Lo.AllowShelving (apelido confirmado) | nomeada | True | Indicates whether a Lo-type Alarm or Event can be shelved. The default value of this property is True. |
| `LoShelveMaxDuration` | Long | RW | type lib | Lo.ShelveMaxDuration (apelido confirmado) | nomeada | 60 (one hour) | Defines a maximum duration, in minutes, for shelving this Lo-type Alarm or Event. The default value of this property is 60 (one hour). |
| `LoShelveMaxCount` | Long | RW | type lib | Lo.ShelveMaxCount (apelido confirmado) | nomeada | 0 (zero), that is, no limits for shelving | Defines how many times a Lo-type Alarm or Event can be shelved. The default value of this property is 0 (zero), that is, no limits for shelving. Server Objects 267 |
| `Hi` | Boolean | RW | type lib | Hi.Enabled (apelido confirmado) | nomeada | — | Enables or disables a check on Hi-type Alarms. |
| `HiLimit` | Double | RW | type lib | Hi.Limit (apelido confirmado) | nomeada | — | Indicates the level in which a Hi-type Alarm is activated. |
| `HiMessageText` | String | RW | type lib | Hi.Message (apelido confirmado) | nomeada | — | Sets a text message for a Hi-type Alarm's limit. |
| `HiSeverity` | EAlarmSeverity | RW | type lib | Hi.Severity (apelido confirmado) | nomeada | — | Indicates the level of importance of a Hi-type Alarm. Possible values for this property are -2: Critical, 0: High, 1: Medium, or 2: Low. |
| `HiAckRequired` | Boolean | RW | type lib | Hi.Ack (apelido confirmado) | nomeada | — | Indicates whether a Hi-type Alarm requires acknowledgment or not. |
| `HiEvent` | Boolean | RW | type lib | Hi.Event (apelido confirmado) | nomeada | — | Defines whether an Alarm's Hi subcondition must be treated as an Event. If the Event property, common to all Alarm Sources, is set to True, this property cannot be modified, and its value always remains in True. This property cannot be changed while this object is active. |
| `HiAllowShelving` | Boolean | RW | type lib | Hi.AllowShelving (apelido confirmado) | nomeada | True | Indicates whether a Hi-type Alarm or Event can be shelved. The default value of this property is True. |
| `HiShelveMaxDuration` | Long | RW | type lib | Hi.ShelveMaxDuration (apelido confirmado) | nomeada | 60 (one hour) | Defines a maximum duration, in minutes, for shelving this Hi-type Alarm or Event. The default value of this property is 60 (one hour). |
| `HiShelveMaxCount` | Long | RW | type lib | Hi.ShelveMaxCount (apelido confirmado) | nomeada | 0 (zero), that is, no limits for shelving | Defines how many times a Hi-type Alarm or Event can be shelved. The default value of this property is 0 (zero), that is, no limits for shelving. |
| `HiHi` | Boolean | RW | type lib | HiHi.Enabled (apelido confirmado) | nomeada | — | Enables or disables a check on HiHi-type Alarms. |
| `HiHiLimit` | Double | RW | type lib | HiHi.Limit (apelido confirmado) | nomeada | — | Indicates the level in which a HiHi-type Alarm is activated. |
| `HiHiMessageText` | String | RW | type lib | HiHi.Message (apelido confirmado) | nomeada | — | Sets a text message for a HiHi-type Alarm's limit. |
| `HiHiSeverity` | EAlarmSeverity | RW | type lib | HiHi.Severity (apelido confirmado) | nomeada | — | Indicates the level of importance of a HiHi-type Alarm. Possible values for this property are -2: Critical, 0: High, 1: Medium, or 2: Low. |
| `HiHiAckRequired` | Boolean | RW | type lib | HiHi.Ack (apelido confirmado) | nomeada | — | Indicates whether a HiHi-type Alarm requires acknowledgment or not. |
| `HiHiEvent` | Boolean | RW | type lib | HiHi.Event (apelido confirmado) | nomeada | — | Defines whether an Alarm's HiHi subcondition must be treated as an Event. If the Event property, common to all Alarm Sources, is set to True, this property cannot be modified, and its value always remains as True. This property cannot be changed while this object is active. |
| `HiHiAllowShelving` | Boolean | RW | type lib | HiHi.AllowShelving (apelido confirmado) | nomeada | True | Indicates whether a HiHi-type Alarm or Event can be shelved. The default value of this property is True. Server Objects 265 |
| `HiHiShelveMaxDuration` | Long | RW | type lib | HiHi.ShelveMaxDuration (apelido confirmado) | nomeada | 60 (one hour) | Defines a maximum duration, in minutes, for shelving this HiHi-type Alarm or Event. The default value of this property is 60 (one hour). |
| `HiHiShelveMaxCount` | Long | RW | type lib | HiHi.ShelveMaxCount (apelido confirmado) | nomeada | 0 (zero), that is, no limits for shelving | Defines how many times a HiHi-type Alarm or Event can be shelved. The default value of this property is 0 (zero), that is, no limits for shelving. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `Hi.Link` | String |  | gravada no .prj | Hi.Link | nomeada | — | sem equivalente na type lib |
| `HiHi.Link` | String |  | gravada no .prj | HiHi.Link | nomeada | — | sem equivalente na type lib |
| `Lo.Link` | String |  | gravada no .prj | Lo.Link | nomeada | — | sem equivalente na type lib |
| `LoLo.Link` | String |  | gravada no .prj | LoLo.Link | nomeada | — | sem equivalente na type lib |

<a id="db-area"></a>
### Area

- CLSID `{BEC2CEB3-2272-45F3-AFAF-8908ABCB2CBD}` · interface `IArea`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Area Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `AlarmVerify` | Boolean | RW | type lib | — | — | — | Enables/disables area alarm checking |
| `Alarm` | Boolean | R | type lib | — | — | — | Reports if this area has at least one active alarm |
| `ActiveAlarms` | Long | R | type lib | — | — | — | Total number of active alarms |
| `ActiveCritAlarms` | Long | R | type lib | — | — | — | Total number of critical severity active alarms |
| `ActiveHighAlarms` | Long | R | type lib | — | — | — | Total number of high severity active alarms |
| `ActiveMedAlarms` | Long | R | type lib | — | — | — | Total number of medium severity active alarms |
| `ActiveLowAlarms` | Long | R | type lib | — | — | — | Total number of low severity active alarms |
| `ActiveNACKAlarms` | Long | R | type lib | — | — | — | Total number of active unacknowledged alarms (both active and inactive) |
| `ActiveCritNACKAlarms` | Long | R | type lib | — | — | — | Total number of critical severity unacknowledged alarms (both active and inactive) |
| `ActiveHighNACKAlarms` | Long | R | type lib | — | — | — | Total number of high severity unacknowledged alarms (both active and inactive) |
| `ActiveMedNACKAlarms` | Long | R | type lib | — | — | — | Total number of medium severity unacknowledged alarms (both active and inactive) |
| `ActiveLowNACKAlarms` | Long | R | type lib | — | — | — | Total number of low severity unacknowledged alarms (both active and inactive) |
| `InactiveNACKAlarms` | Long | R | type lib | — | — | — | Total number of inactive unacknowledged alarms |
| `InactiveCritNACKAlarms` | Long | R | type lib | — | — | — | Total number of critical severity inactive unacknowledged alarms |
| `InactiveHighNACKAlarms` | Long | R | type lib | — | — | — | Total number of high severity inactive unacknowledged alarms |
| `InactiveMedNACKAlarms` | Long | R | type lib | — | — | — | Total number of medium severity inactive unacknowledged alarms |
| `InactiveLowNACKAlarms` | Long | R | type lib | — | — | — | Total number of low severity inactive unacknowledged alarms |
| `UserFields` | IAlarmUserFieldsCollection | R | type lib | — | — | — | Retrieves the collection of user fields |
| `SuppressedAlarms` | Long | R | type lib | — | — | — | Total number of suppressed alarms |
| `ShelvedAlarms` | Long | R | type lib | — | — | — | Total number of shelved alarms |
| `SuppressedByDesignAlarms` | Long | R | type lib | — | — | — | Total number of suppressed by design alarms |
| `OutOfServiceAlarms` | Long | R | type lib | — | — | — | Total number of out of service alarms |

<a id="db-dbserver"></a>
### DBServer

- CLSID `{E49CD931-0244-4DDE-9FF9-3D12B6EA576E}` · interface `IDBServer`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 1 arquivo(s)
- DBServer control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `SourceType` | DBSourceType | RW | type lib | — | não gravada nomeada | — | Indicates the type of database used by this object. Possible values for this property are 0 - stAccess: Access-type database (default), 1 - stOracle: Oracle-type database, 2 - stSqlServer: SQL Server-type database, 3 - stPostgreSQL: PostgreSQL-type database, or 4 - stMySQL: MySQL-type database. |
| `ReconnectDelay` | Long | RW | type lib | ReconnectDelay | nomeada | 2000, or 2 (two) seconds | This property determines a delay time, in milliseconds, for an application to try to restore a lost connection with a database. The default value of this property is 2000, or 2 (two) seconds. |
| `EnableSynchronization` | Boolean | RW | type lib | EnableSynchronization | nomeada | False, that is, syncing is disabled | Indicates, if enabled, that is, in True, that Elipse E3 must also perform a data recording on a second database simultaneously, to improve security. If this property is enabled and there is a server in Standby mode, Elipse E3 then performs a syncing between databases from both servers. The default v… |
| `UseTransaction` | Boolean | RW | type lib | UseTransaction | nomeada | — | Defines whether a Database object uses database transactions or not. If this property is set to True, each block of database operations, 200 Historic, Storage, Formula, and Alarm operations, are executed at once, that is, in a single transaction. |
| `nRetries` | Long | RW | type lib | Retries (apelido confirmado) | nomeada | 5 (five) | This property specifies the number of times Elipse E3 tries to perform a database operation, in addition to the first one. The default value of this property is 5 (five). If the value of this property is equal to 0 (zero), only one try is performed per operation. In case there is a loss of connectio… |
| `TotalFailedWrites` | Long | R | type lib | — | não gravada nomeada | — | Indicates how many operations of .e3o files failed and were discarded since the connection with a database was activated. This property can be automatically zeroed in several situations, such as: When deactivating a Database object If the E3DBEngine process is closed for any reason If the configurat… ⚠ type lib: somente leitura |
| `ConnectionActive` | Boolean | R | type lib | — | não gravada nomeada | — | Indicates whether Elipse E3 has an active connection with a database. Elipse E3 normally uses 2 (two) connections with this database, one for writing and another one for reading. This property is in True if at least one of those 2 (two) connections is connected and working. This property should not … |
| `SourceDatabase` | String | R | type lib | — | não gravada nomeada | — | For an Access-type database, this property corresponds to the name of a file in MDB format. For a SQL Server-type database, this property corresponds to the name of a SQL Server concatenated with the selected database, in the format Server/DB. For an Oracle-type database, this property corresponds t… |
| `UserName` | String | R | type lib | — | não gravada nomeada | — | A login name used to connect to a database. This is a read-only property. |
| `TimeoutConnection` | Long | RW | type lib | TimeoutConnection | nomeada | 15 seconds | Contains a delay time to perform a connection with a database, in seconds, before an application generates a time- out error. The default value of this property is 15 seconds. |
| `TimeoutCommand` | Long | RW | type lib | — | não gravada nomeada | 180, that is, 3 (three) minutes | Contains a delay time for any database operation, in seconds, before an application generates a time-out error. The default value of this property is 180, that is, 3 (three) minutes. |
| `OracleUseADODrivers` | Boolean | RW | type lib | — | não gravada nomeada | — | Allows using ADO (ActiveX Data Objects) interfaces of Oracle-type databases, so that an Elipse E3's Query object recognizes the TIMESTAMP data type, thus enabling the reading from tables of Oracle-type databases containing a precision of milliseconds. If this property is set to False, a database use… |
| `OracleEnableTimestamp` | Boolean | RW | type lib | — | não gravada nomeada | — | Enables using the TIMESTAMP data type of Oracle-type databases, with a precision of milliseconds and available since version 9.0. If this property is configured to False, a database uses the DATE data type, with a precision of seconds. Configuring this property to False has no effect if the OracleUs… |
| `MsSQLNetworkLibrary` | SqlNetworkLibrary | RW | type lib | — | não gravada nomeada | — | Configures or returns the type of network library of a SQL Server-type database. Possible values for this property are described in the NetLibrary property. |
| `MsSQLProvider` | SqlProvider | RW | type lib | — | não gravada nomeada | — | Configures or return the OLE DB data provider to access a SQL Server-type of database. Possible values for this property are 1: SQLOLEDB or 2: MSOLEDBSQL (default). The option for an SQLOLEDB data provider is now deprecated by Microsoft and should not be used. However, applications created in versio… |
| `UseCustomConnectionString` | Boolean | RW | type lib | — | não gravada nomeada | — | Enables or disables using a custom connection String, configured in the CustomConnectionString property, when connecting to a database. |
| `CustomConnectionString` | String | RW | type lib | — | não gravada nomeada | an empty String | Configures or returns a custom String to connect to a database. Configuring this property is only effective when the UseCustomConnectionString property is configured to True. The default value of this property is an empty String. |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `AreaAlarmVerify` | ULong |  | gravada no .prj | AreaAlarmVerify | nomeada | — | sem equivalente na type lib |
| `AreaIsArea` | Boolean |  | gravada no .prj | AreaIsArea | nomeada | — | sem equivalente na type lib |
| `AreaUserFieldIsValueForced#` | Boolean |  | gravada no .prj | AreaUserFieldIsValueForced# | nomeada | — | sem equivalente na type lib (família: 9) |
| `AreaUserFieldsCount` | ULong |  | gravada no .prj | AreaUserFieldsCount | nomeada | — | sem equivalente na type lib |
| `AreaUserFieldValue#` | Long, String |  | gravada no .prj | AreaUserFieldValue# | nomeada | — | sem equivalente na type lib (família: 9) |
| `ConnectTimeOut` | ULong |  | gravada no .prj | ConnectTimeOut | nomeada | — | sem equivalente na type lib |

**Métodos:** `SetDBParameters(ServerName String, UserName String, Password String, DBName String, Port Long)`; `AccessSetDBPassword(DBPwd String)`; `FlushDBReconfig()`

<a id="db-deadbandalarm"></a>
### DeadBandAlarm

- CLSID `{98FFD130-AE1B-44B5-9E7C-1D999C0847D7}` · interface `IDeadBandAlarm`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Dead Band Alarm Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Name assigned to the condition |
| `ConditionName` | String | R | type lib | — | — | — | Name assigned to the condition |
| `Delay` | Long | RW | type lib | — | — | — | Delay in ms before entering/leaving alarm condition |
| `DeadBandSetpoint` | String | RW | type lib | — | — | — | Alarm's dead band limit. Each time the value of the associated Tag exceeds this property's value up or down the DeadBandLimit value, this Alarm occurs. |
| `DeadBandReturnMessageText` | String | RW | type lib | — | — | — | A returning message for this Dead Band-type Alarm. |
| `DeadBand` | Boolean | RW | type lib | — | — | — | Enables or disables a check on a Dead Band-type Alarm. |
| `DeadBandLimit` | Double | RW | type lib | — | — | — | Limit for this Dead Band-type Alarm. |
| `DeadBandMessageText` | String | RW | type lib | — | — | — | A text message for this Dead Band-type Alarm. |
| `DeadBandSeverity` | EAlarmSeverity | RW | type lib | — | — | — | Importance of this Dead Band-type Alarm. Possible values for this property are -2: Critical, 0: High, 1: Medium, or 2: Low. |
| `DeadBandAckRequired` | Boolean | RW | type lib | — | — | — | Indicates whether this Dead Band-type Alarm requires acknowledgment or not. |
| `DeadBandAllowShelving` | Boolean | RW | type lib | — | — | True | Indicates whether this Dead Band-type Alarm or Event can be shelved. The default value of this property is True. |
| `DeadBandShelveMaxDuration` | Long | RW | type lib | — | — | 60 (one hour) | Defines a maximum duration, in minutes, for shelving this Dead Band-type Alarm or Event. The default value of this property is 60 (one hour). |
| `DeadBandShelveMaxCount` | Long | RW | type lib | — | — | 0 (zero), that is, no limits for shelving | Defines how many times this Dead Band-type Alarm or Event can be shelved. The default value of this property is 0 (zero), that is, no limits for shelving. |

<a id="db-digitalalarm"></a>
### DigitalAlarm

- CLSID `{009EEAB4-BF00-49D4-8FA7-FB2FC2C6CD22}` · interface `IDigitalAlarm`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 52416 instâncias em 29 arquivo(s)
- Digital Alarm Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | Name | nomeada | — | Name assigned to the condition |
| `ConditionName` | String | R | type lib | — | não gravada nomeada | — | Name assigned to the condition |
| `Delay` | Long | RW | type lib | Delay | nomeada | — | Delay in ms before entering/leaving alarm condition |
| `DigitalReturnMessageText` | String | RW | type lib | ReturnMessageText (apelido confirmado) | nomeada | — | A returning message for this Digital-type Alarm. |
| `Digital` | Boolean | RW | type lib | — | não gravada nomeada | — | Enables or disables a check on a Digital-type Alarm. |
| `DigitalLimit` | Variant | RW | type lib | Limit (apelido confirmado) | nomeada | — | Limit for this Digital-type Alarm. |
| `DigitalMessageText` | String | RW | type lib | Message (apelido confirmado) | nomeada | — | A text message for this Digital-type Alarm. |
| `DigitalSeverity` | EAlarmSeverity | RW | type lib | Severity (apelido confirmado) | nomeada | — | Severity of this Digital-type Alarm. Possible values for this property are -2: Critical, 0: High, 1: Medium, or 2: Low. |
| `DigitalAckRequired` | Boolean | RW | type lib | Ack (apelido confirmado) | nomeada | — | Indicates whether this Digital-type Alarm requires acknowledgment or not. |
| `DigitalAllowShelving` | Boolean | RW | type lib | AllowShelving (apelido confirmado) | nomeada | True | Indicates whether this Digital-type Alarm or Event can be shelved. The default value of this property is True. |
| `DigitalShelveMaxDuration` | Long | RW | type lib | ShelveMaxDuration (apelido confirmado) | nomeada | 60 (one hour) | Defines a maximum duration, in minutes, for shelving this Digital-type Alarm or Event. The default value of this property is 60 (one hour). |
| `DigitalShelveMaxCount` | Long | RW | type lib | ShelveMaxCount (apelido confirmado) | nomeada | 0 (zero), that is, no limits for shelving | Defines how many times this Digital-type Alarm or Event can be shelved. The default value of this property is 0 (zero), that is, no limits for shelving. |
| `Enabled` | Byte | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `Link` | String |  | gravada no .prj | Link | nomeada | — | sem equivalente na type lib |

<a id="db-discretealarm"></a>
### DiscreteAlarm

- CLSID `{3364CDC9-32D0-4F25-BD75-CEFAA5D0ACA9}` · interface `IDiscreteAlarm`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3754 instâncias em 30 arquivo(s)
- Discrete Alarm Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | Name | nomeada | — | Name assigned to the condition |
| `ConditionName` | String | R | type lib | — | não gravada nomeada | — | Name assigned to the condition |
| `Delay` | Long | RW | type lib | Delay | nomeada | — | Delay in ms before entering/leaving alarm condition |
| `DiscreteReturnMessageText` | String | RW | type lib | ReturnMessageText (apelido confirmado) | nomeada | — | Returns or modifies the returning message of this Discrete-type Alarm. If any object in the collection of Subconditions has its Kind property set to 2 (two, Return), the Message property of that object is then used instead of the value defined in this property. |
| `SubConditions` | IDiscreteAlarmSubconditions | R | type lib | — | não gravada nomeada | — | Returns an object that is a collection of Subconditions of this Discrete-type Alarm. Check topic Collection of Subconditions for more information about the collection of objects returned by this property. This is a read-only property. Server Objects 269 |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `SubCond#AckRequired` | Boolean |  | gravada no .prj | SubCond#AckRequired | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#AllowShelving` | Boolean |  | gravada no .prj | SubCond#AllowShelving | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#Caption` | String |  | gravada no .prj | SubCond#Caption | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#Enabled` | Boolean |  | gravada no .prj | SubCond#Enabled | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#Kind` | ULong |  | gravada no .prj | SubCond#Kind | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#Limit` | Integer |  | gravada no .prj | SubCond#Limit | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#Message` | String |  | gravada no .prj | SubCond#Message | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#Name` | String |  | gravada no .prj | SubCond#Name | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#Severity` | Long |  | gravada no .prj | SubCond#Severity | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#ShelveMaxCount` | UShort |  | gravada no .prj | SubCond#ShelveMaxCount | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubCond#ShelveMaxDuration` | ULong |  | gravada no .prj | SubCond#ShelveMaxDuration | nomeada | — | sem equivalente na type lib (família: 703) |
| `SubConditionCount` | ULong |  | gravada no .prj | SubConditionCount | nomeada | — | sem equivalente na type lib |

<a id="db-formula"></a>
### Formula

- CLSID `{B188BCD0-C5F7-411A-921E-67AF3217B2AD}` · interface `IFormula`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Formula control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `DBServer` | BSTRDBLINK | RW | type lib | — | — | — | Returns/sets the path of the Database object |
| `TableName` | String | RW | type lib | — | — | — | Returns/sets the table name |
| `ImmediateExecute` | Boolean | RW | type lib | — | — | — | Enable Immediate Execute |
| `DataSourceSize` | Long | RW | type lib | — | — | — | Returns/sets the maximum size for the DataSource field |
| `ValueSize` | Long | RW | type lib | — | — | — | Returns/sets the maximum size for the Value field |

**Métodos:** `CreateUnit(UnitName String)`; `DeleteUnit(UnitName String)`; `RenameUnit(UnitName String, NewUnitName String)`; `FindUnit(UnitName String)`; `SetUnitData(UnitName String, TemplateName String, Data String)`; `GetUnitData(UnitName String, TemplateName String, Val Variant)`; `CreateValue(ValueName String)`; `DeleteValue(ValueName String)`; `RenameValue(ValueName String, NewValueName String)`; `FindValue(ValueName String)`; `SetValueData(ValueName String, TemplateName String, Data String)`; `GetValueData(ValueName String, TemplateName String, Val Variant)`; `LoadFormulaValuesQuiet(UnitName String, ValueName String)`; `SaveFormulaValues(UnitName String, ValueName String, IgnoreErrors Boolean)`

<a id="db-hist"></a>
### Hist

- CLSID `{FCC13902-5280-11D4-8E73-00C0DFB1AC67}` · interface `IHist`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 2 arquivo(s)
- Hist control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ScanTime` | Long | RW | type lib | ScanTime | nomeada | 1000 | Defines a time interval variation, in milliseconds, that a Historic waits to perform acquisition and storage of a new record on a table. Use this property if there is a need for more or less amount of data generated per second. Default value of this property is 1000. |
| `DBServer` | BSTRDBLINK | RW | type lib | DBServer | nomeada | an empty String | Indicates a Database object used by this Historic to create tables and to store data. Default value of this property is an empty String. |
| `TableName` | String | RW | type lib | TableName | nomeada | — | Defines a name for a table used in this Historic. |
| `EnableDiscard` | Boolean | RW | type lib | EnableDiscard | nomeada | False | Indicates Historic data discarding after a certain period of time. If set to False, data is stored indefinitely on a table. Otherwise, it is discarded after a certain period of time. Default value of this property is False. |
| `DiscardInterval` | Long | RW | type lib | DiscardUnits (apelido confirmado) | nomeada | 1 (one time unit indicated by the DiscardTimeUni… | This property works with the DiscardTimeUnit property and indicates a time interval in which Historic data is stored on a database table, until it is discarded. Default value of this property is 1 (one time unit indicated by the DiscardTimeUnit property). If this property is set to a value less than… |
| `DiscardTimeUnit` | DBTimeUnit | RW | type lib | DiscardTimeUnit | nomeada | — | This property works with the DiscardInterval property and indicates a time unit in which Historic data remains stored until it is discarded. Available options are 0 - dtHour: Hours, 1 - dtDay: Days, 2 - dtMonth: Months (default), or 3 - dtMinute: Minutes. |
| `VerificationInterval` | Long | RW | type lib | VerificationInterval | nomeada | 1 (one time unit indicated by the VerificationUn… | This property works with the VerificationUnit property to control the time interval that Elipse E3 checks for older Historic data, and then discard them. Default value of this property is 1 (one time unit indicated by the VerificationUnit property). |
| `VerificationUnit` | DBTimeUnit | RW | type lib | VerificationUnit | nomeada | — | This property works with the VerificationInterval property and indicates a time unit in which a Historic data discard verification is performed. Available options are 0 - dtHour: Hours, 1 - dtDay: Days, 2 - dtMonth: Months (default), or 3 - dtMinute: Minutes. |
| `EnableBackupTable` | Boolean | RW | type lib | EnableBackupTable | nomeada | False | Creates a backup table where discarded Historic data remains for security reasons. If set to True, this table is created. Otherwise, there is no backup table. Default value of this property is False. |
| `BackupDiscardInterval` | Long | RW | type lib | BackupDiscardUnits (apelido confirmado) | nomeada | 12 (twelve time units indicated by the BackupDis… | Indicates a maximum time interval, in minutes, hours, days, or months, for Historic data on the backup table until it is discarded, regardless of the time data remains on the main table. For example, to keep data for 24 months on the main table and six more months on the backup table, this option's … |
| `BackupDiscardTimeUnit` | DBTimeUnit | RW | type lib | BackupDiscardTimeUnit | nomeada | — | This property indicates the time unit in which Historic backup data remains stored until it is discarded. Available options are 0 - dtHour: Hours, 1 - dtDay: Days, 2 - dtMonth: Months (default), or 3 - dtMinute: Minutes. This property works with the BackupDiscardInterval property. |
| `CacheSize` | Long | RW | type lib | — | não gravada nomeada | 1 (one) | Defines the size of a record's block that must be read by a Historic before sending it to a database. For example, if this property is equal to 4 (four), blocks with four records each are sent to the associated Database object. Valid values for this property must be in the range between 1 (one) and … |
| `EnableQualityLogs` | Boolean | RW | type lib | EnableQualityLogs | nomeada | — | When in True, a Historic starts and Elipse E3 generates a record equal to the first collected record, but with bad quality (0) and a timestamp of minus one second. Server Objects 359 |
| `UseTagQuality` | Boolean | RW | type lib | UseQualityTag (apelido confirmado) | nomeada | — | If this property is set to True, a Historic uses Tag source's quality value. Otherwise, the old evaluation method is used, that is, 0: Uncertain value or 1: Good value. |
| `CompressedTable` | Boolean | RW | type lib | CompressedTable | nomeada | False | Enables using a dead band for data recording. Default value of this property is False. |
| `DeadBand` | Double | RW | type lib | DeadBand | nomeada | — | This property works with the CompressedTable property and indicates the calculated value over the last stored value, as a percentage, that defines whether this new value is stored or not. If the stored value is not a number, changing it forces all values to be stored. |
| `UserTable` | Boolean | R | type lib | UserTable | nomeada | — | When this property is set to True, identifies this Historic as a user's Historic, that is, its table data was imported from a database. Otherwise, it is an Elipse E3's regular Historic. This is a read-only property. |
| `Fields` | Object | R | type lib | — | não gravada nomeada | — | This property returns an object that represents a collection of Fields created in a Historic. This is a read-only property. For more information about the collection returned by this property, please check topic Fields. NOTES In applications created before Elipse E3 version 5.0, this property is a s… |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `CacheFields` | ULong |  | gravada no .prj | CacheFields | nomeada | — | sem equivalente na type lib |
| `NumberOfTables` | ULong |  | gravada no .prj | NumberOfTables | nomeada | — | sem equivalente na type lib |
| `NumberOfTimeUnits` | ULong |  | gravada no .prj | NumberOfTimeUnits | nomeada | — | sem equivalente na type lib |
| `RecordingType` | ULong |  | gravada no .prj | RecordingType | nomeada | — | sem equivalente na type lib |
| `Retries` | ULong |  | gravada no .prj | Retries | nomeada | — | sem equivalente na type lib |
| `SubType` | ULong |  | gravada no .prj | SubType | nomeada | — | sem equivalente na type lib |
| `TimeUnit` | ULong |  | gravada no .prj | TimeUnit | nomeada | — | sem equivalente na type lib |

**Métodos:** `WriteRecord()`; `StartAcquisition()`; `StopAcquisition()`

<a id="db-histfield"></a>
### HistField

- CLSID `{EE6C0BCE-CE5D-4B47-8195-7AE452D5F5CD}` · interface `IHistField`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 98 instâncias em 2 arquivo(s)
- HistField object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Field` | String | RW | type lib | Field | nomeada | an empty String, that is, uses the value of the … | This property determines the name of a Historic Field on the database table. Default value of this property is an empty String, that is, uses the value of the Name property as the name of this Field on the database table. If this property contains a value different from an empty String, that value i… |
| `Link` | BSTRSIMPLELINK | RW | type lib | Link | nomeada | — | This property determines a data source linked to this Historic Field. This property cannot be changed at run time for tables created by Historic objects, only on user-created tables. |
| `Type` | FieldTypes | RW | type lib | Type | nomeada | 1: fdInteger | This property indicates a data type for this Historic Field. Possible values for this property are 0: fdText, 1: fdInteger, 2: fdDouble, or 3: fdDateTime. Default value of this property is 1: fdInteger. |
| `Size` | Long | RW | type lib | Size | nomeada | 0 (zero) | This property indicates a size for this Historic Field. The value of this property is generally used for Fields whose Type property is equal to 0: fdText. This value cannot be negative and its default value is 0 (zero). |
| `PrimaryKey` | Boolean | RW | type lib | — | não gravada nomeada | False | This property indicates whether this Historic Field is used in the definition of a primary key for the Historic. Default value of this property is False. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Index` | ULong |  | gravada no .prj | Index | nomeada | — | sem equivalente na type lib |
| `OriginalType` | ULong |  | gravada no .prj | OriginalType | nomeada | — | sem equivalente na type lib |
| `Protected` | Boolean |  | gravada no .prj | Protected | nomeada | — | sem equivalente na type lib |
| `Quality` | ULong |  | gravada no .prj | Quality | nomeada | — | sem equivalente na type lib |

<a id="db-histfieldscollection"></a>
### HistFieldsCollection

- CLSID `{99BE1E99-07C0-48F5-AE03-443899FE1CD3}` · interface `IHistFieldsCollection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 2 arquivo(s)
- HistFieldsCollection object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `NextFieldIndex` | ULong |  | gravada no .prj | NextFieldIndex | nomeada | — | sem equivalente na type lib |

**Métodos:** `AddField(Name String, SourceLink String, Type FieldTypes, Size Long)`; `DeleteField(Index Variant)`

<a id="db-histindex"></a>
### HistIndex

- CLSID `{EE856D7F-A5A3-45E7-8761-E8FD7B3BD6CA}` · interface `IHistIndex`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 1 instâncias em 1 arquivo(s)
- HistIndex object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `IndexName` | String | RW | type lib | Index (apelido confirmado) | nomeada | an empty String | This property indicates the name of this Index on the database table. Default value of this property is an empty String. In this case, uses the name of this object as the name of the Index. If this property is filled, this value must be unique among the Indexes created for this Historic. 362 Server … |
| `Unique` | Boolean | RW | type lib | Unique | nomeada | False | This property defines whether the Fields composing this Index must have unique records on the database table. Default value of this property is False. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

<a id="db-histindexescollection"></a>
### HistIndexesCollection

- CLSID `{CC09B034-456B-42D8-A96D-255D4ABC89B8}` · interface `IHistIndexesCollection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 1 instâncias em 1 arquivo(s)
- HistIndexesCollection object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

<a id="db-histindexfield"></a>
### HistIndexField

- CLSID `{DD9926BD-314D-4F31-9278-CEC900F97C48}` · interface `IHistIndexField`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 5 instâncias em 1 arquivo(s)
- HistIndexField object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Field` | BSTRHISTFIELDNAME | RW | type lib | Field | nomeada | an empty String | Field This property defines the name of a field on the database table used as Index in this Historic. Default value of this property is an empty String. |
| `Order` | EFieldOrder | RW | type lib | — | não gravada nomeada | — | Order This property defines a sort order for this Field in the Index. The available options for this property are 0: foAscending (default) or 1: foDescending. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Sort` | Byte |  | gravada no .prj | Sort | nomeada | — | sem equivalente na type lib |

<a id="db-historian"></a>
### Historian

- CLSID `{FEE12933-5381-22D4-8E73-00C0DFB1AC67}` · interface `IHistorian`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Historian control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `DBServer` | BSTRDBLINK | RW | type lib | — | — | an empty String | Indicates a Database object used by this Storage to create tables and store data. Default value of this property is an empty String. |
| `TableName` | String | RW | type lib | — | — | — | Defines a name for a table used in this Storage. |
| `EnableDiscard` | Boolean | RW | type lib | — | — | False | Enables Storage data discarding after a certain period of time. If set to False, data is stored indefinitely on a table. Otherwise, data is discarded after a certain period of time. Default value of this property is False. |
| `DiscardInterval` | Long | RW | type lib | — | — | 1 (one time unit indicated by the DiscardTimeUni… | This property works with the DiscardTimeUnit property. This property indicates a time interval in which Storage data remains stored on a database table, until it is discarded. Default value of this property is 1 (one time unit indicated by the DiscardTimeUnit property). If this property is set to a … |
| `DiscardTimeUnit` | DBTimeUnit | RW | type lib | — | — | — | This property works with the DiscardInterval property. This property indicates a time unit in which Storage data remains stored until it is discarded. Available options are 0 - dtHour: Hours, 1 - dtDay: Days, 2 - dtMonth: Months (default), or 3 - dtMinute: Minutes. |
| `VerificationInterval` | Long | RW | type lib | — | — | 1 (one time unit indicated by the VerificationUn… | This property works with the VerificationUnit property to control the time interval in which Elipse E3 checks how old Storage data is, to discard it later. Default value of this property is 1 (one time unit indicated by the VerificationUnit property). |
| `VerificationUnit` | DBTimeUnit | RW | type lib | — | — | — | This property works with the VerificationInternal property. This property indicates a time unit in which a Storage data discard verification is performed. Available options are 0 - dtHour: Hours, 1 - dtDay: Days, 2 - dtMonth: Months (default), or 3 - dtMinute: Minutes. |
| `EnableBackupTable` | Boolean | RW | type lib | — | — | False | Creates a backup table where discarded Storage data remains for security reasons. If set to True, this table is created. Otherwise, there is no backup table. Default value of this property is False. |
| `CacheSize` | Long | RW | type lib | — | — | 10 | Defines the size of a record's block that must be read by a Storage before sending it to a database. For example, if this property is equal to 4 (four), blocks with four records each are sent to the associated Database object. Default value of this property is 10. A record block is sent every second… |
| `StringFieldSize` | Long | RW | type lib | — | — | — | This property specifies the maximum size that String-type Fields of a Storage can have (this is the size used when creating a Value field of the Strings table). |
| `CompressionRate` | Double | R | type lib | — | — | — | Displays the data compression rate obtained until now. This is a read-only property. |
| `BackupDiscardInterval` | Long | RW | type lib | — | — | 12 (twelve time units indicated by the BackupDis… | Indicates a maximum time interval, in minutes, hours, days, or months, for Storage data on the backup table until it is discarded, regardless of the time data remains on the main table. For example, to keep data for 24 months on the main table and six more months on the backup table, this option's v… |
| `BackupDiscardTimeUnit` | DBTimeUnit | RW | type lib | — | — | — | This property indicates the time unit in which Storage backup data remains stored until it is discarded. Available options are 0 - dtHour: Hours, 1 - dtDay: Days, 2 - dtMonth: Months (default), or 3 - dtMinute: Minutes. This property works with the BackupDiscardInterval property. |
| `Fields` | Object | R | type lib | — | — | — | This property returns an object that represents a collection of Fields created in a Storage and it is a read-only property. For more information about the collection returned by this property, please check topic Fields. Server Objects 379 NOTES In applications created before Elipse E3 version 5.0, t… |

**Métodos:** `StartAcquisition()`; `StopAcquisition()`; `CreateNewSession(DefaultType EStorageFieldType, DefaultMinRecTime ULong, DefaultMaxRecTime ULong, DefaultDeadBand Double, DefaultDeadBandUnit Int, DefaultScanTime ULong)`

<a id="db-histprimarykey"></a>
### HistPrimaryKey

- CLSID `{FF603DA0-70A5-4DE6-8E54-9B3FD8D84CAD}` · interface `IHistPrimaryKey`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 1 instâncias em 1 arquivo(s)
- HistPrimaryKey object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `KeyName` | String | RW | type lib | KeyName | nomeada | — | Returns/sets the name of this primary key in the database |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

<a id="db-histprimarykeyfield"></a>
### HistPrimaryKeyField

- CLSID `{FF6FA59C-A1F7-4F5C-9957-E979F36AF7C5}` · interface `IHistPrimaryKeyField`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- HistPrimaryKeyField object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Field` | BSTRHISTFIELDNAME | RW | type lib | — | — | an empty String | This property defines the name of a field on the database table used as a Primary Key in the Historic. Default value of this property is an empty String. |
| `Order` | EFieldOrder | RW | type lib | — | — | — | This property defines a sort order for this Field in the Primary Key. The available options for this property are 0: foAscending (default) or 1: foDescending. |

<a id="db-histserver"></a>
### HistServer

- CLSID `{1E4DB056-1FFE-4060-BB8F-ABCB057F5C54}` · interface `IHistServer`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 1 arquivo(s)
- Hist Server control

<a id="db-istoragefield"></a>
### IStorageField

- CLSID `{113A5FB2-1B92-4CE7-ADD3-F92B3CCB3906}` · interface `IIStorageField`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- StorageField

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Link` | BSTRSIMPLELINK | RW | type lib | — | — | — | Determines a data source linked to this Storage Field. This property cannot be changed at run time, even if this Storage Field is inactive. |
| `Type` | EStorageFieldType | RW | type lib | — | — | — | Returns a data type of a Storage Field in Storage's format. This property is for reading and writing, but only accepts changes while data collecting for this Storage Field have not started yet. Possible values for this property are 0: Double (default), 1: Bit, 2: Text, or 3: Integer. 382 Server Obje… |
| `MinRecTime` | Long | RW | type lib | — | — | — | Minimum difference, in milliseconds, between timestamps of any two records with the same quality stored on a database, that is, the minimum time to store new data. This parameter is used to limit the number of records written to a database, in case a Tag experiences abrupt variations in its value. T… |
| `MaxRecTime` | Long | RW | type lib | — | — | 3600 (one hour) | Maximum difference, in seconds, between timestamps of two consecutive records stored in a database, that is, the maximum time without storing any data. For example, if a Tag is not varying its value, even then the current value must be written to the database whenever the number of seconds configure… |
| `DeadBand` | Double | RW | type lib | — | — | 1 (one) | Dead band used to calculate Storage's algorithm. Indicates a precision users are willing to loose in each Storage Field to store. The higher the value of this property, the more compact the database (less data is stored). This value can be specified in absolute units or as a percentage of Tag's curr… |
| `DeadBandUnit` | DeadBandUnit | RW | type lib | — | — | 0 (zero) | Unit of the DeadBand property. This value can be specified as a percentage of Tag's current value (0: dbPercent) or in absolute units (1: dbAbsolute). Default value of this property is 0 (zero). |
| `ScanTime` | Long | RW | type lib | — | — | — | Returns or configures a scan time in milliseconds of a Storage Field, that is, how often a Tag's value is sent back to data compression algorithm, if it is not varying. If this property's value is equal to 0 (zero), the value of the MaxRecTime property is used for the same purpose (default behavior)… |

<a id="db-istoragefieldscollection"></a>
### IStorageFieldsCollection

- CLSID `{44C12135-F117-4DE4-A01B-F91EF2A23F57}` · interface `IIStorageFieldsCollection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- StorageFields Collection

**Métodos:** `AddField(FieldLink String, FieldName Variant, FieldType Variant, FieldMinRecTime Variant, FieldMaxRecTime Variant, FieldScanTime Variant, FieldDeadBand Variant, FieldDeadBandUnit Variant)`; `RemoveAll()`; `DeleteField(Index Variant)`

<a id="db-rocalarm"></a>
### ROCAlarm

- CLSID `{F49D00B1-4343-4840-BA5A-9458B088B27D}` · interface `IROCAlarm`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Rate-of-change Alarm Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Name assigned to the condition |
| `ConditionName` | String | R | type lib | — | — | — | Name assigned to the condition |
| `Delay` | Long | RW | type lib | — | — | — | Delay in ms before entering/leaving alarm condition |
| `ROCReturnMessageText` | String | RW | type lib | — | — | — | Returning message for this Rate-of-Change-type of Alarm. |
| `ROC` | Boolean | RW | type lib | — | — | — | Enables or disables a check on a Rate-of-Change-type of Alarm. |
| `ROCLimit` | Double | RW | type lib | — | — | — | Limit for this Rate-of-Change-type of Alarm. For this Alarm to occur, it is enough that the value of the associated Tag exceeds this value by one second. |
| `ROCMessageText` | String | RW | type lib | — | — | — | A text message for this Rate-of-Change-type of Alarm. |
| `ROCSeverity` | EAlarmSeverity | RW | type lib | — | — | — | Importance of this Rate-of-Change-type of Alarm. Possible values for this property are -2: Critical, 0: High, 1: Medium, or 2: Low. |
| `ROCAckRequired` | Boolean | RW | type lib | — | — | — | Indicates whether this Rate-of-Change-type of Alarm requires acknowledgment or not. |
| `ROCAllowShelving` | Boolean | RW | type lib | — | — | True | Indicates whether this Rate-of-Change-type of Alarm or Event can be shelved. The default value of this property is True. |
| `ROCShelveMaxDuration` | Long | RW | type lib | — | — | 60 (one hour) | Defines a maximum duration, in minutes, for shelving this Rate-of-Change-type of Alarm or Event. The default value of this property is 60 (one hour). |
| `ROCShelveMaxCount` | Long | RW | type lib | — | — | 0 (zero), that is, no limits for shelving | Defines how many times this Rate-of-Change-type of Alarm or Event can be shelved. The default value of this property is 0 (zero), that is, no limits for shelving. |

<a id="db-storagesession"></a>
### StorageSession

- CLSID `{A43CF9F1-0A42-4FAE-9AA9-3D12B6EA576A}` · interface `IStorageSession`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- StorageSession control

**Métodos:** `AddField(FieldName String, Type Variant, MinRecTime Variant, MaxRecTime Variant, DeadBand Variant, DeadBandUnit Variant, ScanTime Variant)`; `AddValue(FieldName String, Timestamp Date, Quality UShort, Value Variant)`; `Commit()`

### Enumerações de DB

- **DBSourceType**: stUnknown=-1, stAccess=0, stOracle=1, stSqlServer=2, stPostgreSQL=3, stMySQL=4
- **DBSubType**: stContinuous=0, stBatch=1
- **DBTimeUnit**: dtHour=0, dtDay=1, dtMonth=2, dtMinute=3
- **DBType**: dtColumns=0
- **DeadBandUnit**: dbPercent=0, dbAbsolute=1
- **EAlarmSeverity**: asCritical=-2, asInvalid=-1, asHigh=0, asMedium=1, asLow=2
- **EFieldOrder**: foAscending=0, foDescending=1
- **EStorageFieldType**: eStorageDouble=0, eStorageBit=1, eStorageText=2, eStorageInteger=3
- **ESubConditionKind**: eSubConditionAlarm=0, eSubConditionEvent=1, eSubConditionExit=2
- **EventFieldType**: AckRequired=1, Acked=2, ActorID=3, ChangeMask=4, ConditionName=5, ConditionActive=6, Cookie=7, Enabled=8, EventCategory=9, EventType=10, Message=11, Quality=12, Severity=13, Source=14, SubConditionName=15, EventTime=16, EventTimeUTC=17, CurrentValue=18, AlarmArea=19, AlarmSourceName=20, EventTimeMS=21, InTime=22, InTimeMS=23, OutTime=24, OutTimeMS=25, AckTime=26, AckTimeMS=27, FullAlarmSourceName=28, FormattedValue=29, InTimeDbl=30, OutTimeDbl=31, AckTimeDbl=32, EventTimeDbl=33, EventCLSID=34, ActiveSource=35, Unbound=36, Deleted=37, AllowShelving=38, Shelved=39, ShelvedTime=40, ShelvedOutTime=41, ShelveDuration=42, ShelveMaxDuration=43, ShelveCount=44, ShelveMaxCount=45, ShelveActorID=46, ShelveReason=47, E3TimeStamp=48, Suppressed=49, SuppressedTime=50, SequentialNumber=51, AlarmState=52, ShelvedExpirationTime=53, OutOfService=54, OutOfServiceTime=55, ReturnToServiceTime=56, OutOfServiceReason=57, OutOfServiceActorID=58, UserFieldFirst=1073741823
- **FieldTypes**: fdText=0, fdInteger=1, fdDouble=2, fdDateTime=3, fdNone=4, fdGUID=5
- **SqlNetworkLibrary**: nlDefault=0, nlNamedPipes=1, nlTcpIp=2, nlSpxIpx=3, nlBanyanVines=4, nlMultiProtocol=5
- **SqlProvider**: SQLOLEDB=1, MSOLEDBSQL=2
- **tagEUserFieldValueSource**: evsInherited=0, evsLink=1, evsForcedValue=2

---

## IODrv

Arquivo `IODrv.e3` · versão 1.1 · LIBID `{F8C27E94-596D-11D4-A662-000021FA1539}` · E3 IODrv Library 1.1

Classes: [IOBlock](#iodrv-ioblock), [IOBlockElement](#iodrv-ioblockelement), [IODriver](#iodrv-iodriver), [IOFolder](#iodrv-iofolder), [IOTag](#iodrv-iotag), [OPCDriver](#iodrv-opcdriver), [OPCElementBlock](#iodrv-opcelementblock), [OPCFolder](#iodrv-opcfolder), [OPCGroup](#iodrv-opcgroup), [OPCTag](#iodrv-opctag), [OPCTagBlock](#iodrv-opctagblock), [UaDriver](#iodrv-uadriver), [UaElementBlock](#iodrv-uaelementblock), [UaFolder](#iodrv-uafolder), [UaSubscription](#iodrv-uasubscription), [UaTag](#iodrv-uatag), [UaTagBlock](#iodrv-uatagblock)

<a id="iodrv-ioblock"></a>
### IOBlock

- CLSID `{951E092F-1429-43BC-997C-A82F432FC990}` · interface `IIOBlock` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 86 instâncias em 2 arquivo(s)
- IOBlock Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Scan` | Long | RW | type lib | Scan | nomeada | 1,000, or one second | Specifies which scan time is used by the server to update an I/O Block. This property is represented in milliseconds and can be modified after communication starts, and it is used only when the AllowRead property is set to True. When users set this property in several I/O Blocks in an application, i… |
| `Quality` | Byte | R | type lib | — | não gravada nomeada | 0 (zero, Bad Quality) | This property informs the quality of the value contained in the Value property. Each time an I/O Driver sets a new value to an I/O Block, it also sets a quality for that data. This is a read-only property. The default value of this property is 0 (zero, Bad Quality). For more information about qualit… |
| `AllowRead` | Boolean | RW | type lib | AllowRead | nomeada | True | Defines whether this I/O Block is read by the I/O Driver. If this property is enabled, the I/O Driver automatically updates all I/O Block Elements inserted in this I/O Block, in time spans defined by the Scan property. Otherwise, this I/O Block is neither read nor updated. The default value of this … |
| `AllowWrite` | Boolean | RW | type lib | AllowWrite | nomeada | — | Defines whether this I/O Block is written automatically when the Value property of its I/O Block Elements is modified. If this property is set to True, all changes are sent to the device associated to the I/O Driver. Otherwise, all modifications are ignored. I/O Block Elements do not accept values i… |
| `TimeStamp` | Date | RW | type lib | — | não gravada nomeada | "00:00:00" | This property is updated whenever there is a change in value or status in either the Value or the Quality properties. This property Informs which is the date and time associated to both value and quality in an I/O Block. This is a read- only property. The default value of this property is "00:00:00"… |
| `EnableDriverEvent` | Boolean | RW | type lib | EnableDriverEvent | nomeada | — | This property is used to control the generation of OnTagRead events, which occur in the I/O Driver that contains this I/O Block. If this property of an I/O Tag is set to True, the OnTagRead event generation is then enabled for that I/O Block. Otherwise, it does not occur. I/O Tags, I/O Blocks, and I… |
| `AdviseType` | AdviseTypes | RW | type lib | AdviseType | nomeada | — | Controls the Advise mode. The available options are described on the next table. Available options for the AdviseType property 0 - AlwaysInAdvise The I/O Block is updated if the AllowRead property is set to True 1 - AdviseWhenLinked The I/O Block is updated only if the AllowRead property is set to T… |
| `EnableDeadband` | Boolean | RW | type lib | EnableDeadband | nomeada | True | Enables or disables the PercentDeadBand property of I/O Block Elements. If this property is set to True, the I/O Block value is only updated when it changes, and its new value exceeds the limit defined by the PercentDeadBand property of any of its I/O Block Elements. Otherwise, this I/O Block is alw… |
| `B1` | Long | RW | type lib | B# (família) | nomeada | — | Specifies to which data set in the device this I/O Block is linked. Please check Driver's documentation for appropriate parameters. This property can be modified once communication starts. The next script contains an example of using this property. Sub Block1_BeforeStart() B1 = 2 B2 = 1 B3 = 9600 Se… |
| `B2` | Long | RW | type lib | B# (família) | nomeada | — | Specifies to which data set in the device this I/O Block is linked. Please check Driver's documentation for appropriate parameters. This property can be modified once communication starts. The next script contains an example of using this property. Sub Block1_BeforeStart() B1 = 2 B2 = 1 B3 = 9600 |
| `B3` | Long | RW | type lib | B# (família) | nomeada | — | Specifies to which data set in the device this I/O Block is linked. Please check Driver's documentation for appropriate parameters. This property can be modified once communication starts. The next script contains an example of using this property. Sub Block1_BeforeStart() B1 = 2 B2 = 1 B3 = 9600 |
| `B4` | Long | RW | type lib | B# (família) | nomeada | — | Specifies to which data set in the device this I/O Block is linked. Please check Driver's documentation for appropriate parameters. This property can be modified once communication starts. The next script contains an example of using this property. Sub Block1_BeforeStart() B1 = 2 B2 = 1 B3 = 9600 B4… |
| `Size` | Long | RW | type lib | Size | nomeada | 0 (zero) | Defines the size of value sets in this I/O Block. Please check Driver's documentation for this property's limits, according to B1 to B4 parameters. By creating I/O Block Elements, users can access reading and writing values for the device. The default value of this property is 0 (zero). The next scr… |
| `ParamDevice` | String | RW | type lib | ParamDevice | nomeada | — | Defines the address of the device accessed by this I/O Block. This property is inherited from the I/O Driver, but its value can be overridden, if necessary. 314 Server Objects |
| `ParamItem` | String | RW | type lib | ParamItem | nomeada | — | Identifies data accessed by this I/O Block from the device. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Inherit#` | ULong | RW | framework | Inherit# | nomeada | — | Herança de configuração (família numerada) |
| `B#` | UShort |  | gravada no .prj | B# | nomeada | — | sem equivalente na type lib (família: 4) |
| `FormatB#` | Byte |  | gravada no .prj | FormatB# | nomeada | — | sem equivalente na type lib (família: 4) |

**Métodos:** `Write(EWriteSyncMode EWriteSyncMode)`; `WriteEx(Value Variant, TimeStamp Variant, Quality ULong, WriteStatus Variant, EWriteSyncMode EWriteSyncMode)`

**Eventos:** `OnRead()`

<a id="iodrv-ioblockelement"></a>
### IOBlockElement

- CLSID `{7B2DDE33-7C81-4AAF-B8C7-A18DBCD04366}` · interface `IIOBlockElement`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 344 instâncias em 2 arquivo(s)
- IOElementBlock Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | — | não gravada nomeada | empty | Value Updated whenever a new valid reading from a device is performed, using N1 to N4 configuration of the I/O Block where this I/O Block Element is inserted, and considering its position on the table read from the Index property. Data type of this variable, such as integer, floating point, or text,… |
| `RawValue` | Variant | RW | type lib | — | não gravada nomeada | — | RawValue Accesses this I/O Block Element's original value previous to the scale, that is, regardless of how the EnableScaling property is configured. Therefore, if this property is set to False, the Value property and this property behave identically. |
| `Index` | Long | RW | type lib | Index | nomeada | — | Index Specifies this I/O Block Element's position among the other Elements configured by the I/O Block's Size property where it is inserted. This property accepts values between 0 (zero) and a value less than the value defined in the Size Server Objects 317 property. For example, when configuring an… |
| `Quality` | Byte | R | type lib | — | não gravada nomeada | 0 (zero, Bad Quality) | Quality This property informs the quality of the value contained in the Value property. Each time an I/O Driver attributes a new value to the I/O Block Element, it also sets the quality of that data. This is a read-only property. The default value of this property is 0 (zero, Bad Quality). For more … |
| `EU` | String | RW | type lib | EU | nomeada | empty | EU This property is used to identify which engineering unit its value represents, such as degrees, meters, or KW/h. The default value of this property is empty. The next script contains an example of using this property. Sub Tag_OnStartRunning() ' Adjusts the scale of temperature ' ranging from 0 to… |
| `PercentDeadband` | Double | RW | type lib | PercDeadband (apelido confirmado) | nomeada | 0 (zero) | PercentDeadBand This property determines a minimum variation or dead band of an I/O Block Element's value, so that this value is updated in Elipse E3. This value is specified as a percentage of the difference between DeviceHigh and DeviceLow properties. This property is only used if I/O Block's Enab… |
| `EnableScaling` | Boolean | RW | type lib | Scaling (apelido confirmado) | nomeada | False | EnableScaling This property enables or disables a scale of values for the value sent to or received from a device. If this property is set to True, all values from the device receive scale adjustments according to the DeviceHigh, DeviceLow, EUHigh, and EULow properties before setting them to the Val… |
| `DeviceLow` | Double | RW | type lib | DevLow (apelido confirmado) | nomeada | 0 (zero) | DeviceLow This property defines the lowest value reached by an I/O Block Element in the device. This property is used in the calculation of the PercentDeadBand property's value, and also to adjust the device's scale value before setting it to the Value property. Likewise, the inverse operation is pe… |
| `DeviceHigh` | Double | RW | type lib | DevHigh (apelido confirmado) | nomeada | 1,000 | DeviceHigh This property defines the highest value reached by an I/O Block Element in the device. This property is used in the calculation of the PercentDeadBand property's value, and also to adjust the device's scale value before setting it to the Value property. Likewise, the inverse operation is … |
| `EULow` | Double | RW | type lib | EULow | nomeada | 0 (zero) | EULow Defines the lowest value to attribute to the Value property, adjusting the scale to the value from the device before this attribution. Likewise, the inverse operation is performed before sending the value to the I/O Driver, when writing. This conversion happens only when the EnableScaling prop… |
| `EUHigh` | Double | RW | type lib | EUHigh | nomeada | 1,000 | EUHigh Defines the highest value to attribute to the Value property, adjusting the scale to the value from the device before this attribution. Likewise, the inverse operation is performed before sending the value to the I/O Driver, when writing. This conversion happens only when the EnableScaling pr… |
| `UseBitFields` | Boolean | RW | type lib | UseBitFields | nomeada | False | UseBitFields If this property is set to True, every time the value in the Value property changes, the bits referring to Bit00 to Bit31 properties are updated. Also, updates the value of the Value property every time any Bit00 to Bit31 properties change their values and then sent to a device if I/O B… |
| `Bit00` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 0 |
| `Bit01` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 1 |
| `Bit02` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 2 |
| `Bit03` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 3 |
| `Bit04` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 4 |
| `Bit05` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 5 |
| `Bit06` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 6 |
| `Bit07` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 7 |
| `Bit08` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 8 |
| `Bit09` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 9 |
| `Bit10` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 10 |
| `Bit11` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 11 |
| `Bit12` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 12 |
| `Bit13` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 13 |
| `Bit14` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 14 |
| `Bit15` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 15 |
| `Bit16` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 16 |
| `Bit17` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 17 |
| `Bit18` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 18 |
| `Bit19` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 19 |
| `Bit20` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 20 |
| `Bit21` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 21 |
| `Bit22` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 22 |
| `Bit23` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 23 |
| `Bit24` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 24 |
| `Bit25` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 25 |
| `Bit26` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 26 |
| `Bit27` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 27 |
| `Bit28` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 28 |
| `Bit29` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 29 |
| `Bit30` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 30 |
| `Bit31` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 31 |
| `EnableDriverEvent` | Boolean | RW | type lib | EnableDriverEvent | nomeada | — | EnableDriverEvent This property is used to control the generation of the OnTagRead event, which occurs in the I/O Driver that contains the I/O Block Element. If this I/O Block Element's property is set to True, then the OnTagRead event generation is enabled by the I/O Block Element. Otherwise, it do… |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |

**Métodos:** `Write(WriteSyncMode EWriteSyncMode)`; `WriteEx(Value Variant, TimeStamp Variant, Quality ULong, WriteStatus Variant, WriteSyncMode EWriteSyncMode)`

<a id="iodrv-iodriver"></a>
### IODriver

- CLSID `{CC264052-5BC6-11D4-A663-000021FA1539}` · interface `IIODriver` · eventos `DIODriverEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 57 instâncias em 29 arquivo(s)
- IODriver Server

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `DriverLocation` | BSTRFILE | RW | type lib | _DriverLocation (apelido confirmado) | nomeada | an empty String | Defines which Driver is used by this I/O Driver object to communicate with a device. This property accepts a String with the complete Driver's path, in case it is not in the same Domain's directory, or the relative Driver's path if it is in the same Domain's directory. In case there is no open Domai… |
| `DriverName` | String | R | type lib | — | não gravada nomeada | — | Contains a String describing the library associated to this I/O Driver object. For this, users must first set the DriverLocation property. This is a read-only property. In case of error loading the library of a linked Driver, that is, a file with the .dll extension, this property show the returned e… |
| `P1` | Long | RW | type lib | P# (família) | nomeada | 0 (zero) | Use the P1 property to configure an I/O Driver. Please check Driver's documentation to correctly set its parameters. This property cannot be modified after communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. Sub Driver1_Be… |
| `P2` | Long | RW | type lib | P# (família) | nomeada | 0 (zero) | Use the P2 property to configure an I/O Driver. Please check Driver's documentation to correctly set its parameters. This property cannot be modified after communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. Sub Driver1_Be… |
| `P3` | Long | RW | type lib | P# (família) | nomeada | 0 (zero) | Use the P3 property to configure an I/O Driver. Please check Driver's documentation to correctly set its parameters. This property cannot be modified after communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. Sub Driver1_Be… |
| `P4` | Long | RW | type lib | P# (família) | nomeada | 0 (zero) | Use the P4 property to configure an I/O Driver. Please check Driver's documentation to correctly set its parameters. This property cannot be modified after communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. Sub Driver1_Be… |
| `ShareServer` | Boolean | RW | type lib | ShareServer | nomeada | False | If this property is set to True, this I/O Driver shares its execution among all other I/O Drivers with the same String in the DriverLocation property. This means that only the first configured I/O Driver executes the communication's initialization procedure. All other shared I/O Drivers ignore all s… |
| `ShareMaximum` | Long | RW | type lib | ShareMaximum | nomeada | — | This property defines the maximum number of I/O Drivers that are grouped into a shared I/O Server. This property is only used when the ShareServer property is enabled. The next script contains an example of using this property. ' This driver will not be shared ShareServer = False ShareMaximum = <any… |
| `ReadRetries` | Long | RW | type lib | ReadRetries | nomeada | — | Indicates the number of I/O Driver's reading retries, in case of error. If it is set to 2 (two), for example, this means that this I/O Driver retries failed communications twice, apart from the original try. |
| `WriteRetries` | Long | RW | type lib | WriteRetries | nomeada | — | Indicates the number of I/O Driver's writing retries, in case of error. If it is set to 2 (two), for example, this means this I/O Driver retries a failed communication twice, apart from the original try. |
| `WriteFeedbackMode` | WriteFeedbackModes | RW | type lib | WriteMode (apelido a confirmar) | nomeada | — | This property allows controlling writing feedback confirmation to I/O Tags. It applies only to readable I/O Tags, that is, I/O Tags whose AllowRead property is set to True. Through this property, reading I/O Tags that receive writings is quicker. This property contains the configuration options desc… |
| `WriteSyncMode` | EWriteSyncMode | RW | type lib | WriteSyncMode | nomeada | — | Determines how writings are sent to the I/O Server, in synchronous or asynchronous mode. This property contains the configuration options described on the next table. Available options for the WriteSyncMode property 0 - wsmDefault Synchronous mode. This is the default value 1 - wsmSync Synchronous m… |
| `AsyncBatchSize` | Long | RW | type lib | AsyncBatchSize | nomeada | -1 (minus one), that is, grouping is defined in … | This property defines the maximum number of operations per I/O Driver on E3Run's memory before sending them to an I/O Server. Possible values for this property range from 2 (two) to 100000. The value 0 (zero) disables grouping operations for this I/O Driver. The default value of this property is -1 … |
| `AsyncBatchFlushTimeMs` | Long | RW | type lib | AsyncBatchFlushTimeMs | nomeada | -1 (minus one), that is, the waiting time is def… | This property defines the maximum time an asynchronous operation can wait in E3Run before it is sent to an I/O Server. Possible values for this property range between 10 and 10000 (10 seconds). Values less than 10 use the value of 10 milliseconds. The default value of this property is -1 (minus one)… |
| `EnableReadGrouping` | Boolean | RW | type lib | ReadGrouping (apelido confirmado) | nomeada | True | Enables reading optimizations or automatic I/O Tag grouping. This property cannot be changed while this object is active. The default value of this property is True. Reading optimizations only happens if this I/O Driver supports this feature. |
| `ParamDevice` | String | RW | type lib | ParamDevice | nomeada | — | Defines the address of a device accessed by this I/O Driver. This property is inherited by this object's I/O Tags, which can override this value, if necessary. |
| `DisableIOServerPool` | Boolean | RW | type lib | DisablePool (apelido confirmado) | nomeada | False | Forces this I/O Driver to not participate in the Pool of I/O Server processes, that is, this I/O Driver executes in an exclusive I/O Server. The default value of this property is False. For more information, please check topic Pool of I/O Server Processes on Elipse E3 User's Manual. |
| `WriteNullAsEmpty` | Boolean | RW | type lib | WriteNullAsEmpty | nomeada | False | This property allows an I/O Driver to convert a value received as Null to Empty in cases where that I/O Driver does not accept null values. Both value's quality and timestamp are propagated unchanged, except on cases where the value received as Null contains a good quality. In these situations, this… |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Expose` | ULong | RW | framework | Expose | nomeada | — | Expõe o objeto (flag de framework) |
| `Inherit#` | ULong | RW | framework | Inherit# | nomeada | — | Herança de configuração (família numerada) |
| `DriverData` | String |  | gravada no .prj | DriverData | nomeada | — | sem equivalente na type lib |
| `FormatP#` | Byte |  | gravada no .prj | FormatP# | nomeada | — | sem equivalente na type lib (família: 4) |
| `P#` | UShort |  | gravada no .prj | P# | nomeada | — | sem equivalente na type lib (família: 4) |

**Métodos:** `Write(N1 Long, N2 Long, N3 Long, N4 Long, Value Variant, WriteSyncMode EWriteSyncMode)`; `WriteEx(N1 Long, N2 Long, N3 Long, N4 Long, Value Variant, TimeStamp Variant, Quality ULong, WriteStatus Variant, WriteSyncMode EWriteSyncMode)`

**Eventos:** `OnCommError(EvtType Integer, Size Integer, Element Integer, N1 Long, N2 Long, N3 Long, N4 Long)`; `OnCommErrorEx(ErrorInfo ICommErrorInfo)`; `BeforeStart()`; `AfterStart()`; `BeforeStop()`; `AfterStop()`; `OnTagRead(Tag Object)`; `OnTagWrite(Tag Object, Succeeded Boolean, User String)`

<a id="iodrv-iofolder"></a>
### IOFolder

- CLSID `{1F75BDD2-5BC8-11D4-A663-000021FA1539}` · interface `IIOFolder`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 20817 instâncias em 29 arquivo(s)
- IOFolder Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ParamDevice` | String | RW | type lib | ParamDevice | nomeada | — | Defines the address of the device accessed by this I/O Folder. This property is inherited from the I/O Driver, and its value can be overwritten, if needed. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Expose` | ULong | RW | framework | Expose | nomeada | — | Expõe o objeto (flag de framework) |
| `Inherit#` | ULong | RW | framework | Inherit# | nomeada | — | Herança de configuração (família numerada) |

<a id="iodrv-iotag"></a>
### IOTag

- CLSID `{1F75BDC2-5BC8-11D4-A663-000021FA1539}` · interface `IIOTag` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 140306 instâncias em 29 arquivo(s)
- IOTag Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Scan` | Long | RW | type lib | Scan | nomeada | 1,000 (1 second) | Use this property to specify a scan time used by the server to update the Value property. This property is represented in milliseconds and can be modified after communication starts, and it is used only when the AllowRead property is set to True. When configuring this property in several application… |
| `Quality` | Byte | R | type lib | — | não gravada nomeada | 0 (zero, Bad Quality) | This property informs the quality of the value contained in the Value property. Each time an I/O Driver sets a new value to an I/O Tag, it also configures the quality of that data. This is a read-only property. The default value of this property is 0 (zero, Bad Quality). For more information about q… |
| `AllowRead` | Boolean | RW | type lib | AllowRead | nomeada | True | Configure this property to define whether this I/O Tag is read by the I/O Driver or not. If this property is set to True, the I/O Driver automatically updates Value, from Bit00 to Bit31, and RawValue properties, in time spans defined by the Scan property. Otherwise, this I/O Tag is not read. The def… |
| `AllowWrite` | Boolean | RW | type lib | AllowWrite | nomeada | True | Configure this property to define whether this I/O Tag must be written or not automatically when the Value, from Bit00 to Bit31, or RawValue properties are modified. If this property is set to True, these changes are sent to the device associated to the I/O Driver. Otherwise, changes are ignored. Th… |
| `TimeStamp` | Date | RW | type lib | — | não gravada nomeada | "00:00:00" | This property is updated whenever a change occurs in value or status in either Value or Quality properties. It informs a time stamp associated to both value and quality in an I/O Tag. This is a read-only property. The default value of this property is "00:00:00". ⚠ manual: somente leitura |
| `EnableDriverEvent` | Boolean | RW | type lib | EnableDriverEvent | nomeada | — | This property is used to control the generation of the OnTagRead event, which occurs in the I/O Driver that contains this I/O Tag. If this property is set to True, then this I/O Tag's OnTagRead event is enabled. Otherwise, it is disabled. I/O Tags, I/O Blocks, and I/O Block Elements can generate thi… |
| `AdviseType` | AdviseTypes | RW | type lib | AdviseType | nomeada | — | Controls the Advise mode. The available options are described on the next table. Available options for the AdviseType property 0 - AlwaysInAdvise This I/O Tag is kept updated if the AllowRead property is equal to True 1 - AdviseWhenLinked This I/O Tag is only updated if the AllowRead is equal to Tru… |
| `EnableDeadband` | Boolean | RW | type lib | EnableDeadband | nomeada | True | This enables or disables the PercentDeadBand property. If this property is set to True, I/O Tag's value is only updated when it changes, and its new value exceeds the limit defined by the PercentDeadBand property. Otherwise, the I/O Tag is always updated, and the dead band limit is not checked. Alwa… |
| `Value` | Variant | RW | type lib | — | não gravada nomeada | empty | Updated whenever a new valid reading from a device is performed, using N1 to N4 parameter configuration. Data type of this variable, such as integer, floating point, or text, depends on the I/O Driver to which the I/O Tag is associated and its configuration. This property is only updated this way if… |
| `RawValue` | Variant | RW | type lib | — | não gravada nomeada | — | Accesses I/O Tag's original value before the scale, that is, regardless of the configuration on the EnableScaling property. Therefore, if this property is set to False, the Value property and this property behave identically. |
| `N1` | Long | RW | type lib | N# (família) | nomeada | 0 (zero) | Specifies the device's variable that this I/O Tag is linked to. Please check Driver's documentation for an appropriate configuration. This property can be modified once communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. S… |
| `N2` | Long | RW | type lib | N# (família) | nomeada | 0 (zero) | Specifies the device's variable that this I/O Tag is linked to. Please check Driver's documentation for an appropriate configuration. This property can be modified once communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. S… |
| `N3` | Long | RW | type lib | N# (família) | nomeada | 0 (zero) | Specifies the device's variable that this I/O Tag is linked to. Please check Driver's documentation for an appropriate configuration. This property can be modified once communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. S… |
| `N4` | Long | RW | type lib | N# (família) | nomeada | 0 (zero) | Specifies the device's variable that this I/O Tag is linked to. Please check Driver's documentation for an appropriate configuration. This property can be modified once communication starts. The default value of this property is 0 (zero). The next script contains an example of using this property. S… |
| `ParamDevice` | String | RW | type lib | ParamDevice | nomeada | — | Defines the address of a device accessed by this I/O Tag. This property is inherited from the I/O Driver, but its value can be overwritten, if necessary. |
| `ParamItem` | String | RW | type lib | ParamItem | nomeada | — | Identifies data this I/O Tag accesses from a device. |
| `EU` | String | RW | type lib | EU | nomeada | empty | This property is used to identify the engineering unit that the value represents, such as degrees, meters, or KW/h. The default value of this property is empty. The next script contains an example of using this property. Sub Tag_OnStartRunning() ' Adjusts the scale of temperature ' ranging from 0 to… |
| `PercentDeadband` | Double | RW | type lib | PercDeadband (apelido confirmado) | nomeada | 0 (zero) | This property determines the minimum variation of an I/O Tag's value or dead band, so that this value can be updated on Elipse E3. This value is specified as a percentage of the difference between DeviceHigh and DeviceLow properties. This property is only used if I/O Tag's EnableDeadBand property is… |
| `EnableScaling` | Boolean | RW | type lib | Scaling (apelido confirmado) | nomeada | — | This property enables or disables a value scale for the value sent to or received from a device. If this property is set to True, all values from the device receive scale adjustments in DeviceHigh, DeviceLow, EUHigh and EULow properties before setting it to the Value property. Otherwise, no scale ad… |
| `DeviceLow` | Double | RW | type lib | DevLow (apelido confirmado) | nomeada | 0 (zero) | This property defines the lowest value achieved by this I/O Tag in a device. This property is used to perform a scale adjustment of the value received from a device before setting it to the Value property. Likewise, the inverse operation is performed before sending that value to the I/O Driver, when… |
| `DeviceHigh` | Double | RW | type lib | DevHigh (apelido confirmado) | nomeada | 1,000 | This property defines the highest value achieved by this I/O Tag in a device. This property is used to perform a scale adjustment of the value received from a device before setting it to the Value property. Likewise, the inverse operation is performed before sending that value to the I/O Driver, whe… |
| `EULow` | Double | RW | type lib | EULow | nomeada | 0 (zero) | Defines the lowest value to set to the Value property, adjusting the scale to the value from the device before this attribution. Likewise, the inverse operation is performed before sending the value to the I/O Driver, when writing. This conversion happens only when EnableScaling property is set to T… |
| `EUHigh` | Double | RW | type lib | EUHigh | nomeada | 1,000 | Defines the highest value to set to the Value property, adjusting the scale to the value from the device before this attribution. Likewise, the inverse operation is performed before sending the value to the I/O Driver, when writing. This conversion happens only when the EnableScaling property is set… |
| `UseBitFields` | Boolean | RW | type lib | UseBitFields | nomeada | — | If this property is set to True, every time the value from Value property is modified, it updates the bits referring to Bit00 to Bit31 properties. Likewise, every time the value from Bit00 to Bit31 properties are modified, the value from Value property is updated and sent to the device, if the Allow… |
| `Bit00` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 0 |
| `Bit01` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 1 |
| `Bit02` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 2 |
| `Bit03` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 3 |
| `Bit04` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 4 |
| `Bit05` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 5 |
| `Bit06` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 6 |
| `Bit07` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 7 |
| `Bit08` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 8 |
| `Bit09` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 9 |
| `Bit10` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 10 |
| `Bit11` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 11 |
| `Bit12` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 12 |
| `Bit13` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 13 |
| `Bit14` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 14 |
| `Bit15` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 15 |
| `Bit16` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 16 |
| `Bit17` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 17 |
| `Bit18` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 18 |
| `Bit19` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 19 |
| `Bit20` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 20 |
| `Bit21` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 21 |
| `Bit22` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 22 |
| `Bit23` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 23 |
| `Bit24` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 24 |
| `Bit25` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 25 |
| `Bit26` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 26 |
| `Bit27` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 27 |
| `Bit28` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 28 |
| `Bit29` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 29 |
| `Bit30` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 30 |
| `Bit31` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 31 |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Inherit#` | ULong | RW | framework | Inherit# | nomeada | — | Herança de configuração (família numerada) |
| `FormatN#` | Byte |  | gravada no .prj | FormatN# | nomeada | — | sem equivalente na type lib (família: 4) |
| `N#` | UShort |  | gravada no .prj | N# | nomeada | — | sem equivalente na type lib (família: 4) |

**Métodos:** `Write(EWriteSyncMode EWriteSyncMode)`; `WriteEx(Value Variant, TimeStamp Variant, Quality ULong, WriteStatus Variant, EWriteSyncMode EWriteSyncMode)`

**Eventos:** `OnRead()`

<a id="iodrv-opcdriver"></a>
### OPCDriver

- CLSID `{BBDDFC11-3C1F-4B4F-B01C-D1764FA5FF53}` · interface `IOPCDriver` · eventos `DOPCDriverEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPCDriver Server

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ServerId` | String | RW | type lib | — | — | empty, if this value is empty the OPC Driver is … | Determines the OPC Server to which the OPC Driver must connect. Although the default value of this property is empty, if this value is empty the OPC Driver is not going to connect. This property can only be modified when an OPC Driver is not connected. The next script contains an example of using th… |
| `ServerMachine` | String | RW | type lib | — | — | — | This property determines the address of the station where the main OPC Server is executing. For applications executing locally, this property may remain blank (default). Otherwise, users must specify a path, such as "\ \ServerName". If the OPC Server indicated in this property returns a value differ… |
| `ServerMachine2` | String | RW | type lib | — | — | — | This property determines the address of the station where the redundant OPC Server is executing, for cases in which the connection to the OPC Server indicated in the ServerMachine property fails or takes a time longer than the specified in the ConnectionTimeout property. The connection to this redun… |
| `ServerName` | String | R | type lib | — | — | — | This property returns the name or description of an OPC Server. This property is different from the ServerID property, which is a code. This is a read-only property. The next script contains an example of using this property. Sub OPCDriver1_AfterStart() MsgBox _ Application.GetObject("OPCDriver1.OPC… |
| `Compatibility` | OPCCompatibilityModes | RW | type lib | — | — | — | Allows controlling the usage of OPC's default interfaces by Elipse E3's OPC Client. Possible values for this property are: 0 - AnyVersion: Normal operation, default and recommended, the OPC Driver communicates with both OPC DA 2.0x and 1.0a Servers, with preference to 2.0x interfaces 1 - Version10A:… |
| `ReconnectPeriod` | Long | RW | type lib | — | — | — | Controls the period of connection to the OPC Server. If connection is lost, OPC Driver stops and restarts until this action returns success. The period is configured in milliseconds and when its value is set to 0 (zero), reconnection is disabled. Because the OPC Driver is stopped and started, Before… |
| `ServerStatus` | OPCStatus | R | type lib | — | — | — | Determines the status of an OPC Server connection. This is a read-only property. The available options are described on the next table. Available options for the ServerStatus property -1 - ServerStatus_Unknown The OPC Driver is connected to an OPC Server but either status is not informed or OPC Clie… |
| `WriteFeedbackMode` | WriteFeedbackModes | RW | type lib | — | — | — | This property allows controlling feedback from OPC Tag writings. The configuration options of this property are described on the next table. Available options for the WriteFeedbackMode property 0 - wfWaitNextRead After writing, waits normally for the next reading, which is the default for applicatio… |
| `ConnectionTimeout` | Long | RW | type lib | — | — | 10,000 (10 seconds) | Specifies a maximum time-out to establish a connection with an OPC Server, including all connection steps, even steps before accessing the OPC Server itself, such as access to the OPCENUM service or to Windows Registry. This property's value cannot be negative. Configuring this property with value 0… |
| `CallTimeout` | Long | RW | type lib | — | — | 10,000 (10 seconds) | Specifies a time-out for an answer on any call or access to an OPC Server, such as writings, creation of OPC Groups, OPC Tag creation, removal, or browsing, or changes to OPC Tag's Advise mode, among others. If this time-out is exceeded, Elipse E3 considers the OPC Server as locked or unavailable an… |
| `ActiveServer` | String | R | type lib | — | — | — | This property indicates the active OPC Server at a certain moment, which can be both the server indicated in the ServerMachine property (main) or the server indicated in the ServerMachine2 property (redundant). This is a read- only property. |

**Eventos:** `BeforeStart()`; `AfterStart()`; `BeforeStop()`; `AfterStop()`; `OnTagRead(Tag Object)`; `OnTagWrite(Tag Object, Succeeded Boolean, User String)`

<a id="iodrv-opcelementblock"></a>
### OPCElementBlock

- CLSID `{3395A216-DB8D-4C6C-A185-A73137E1F2AD}` · interface `IOPCElementBlock` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPCElementBlock Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | — | — | — | Value Updated whenever a new value is read from the OPC Server, according to OPC Block's ItemID property specifications where this OPC Block Element is inserted, and also considering the Index property, which specifies the position of an OPC Block Element in an OPC Block array. This property's data … |
| `RawValue` | Variant | RW | type lib | — | — | — | RawValue Accesses the original value of an OPC Block Element previous to the scale, that is, regardless of EnableScaling property's configuration. Therefore, if this property is set to False, the Value property and this property have the same behavior. |
| `EU` | String | RW | type lib | — | — | empty | EU Identifies the engineering unit represented by this value, such as degrees, meters, or KW/h. The default value of this property is empty. The next script contains an example of using this property. Sub Element_OnStartRunning() ' Performs a scale adjustment of an ' Element's temperature ' ranging … |
| `EnableScaling` | Boolean | RW | type lib | — | — | False | EnableScaling This property enables or disables the scale of values for a value sent or received from a device. If this property is set to True, all values from the device receive a scale adjustment according to DeviceHigh, DeviceLow, EUHigh, and EULow properties before setting it to the Value prope… |
| `DeviceLow` | Double | RW | type lib | — | — | 0 (zero) | DeviceLow This property defines the lowest value reached by an OPC Block Element in the device. This property is used to perform a scale adjustment of the value from a device before setting it to the Value property. Likewise, at the moment of a writing the inverse operation is performed before sendi… |
| `DeviceHigh` | Double | RW | type lib | — | — | 1000 | DeviceHigh This property defines the highest value reached by an OPC Block Element in the device. This property is used to perform a scale adjustment of the value from a device before setting it to the Value property. Likewise, at the moment of a writing the inverse operation is performed before sen… |
| `EULow` | Double | RW | type lib | — | — | 0 (zero) | EULow Defines the lowest value to set to the Value property, adjusting the scale to the device's value before setting it. Likewise, at the moment of a writing the inverse operation is performed before sending the value to the Driver. This conversion only occurs when the EnableScaling property is set… |
| `EUHigh` | Double | RW | type lib | — | — | 1000 | EUHigh Defines the highest value to set to the Value property, adjusting the scale to the device's value before setting it. Likewise, at the moment of a writing the inverse operation is performed before sending the value to the Driver. This conversion only occurs when the EnableScaling property is s… |
| `UseBitFields` | Boolean | RW | type lib | — | — | False | UseBitFields If this property is set to True, every time the value in the Value property changes, it updates all bits referring to the Bit00 to Bit31 properties. Likewise, it updates the value in the Value property every time any of the Bit00 to Bit31 properties change their values, and later send i… |
| `Bit00` | Boolean | RW | type lib | — | — | — | Value of bit 0 |
| `Bit01` | Boolean | RW | type lib | — | — | — | Value of bit 1 |
| `Bit02` | Boolean | RW | type lib | — | — | — | Value of bit 2 |
| `Bit03` | Boolean | RW | type lib | — | — | — | Value of bit 3 |
| `Bit04` | Boolean | RW | type lib | — | — | — | Value of bit 4 |
| `Bit05` | Boolean | RW | type lib | — | — | — | Value of bit 5 |
| `Bit06` | Boolean | RW | type lib | — | — | — | Value of bit 6 |
| `Bit07` | Boolean | RW | type lib | — | — | — | Value of bit 7 |
| `Bit08` | Boolean | RW | type lib | — | — | — | Value of bit 8 |
| `Bit09` | Boolean | RW | type lib | — | — | — | Value of bit 9 |
| `Bit10` | Boolean | RW | type lib | — | — | — | Value of bit 10 |
| `Bit11` | Boolean | RW | type lib | — | — | — | Value of bit 11 |
| `Bit12` | Boolean | RW | type lib | — | — | — | Value of bit 12 |
| `Bit13` | Boolean | RW | type lib | — | — | — | Value of bit 13 |
| `Bit14` | Boolean | RW | type lib | — | — | — | Value of bit 14 |
| `Bit15` | Boolean | RW | type lib | — | — | — | Value of bit 15 |
| `Bit16` | Boolean | RW | type lib | — | — | — | Value of bit 16 |
| `Bit17` | Boolean | RW | type lib | — | — | — | Value of bit 17 |
| `Bit18` | Boolean | RW | type lib | — | — | — | Value of bit 18 |
| `Bit19` | Boolean | RW | type lib | — | — | — | Value of bit 19 |
| `Bit20` | Boolean | RW | type lib | — | — | — | Value of bit 20 |
| `Bit21` | Boolean | RW | type lib | — | — | — | Value of bit 21 |
| `Bit22` | Boolean | RW | type lib | — | — | — | Value of bit 22 |
| `Bit23` | Boolean | RW | type lib | — | — | — | Value of bit 23 |
| `Bit24` | Boolean | RW | type lib | — | — | — | Value of bit 24 |
| `Bit25` | Boolean | RW | type lib | — | — | — | Value of bit 25 |
| `Bit26` | Boolean | RW | type lib | — | — | — | Value of bit 26 |
| `Bit27` | Boolean | RW | type lib | — | — | — | Value of bit 27 |
| `Bit28` | Boolean | RW | type lib | — | — | — | Value of bit 28 |
| `Bit29` | Boolean | RW | type lib | — | — | — | Value of bit 29 |
| `Bit30` | Boolean | RW | type lib | — | — | — | Value of bit 30 |
| `Bit31` | Boolean | RW | type lib | — | — | — | Value of bit 31 |
| `Quality` | Long | R | type lib | — | — | — | Quality This property represents the quality status of a value in the Value property. This is a read-only property. For more information about quality, please check topic Quality on Elipse E3 User's Manual. |
| `Index` | Long | RW | type lib | — | — | 0 (zero), | Index Use this property to specify the position that an OPC Block Element occupies among the OPC Block Elements configured in the OPC Block's Size property where it is inserted. This property's accepts values from 0 (zero) to a value less than the value defined in the Size property. For example, con… |

**Eventos:** `OnRead()`

<a id="iodrv-opcfolder"></a>
### OPCFolder

- CLSID `{AA29ECFE-8B8C-4DF3-8BB3-792BE3EDF020}` · interface `IOPCFolder`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPCFolder Object

<a id="iodrv-opcgroup"></a>
### OPCGroup

- CLSID `{77A98211-FEA0-490D-AA71-2176B1057124}` · interface `IOPCGroup`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPCGroup Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Enable` | Boolean | RW | type lib | — | — | — | This property enables updating OPC Tags inside an OPC Group. If this property is set to False, no OPC Tag inside the OPC Group is updated. Otherwise, OPC Tags with their AllowRead property set to True and in Advise mode are kept updated according to OPC Group's update time, the Scan property, and de… |
| `Scan` | Long | RW | type lib | — | — | 1,000 | Specifies the update's scan time of OPC Tags from an OPC Group used by the OPC Server. This property is represented in milliseconds and it can be modified after starting communication, and it is used only when the Enable property is set to True. When configuring this property in several OPC Tags of … |
| `DeadBand` | Single | RW | type lib | — | — | 0 (zero) | This property allows adjusting a minimum variation level of an OPC Tag, so that it can be updated. This property only applies to OPC Tags of an OPC Group that are considered as of analog type by the OPC Server to which the OPC Driver is connected. The valid interval for this property is between 0 (z… |
| `RealScan` | Long | R | type lib | — | — | — | Scan time effectively used by the OPC Server. This is a read-only property. |
| `BlockMode` | Boolean | RW | type lib | — | — | — | This property determines the behavior when activating or deactivating an OPC Group. When this property is set to True, communication of OPC Tags of an OPC Group starts at once. This usually improves performance, a shorter activation time, by minimizing the number of calls to the OPC Server. When thi… |

**Métodos:** `Refresh(Source OPCRefreshSource)`

<a id="iodrv-opctag"></a>
### OPCTag

- CLSID `{992C4975-D452-4B7A-9139-6794A2C438B5}` · interface `IOPCTag` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPCTag Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | — | — | empty | Value This property is updated whenever performing a new valid reading of a value from a device using its configuration, but the data type of this variable, such as integer, floating point, or text, depends on the OPC Driver to which it is linked and on its configuration. This property is only updat… |
| `RawValue` | Variant | RW | type lib | — | — | — | RawValue Accesses the original value of the OPC Tag previous to the scale, that is, regardless of EnableScaling property's configuration. Therefore, if this property is set to False, the Value property and this property have the same behavior. |
| `EU` | String | RW | type lib | — | — | empty | EU Identifies the engineering unit represented by the value, such as degrees, meters, or KW/h. The default value of this property is empty. The next script contains an example of using this property. 338 Server Objects Sub Tag_OnStartRunning() ' Performs a scale adjustment of a ' Tag's temperature '… |
| `EnableScaling` | Boolean | RW | type lib | — | — | False | EnableScaling If this property is set to True, all values from the device receive a scale adjustment, according to EUHigh and EULow properties before setting it to the Value property. If this property is set to False, no scale adjustment is performed in neither way, writing and reading. The default … |
| `DeviceLow` | Double | RW | type lib | — | — | 0 (zero) | DeviceLow This property defines the lowest value reached by this OPC Tag in the device. This property is used to perform a scale adjustment of the value from a device before setting it to the Value property. Likewise, at the moment of a writing the inverse operation is performed before sending the v… |
| `DeviceHigh` | Double | RW | type lib | — | — | 1,000 | DeviceHigh This property defines the highest value reached by this OPC Tag in the device. This property is used to perform a scale adjustment of the value from a device before setting it to the Value property. Likewise, at the moment of a writing the inverse operation is performed before sending the… |
| `EULow` | Double | RW | type lib | — | — | 0 (zero) | EULow Defines the lowest value to set to the Value property, adjusting the scale to the device's value before setting it. Likewise, at the moment of a writing the inverse operation is performed before sending the value to the Driver. This conversion only occurs when the EnableScaling property is set… |
| `EUHigh` | Double | RW | type lib | — | — | 1,000 | EUHigh Defines the highest value to set to the Value property, adjusting the scale to the device's value before setting it. Likewise, at the moment of a writing the inverse operation is performed before sending the value to the Driver. This conversion only occurs when the EnableScaling property is s… |
| `UseBitFields` | Boolean | RW | type lib | — | — | False | UseBitFields If this property is set to True, every time the value in the Value property changes, it updates all bits referring to Bit00 to Bit31 properties. Likewise, it updates the value in the Value property every time any of the Bit00 to Bit31 properties change their values, and later send it to… |
| `Bit00` | Boolean | RW | type lib | — | — | — | Value of bit 0 |
| `Bit01` | Boolean | RW | type lib | — | — | — | Value of bit 1 |
| `Bit02` | Boolean | RW | type lib | — | — | — | Value of bit 2 |
| `Bit03` | Boolean | RW | type lib | — | — | — | Value of bit 3 |
| `Bit04` | Boolean | RW | type lib | — | — | — | Value of bit 4 |
| `Bit05` | Boolean | RW | type lib | — | — | — | Value of bit 5 |
| `Bit06` | Boolean | RW | type lib | — | — | — | Value of bit 6 |
| `Bit07` | Boolean | RW | type lib | — | — | — | Value of bit 7 |
| `Bit08` | Boolean | RW | type lib | — | — | — | Value of bit 8 |
| `Bit09` | Boolean | RW | type lib | — | — | — | Value of bit 9 |
| `Bit10` | Boolean | RW | type lib | — | — | — | Value of bit 10 |
| `Bit11` | Boolean | RW | type lib | — | — | — | Value of bit 11 |
| `Bit12` | Boolean | RW | type lib | — | — | — | Value of bit 12 |
| `Bit13` | Boolean | RW | type lib | — | — | — | Value of bit 13 |
| `Bit14` | Boolean | RW | type lib | — | — | — | Value of bit 14 |
| `Bit15` | Boolean | RW | type lib | — | — | — | Value of bit 15 |
| `Bit16` | Boolean | RW | type lib | — | — | — | Value of bit 16 |
| `Bit17` | Boolean | RW | type lib | — | — | — | Value of bit 17 |
| `Bit18` | Boolean | RW | type lib | — | — | — | Value of bit 18 |
| `Bit19` | Boolean | RW | type lib | — | — | — | Value of bit 19 |
| `Bit20` | Boolean | RW | type lib | — | — | — | Value of bit 20 |
| `Bit21` | Boolean | RW | type lib | — | — | — | Value of bit 21 |
| `Bit22` | Boolean | RW | type lib | — | — | — | Value of bit 22 |
| `Bit23` | Boolean | RW | type lib | — | — | — | Value of bit 23 |
| `Bit24` | Boolean | RW | type lib | — | — | — | Value of bit 24 |
| `Bit25` | Boolean | RW | type lib | — | — | — | Value of bit 25 |
| `Bit26` | Boolean | RW | type lib | — | — | — | Value of bit 26 |
| `Bit27` | Boolean | RW | type lib | — | — | — | Value of bit 27 |
| `Bit28` | Boolean | RW | type lib | — | — | — | Value of bit 28 |
| `Bit29` | Boolean | RW | type lib | — | — | — | Value of bit 29 |
| `Bit30` | Boolean | RW | type lib | — | — | — | Value of bit 30 |
| `Bit31` | Boolean | RW | type lib | — | — | — | Value of bit 31 |
| `Quality` | Long | R | type lib | — | — | 0 (zero, bad quality) | Quality This property informs the quality of the value contained in the Value property. Each time the OPC Driver attributes a new value to the OPC Tag, it also configures the quality of that data. This is a read-only property. The default value of this property is 0 (zero, bad quality). For more inf… |
| `AllowRead` | Boolean | RW | type lib | — | — | True | AllowRead Defines whether this OPC Tag must be read or not by the OPC Driver. If this property is set to True, the OPC Driver automatically updates Value, from Bit00 to Bit31, and RawValue properties of this object in time spans. Otherwise, this OPC Tag is not read. The default value of this propert… |
| `AllowWrite` | Boolean | RW | type lib | — | — | True | AllowWrite Defines whether this OPC Tag must be written or not automatically when the Value, from Bit00 to Bit31, or RawValue properties change. If this property is set to True, these modifications are sent to the device associated to the OPC Driver. Otherwise, these modifications are ignored. The d… |
| `SyncWrite` | Boolean | RW | type lib | — | — | False | SyncWrite This property determines the type of writing used by an OPC Tag. If this property is set to True, this writing is synchronous, that is, the OPC Driver waits for the result of a writing from the OPC Server. Otherwise, this writing is asynchronous, that is, OPC Tag's value is sent and OPC Dr… |
| `TimeStamp` | Date | RW | type lib | — | — | "00:00:00" | TimeStamp This property is updated whenever there is a change in value or status in either Value or Quality properties. This property informs a date and time linked to OPC Tag's value, as well as to OPC Tag's quality. This is a read-only property. The default value of this property is "00:00:00". ⚠ manual: somente leitura |
| `ItemID` | String | RW | type lib | — | — | an empty String, users must specify a value for … | ItemID This property determines the path that identifies the OPC Tag on the OPC Server to which the OPC Driver connects. Definition of this path is flexible and depends on the specific OPC Server. Usually, OPC Servers specify an ID space with hierarchical items, such as ParentItem.ChildItem.Tag1. Th… |
| `DataType` | OPCEnumVts | R | type lib | — | — | — | DataType Determines the data type associated to this OPC Tag. This is a read-only property. Please check the Available options for the DataType property table on OPC Block's DataType property for all available values for this property. |
| `AdviseType` | AdviseTypes | RW | type lib | — | — | — | AdviseType Controls the Advise mode. The available options are described on the next table. Available options for the AdviseType property 0 - AlwaysInAdvise OPC Tag is kept updated if its AllowRead property is set to True, and OPC Group's Enable property is also set to True 336 Server Objects 1 - Ad… |
| `EnableDriverEvent` | Boolean | RW | type lib | — | — | False | EnableDriverEvent This property is used to control the generation of the OnTagRead event, which occurs in the OPC Driver that contains the OPC Tag. If this property is set to True, at each reading that comes from the OPC Server, whether on error or not, the OnTagRead event is generated on the OPC Dr… |

**Métodos:** `Write()`; `WriteEx(Value Variant, SyncWrite Variant)`

**Eventos:** `OnRead()`

<a id="iodrv-opctagblock"></a>
### OPCTagBlock

- CLSID `{EE291957-6E24-469A-B5E6-9ABB9C508FC5}` · interface `IOPCTagBlock` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPCTagBlock Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `AllowRead` | Boolean | RW | type lib | — | — | True | 1 - AdviseWhenLinked OPC Block is updated only if OPC Block's AllowRead property and OPC Group's Enable property are set to True, and the OPC Block is associated to an active object, such as a Display on an open Screen or an enabled Alarm, among others. An OPC Block link for this purpose can be assi… |
| `AllowWrite` | Boolean | RW | type lib | — | — | True | AllowWrite Configure this property to define whether this OPC Block must be automatically written when the Value property or any Bit property, from Bit00 to Bit31, is modified. If this property is set to True, changes are sent to the device or equipment linked to the OPC Driver, otherwise these chan… |
| `SyncWrite` | Boolean | RW | type lib | — | — | False | SyncWrite This property determines the type of writing used by an OPC Block. If this property is set to True, this writing is synchronous, that is, the OPC Driver waits for the result of a writing from the OPC Server. Otherwise, this writing is asynchronous, that is, OPC Block's value is sent and OP… |
| `Quality` | Long | R | type lib | — | — | 0 (zero, bad quality) | Quality This property informs the quality of the value contained in the Value property. Every time the OPC Driver attributes a new value to the OPC Block, it also configures the quality of that data. This is a read-only property. The default value of this property is 0 (zero, bad quality). For more … |
| `TimeStamp` | Date | RW | type lib | — | — | "00:00:00" | TimeStamp This property is updated whenever a change in value or status in either Value or Quality properties occurs. This property informs a date and time linked to OPC Block's value, as well as to OPC Block's quality. This is a read-only property. The default value of this property is "00:00:00". ⚠ manual: somente leitura |
| `ItemID` | String | RW | type lib | — | — | empty, users must specify a value for this OPC B… | ItemID This property determines the path identifying the OPC Block on the OPC Server to which the OPC Driver connects. Definition of this path is flexible and depends on the specific OPC Server. Usually, OPC Servers specify an ID space with hierarchical items, such as ParentItem.ChildItem.Tag1. This… |
| `Size` | Long | RW | type lib | — | — | 0 (zero) | Size Defines the size of OPC Block's set of values. Please check Driver's documentation for information about the limit for this property, according to B1 to B4 parameters. By creating OPC Block Elements for the OPC Block, it allows both accessing the values read and also allows writing values to th… |
| `DataType` | OPCEnumVts | R | type lib | — | — | — | DataType Determines the data type associated to this OPC Block. This is a read-only property. Possible values for this property are described on the next table. Available options for the DataType property 0 - _Undefined Unidimensional undefined value (empty, default) 1 - _Null Null value 2 - _Intege… |
| `AdviseType` | AdviseTypes | RW | type lib | — | — | — | AdviseType Controls the Advise mode. The available options are described on the next table. Available options for the AdviseType property 0 - AlwaysInAdvise OPC Block is updated if OPC Block's AllowRead property is set to True and OPC Group's Enable property is also set to True |
| `EnableDriverEvent` | Boolean | RW | type lib | — | — | False | EnableDriverEvent This property is used to control the generation of an OnTagRead event, which occurs in the OPC Driver that contains the OPC Block. If this property is set to True, at each reading coming from the OPC Server, whether on error or not, the OnTagRead event is generated on the OPC Drive… |

**Métodos:** `Write()`; `WriteEx(Value Variant, SyncWrite Variant)`

**Eventos:** `OnRead()`

<a id="iodrv-uadriver"></a>
### UaDriver

- CLSID `{33ED8DEF-19E2-4E3D-8AA4-6B7E422667B7}` · interface `IUaDriver` · eventos `DUaDriverEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 2 instâncias em 1 arquivo(s)
- OPC UA Client object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `EndpointURL` | String | RW | type lib | URL (apelido confirmado) | nomeada | — | Read-and-write property specifying the path or endpoint of an OPC UA Server to which the OPC UA Client connects. This property cannot be changed while communication is active. |
| `SecurityMode` | UaSecurityModes | RW | type lib | SecMode (apelido confirmado) | nomeada | — | Read-and-write property specifying the security mode used when connecting to an OPC UA Server. This property cannot be changed while communication is active. Possible values for this property are 1 - usmNone: Does not use any security mode in the connection (default), 2 - usmSign: Uses authenticatio… |
| `SecurityPolicy` | UaSecurityPolicies | RW | type lib | SecPol (apelido confirmado) | nomeada | — | Read-and-write property specifying the security policy or encryption used when connecting to an OPC UA Server. This property cannot be changed while communication is active. Possible values for this property are 1 - uspNone: Does not use encryption in the connection (default), 2 - uspBasic128Rsa15: … |
| `UserName` | String | RW | type lib | User (apelido confirmado) | nomeada | an empty String | Read-and-write property specifying the user's name used in an OPC UA Server's connection. This property is used together with the Password property. The default value of this property is an empty String. This property can be changed while communication is active, but that change is only effective af… |
| `Password` | BSTRPASSWORD | RW | type lib | Pwd (apelido confirmado) | nomeada | an empty String | Read-and-write property specifying the user's password used in the connection with an OPC UA Server. This property is used together with the UserName property and its default value is an empty String. This property can be changed while communication is active, but that change is only effective after… |
| `TimeoutCall` | Long | RW | type lib | CallTimeout (apelido confirmado) | nomeada | 10,000 (10 seconds) | Read-and-write property specifying a time limit for a call to an OPC UA Server, in milliseconds. This property cannot be changed while communication is active, its value must be greater than 0 (zero), and its default value is 10,000 (10 seconds). In OPC UA standard, several calls allow to continue c… |
| `TimeoutConnection` | Long | RW | type lib | ConnTimeout (apelido confirmado) | nomeada | 10,000 (10 seconds) | Read-and-write property specifying the time limit of a connection, in milliseconds. Default value of this property is 10,000 (10 seconds) and its value must be greater than 0 (zero). This property cannot be changed while communication is active. |
| `TimeoutSession` | Long | RW | type lib | SessTimeout (apelido confirmado) | nomeada | 600,000 (10 minutes) | Read-and-write property specifying a time limit for renewing a communication session from an E3 Client to an OPC UA Server, in milliseconds. Default value of this property is 600,000 (10 minutes) and its value must be greater than 0 (zero). This property cannot be changed while communication is acti… |
| `PublishLimit` | Long | RW | type lib | PubLimit (apelido confirmado) | nomeada | 5 (five) | Configures a limit for publish requests of an OPC UA Driver, to avoid a request overload in OPC UA Servers. The default value of this property is 5 (five). NOTES For applications created using versions previous to version 6.7 and opened in versions starting from version 6.7, the default value of thi… |
| `WriteFeedbackMode` | WriteFeedbackModes | RW | type lib | WfMode (apelido confirmado) | nomeada | — | This property allows controlling a confirmation or feedback of OPC UA Tag writings. The configuration options for this property are described on the next table. Available options for the WriteFeedbackMode property 0 - wfWaitNextRead After writing, waits normally for the next reading 1 - wfImmediateR… |
| `WriteValueMode` | EWriteValueMode | RW | type lib | WvMode (apelido confirmado) | nomeada | — | Read-and-write property controlling the behavior of sending a value in writing operations. This property must be configured according to the OPC UA Server in use, otherwise this writing fails. Possible values for this property are 0 - wvmDefault: Follows the default behavior of the OPC UA Driver to … |
| `ServerState` | UaServerState | R | type lib | — | não gravada nomeada | — | Returns the status of a connection or of an OPC UA Server. This is a read-only property. Possible values for this property are -1 - ussNotConnected: OPC UA Server is not connected (default), 0 - ussRunning: OPC UA Server is executing normally, 1 - ussFailed: OPC UA Server is not executing, 2 - ussNo… |
| `MaxNodesPerClientCall` | Long | RW | type lib | MaxNodesCall (apelido confirmado) | nomeada | 0 (zero), | This property manages the size of the array of nodes passed by default in synchronous requests to an OPC UA Server. Default value of this property is 0 (zero), which disables this management. This property's usage allows splitting a request into smaller requests, thus avoiding BadTooManyOperations-t… |
| `OverrideEndpointURLHost` | Boolean | RW | type lib | OverrideURLHost (apelido confirmado) | nomeada | False | This property forces using the endpoint used to connect to an OPC UA Server, configured in the EndPointURL property, in cases where an OPC UA Server returns a list of endpoints that may or may not be accessible to an OPC UA Client. The default value of this property is False. |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Expose` | ULong | RW | framework | Expose | nomeada | — | Expõe o objeto (flag de framework) |
| `AreaAlarmVerify` | ULong |  | gravada no .prj | AreaAlarmVerify | nomeada | — | sem equivalente na type lib |
| `AreaIsArea` | Boolean |  | gravada no .prj | AreaIsArea | nomeada | — | sem equivalente na type lib |
| `AreaUserFieldIsValueForced1` | Boolean |  | gravada no .prj | AreaUserFieldIsValueForced1 | nomeada | — | sem equivalente na type lib |
| `AreaUserFieldsCount` | ULong |  | gravada no .prj | AreaUserFieldsCount | nomeada | — | sem equivalente na type lib |
| `AreaUserFieldValue1` | String |  | gravada no .prj | AreaUserFieldValue1 | nomeada | — | sem equivalente na type lib |
| `Ns#` | String |  | gravada no .prj | Ns# | nomeada | — | sem equivalente na type lib (família: 4) |
| `NsCount` | ULong |  | gravada no .prj | NsCount | nomeada | — | sem equivalente na type lib |

**Métodos:** `RefreshUaNodeIds()`

**Eventos:** `OnTagRead(Tag Object)`; `OnTagWrite(Tag Object, Succeeded Boolean, User String)`

<a id="iodrv-uaelementblock"></a>
### UaElementBlock

- CLSID `{44ABD8E4-1499-4255-BD76-26E1B59B712D}` · interface `IUaElementBlock` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPC UA Element Block Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | — | — | — | Value Updated whenever a new value is read from an OPC UA Server, according to the specification of the ItemID property of the OPC UA Block Tag where this object is inserted, and considering the Index property, which specifies the position of this OPC UA Block Element in OPC UA Block Tag's array. Th… |
| `RawValue` | Variant | RW | type lib | — | — | — | RawValue Accesses the original value of an OPC UA Block Element before the scale, that is, regardless of the configuration of the EnableScaling property. Therefore, if this property is set to False, the Value property and this property have the same behavior. |
| `EU` | String | RW | type lib | — | — | empty | EU Identifies the engineering unit represented by this value, such as degrees, meters, or KW/h. The default value of this property is empty. 348 Server Objects |
| `EnableScaling` | Boolean | RW | type lib | — | — | False | EnableScaling This property enables or disables a scale of values for the value sent to or received from a device. If this property is set to True, any value coming from a device suffers a scale adjustment according to DeviceHigh, DeviceLow, EUHigh, and EULow properties before setting it to the Valu… |
| `DeviceLow` | Double | RW | type lib | — | — | 0 (zero) | DeviceLow This property defines the minimum value reached by an OPC UA Block Element on a device. This property is used to perform a scale adjustment on a value coming from a device before setting it to the Value property. Likewise, at the moment of the writing an inverse operation is executed befor… |
| `DeviceHigh` | Double | RW | type lib | — | — | 1,000 | DeviceHigh This property defines the maximum value reached by an OPC UA Block Element in a device. This property is used to execute a scale adjustment on the value coming from a device before setting it to the Value property. Likewise, at the moment of the writing an inverse operation is executed be… |
| `EULow` | Double | RW | type lib | — | — | 0 (zero) | EULow Defines the minimum value to set to the Value property, adjusting the scale to the value on a device before this attribution. Likewise, at the moment of the writing the inverse operation is executed before sending a value to the Driver. This conversion only occurs when the EnableScaling proper… |
| `EUHigh` | Double | RW | type lib | — | — | 1,000 | EUHigh Defines the maximum value to set to the Value property, adjusting the scale to the value on a device before this attribution. Likewise, at the moment of the writing the inverse operation is executed before sending a value to the Driver. This conversion only occurs when the EnableScaling prope… |
| `UseBitFields` | Boolean | RW | type lib | — | — | False | UseBitFields If this property is set to True, each time the value of the Value property changes, it updates all bits referring to properties from Bit00 to Bit31. Likewise, it updates the value of Value each time any of Bit00 to Bit31 properties change their values and later send to a device if the A… |
| `Bit00` | Boolean | RW | type lib | — | — | — | Value of bit 0. |
| `Bit01` | Boolean | RW | type lib | — | — | — | Value of bit 1. |
| `Bit02` | Boolean | RW | type lib | — | — | — | Value of bit 2. |
| `Bit03` | Boolean | RW | type lib | — | — | — | Value of bit 3. |
| `Bit04` | Boolean | RW | type lib | — | — | — | Value of bit 4. |
| `Bit05` | Boolean | RW | type lib | — | — | — | Value of bit 5. |
| `Bit06` | Boolean | RW | type lib | — | — | — | Value of bit 6. |
| `Bit07` | Boolean | RW | type lib | — | — | — | Value of bit 7. |
| `Bit08` | Boolean | RW | type lib | — | — | — | Value of bit 8. |
| `Bit09` | Boolean | RW | type lib | — | — | — | Value of bit 9. |
| `Bit10` | Boolean | RW | type lib | — | — | — | Value of bit 10. |
| `Bit11` | Boolean | RW | type lib | — | — | — | Value of bit 11. |
| `Bit12` | Boolean | RW | type lib | — | — | — | Value of bit 12. |
| `Bit13` | Boolean | RW | type lib | — | — | — | Value of bit 13. |
| `Bit14` | Boolean | RW | type lib | — | — | — | Value of bit 14. |
| `Bit15` | Boolean | RW | type lib | — | — | — | Value of bit 15. |
| `Bit16` | Boolean | RW | type lib | — | — | — | Value of bit 16. |
| `Bit17` | Boolean | RW | type lib | — | — | — | Value of bit 17. |
| `Bit18` | Boolean | RW | type lib | — | — | — | Value of bit 18. |
| `Bit19` | Boolean | RW | type lib | — | — | — | Value of bit 19. |
| `Bit20` | Boolean | RW | type lib | — | — | — | Value of bit 20. |
| `Bit21` | Boolean | RW | type lib | — | — | — | Value of bit 21. |
| `Bit22` | Boolean | RW | type lib | — | — | — | Value of bit 22. |
| `Bit23` | Boolean | RW | type lib | — | — | — | Value of bit 23. |
| `Bit24` | Boolean | RW | type lib | — | — | — | Value of bit 24. |
| `Bit25` | Boolean | RW | type lib | — | — | — | Value of bit 25. |
| `Bit26` | Boolean | RW | type lib | — | — | — | Value of bit 26. |
| `Bit27` | Boolean | RW | type lib | — | — | — | Value of bit 27. |
| `Bit28` | Boolean | RW | type lib | — | — | — | Value of bit 28. |
| `Bit29` | Boolean | RW | type lib | — | — | — | Value of bit 29. |
| `Bit30` | Boolean | RW | type lib | — | — | — | Value of bit 30. |
| `Bit31` | Boolean | RW | type lib | — | — | — | Value of bit 31. |
| `Quality` | Long | R | type lib | — | — | — | Quality This property represents the quality status of the value in the Value property. This is a read-only property. For more information about quality, please check topic Quality on Elipse E3 User's Manual. |
| `Index` | Long | RW | type lib | — | — | 0 (zero), | Index Use this property to specify the position an OPC UA Block Element occupies among the OPC UA Block Elements configured by the Size property of the OPC UA Block Tag in which it is inserted. This property accepts values from 0 (zero) to a number less than the value defined in Size. For example, w… |

**Eventos:** `OnRead()`

<a id="iodrv-uafolder"></a>
### UaFolder

- CLSID `{DD8B6E84-2340-4C9B-9505-F503D1F9E38D}` · interface `IUaFolder`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 27 instâncias em 1 arquivo(s)
- OPC UA Folder Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Expose` | ULong | RW | framework | Expose | nomeada | — | Expõe o objeto (flag de framework) |
| `AreaAlarmVerify` | ULong |  | gravada no .prj | AreaAlarmVerify | nomeada | — | sem equivalente na type lib |
| `AreaIsArea` | Boolean |  | gravada no .prj | AreaIsArea | nomeada | — | sem equivalente na type lib |
| `AreaUserFieldLink#` | String |  | gravada no .prj | AreaUserFieldLink# | nomeada | — | sem equivalente na type lib (família: 3) |
| `AreaUserFieldsCount` | ULong |  | gravada no .prj | AreaUserFieldsCount | nomeada | — | sem equivalente na type lib |

<a id="iodrv-uasubscription"></a>
### UaSubscription

- CLSID `{446D47A8-2701-4B11-B650-CB4CBD70E234}` · interface `IUaSubscription`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 1 instâncias em 1 arquivo(s)
- OPC UA Subscription Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Enable` | Boolean | RW | type lib | — | não gravada nomeada | — | This property enables updating OPC UA Tags inside an OPC UA Subscription. If this property is set to False, no OPC UA Tag inside an OPC UA Subscription is updated. Otherwise, OPC UA Tags with their AllowRead property set to True and in Advise mode are kept updated according to the update time, defin… |
| `RealScan` | Long | R | type lib | — | não gravada nomeada | — | Scan time effectively used by an OPC UA Server. This is a read-only property. |
| `Scan` | Long | RW | type lib | Scan | nomeada | 1,000 | Specifies a scan time to update OPC UA Tags from an OPC UA Subscription that is used by an OPC UA Server. This property is represented in milliseconds, can be changed after communication starts, and it is used only when the Enable property is set to True. When configuring this property in all OPC UA… |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `Expose` | ULong | RW | framework | Expose | nomeada | — | Expõe o objeto (flag de framework) |
| `AllowR` | ULong |  | gravada no .prj | AllowR | nomeada | — | sem equivalente na type lib |

<a id="iodrv-uatag"></a>
### UaTag

- CLSID `{33377ADB-AB66-40E5-9DE4-F8D62324275A}` · interface `IUaTag` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 48 instâncias em 1 arquivo(s)
- OPC UA Tag Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Value` | Variant | RW | type lib | — | não gravada nomeada | empty | Value This property is updated when performing a new valid reading from a device using its configuration, but this variable's data type, such as integer, floating point, or text, depends on the OPC UA Driver to which it is linked and on its configuration. This property is only updated this way if th… |
| `RawValue` | Variant | RW | type lib | — | não gravada nomeada | — | RawValue Accesses the original value of this OPC UA Tag before the scale, that is, regardless of the configuration of the EnableScaling property. Therefore, if this property is set to False, the Value property and this property have the same behavior. |
| `EU` | String | RW | type lib | EU | nomeada | empty | EU Identifies the engineering unit represented by the value, such as degrees, meters, or KW/h. The default value of this property is empty. |
| `EnableScaling` | Boolean | RW | type lib | — | não gravada nomeada | False | EnableScaling If this property is set to True, any value coming from a device suffers a scale adjustment according to the EUHigh and EULow properties before setting it to the Value property. If this property is set to False, no scale adjustment is performed in both directions, writing or reading. Th… |
| `DeviceLow` | Double | RW | type lib | DevLo (apelido confirmado) | nomeada | 0 (zero) | DeviceLow This property defines the minimum value reached by an OPC UA Tag on a device. This property is used to perform a scale adjustment of a value coming from a device before setting it to the Value property. Likewise, at the moment of the writing the inverse operation is performed before sendin… |
| `DeviceHigh` | Double | RW | type lib | DevHi (apelido confirmado) | nomeada | 1,000 | DeviceHigh This property defines the maximum value reached by an OPC UA Tag on a device. This property is used to execute a scale adjustment of the value coming from a device before setting it to the Value property. Likewise, at the moment of the writing the inverse operation is performed before sen… |
| `EULow` | Double | RW | type lib | EULo (apelido confirmado) | nomeada | 0 (zero) | EULow Defines the minimum value to set to the Value property, adjusting the scale to the value of a device before this attribution. Likewise, at the moment of the writing, the inverse operation is performed before sending the value to the Driver. This conversion only occurs when the EnableScaling pr… |
| `EUHigh` | Double | RW | type lib | EUHi (apelido confirmado) | nomeada | 1,000 | EUHigh Defines the maximum value to set to the Value property, adjusting the scale to the value of a device before this attribution. Likewise, at the moment of the writing the inverse operation is performed before sending the value to the Driver. This conversion only occurs when the EnableScaling pr… |
| `UseBitFields` | Boolean | RW | type lib | — | não gravada nomeada | False | UseBitFields If this property is set to True, whenever the value of the Value property changes it updates all bits referring to the Bit00 to Bit31 properties. Likewise, it updates the value of Value whenever any of the Bit00 to Bit31 properties change their values and later sends to a device if the … |
| `Bit00` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 0. |
| `Bit01` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 1. |
| `Bit02` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 2. |
| `Bit03` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 3. |
| `Bit04` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 4. |
| `Bit05` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 5. |
| `Bit06` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 6. |
| `Bit07` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 7. |
| `Bit08` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 8. |
| `Bit09` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 9. |
| `Bit10` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 10. |
| `Bit11` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 11. |
| `Bit12` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 12. |
| `Bit13` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 13. |
| `Bit14` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 14. |
| `Bit15` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 15. |
| `Bit16` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 16. |
| `Bit17` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 17. |
| `Bit18` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 18. |
| `Bit19` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 19. |
| `Bit20` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 20. |
| `Bit21` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 21. |
| `Bit22` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 22. |
| `Bit23` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 23. |
| `Bit24` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 24. |
| `Bit25` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 25. |
| `Bit26` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 26. |
| `Bit27` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 27. |
| `Bit28` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 28. |
| `Bit29` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 29. |
| `Bit30` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 30. |
| `Bit31` | Boolean | RW | type lib | — | não gravada nomeada | — | Value of bit 31. |
| `Quality` | Long | R | type lib | — | não gravada nomeada | 0 (zero, bad quality) | Quality This property informs the quality of the value in the Value property. Every time an OPC UA Subscription sets a new value to an OPC UA Tag, it also configures the quality of that data. This is a read-only property. The default value of this property is 0 (zero, bad quality). For more informat… |
| `AdviseType` | AdviseTypes | RW | type lib | AdviseType | nomeada | — | AdviseType Controls the Advise mode. The available options are described on the next table. Available options for the AdviseType property 0 - AlwaysInAdvise OPC UA Tag is kept updated if the AllowRead property is set to True and the OPC UA Subscription's Enable property is also set to True 1 - Advis… |
| `AllowRead` | Boolean | RW | type lib | — | não gravada nomeada | True | AllowRead Defines whether this OPC UA Tag must be read or not by an OPC UA Subscription. If this property is set to True, the OPC UA Subscription automatically updates the Value, the properties from Bit00 to Bit31, and RawValue properties of 350 Server Objects this object in time spans. Otherwise, t… |
| `AllowWrite` | Boolean | RW | type lib | — | não gravada nomeada | True | AllowWrite Defines whether this OPC UA Tag must be written or not automatically when the Value, the properties from Bit00 to Bit31, or RawValue properties change. If this property is set to True, these changes are sent to the device linked to the OPC UA Subscription. Otherwise, changes are ignored. … |
| `DataType` | UaDataTypes | R | type lib | DataType | nomeada | — | DataType Property filled when Elipse E3 connects to an OPC UA Server, which indicates the data type on an OPC UA Server. This property is initially filled in the browsing process, if performed, and at each communication or connection with an OPC UA Server. Values below 1,000 are scalars and values a… |
| `EnableDriverEvent` | Boolean | RW | type lib | DriverEvent (apelido confirmado) | nomeada | False | EnableDriverEvent This property is used to control the generation of the OnTagRead event, which occurs on the OPC UA Driver that contains the OPC UA Tag. If this property is set to True, at each reading from an OPC UA Server, whether in error or not, the OnTagRead event is generated on the OPC UA Dr… |
| `ItemID` | String | RW | type lib | ItemID | nomeada | — | ItemID Specifies the path to perform a browsing of an OPC UA Tag on an OPC UA Server. This path is used in OPC UA Driver's RefreshUaNodeIds method to retrieve an OPC UA Node Identifier of an OPC UA Tag, when needed. |
| `SyncWrite` | Boolean | RW | type lib | SyncW (apelido confirmado) | nomeada | False | SyncWrite This property determines the type of writing used by an OPC UA Tag. If this property is set to True, this writing is synchronous, that is, the OPC UA Subscription waits for the result of that writing from an OPC UA Server. Otherwise, this writing is asynchronous, that is, the value of the … |
| `TimeStamp` | Date | RW | type lib | — | não gravada nomeada | "00:00:00" | TimeStamp This property is updated whenever any value or status change occurs in the Value or Quality properties. This property informs the date and time linked both to value and quality of the OPC UA Tag. This is a read-only property. The default value of this property is "00:00:00". 354 Server Obj… ⚠ manual: somente leitura |
| `UaNodeId` | IE3UaNodeId | RW | type lib | — | não gravada nomeada | — | UaNodeId Specifies the path to perform a browsing of an OPC UA Tag on an OPC UA Server. This path is used in OPC UA Driver's RefreshUaNodeIds method to retrieve an OPC UA Node Identifier of an OPC UA Tag, when needed. This property must be filled in to establish communication with an OPC UA Server. |
| `WriteValueMode` | EWriteValueMode | RW | type lib | WriteValueMode | nomeada | — | WriteValueMode Read-and-write property controlling the behavior of sending a value on writing operations. This property must be configured according to the OPC UA Server used, or this writing fails. Possible values for this property are 0 - wvmDefault: Follows the default behavior, that is, the beha… |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `AllowR` | ULong |  | gravada no .prj | AllowR | nomeada | — | sem equivalente na type lib |
| `AllowW` | ULong |  | gravada no .prj | AllowW | nomeada | — | sem equivalente na type lib |
| `NodeIdData` | String |  | gravada no .prj | NodeIdData | nomeada | — | sem equivalente na type lib |
| `NodeIdIndex` | ULong |  | gravada no .prj | NodeIdIndex | nomeada | — | sem equivalente na type lib |
| `NodeIdType` | ULong |  | gravada no .prj | NodeIdType | nomeada | — | sem equivalente na type lib |
| `Scale` | ULong |  | gravada no .prj | Scale | nomeada | — | sem equivalente na type lib |
| `UseBits` | ULong |  | gravada no .prj | UseBits | nomeada | — | sem equivalente na type lib |

**Métodos:** `Write()`; `WriteEx(Value Variant, NewTimestamp Variant, NewQuality Variant, SyncWrite Variant)`

**Eventos:** `OnRead()`

<a id="iodrv-uatagblock"></a>
### UaTagBlock

- CLSID `{22EFB9F8-12D6-4162-9E22-8F15DFDFBFC7}` · interface `IUaTagBlock` · eventos `DCommonTagEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- OPC UA Tag Block Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `AdviseType` | AdviseTypes | RW | type lib | — | — | — | AdviseType Controls the Advise mode. The available options are described on the next table. Available options for the AdviseType property 0 - AlwaysInAdvise OPC UA Block Tag is kept updated if the OPC UA Block Tag's AllowRead property is set to True and the OPC UA Subscription's Enable property is a… |
| `AllowRead` | Boolean | RW | type lib | — | — | True | AllowRead Configure this property to define whether this OPC UA Block Tag must be read or not by an OPC UA Driver. If this property is set to True, then the OPC UA Driver automatically updates the OPC UA Block Element's Value and Bits, from Bit00 to Bit31, properties in time spans. Otherwise, this O… |
| `AllowWrite` | Boolean | RW | type lib | — | — | True | AllowWrite Configure this property to define whether this OPC UA Block Tag must be read or not by an OPC UA Driver. If this property is set to True, then the OPC UA Driver automatically updates the OPC UA Block Element's Value and Bits, from Bit00 to Bit31, properties in span times. Otherwise, this … |
| `DataType` | UaDataTypes | R | type lib | — | — | — | DataType Property filled when Elipse E3 connects to an OPC UA Server, which indicates the data type on that OPC UA Server. This property is initially filled during the browsing process, if performed, and in any communication or connection to an OPC UA Server. Values below 1,000 are scalar and values… |
| `EnableDriverEvent` | Boolean | RW | type lib | — | — | False | EnableDriverEvent This property is used to control the generation of the OnTagRead event, which occurs in the OPC UA Driver that contains this OPC UA Block Tag. If this property is set to True, at each reading from an OPC UA Server, whether in error or not, the OnTagRead event in the OPC UA Driver t… |
| `ItemID` | String | RW | type lib | — | — | — | ItemID Specifies the path to perform a browsing of an OPC UA Block Tag on an OPC UA Server. This path is used in OPC UA Driver's RefreshUaNodeIds method to retrieve an OPC UA Node Identifier of an OPC UA Block Tag, when needed. |
| `Quality` | Long | R | type lib | — | — | 0 (zero, bad quality) | Quality This property informs the quality of the value in the Value property. Each time an OPC UA Driver attributes a new value to this OPC UA Block Tag, it also configures the quality of that data. This is a read-only property. The default value of this property is 0 (zero, bad quality). For more i… |
| `Size` | Long | RW | type lib | — | — | 0 (zero) | Size Defines the size of an OPC UA Block Tag's set of values. Please check the documentation of the Driver used to verify the limit for this property, according to B1 to B4 parameters. By creating the OPC UA Block Elements for this OPC UA Block Tag, users can access all values read and also allows w… |
| `SyncWrite` | Boolean | RW | type lib | — | — | False | SyncWrite This property determines the type of writing used by an OPC UA Block Tag. If this property is set to True, this writing is synchronous, that is, the OPC UA Driver waits for the result of the writing to an OPC UA Server. Otherwise, this writing is asynchronous, that is, the value in the OPC… |
| `TimeStamp` | Date | RW | type lib | — | — | "00:00:00" | TimeStamp This property is updated whenever any change of value or status in the Value or Quality properties occurs. This property informs the linked date and time to both value and quality of an OPC UA Block Tag. This is a read-only property. The default value of this property is "00:00:00". ⚠ manual: somente leitura |
| `UaNodeId` | IE3UaNodeId | RW | type lib | — | — | — | UaNodeId Specifies the path to perform a browsing of an OPC UA Block Tag on an OPC UA Server. This path is used in OPC UA Driver's RefreshUaNodeIds method to retrieve an OPC UA Node Identifier of an OPC UA Block Tag, when needed. This property must be filled in to establish communication with an OPC… |
| `WriteValueMode` | EWriteValueMode | RW | type lib | — | — | — | WriteValueMode Read-and-write property controlling the behavior of sending a value in writing operations. This property must be configured according to the OPC UA Server used, or the writing fails. Possible values for this property are 0 - wvmDefault: Follows the default behavior, that is, the behav… |

**Métodos:** `Write()`; `WriteEx(Value Variant, NewTimestamp Variant, NewQuality Variant, SyncWrite Variant)`

**Eventos:** `OnRead()`

### Enumerações de IODrv

- **__MIDL___MIDL_itf_IODrvLib_0002_0056_0001**: nitNumeric=0, nitString=1, nitGUID=2, nitOpaque=3
- **AdviseTypes**: AlwaysInAdvise=0, AdviseWhenLinked=1
- **EWriteSyncMode**: wsmDefault=0, wsmSync=1, wsmAsyncUnconfirmed=2
- **EWriteValueMode**: wvmDefault=0, wvmValueOnly=1, wvmValueQualityTimestamp=2
- **IOQUALITY**: IQ_BAD_OFFSCAN=28, IQ_BAD_INITIAL=24, IQ_BAD_COMMERROR=20, IQ_GOOD=192
- **OPCCompatibilityModes**: AnyVersion=0, Version10A=1, Version20=2
- **OPCEnumVts**: _Undefined=0, _Null=1, _Integer=2, _Long=3, _Single=4, _Double=5, _Currency=6, _Date=7, _String=8, _Object=9, _Error=10, _Boolean=11, _Variant=12, _UnkObject=13, _Decimal=14, _Record=36, _Char=16, _Byte=17, _Word=18, _DWord=19, _LongLong=20, _DDWord=21, _Integer_=22, _UInteger=23, _ArrInteger=8194, _ArrLong=8195, _ArrSingle=8196, _ArrDouble=8197, _ArrCurrency=8198, _ArrDate=8199, _ArrString=8200, _ArrObject=8201, _ArrError=8202, _ArrBoolean=8203, _ArrVariant=8204, _ArrUnkObject=8205, _ArrDecimal=8206, _ArrRecord=8228, _ArrChar=8208, _ArrByte=8209, _ArrWord=8210, _ArrDWord=8211, _ArrLongLong=8212, _ArrDDWord=8213, _ArrInteger_=8214, _ArrUInteger=8215
- **OPCRefreshSource**: RefreshFromCache=1, RefreshFromDevice=2
- **OPCStatus**: ServerStatus_Unknown=-1, ServerStatus_NotConnected=0, ServerStatus_Running=1, ServerStatus_Failed=2, ServerStatus_NoConfig=3, ServerStatus_Suspended=4, ServerStatus_Test=5
- **UaDataTypes**: udtUnknown=-1, udtNull=0, udtBoolean=1, udtSByte=2, udtByte=3, udtInt16=4, udtUInt16=5, udtInt32=6, udtUInt32=7, udtInt64=8, udtUInt64=9, udtFloat=10, udtDouble=11, udtString=12, udtDateTime=13, udtGuid=14, udtByteString=15, udtXmlElement=16, udtNodeId=17, udtExpandedNodeId=18, udtStatusCode=19, udtQualifiedName=20, udtLocalizedText=21, udtStructure=22, udtDataValue=23, udtVariant=24, udtDiagnosticInfo=25, udtArrayUnknown=1000, udtArrayBoolean=1001, udtArraySByte=1002, udtArrayByte=1003, udtArrayInt16=1004, udtArrayUInt16=1005, udtArrayInt32=1006, udtArrayUInt32=1007, udtArrayInt64=1008, udtArrayUInt64=1009, udtArrayFloat=1010, udtArrayDouble=1011, udtArrayString=1012, udtArrayDateTime=1013, udtArrayGuid=1014, udtArrayByteString=1015, udtArrayXmlElement=1016, udtArrayNodeId=1017, udtArrayExpandedNodeId=1018, udtArrayStatusCode=1019, udtArrayQualifiedName=1020, udtArrayLocalizedText=1021, udtArrayStructure=1022, udtArrayDataValue=1023, udtArrayVariant=1024
- **UaSecurityModes**: usmNone=1, usmSign=2, usmSignAndEncrypt=3
- **UaSecurityPolicies**: uspNone=1, uspBasic128Rsa15=2, uspBasic256=3, uspBasic256Sha256=4, uspAes128_Sha256_RsaOaep=5, uspAes256_Sha256_RsaPss=6
- **UaServerState**: ussNotConnected=-1, ussRunning=0, ussFailed=1, ussNoConfig=2, ussSuspended=3, ussShutdown=4, ussTest=5, ussCommunicationFault=6, ussUnknown=7
- **WriteFeedbackModes**: wfWaitNextRead=0, wfImmediateReadAfterWrite=1, wfTrustWriteSuccess=2

---

## E3Alarm

Arquivo `E3Alarm.dll` · versão 5.5 · LIBID `{8193992F-15B9-49C4-A179-348FF81671AA}` · E3Alarm ActiveX

Classes: [E3Alarm](#e3alarm-e3alarm), [E3AlarmColorObject](#e3alarm-e3alarmcolorobject)

<a id="e3alarm-e3alarm"></a>
### E3Alarm

- CLSID `{FBCECFF1-9034-4F17-983F-B07E77ABDCE4}` · interface `_DE3Alarm` · eventos `_DE3AlarmEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 46 instâncias em 27 arquivo(s)
- E3Alarm Control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Font` | Font | RW | type lib | — | não gravada nomeada | — | Determines the font for this object's header and rows. This is a read-only property and can only be modified in Elipse E3 Studio, not at run time. Please check topic Font for more information about the sub-properties of this property. ⚠ manual: somente leitura |
| `Events` | IEventStatusCollection | R | type lib | — | não gravada nomeada | — | Returns a collection of Events on this object. This is a read-only property. For more information about the collection returned by this property, please check topic Collection of Events. |
| `Connections` | IAlarmConnectionCollection | R | type lib | — | não gravada nomeada | — | Returns a collection of Connections on this object. This is a read-only property. For more information about the collection returned by this property, please check topic Collection of Connections. |
| `Filters` | IConnectionFilterCollection | R | type lib | — | não gravada nomeada | — | Returns a collection of Filters on this object. This is a read-only property. For more information about the collection returned by this property, please check topic Collection of Filters. |
| `Fields` | IAlarmFieldCollection | R | type lib | — | não gravada nomeada | — | Returns a collection of Fields on this object. This is a read-only property. For more information about the collection returned by this property, please check topic Collection of Fields. |
| `AlarmCount` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of Alarms on this object. This is a read-only property. |
| `ActiveNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms on this object, active or not. This is a read-only property. |
| `ActiveHighNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a High severity on this object. This is a read-only property. |
| `ActiveMedNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a Medium severity on this object. This is a read-only property. |
| `ActiveLowNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a Low severity on this object. This is a read-only property. |
| `ActiveAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of active Alarms on this object. This is a read-only property. |
| `ActiveHighAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a High severity on this object. This is a read-only property. |
| `ActiveMedAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a Medium severity on this object. This is a read-only property. |
| `ActiveLowAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a Low severity on this object. This is a read-only property. |
| `InactiveNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Determines the number of inactive and unacknowledged Alarms on this object. This is a read-only property. |
| `InactiveHighNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a High severity on this object. This is a read-only property. |
| `InactiveMedNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a Medium severity on this object. This is a read- only property. |
| `InactiveLowNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a Low severity on this object. This is a read-only property. |
| `ActiveCritNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of unacknowledged Alarms with a Critical severity on this object. This is a read-only property. |
| `ActiveCritAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of active Alarms with a Critical severity on this object. This is a read-only property. |
| `InactiveCritNACKAlarms` | Long | R | type lib | — | não gravada nomeada | — | Indicates the number of inactive and unacknowledged Alarms with a Critical severity on this object. This is a read-only property. |
| `ColorActiveAlarm[lSeverity EAlarmSeverity]` | IE3AlarmColorObject | RW | type lib | — | não gravada nomeada | — | Defines an object that configures the colors of an active Alarm. This property is indexed by the Alarm severity and is only available via script. The next table contains all available options for the index of this property. Available options for the index of the ColorActiveAlarm property INDEX SEVER… |
| `ColorAckedAlarm[lSeverity EAlarmSeverity]` | IE3AlarmColorObject | RW | type lib | — | não gravada nomeada | — | Defines an object that configures the colors of an acknowledged Alarm. This property is indexed by the Alarm severity and is only available via script. For more information about this property's behavior, please check the ColorActiveAlarm property. |
| `ColorNAckAlarm[lSeverity EAlarmSeverity]` | IE3AlarmColorObject | RW | type lib | — | não gravada nomeada | — | Defines an object that configures the colors of an unacknowledged Alarm. This property is indexed by the Alarm severity and is only available via script. For more information about this property's behavior, please check the ColorActiveAlarm property. |
| `ColorActiveEvent[lSeverity EAlarmSeverity]` | IE3AlarmColorObject | RW | type lib | — | não gravada nomeada | — | Defines an object that configures the colors of an active Event. This property is indexed by the Alarm severity and is only available via script. For more information about this property's behavior, please check the ColorActiveAlarm property. |
| `Domain` | String | RW | type lib | Domain | nomeada | an empty String, that is, this object connects t… | Specifies the Domain to which this object connects, such as "\\NameOfAnotherServer". The default value of this property is an empty String, that is, this object connects to the same Elipse E3 Viewer's Domain where it is. |
| `AlarmServer` | BSTRALARMLINK | RW | type lib | AlarmServer | nomeada | — | Name of a unique Alarm Server in an application. |
| `Filter` | String | RW | type lib | Filter | nomeada | — |  |
| `ShowMediumPriority` | Boolean | RW | type lib | ShowMediumPriority | nomeada | True | If this property is set to True, displays Alarms with a Medium severity. The default value of this property is True. |
| `ShowLowPriority` | Boolean | RW | type lib | ShowLowPriority | nomeada | True | If this property is set to True, displays Alarms with a Low severity. The default value of this property is True. |
| `ShowHighPriority` | Boolean | RW | type lib | ShowHighPriority | nomeada | True | If this property is set to True, displays Alarms with a High severity. The default value of this property is True. |
| `ColumnHeader` | Boolean | RW | type lib | ColumnHeader | nomeada | True | When set to True, this property enables viewing this object's header. This header also allows performing a table's data reordering visually. For more information, please check the AllowColumnClick property. The default value of this property is True. |
| `GridBkColor` | OLE_COLOR | RW | type lib | GridBkColor | nomeada | the color configured in Windows for the Window i… | Determines a color for this object's background. The default value of this property is the color configured in Windows for the Window item, on Control Panel - Display - Appearance - Advanced. |
| `PrimarySortField` | String | RW | type lib | — | não gravada nomeada | "EventTime" | Determines a primary Field for sorting Events on this object. Please check all available Fields on Elipse E3 User's Manual. The default value of this property is "EventTime". When this property is an empty String, the SecondarySortField, ThirdSortField, and FourthSortField properties do not have any… |
| `PrimarySortAscending` | Boolean | RW | type lib | — | não gravada nomeada | False | When this property is set to False, the sort order of Events by a primary Field is performed in descending order. Otherwise, it is performed in ascending order. The default value of this property is False. |
| `SecondarySortField` | String | RW | type lib | — | não gravada nomeada | an empty String | Determines a secondary Field for sorting Events on this object. Please check all available Fields on Elipse E3 User's Manual. The default value of this property is an empty String. This property does not have any effect when the PrimarySortField property is an empty String. |
| `SecondarySortAscending` | Boolean | RW | type lib | — | não gravada nomeada | False | When this property is set to False, the sort order of Events by a secondary Field is performed in descending order. Otherwise, it is performed in ascending order. The default value of this property is False. |
| `AllowColumnClick` | Boolean | RW | type lib | AllowColumnClick | nomeada | — | Enables or disables Field selection and their sort direction, by clicking this object's column headers at run time. If True, and the header is invisible when users click the column title, data is sorted using this column as the key. For more information, please check the ColumnHeader property. When … |
| `PopupMenu` | Boolean | RW | type lib | PopupMenu | nomeada | True | Enables a contextual menu when right-clicking this object. The default value of this property is True. 172 View |
| `AllowAckSelected` | Boolean | RW | type lib | AllowAckSelected | nomeada | True | Enables or disables the Only the selected events item of the ACK Alarms option on this object's contextual menu, which allows acknowledging the selected Alarms. If there are no selected Alarms, this property has no effect. The default value of this property is True. 168 View |
| `AllowAckCurrentFilter` | Boolean | RW | type lib | AllowAckCurrentFilter | nomeada | True | Enables or disables the All events of the current filter item of the ACK Alarms option on this object's contextual menu, which allows acknowledging all Alarms of the current Filter. If there are no visible Alarms, this property has no effect. The default value of this property is True. |
| `AllowAckAll` | Boolean | RW | type lib | AllowAckAll | nomeada | True | Enables or disables the ACK Alarms option on this object's contextual menu, which allows acknowledging all Alarms. The default value of this property is True. |
| `SimpleAreaFilter` | Boolean | RW | type lib | SimpleAreaFilter | nomeada | — | When this property is set to True, the behavior of filtering by Alarm Area names is based only on the coincidence of the initial part of a name. When this property is set to False, this behavior considers the entire Area name, but allows using wildcard characters and multiple Area Filters, which mus… |
| `FilterType` | AlarmFilterType | RW | type lib | FilterType | nomeada | — | Performs the Alarm Filters. Possible values for this property are 1 - OnlyAlarms: Displays only Alarms (default), 2 - OnlyEvents: Displays only Events, or 3 - AlarmsAndEvents: Displays both Alarms and Events. |
| `AreaFilter` | String | RW | type lib | Filter1 (apelido confirmado) | nomeada | an empty String, that is, no filtering by Area | Controls visible Alarm Areas on this object. If its value is not an empty String, it displays events whose Area names start with the indicated text. For example, if this property is equal to "Ana", it displays Alarm Areas such as "Analog.Production" or "Analysis", but not "Digital.Analysis" or "Digi… |
| `CustomFilter` | String | RW | type lib | CustomFilter | nomeada | — | Allows informing a customized Filter for Alarms as an expression. Please check Alarm Filter's CustomFilter property for more information about the available Fields for use on this Filter's expression. User-defined Fields can also be used on a Filter expression, by using the name defined on the Alarm… |
| `ThirdSortField` | String | RW | type lib | — | não gravada nomeada | an empty String | Determines a third Field for sorting Events in this object. Please check all available Fields on Elipse E3 User's Manual. The default value of this property is an empty String. This property has no effect when the PrimarySortField or SecondarySortField properties are configured as an empty String. |
| `ThirdSortAscending` | Boolean | RW | type lib | — | não gravada nomeada | False | When this property is set to False, the sort order of Events by a third Field is performed in descending order. Otherwise, it is performed in ascending order. The default value of this property is False. |
| `FourthSortField` | String | RW | type lib | — | não gravada nomeada | an empty String | Determines a fourth Field for sorting Events on this object. Please check all available Fields on Elipse E3 User's Manual. The default value of this property is an empty String. This property has no effect when the PrimarySortField, SecondarySortField, or ThirdSortField properties are configured as … |
| `FourthSortAscending` | Boolean | RW | type lib | — | não gravada nomeada | False | When this property is set to False, the sort order of Events by a fourth Field is performed in descending order. Otherwise, it is performed in ascending order. The default value of this property is False. |
| `BorderColor` | OLE_COLOR | RW | type lib | BorderColor | nomeada | black (RGB(0, 0, 0)) | Defines a border color for this object. The default value of this property is black (RGB(0, 0, 0)). |
| `BorderThickness` | Long | RW | type lib | BorderThickness | nomeada | 1 (one) | Defines a border thickness for this object. This property's value ranges from 0 (zero, which disables the border) to 10, and its default value is 1 (one). |
| `BannerMode` | Boolean | RW | type lib | BannerMode | nomeada | False | Enables the visualization of a single message on this object. The displayed message depends on the sort configuration and it is always selected. The default value of this property is False. For more information about the sort configuration, please check topic Sorting Tab on Elipse E3 User's Manual. |
| `ShowConnectionStatusBar` | Boolean | RW | type lib | ShowConnecBar (apelido confirmado) | nomeada | False | Shows or hides this object's connection status bar. The default value of this property is False. |
| `ConnectionStatusBarColor` | OLE_COLOR | RW | type lib | ConnStatusColor (apelido confirmado) | nomeada | black (RGB(0, 0, 0)) | Specifies a color for the connection status bar of this object. The default value of this property is black (RGB(0, 0, 0)). |
| `PictureConnected` | BSTRPICTURE | RW | type lib | PictureConnected | nomeada | an empty String, that is, this object displays t… | Path of an image file with an icon to represent a Connection from this object's Collection of Connections successfully connected to an Alarm Server. The default value of this property is an empty String, that is, this object displays the icon on its connection status bar for this Connection. |
| `PictureNotConnected` | BSTRPICTURE | RW | type lib | PictureConnectionError (apelido confirmado) | nomeada | an empty String, that is, this object displays t… | Path of an image file with an icon to represent a Connection from this object's Collection of Connections not connected to an Alarm Server. The default value of this property is an empty String, that is, this object displays the icon on its connection status bar for this Connection. |
| `PictureUnknown` | BSTRPICTURE | RW | type lib | PictureUnknownConnection (apelido confirmado) | nomeada | an empty String, that is, this object displays t… | Path of an image file with an icon to represent a Connection on this object's Collection of Connections with an unknown status. The default value of this property is an empty String, that is, this object displays the icon on its connection status bar for this Connection. An unknown status indicates … |
| `AllowDeleteUnboundAlarms` | Boolean | RW | type lib | AllowDeleteAllUnbound (apelido confirmado) | nomeada | True | Enables or disables the Delete unbound alarms option on this object's contextual menu, which allows removing unbound Alarms. If there are no unbound Alarms, this property has no effect. The default value of this property is True. |
| `EnableSortMarker` | Boolean | RW | type lib | EnableSortMarker | nomeada | True | Enables or disables an indication of column sorting on this object. Only the first column used on sorting displays this indication. For applications created with version 4.8 or later, the default value of this property is True. For applications created in earlier versions and then updated to version… |
| `ShowCriticalPriority` | Boolean | RW | type lib | ShowCriticalPriority | nomeada | True | If this property is set to True, displays Alarms with a Critical severity. The default value of this property is True. |
| `AllowShelveAlarms` | Boolean | RW | type lib | AllowShelveAlarms | nomeada | True | Enables or disables the Shelve Alarms and Unshelve Alarms options on the contextual menu of this object, which allow shelving or unshelving all Alarms or Events. The default value of this property is True. |
| `ShowIcon` | Boolean | RW | type lib | ShowIcon | nomeada | True | Allows showing or hiding the icon on the first column of Events. The default value of this property is True. |
| `AllowRemoveFromServiceAlarms` | Boolean | RW | type lib | AllowRemoveFromServiceAlarms | nomeada | True | Configures whether this object allows or not the suppression of Alarms of type Out-of-Service. The default value of this property is True. |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_ExtentX` | Long |  | gravada no .prj | _ExtentX | nomeada | — | sem equivalente na type lib |
| `_ExtentY` | Long |  | gravada no .prj | _ExtentY | nomeada | — | sem equivalente na type lib |
| `_StockProps` | Long |  | gravada no .prj | _StockProps | nomeada | — | sem equivalente na type lib |
| `_Version` | Long |  | gravada no .prj | _Version | nomeada | — | sem equivalente na type lib |
| `AckBackColor` | Long |  | gravada no .prj | AckBackColor | nomeada | — | sem equivalente na type lib |
| `AckBlink` | Long |  | gravada no .prj | AckBlink | nomeada | — | sem equivalente na type lib |
| `AckCritBkColor` | Long |  | gravada no .prj | AckCritBkColor | nomeada | — | sem equivalente na type lib |
| `AckCritBlink` | Long |  | gravada no .prj | AckCritBlink | nomeada | — | sem equivalente na type lib |
| `AckCritTextColor` | Long |  | gravada no .prj | AckCritTextColor | nomeada | — | sem equivalente na type lib |
| `AckCritTextColor2` | Long |  | gravada no .prj | AckCritTextColor2 | nomeada | — | sem equivalente na type lib |
| `AckHiBkColor` | Long |  | gravada no .prj | AckHiBkColor | nomeada | — | sem equivalente na type lib |
| `AckHiBlink` | Long |  | gravada no .prj | AckHiBlink | nomeada | — | sem equivalente na type lib |
| `AckHiTextColor` | Long |  | gravada no .prj | AckHiTextColor | nomeada | — | sem equivalente na type lib |
| `AckHiTextColor2` | Long |  | gravada no .prj | AckHiTextColor2 | nomeada | — | sem equivalente na type lib |
| `AckLowBkColor` | Long |  | gravada no .prj | AckLowBkColor | nomeada | — | sem equivalente na type lib |
| `AckLowBlink` | Long |  | gravada no .prj | AckLowBlink | nomeada | — | sem equivalente na type lib |
| `AckLowTextColor` | Long |  | gravada no .prj | AckLowTextColor | nomeada | — | sem equivalente na type lib |
| `AckLowTextColor2` | Long |  | gravada no .prj | AckLowTextColor2 | nomeada | — | sem equivalente na type lib |
| `AckMedBkColor` | Long |  | gravada no .prj | AckMedBkColor | nomeada | — | sem equivalente na type lib |
| `AckMedBlink` | Long |  | gravada no .prj | AckMedBlink | nomeada | — | sem equivalente na type lib |
| `AckMedTextColor` | Long |  | gravada no .prj | AckMedTextColor | nomeada | — | sem equivalente na type lib |
| `AckMedTextColor2` | Long |  | gravada no .prj | AckMedTextColor2 | nomeada | — | sem equivalente na type lib |
| `AckOverrideBkCritPri` | Boolean |  | gravada no .prj | AckOverrideBkCritPri | nomeada | — | sem equivalente na type lib |
| `AckOverrideBkHiPri` | Boolean |  | gravada no .prj | AckOverrideBkHiPri | nomeada | — | sem equivalente na type lib |
| `AckOverrideBkLowPri` | Boolean |  | gravada no .prj | AckOverrideBkLowPri | nomeada | — | sem equivalente na type lib |
| `AckOverrideBkMedPri` | Boolean |  | gravada no .prj | AckOverrideBkMedPri | nomeada | — | sem equivalente na type lib |
| `AckOverrideCritBlink` | Boolean |  | gravada no .prj | AckOverrideCritBlink | nomeada | — | sem equivalente na type lib |
| `AckOverrideCritPri` | Boolean |  | gravada no .prj | AckOverrideCritPri | nomeada | — | sem equivalente na type lib |
| `AckOverrideHiBlink` | Boolean |  | gravada no .prj | AckOverrideHiBlink | nomeada | — | sem equivalente na type lib |
| `AckOverrideHiPri` | Boolean |  | gravada no .prj | AckOverrideHiPri | nomeada | — | sem equivalente na type lib |
| `AckOverrideLowBlink` | Boolean |  | gravada no .prj | AckOverrideLowBlink | nomeada | — | sem equivalente na type lib |
| `AckOverrideLowPri` | Boolean |  | gravada no .prj | AckOverrideLowPri | nomeada | — | sem equivalente na type lib |
| `AckOverrideMedBlink` | Boolean |  | gravada no .prj | AckOverrideMedBlink | nomeada | — | sem equivalente na type lib |
| `AckOverrideMedPri` | Boolean |  | gravada no .prj | AckOverrideMedPri | nomeada | — | sem equivalente na type lib |
| `AckTextColor` | Long |  | gravada no .prj | AckTextColor | nomeada | — | sem equivalente na type lib |
| `AckTextColor2` | Long |  | gravada no .prj | AckTextColor2 | nomeada | — | sem equivalente na type lib |
| `AlmBackColor` | Long |  | gravada no .prj | AlmBackColor | nomeada | — | sem equivalente na type lib |
| `AlmCritBkColor` | Long |  | gravada no .prj | AlmCritBkColor | nomeada | — | sem equivalente na type lib |
| `AlmCritBlink` | Long |  | gravada no .prj | AlmCritBlink | nomeada | — | sem equivalente na type lib |
| `AlmCritTextColor` | Long |  | gravada no .prj | AlmCritTextColor | nomeada | — | sem equivalente na type lib |
| `AlmCritTextColor2` | Long |  | gravada no .prj | AlmCritTextColor2 | nomeada | — | sem equivalente na type lib |
| `AlmDefBlink` | Long |  | gravada no .prj | AlmDefBlink | nomeada | — | sem equivalente na type lib |
| `AlmDefTextColor` | Long |  | gravada no .prj | AlmDefTextColor | nomeada | — | sem equivalente na type lib |
| `AlmDefTextColor2` | Long |  | gravada no .prj | AlmDefTextColor2 | nomeada | — | sem equivalente na type lib |
| `AlmHiBkColor` | Long |  | gravada no .prj | AlmHiBkColor | nomeada | — | sem equivalente na type lib |
| `AlmHiBlink` | Long |  | gravada no .prj | AlmHiBlink | nomeada | — | sem equivalente na type lib |
| `AlmHiTextColor` | Long |  | gravada no .prj | AlmHiTextColor | nomeada | — | sem equivalente na type lib |
| `AlmHiTextColor2` | Long |  | gravada no .prj | AlmHiTextColor2 | nomeada | — | sem equivalente na type lib |
| `AlmLowBkColor` | Long |  | gravada no .prj | AlmLowBkColor | nomeada | — | sem equivalente na type lib |
| `AlmLowBlink` | Long |  | gravada no .prj | AlmLowBlink | nomeada | — | sem equivalente na type lib |
| `AlmLowTextColor` | Long |  | gravada no .prj | AlmLowTextColor | nomeada | — | sem equivalente na type lib |
| `AlmLowTextColor2` | Long |  | gravada no .prj | AlmLowTextColor2 | nomeada | — | sem equivalente na type lib |
| `AlmMedBkColor` | Long |  | gravada no .prj | AlmMedBkColor | nomeada | — | sem equivalente na type lib |
| `AlmMedBlink` | Long |  | gravada no .prj | AlmMedBlink | nomeada | — | sem equivalente na type lib |
| `AlmMedTextColor` | Long |  | gravada no .prj | AlmMedTextColor | nomeada | — | sem equivalente na type lib |
| `AlmMedTextColor2` | Long |  | gravada no .prj | AlmMedTextColor2 | nomeada | — | sem equivalente na type lib |
| `AlmOverrideCritBlink` | Boolean |  | gravada no .prj | AlmOverrideCritBlink | nomeada | — | sem equivalente na type lib |
| `AlmOverrideHiBlink` | Boolean |  | gravada no .prj | AlmOverrideHiBlink | nomeada | — | sem equivalente na type lib |
| `AlmOverrideLowBlink` | Boolean |  | gravada no .prj | AlmOverrideLowBlink | nomeada | — | sem equivalente na type lib |
| `AlmOverrideMedBlink` | Boolean |  | gravada no .prj | AlmOverrideMedBlink | nomeada | — | sem equivalente na type lib |
| `Asc1` | Long |  | gravada no .prj | Asc1 | nomeada | — | sem equivalente na type lib |
| `Asc2` | Long |  | gravada no .prj | Asc2 | nomeada | — | sem equivalente na type lib |
| `AscendingSort#` | Boolean |  | gravada no .prj | AscendingSort# | nomeada | — | sem equivalente na type lib (família: 4) |
| `Charset` | Integer |  | gravada no .prj | Charset | nomeada | — | sem equivalente na type lib |
| `ConnectionName` | String |  | gravada no .prj | ConnectionName | nomeada | — | sem equivalente na type lib |
| `ConnFilterName` | String |  | gravada no .prj | ConnFilterName | nomeada | — | sem equivalente na type lib |
| `ConnFilterName1` | String |  | gravada no .prj | ConnFilterName1 | nomeada | — | sem equivalente na type lib |
| `ConnSize` | Long |  | gravada no .prj | ConnSize | nomeada | — | sem equivalente na type lib |
| `CustomFilter1` | String |  | gravada no .prj | CustomFilter1 | nomeada | — | sem equivalente na type lib |
| `DomainName` | String |  | gravada no .prj | DomainName | nomeada | — | sem equivalente na type lib |
| `EvtBackColor` | Long |  | gravada no .prj | EvtBackColor | nomeada | — | sem equivalente na type lib |
| `EvtCritBkColor` | Long |  | gravada no .prj | EvtCritBkColor | nomeada | — | sem equivalente na type lib |
| `EvtCritBlink` | Long |  | gravada no .prj | EvtCritBlink | nomeada | — | sem equivalente na type lib |
| `EvtCritTextColor` | Long |  | gravada no .prj | EvtCritTextColor | nomeada | — | sem equivalente na type lib |
| `EvtCritTextColor2` | Long |  | gravada no .prj | EvtCritTextColor2 | nomeada | — | sem equivalente na type lib |
| `EvtDefBlink` | Long |  | gravada no .prj | EvtDefBlink | nomeada | — | sem equivalente na type lib |
| `EvtDefTextColor` | Long |  | gravada no .prj | EvtDefTextColor | nomeada | — | sem equivalente na type lib |
| `EvtDefTextColor2` | Long |  | gravada no .prj | EvtDefTextColor2 | nomeada | — | sem equivalente na type lib |
| `EvtHiBkColor` | Long |  | gravada no .prj | EvtHiBkColor | nomeada | — | sem equivalente na type lib |
| `EvtHiBlink` | Long |  | gravada no .prj | EvtHiBlink | nomeada | — | sem equivalente na type lib |
| `EvtHiTextColor` | Long |  | gravada no .prj | EvtHiTextColor | nomeada | — | sem equivalente na type lib |
| `EvtHiTextColor2` | Long |  | gravada no .prj | EvtHiTextColor2 | nomeada | — | sem equivalente na type lib |
| `EvtLowBkColor` | Long |  | gravada no .prj | EvtLowBkColor | nomeada | — | sem equivalente na type lib |
| `EvtLowBlink` | Long |  | gravada no .prj | EvtLowBlink | nomeada | — | sem equivalente na type lib |
| `EvtLowTextColor` | Long |  | gravada no .prj | EvtLowTextColor | nomeada | — | sem equivalente na type lib |
| `EvtLowTextColor2` | Long |  | gravada no .prj | EvtLowTextColor2 | nomeada | — | sem equivalente na type lib |
| `EvtMedBkColor` | Long |  | gravada no .prj | EvtMedBkColor | nomeada | — | sem equivalente na type lib |
| `EvtMedBlink` | Long |  | gravada no .prj | EvtMedBlink | nomeada | — | sem equivalente na type lib |
| `EvtMedTextColor` | Long |  | gravada no .prj | EvtMedTextColor | nomeada | — | sem equivalente na type lib |
| `EvtMedTextColor2` | Long |  | gravada no .prj | EvtMedTextColor2 | nomeada | — | sem equivalente na type lib |
| `EvtOverrideBkCritPri` | Boolean |  | gravada no .prj | EvtOverrideBkCritPri | nomeada | — | sem equivalente na type lib |
| `EvtOverrideBkHiPri` | Boolean |  | gravada no .prj | EvtOverrideBkHiPri | nomeada | — | sem equivalente na type lib |
| `EvtOverrideBkLowPri` | Boolean |  | gravada no .prj | EvtOverrideBkLowPri | nomeada | — | sem equivalente na type lib |
| `EvtOverrideBkMedPri` | Boolean |  | gravada no .prj | EvtOverrideBkMedPri | nomeada | — | sem equivalente na type lib |
| `EvtOverrideCritBlink` | Boolean |  | gravada no .prj | EvtOverrideCritBlink | nomeada | — | sem equivalente na type lib |
| `EvtOverrideCritPri` | Boolean |  | gravada no .prj | EvtOverrideCritPri | nomeada | — | sem equivalente na type lib |
| `EvtOverrideHiBlink` | Boolean |  | gravada no .prj | EvtOverrideHiBlink | nomeada | — | sem equivalente na type lib |
| `EvtOverrideHiPri` | Boolean |  | gravada no .prj | EvtOverrideHiPri | nomeada | — | sem equivalente na type lib |
| `EvtOverrideLowBlink` | Boolean |  | gravada no .prj | EvtOverrideLowBlink | nomeada | — | sem equivalente na type lib |
| `EvtOverrideLowPri` | Boolean |  | gravada no .prj | EvtOverrideLowPri | nomeada | — | sem equivalente na type lib |
| `EvtOverrideMedBlink` | Boolean |  | gravada no .prj | EvtOverrideMedBlink | nomeada | — | sem equivalente na type lib |
| `EvtOverrideMedPri` | Boolean |  | gravada no .prj | EvtOverrideMedPri | nomeada | — | sem equivalente na type lib |
| `FieldAckType#` | Long |  | gravada no .prj | FieldAckType# | nomeada | — | sem equivalente na type lib (família: 7) |
| `FieldBlink#` | Boolean |  | gravada no .prj | FieldBlink# | nomeada | — | sem equivalente na type lib (família: 7) |
| `FieldColumn#` | String |  | gravada no .prj | FieldColumn# | nomeada | — | sem equivalente na type lib (família: 7) |
| `FieldCount` | Long |  | gravada no .prj | FieldCount | nomeada | — | sem equivalente na type lib |
| `FieldFormat#` | String |  | gravada no .prj | FieldFormat# | nomeada | — | sem equivalente na type lib (família: 7) |
| `FieldName#` | String |  | gravada no .prj | FieldName# | nomeada | — | sem equivalente na type lib (família: 7) |
| `FieldSize#` | Long |  | gravada no .prj | FieldSize# | nomeada | — | sem equivalente na type lib (família: 7) |
| `FieldVisible#` | Boolean |  | gravada no .prj | FieldVisible# | nomeada | — | sem equivalente na type lib (família: 7) |
| `FilterName` | String |  | gravada no .prj | FilterName | nomeada | — | sem equivalente na type lib |
| `FiltersCount` | Long |  | gravada no .prj | FiltersCount | nomeada | — | sem equivalente na type lib |
| `FilterType1` | Long |  | gravada no .prj | FilterType1 | nomeada | — | sem equivalente na type lib |
| `IgnoreDiacritics` | Boolean |  | gravada no .prj | IgnoreDiacritics | nomeada | — | sem equivalente na type lib |
| `IgnoreDiacritics1` | Boolean |  | gravada no .prj | IgnoreDiacritics1 | nomeada | — | sem equivalente na type lib |
| `Italic` | Boolean |  | gravada no .prj | Italic | nomeada | — | sem equivalente na type lib |
| `NAckCritBkColor` | Long |  | gravada no .prj | NAckCritBkColor | nomeada | — | sem equivalente na type lib |
| `NAckCritBlink` | Long |  | gravada no .prj | NAckCritBlink | nomeada | — | sem equivalente na type lib |
| `NAckCritTextColor` | Long |  | gravada no .prj | NAckCritTextColor | nomeada | — | sem equivalente na type lib |
| `NAckCritTextColor2` | Long |  | gravada no .prj | NAckCritTextColor2 | nomeada | — | sem equivalente na type lib |
| `NAckHiBkColor` | Long |  | gravada no .prj | NAckHiBkColor | nomeada | — | sem equivalente na type lib |
| `NAckHiBlink` | Long |  | gravada no .prj | NAckHiBlink | nomeada | — | sem equivalente na type lib |
| `NAckHiTextColor` | Long |  | gravada no .prj | NAckHiTextColor | nomeada | — | sem equivalente na type lib |
| `NAckHiTextColor2` | Long |  | gravada no .prj | NAckHiTextColor2 | nomeada | — | sem equivalente na type lib |
| `NAckLowBkColor` | Long |  | gravada no .prj | NAckLowBkColor | nomeada | — | sem equivalente na type lib |
| `NAckLowBlink` | Long |  | gravada no .prj | NAckLowBlink | nomeada | — | sem equivalente na type lib |
| `NAckLowTextColor` | Long |  | gravada no .prj | NAckLowTextColor | nomeada | — | sem equivalente na type lib |
| `NAckLowTextColor2` | Long |  | gravada no .prj | NAckLowTextColor2 | nomeada | — | sem equivalente na type lib |
| `NAckMedBkColor` | Long |  | gravada no .prj | NAckMedBkColor | nomeada | — | sem equivalente na type lib |
| `NAckMedBlink` | Long |  | gravada no .prj | NAckMedBlink | nomeada | — | sem equivalente na type lib |
| `NAckMedTextColor` | Long |  | gravada no .prj | NAckMedTextColor | nomeada | — | sem equivalente na type lib |
| `NAckMedTextColor2` | Long |  | gravada no .prj | NAckMedTextColor2 | nomeada | — | sem equivalente na type lib |
| `NAckOverrideBkCritPri` | Boolean |  | gravada no .prj | NAckOverrideBkCritPri | nomeada | — | sem equivalente na type lib |
| `NAckOverrideBkHiPri` | Boolean |  | gravada no .prj | NAckOverrideBkHiPri | nomeada | — | sem equivalente na type lib |
| `NAckOverrideBkLowPri` | Boolean |  | gravada no .prj | NAckOverrideBkLowPri | nomeada | — | sem equivalente na type lib |
| `NAckOverrideBkMedPri` | Boolean |  | gravada no .prj | NAckOverrideBkMedPri | nomeada | — | sem equivalente na type lib |
| `NAckOverrideCritBlink` | Boolean |  | gravada no .prj | NAckOverrideCritBlink | nomeada | — | sem equivalente na type lib |
| `NAckOverrideCritPri` | Boolean |  | gravada no .prj | NAckOverrideCritPri | nomeada | — | sem equivalente na type lib |
| `NAckOverrideHiBlink` | Boolean |  | gravada no .prj | NAckOverrideHiBlink | nomeada | — | sem equivalente na type lib |
| `NAckOverrideHiPri` | Boolean |  | gravada no .prj | NAckOverrideHiPri | nomeada | — | sem equivalente na type lib |
| `NAckOverrideLowBlink` | Boolean |  | gravada no .prj | NAckOverrideLowBlink | nomeada | — | sem equivalente na type lib |
| `NAckOverrideLowPri` | Boolean |  | gravada no .prj | NAckOverrideLowPri | nomeada | — | sem equivalente na type lib |
| `NAckOverrideMedBlink` | Boolean |  | gravada no .prj | NAckOverrideMedBlink | nomeada | — | sem equivalente na type lib |
| `NAckOverrideMedPri` | Boolean |  | gravada no .prj | NAckOverrideMedPri | nomeada | — | sem equivalente na type lib |
| `Order1` | String |  | gravada no .prj | Order1 | nomeada | — | sem equivalente na type lib |
| `Order2` | String |  | gravada no .prj | Order2 | nomeada | — | sem equivalente na type lib |
| `OverrideBkCritPri` | Boolean |  | gravada no .prj | OverrideBkCritPri | nomeada | — | sem equivalente na type lib |
| `OverrideBkHiPri` | Boolean |  | gravada no .prj | OverrideBkHiPri | nomeada | — | sem equivalente na type lib |
| `OverrideBkLowPri` | Boolean |  | gravada no .prj | OverrideBkLowPri | nomeada | — | sem equivalente na type lib |
| `OverrideBkMedPri` | Boolean |  | gravada no .prj | OverrideBkMedPri | nomeada | — | sem equivalente na type lib |
| `OverrideCritPri` | Boolean |  | gravada no .prj | OverrideCritPri | nomeada | — | sem equivalente na type lib |
| `OverrideHiPri` | Boolean |  | gravada no .prj | OverrideHiPri | nomeada | — | sem equivalente na type lib |
| `OverrideLowPri` | Boolean |  | gravada no .prj | OverrideLowPri | nomeada | — | sem equivalente na type lib |
| `OverrideMedPri` | Boolean |  | gravada no .prj | OverrideMedPri | nomeada | — | sem equivalente na type lib |
| `ShowCriticalPriority1` | Boolean |  | gravada no .prj | ShowCriticalPriority1 | nomeada | — | sem equivalente na type lib |
| `ShowHighPriority1` | Boolean |  | gravada no .prj | ShowHighPriority1 | nomeada | — | sem equivalente na type lib |
| `ShowLowPriority1` | Boolean |  | gravada no .prj | ShowLowPriority1 | nomeada | — | sem equivalente na type lib |
| `ShowMediumPriority1` | Boolean |  | gravada no .prj | ShowMediumPriority1 | nomeada | — | sem equivalente na type lib |
| `SimpleAreaFilter1` | Boolean |  | gravada no .prj | SimpleAreaFilter1 | nomeada | — | sem equivalente na type lib |
| `SortingField#` | String |  | gravada no .prj | SortingField# | nomeada | — | sem equivalente na type lib (família: 4) |
| `Strikethrough` | Boolean |  | gravada no .prj | Strikethrough | nomeada | — | sem equivalente na type lib |
| `UnAckBackColor` | Long |  | gravada no .prj | UnAckBackColor | nomeada | — | sem equivalente na type lib |
| `UnAckBlink` | Long |  | gravada no .prj | UnAckBlink | nomeada | — | sem equivalente na type lib |
| `UnAckTextColor` | Long |  | gravada no .prj | UnAckTextColor | nomeada | — | sem equivalente na type lib |
| `UnAckTextColor2` | Long |  | gravada no .prj | UnAckTextColor2 | nomeada | — | sem equivalente na type lib |
| `Underline` | Boolean |  | gravada no .prj | Underline | nomeada | — | sem equivalente na type lib |
| `UserFieldCount` | Long |  | gravada no .prj | UserFieldCount | nomeada | — | sem equivalente na type lib |
| `Weight` | Integer |  | gravada no .prj | Weight | nomeada | — | sem equivalente na type lib |

**Métodos:** `AboutBox()`; `GetFocusedEvent()`; `GetEventByIndex(Index UInt)`; `AckSelected(Operator Variant)`; `AckCurrentFilter(Operator Variant)`; `AckAll(Operator Variant)`; `DeleteUnboundSelected(Operator Variant)`; `DeleteUnboundCurrentFilter(Operator Variant)`; `DeleteUnboundAll(Operator Variant)`; `ShelveSelected(Duration ULong, bstrReason String, Operator Variant)`; `ShelveCurrentFilter(Duration ULong, bstrReason String, Operator Variant)`; `ShelveAll(Duration ULong, bstrReason String, Operator Variant)`; `UnshelveSelected(bstrReason String, Operator Variant)`; `UnshelveCurrentFilter(bstrReason String, Operator Variant)`; `UnshelveAll(bstrReason String, Operator Variant)`; `RemoveFromServiceSelected(bstrReason String, Operator Variant)`; `RemoveFromServiceCurrentFilter(bstrReason String, Operator Variant)`; `RemoveFromServiceAll(bstrReason String, Operator Variant)`; `ReturnToServiceSelected(Operator Variant)`; `ReturnToServiceCurrentFilter(Operator Variant)`; `ReturnToServiceAll(Operator Variant)`

**Eventos:** `Click()`; `DblClick()`; `KeyDown(KeyCode Integer, Shift Integer)`; `KeyPress(KeyAscii Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, Shift Integer, x OLE_XPOS_PIXELS, y OLE_YPOS_PIXELS)`; `MouseMove(Button Integer, Shift Integer, x OLE_XPOS_PIXELS, y OLE_YPOS_PIXELS)`

<a id="e3alarm-e3alarmcolorobject"></a>
### E3AlarmColorObject

- CLSID `{7989E685-4258-4E8A-950C-0835EA5EDC2C}` · interface `IE3AlarmColorObject`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- E3AlarmColor Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Severity` | EAlarmSeverity | R | type lib | — | — | — | Returns an Alarm's severity. Possible values for this property are -2: Critical, -1: Default, 0: High, 1: Medium, or 2: Low. This is a read-only property. |
| `BackgroundColor` | ECO_COLOR | RW | type lib | — | — | — | Defines a background color for the Alarm or severity. |
| `OverrideBackgroundColor` | Boolean | RW | type lib | — | — | — | Defines whether the background color configured in the BackgroundColor property is applied to the severity or not. If this property is configured as False, the severity uses the background color defined as default for the Alarm. 174 View |
| `TextColor` | ECO_COLOR | RW | type lib | — | — | — | Defines a text color for the Alarm or severity. |
| `OverrideTextColor` | Boolean | RW | type lib | — | — | — | Defines whether the text color defined in the TextColor property is applied to the severity or not. If this property is configured as False, the severity uses the text color configured as default for the Alarm. |
| `BlinkMode` | BlinkModeConstants | RW | type lib | — | — | — | Defines a blinking mode for the Alarm or severity. Possible values for this property are 0: Does not blink, 1: Blinks background and text, 2: Blinks only text, or 3: Blinks only text by switching to the color defined in the TextColor2 property. |
| `OverrideBlinkMode` | Boolean | RW | type lib | — | — | — | Defines whether the blinking mode configured in the BlinkMode property is applied to the severity or not. If this property is configured as False, the severity uses the blinking mode defined as default for the Alarm. |
| `TextColor2` | ECO_COLOR | RW | type lib | — | — | — | Defines a text color for the Alarm or severity when the BlinkMode property is configured to 3 (three). |

**Métodos:** `SetConfig(BackgroundColor Variant, TextColor Variant, BlinkMode Variant, TextColor2 Variant)`

### Enumerações de E3Alarm

- **__MIDL___MIDL_itf_E3AlarmControl_0002_0024_0011**: eNotConnected=0, eConnected=1, eEFilterNotConfigured=2, eEServerNotConfigured=3, eEUnexpected=4, eUnknownStatus=5
- **__MIDL___MIDL_itf_E3AlarmControl_0003_0102_0002**: stNormal=1, stUnacked=2, stAcked=3, stNormalUnacked=4, stShelved=5, stSuppressedByDesign=6, stOutOfService=7, stNoAckRequired=8, stEvent=9, stTrack=10
- **AlarmFilterType**: OnlyAlarms=1, OnlyEvents=2, AlarmsAndEvents=3
- **AlarmStatusConstants**: asActive=0, asAcked=1, asNAck=2, asEvent=3
- **BlinkModeConstants**: bmBlinkNone=0, bmBlinkAll=1, bmBlinkEraseText=2, bmBlinkText2Colors=3
- **EAlarmSeverity**: asCritical=-2, asInvalid=-1, asHigh=0, asMedium=1, asLow=2
- **tagEAckOnClick**: ACKNONE=0, ACKCLICK=1, ACKDBCLK=2
- **tagEFieldID**: AF_NONE=0, AF_ACKREQUIRED=1, AF_ACKED=2, AF_ACTORID=3, AF_CHANGEMASK=4, AF_CONDITIONNAME=5, AF_CONDITIONACTIVE=6, AF_COOKIE=7, AF_ENABLED=8, AF_EVENTCATEGORY=9, AF_EVENTTYPE=10, AF_MESSAGE=11, AF_QUALITY=12, AF_SEVERITY=13, AF_SOURCE=14, AF_SUBCONDITIONNAME=15, AF_EVENTTIME=16, AF_EVENTTIMEUTC=17, AF_CV=18, AF_AREA=19, AF_ALARMSOURCENAME=20, AF_INTIME=21, AF_OUTTIME=22, AF_ACKTIME=23, AF_FULLSOURCENAME=24, AF_FORMATTEDVALUE=25, AF_ACTIVESOURCE=26, AF_DOMAINNAME=27, AF_UNBOUND=28, AF_DELETED=29, AF_ALLOWSHELVING=30, AF_SHELVED=31, AF_SHELVEDTIME=32, AF_SHELVEDOUTTIME=33, AF_SHELVEDURATION=34, AF_SHELVEMAXDURATION=35, AF_SHELVECOUNT=36, AF_SHELVEMAXCOUNT=37, AF_SHELVEREASON=38, AF_SHELVEACTORID=39, AF_E3TIMESTAMP=40, AF_SUPPRESSED=41, AF_SUPPRESSEDTIME=42, AF_ALARMSTATE=43, AF_SHELVEDEXPIRATIONTIME=44, AF_OUTOFSERVICE=45, AF_OUTOFSERVICETIME=46, AF_RETURNTOSERVICETIME=47, AF_OUTOFSERVICEREASON=48, AF_OUTOFSERVICEACTORID=49, AF_USERFIELDFIRST=1000

---

## E3Chart

Arquivo `E3Chart.dll` · versão 1.9 · LIBID `{D2699CDF-61DC-43F8-9AE3-C709A50AFC32}` · E3Chart ActiveX

Classes: [E3Chart](#e3chart-e3chart)

<a id="e3chart-e3chart"></a>
### E3Chart

- CLSID `{359E6F05-83DC-4E4D-A330-F03C755F8A0C}` · interface `_DE3Chart` · eventos `_DE3ChartEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 29 instâncias em 2 arquivo(s)
- E3Chart Control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `RefreshTime` | Double | RW | type lib | RefreshTime | nomeada | — | This property determines an E3Chart's update time. |
| `TimeSpan` | Double | RW | type lib | — | não gravada nomeada | 60 | Indicates a time scale that appears on E3Chart's main Horizontal Axis, when it is configured to display a real-time scale. This property's value is always in seconds. Default value of this property is 60. |
| `HorScaleFormat` | BSTRFORMAT | RW | type lib | — | não gravada nomeada | — | Contains a text that represents a mask, in which all values of an horizontal scale are displayed. This mask can represent several types of values: General: It has no specific format, automatically adapting itself to the specified value Number: Displays numbers with an integer and a fraction part. Us… |
| `VerScaleFormat` | BSTRFORMAT | RW | type lib | FormatProp_# (apelido inferido) | nomeada | — | Contains a text that represents a mask, in which all values of a vertical scale are displayed. This mask can represent several types of values: General: It has no specific format, automatically adapting itself to the specified value Number: Displays numbers with an integer and a fraction part. Users… |
| `ScaleFont` | Font | RW | type lib | — | não gravada nomeada | — | Determines a font for the text used on a grid. Please check topic Font for more information about the subproperties of this property. |
| `TitleFont` | Font | RW | type lib | — | não gravada nomeada | — | Determines E3Chart's main title font. Please check topic Font for more information about the subproperties of this property. |
| `TitleColor` | OLE_COLOR | RW | type lib | TitleColor | nomeada | — | Determines the color of the text of an E3Chart's title. |
| `ShowRightScale` | Boolean | RW | type lib | — | não gravada nomeada | — | If this property is set to True, the main Vertical Axis is displayed on the right size of the grid. Otherwise, it remains invisible. The next script contains an example of using this property. Sub CommandButton1_Click() Set Chart = Screen.Item("E3Chart1") Chart.ShowRightScale = Not Chart.ShowRightSc… |
| `ShowBackground` | Boolean | RW | type lib | ShowBackGround | nomeada | — | Enables or disables viewing an E3Chart's background. If this property is equal to True, E3Chart's background is displayed. Otherwise, this E3Chart contains a transparent background. The color selected in the BackColor property does not appear if this property is equal to False (default). The next sc… |
| `ShowGridBackGround` | Boolean | RW | type lib | ShowGridBackGround | nomeada | — | Enables or disables viewing a grid's background. If this property is equal to True (default), a grid's background is displayed. Otherwise, a grid remains with a transparent background. The selected color in the GridBkColor property does not appear if this property is equal to False. The next script … |
| `ShowLeftScale` | Boolean | RW | type lib | — | não gravada nomeada | — | If this property is set to True, the main Vertical Axis is displayed on the left side of the grid. Otherwise, it remains invisible. The next script contains an example of using this property. Sub CommandButton1_Click() Set Chart = Screen.Item("E3Chart1") Chart.ShowLeftScale = Not Chart.ShowLeftScale |
| `ShowTopScale` | Boolean | RW | type lib | — | não gravada nomeada | False | If this property is set to True, the main Horizontal Axis is displayed on top of the grid. Otherwise, it is not displayed. Default value is False. The next script contains an example of using this property. Sub CommandButton1_Click() Set Chart = Screen.Item("E3Chart1") Chart.ShowTopScale = Not Chart… |
| `ShowBottomScale` | Boolean | RW | type lib | — | não gravada nomeada | True | If this property is set to True, the main Horizontal Axis is displayed at grid's bottom. Otherwise, it is not displayed. Default value is True. The next script contains an example of using this property. Sub CommandButton1_Click() Set E3Chart1 = Screen.Item("E3Chart1") oldBottomScale = E3Chart1.Show… |
| `HorGrid` | enumGridStyle | RW | type lib | — | não gravada nomeada | — | Determines the line type applied to an E3Chart's horizontal grid. The available options are described on the next table. Available options for the HorGrid property 0 - Solid Applies a solid line on an E3Chart's horizontal grid 1 - Dash Applies a dashed line on an E3Chart's horizontal grid 2 - Dot Ap… |
| `VerGrid` | enumGridStyle | RW | type lib | — | não gravada nomeada | — | Determines a type of line to apply on E3Chart's vertical grid. The available options are described on the next table. Available options for the VerGrid property 0 - Solid Applies a solid line on E3Chart's vertical grid 1 - Dash Applies a dashed line on E3Chart's vertical grid 2 - Dot Applies a dotte… |
| `HorTickUnit` | Double | RW | type lib | — | não gravada nomeada | — | Determines the number of subdivisions between grid marks. When this property is equal to 0 (zero), spacing is automatic. The next script contains an example of using this property. Sub SubCommandButton1_Click() Set E3Chart1 = Screen.Item("E3Chart1") Old = E3Chart1.HorTickUnit For i = 0 To 30 Step 10… |
| `VerTickUnit` | Double | RW | type lib | — | não gravada nomeada | — | Determines the number of subdivisions between grid marks. When this property is set to 0 (zero), spacing is automatic. The next script contains an example of using this property. Sub CommandButton1_Click() Set E3Chart1 = Screen.Item("E3Chart1") Old = E3Chart1.VerTickUnit For i = 0 To 30 Step 10 E3Ch… |
| `HorScaleEnd` | Variant | RW | type lib | ScaleDateEndProp_# (apelido inferido) | nomeada | — | Determines the final value applied on a grid's main horizontal scale. This value can either be numerical for XY E3Charts or data for E3Charts with fixed-time scales. For real-time E3Charts this property is not applied, which uses the TimeSpan property instead. The next script contains an example of … |
| `HorScaleBegin` | Variant | RW | type lib | ScaleDateBeginProp_# (apelido inferido) | nomeada | — | Determines an initial value applied on a grid's main horizontal scale. This value can either be numerical for XY E3Charts or data for E3Charts with fixed-time scales. For real-time E3Charts, this property is not applied, which uses the TimeSpan property instead. 196 View |
| `VerScaleEnd` | Variant | RW | type lib | ScaleEndProp_# (apelido inferido) | nomeada | -100 | Determines the value at the bottom of grid's main Vertical Axis. Default value of this property is -100. |
| `VerScaleBegin` | Variant | RW | type lib | ScaleBeginProp_# (apelido inferido) | nomeada | 100 | Determines the value on top of grid's main Vertical Axis. Default value of this property is 100. |
| `VerMinorTicks` | Double | RW | type lib | — | não gravada nomeada | 1 (one) | Determines the number of subdivisions between marks of grid's main Vertical Axis. Default value of this property is 1 (one). |
| `HorMinorTicks` | Double | RW | type lib | — | não gravada nomeada | 1 (one) | Determines the number of subdivisions of horizontal scales of a grid. Default value of this property is 1 (one). The next script contains an example of using this property. Sub CommandButton1_Click() Set E3Chart1 = Screen.Item("E3Chart1") Old = E3Chart1.HorMinorTicks For i = 0 To 5 E3Chart1.HorMinor… |
| `GridBkColor` | OLE_COLOR | RW | type lib | GridBkColor | nomeada | white (RGB(255, 255, 255)) | Determines a color for an E3Chart grid's background. Default value of this property is white (RGB(255, 255, 255)). The next script contains an example of using this property. Sub CommandButton1_Click() Set E3Chart1 = Screen.Item("E3Chart1") Old = E3Chart1.GridBkColor MsgBox "Next" E3Chart1.GridBkCol… |
| `HorGridColor` | OLE_COLOR | RW | type lib | ColorProp_# (apelido inferido) | nomeada | gray (RGB(192, 192, 192)) | Determines a color for an E3Chart's horizontal grid. Default value of this property is gray (RGB(192, 192, 192)). The next script contains an example of using this property. Sub CommandButton1_Click() Set E3Chart1 = Screen.Item("E3Chart1") Old = E3Chart1.HorGridColor MsgBox "Next" E3Chart1.HorGridCo… |
| `VerGridColor` | OLE_COLOR | RW | type lib | GridColorProp_# (apelido inferido) | nomeada | gray (RGB(192, 192, 192)) | Determines a color for the line on grid's main Vertical Axis. Default value of this property is gray (RGB(192, 192, 192)). |
| `CursorColor` | OLE_COLOR | RW | type lib | CursorColor | nomeada | red (RGB(255, 0, 0)) | Establishes a color for an interval search cursor. Default value is red (RGB(255, 0, 0)). |
| `CursorBegin` | Double | RW | type lib | — | não gravada nomeada | — | Defines the initial cursor position, between 0 (zero) and 1 (one). To display these cursors, users must execute the ShowCursors method or enable the Interval Search option. |
| `CursorEnd` | Double | RW | type lib | — | não gravada nomeada | — | Defines the final cursor position, between 0 (zero) and 1 (one). To display these cursors, users must execute the ShowCursors method or enable the Interval Search option. |
| `CursorLineStyle` | ELineStyle | RW | type lib | CursorLineStyle | nomeada | — | Line style for an interval search cursor. The available options are described on the next table. Available options for the CursorLineStyle property 0 - LS_Solid Applies a solid line on an E3Chart's interval cursor (default) 1 - LS_Dash Applies a dashed line on an E3Chart's interval cursor 2 - LS_Dot… |
| `CursorLineWidth` | Long | RW | type lib | CursorLineWidth | nomeada | — | Establishes the width of an interval cursor. |
| `CursorSearchStyle` | SearchStyles | RW | type lib | SearchStyle (apelido confirmado) | nomeada | — | Allows a cursor to search for chart points. Possible values are 0 - PointNearest: Searches for the nearest point (default), 1 - LinearInterpolation: Searches for an interpolated point, or 2 - PointPrevious: Searches for the previous point. |
| `Pens` | IDispPenCollection | R | type lib | — | não gravada nomeada | — | Returns an E3Chart's Pen Collection object. A Pen Collection object is used to insert, remove, or access all available Pens of an E3Chart. This is a read-only property. The next script contains an example of using this property. Sub CommandButton1_Click() For Each pen In Screen.Item("E3Chart1").Pens… |
| `Queries` | IDispQueryCollection | R | type lib | — | não gravada nomeada | — | Returns an E3Chart's Query Collection object. A Query Collection object is used to insert, remove, or access all available Queries of an E3Chart. This is a read-only property. |
| `Legend` | ILegend | R | type lib | — | não gravada nomeada | — | Returns an E3Chart's Legend object. Then, all Legend properties can be changed. This is a read-only property. |
| `Axes` | IAxisCollection | R | type lib | — | não gravada nomeada | — | Returns a collection of E3Chart's Axes. Then, all properties of this Axes collection can be modified. This is a read- only property. |
| `ShowTitle` | Boolean | RW | type lib | ShowTitle | nomeada | — | If this property is set to True, E3Chart's main title is visible. Otherwise, it remains invisible. The Title property contains a title to display on an E3Chart. The next script contains an example of using this property. Sub CommandButton1_Click() Set E3Chart1 = Screen.Item("E3Chart1") oldTitle = E3… |
| `Title` | String | RW | type lib | Title | nomeada | — | Determines E3Chart's main title. For this title to appear on an E3Chart, the ShowTitle property must be set to True. |
| `HorAxisTitle` | String | RW | type lib | — | não gravada nomeada | — | Determines a title for the main Horizontal Axis. The next script contains an example of using this property. Sub CommandButton1_Click() Set E3Chart1= Screen.Item("E3Chart1") Old = E3Chart1.HorAxisTitle MsgBox "Next" E3Chart1.HorAxisTitle = "!Test" MsgBox "Return" E3Chart1.HorAxisTitle = Old |
| `VerAxisTitle` | String | RW | type lib | TitleProp_# (apelido inferido) | nomeada | — | Determines a title for the main Vertical Axis. |
| `RenderQuality` | ERenderQuality | RW | type lib | RenderQuality | nomeada | — | Controls the drawing quality of E3Chart Pens. Possible values for this property are the following: 0 - rqDefault: Uses the quality mode configured in Screen's RenderQuality property, if different from 0 (zero), or the quality mode configured in Viewer's RenderQuality property, also if different from… |
| `ShowBorder` | Boolean | RW | type lib | ShowBorder | nomeada | True | Enables or disables an external border on an E3Chart, when the visualization of scales (the ShowBottomScale, ShowLeftScale, ShowRightScale, and ShowTopScale properties) is disabled. Default value of this property is True. |
| `Padding` | Long | RW | type lib | Padding | nomeada | 10 | This property determines the distance, in pixels, between a chart and an E3Chart's border, as seen on the next figures with red arrows. Default value of this property is 10. Padding property equal to 10 198 View Padding property equal to 30 |
| `MouseMode` | MouseModeEnum | RW | type lib | MouseMode | nomeada | — | Selects one of the runtime options of an E3Chart's contextual menu. Possible values for this property are the following: 0 - MouseModeZoom: Places the mouse pointer in Zoom mode by selected area. This option is available in numerical scale charts in XY and fixed scale. This is equivalent of selectin… |
| `ShowPopupMenu` | Boolean | RW | type lib | ShowPopupMenu | nomeada | True | Enables or disables the option of displaying E3Chart's runtime menu. If its value is equal to True, this menu is displayed when users right-click E3Chart's chart. If its value is equal to False, this menu is not displayed. Default value of this property is True. |
| `BackColor` | OLE_COLOR | RW | type lib | BackColor | nomeada | beige (RGB(236, 233, 216)) | Determines a background color for an E3Chart. To display this color, the ShowBackground property must be configured as True. Default value of this property is beige (RGB(236, 233, 216)). 194 View |
| `ForeColor` | OLE_COLOR | RW | type lib | ForeColor | nomeada | black (RGB(0, 0, 0)) | Determines a color for an E3Chart's foreground. Default value of this property is black (RGB(0, 0, 0)). |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_ExtentX` | Long |  | gravada no .prj | _ExtentX | nomeada | — | sem equivalente na type lib |
| `_ExtentY` | Long |  | gravada no .prj | _ExtentY | nomeada | — | sem equivalente na type lib |
| `_StockProps` | Long |  | gravada no .prj | _StockProps | nomeada | — | sem equivalente na type lib |
| `_Version` | Long |  | gravada no .prj | _Version | nomeada | — | sem equivalente na type lib |
| `AxisCount` | Long |  | gravada no .prj | AxisCount | nomeada | — | sem equivalente na type lib |
| `BandColor_#` | Long |  | gravada no .prj | BandColor_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `BandHighValue_#` | Double |  | gravada no .prj | BandHighValue_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `BandLowValue_#` | Double |  | gravada no .prj | BandLowValue_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `BandVisible_#` | Boolean |  | gravada no .prj | BandVisible_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `Charset` | Integer |  | gravada no .prj | Charset | nomeada | — | sem equivalente na type lib |
| `Column_#` | Long |  | gravada no .prj | Column_# | nomeada | — | sem equivalente na type lib (família: 22) |
| `ColumnAlign_#` | Long |  | gravada no .prj | ColumnAlign_# | nomeada | — | sem equivalente na type lib (família: 22) |
| `ColumnCaption_#` | String |  | gravada no .prj | ColumnCaption_# | nomeada | — | sem equivalente na type lib (família: 22) |
| `ColumnFormat_#` | String |  | gravada no .prj | ColumnFormat_# | nomeada | — | sem equivalente na type lib (família: 22) |
| `ColumnIndex_#` | Long |  | gravada no .prj | ColumnIndex_# | nomeada | — | sem equivalente na type lib (família: 22) |
| `ColumnsCount` | Long |  | gravada no .prj | ColumnsCount | nomeada | — | sem equivalente na type lib |
| `ColumnVisible_#` | Boolean |  | gravada no .prj | ColumnVisible_# | nomeada | — | sem equivalente na type lib (família: 22) |
| `ColumnWidth_#` | Long |  | gravada no .prj | ColumnWidth_# | nomeada | — | sem equivalente na type lib (família: 22) |
| `DataSourceType_0` | Long |  | gravada no .prj | DataSourceType_0 | nomeada | — | sem equivalente na type lib |
| `DataSourceType_1` | Long |  | gravada no .prj | DataSourceType_1 | nomeada | — | sem equivalente na type lib |
| `Domain` | String |  | gravada no .prj | Domain | nomeada | — | sem equivalente na type lib |
| `EnableScaleColor_#` | Boolean |  | gravada no .prj | EnableScaleColor_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `GridStyleProp_#` | Long |  | gravada no .prj | GridStyleProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `HeaderBackColor` | Long |  | gravada no .prj | HeaderBackColor | nomeada | — | sem equivalente na type lib |
| `HeaderBorderStyle` | Long |  | gravada no .prj | HeaderBorderStyle | nomeada | — | sem equivalente na type lib |
| `HeaderTextColor` | Long |  | gravada no .prj | HeaderTextColor | nomeada | — | sem equivalente na type lib |
| `InverseProp_#` | Boolean |  | gravada no .prj | InverseProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `IsCursorValid_0` | Boolean |  | gravada no .prj | IsCursorValid_0 | nomeada | — | sem equivalente na type lib |
| `IsCursorValid_1` | Boolean |  | gravada no .prj | IsCursorValid_1 | nomeada | — | sem equivalente na type lib |
| `Italic` | Boolean |  | gravada no .prj | Italic | nomeada | — | sem equivalente na type lib |
| `LegendBackColor` | Long |  | gravada no .prj | LegendBackColor | nomeada | — | sem equivalente na type lib |
| `LegendBorderStyle` | Long |  | gravada no .prj | LegendBorderStyle | nomeada | — | sem equivalente na type lib |
| `LegendEnableTextColor` | Boolean |  | gravada no .prj | LegendEnableTextColor | nomeada | — | sem equivalente na type lib |
| `LegendPos` | Long |  | gravada no .prj | LegendPos | nomeada | — | sem equivalente na type lib |
| `LegendSize` | Long |  | gravada no .prj | LegendSize | nomeada | — | sem equivalente na type lib |
| `LegendTextColor` | Long |  | gravada no .prj | LegendTextColor | nomeada | — | sem equivalente na type lib |
| `LogScaleProp_#` | Boolean |  | gravada no .prj | LogScaleProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `MinorTicksProp_#` | Long |  | gravada no .prj | MinorTicksProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `MirrorProp_#` | Boolean |  | gravada no .prj | MirrorProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `NameProp_#` | String |  | gravada no .prj | NameProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `Pen_AutoAxis_0` | Boolean |  | gravada no .prj | Pen_AutoAxis_0 | nomeada | — | sem equivalente na type lib |
| `Pen_AutoAxis_1` | Boolean |  | gravada no .prj | Pen_AutoAxis_1 | nomeada | — | sem equivalente na type lib |
| `Pen_AutoPlotMode_0` | Boolean |  | gravada no .prj | Pen_AutoPlotMode_0 | nomeada | — | sem equivalente na type lib |
| `Pen_AutoPlotMode_1` | Boolean |  | gravada no .prj | Pen_AutoPlotMode_1 | nomeada | — | sem equivalente na type lib |
| `Pen_AutoQuery_0` | Boolean |  | gravada no .prj | Pen_AutoQuery_0 | nomeada | — | sem equivalente na type lib |
| `Pen_AutoQuery_1` | Boolean |  | gravada no .prj | Pen_AutoQuery_1 | nomeada | — | sem equivalente na type lib |
| `Pen_BkColor_0` | Long |  | gravada no .prj | Pen_BkColor_0 | nomeada | — | sem equivalente na type lib |
| `Pen_BkColor_1` | Long |  | gravada no .prj | Pen_BkColor_1 | nomeada | — | sem equivalente na type lib |
| `Pen_BufferSize_0` | Long |  | gravada no .prj | Pen_BufferSize_0 | nomeada | — | sem equivalente na type lib |
| `Pen_BufferSize_1` | Long |  | gravada no .prj | Pen_BufferSize_1 | nomeada | — | sem equivalente na type lib |
| `Pen_Color_0` | Long |  | gravada no .prj | Pen_Color_0 | nomeada | — | sem equivalente na type lib |
| `Pen_Color_1` | Long |  | gravada no .prj | Pen_Color_1 | nomeada | — | sem equivalente na type lib |
| `Pen_DataOffSet_0` | Double |  | gravada no .prj | Pen_DataOffSet_0 | nomeada | — | sem equivalente na type lib |
| `Pen_DataOffSet_1` | Double |  | gravada no .prj | Pen_DataOffSet_1 | nomeada | — | sem equivalente na type lib |
| `Pen_DataOffSetUnit_0` | Long |  | gravada no .prj | Pen_DataOffSetUnit_0 | nomeada | — | sem equivalente na type lib |
| `Pen_DataOffSetUnit_1` | Long |  | gravada no .prj | Pen_DataOffSetUnit_1 | nomeada | — | sem equivalente na type lib |
| `Pen_DigitalData_0` | Boolean |  | gravada no .prj | Pen_DigitalData_0 | nomeada | — | sem equivalente na type lib |
| `Pen_DigitalData_1` | Boolean |  | gravada no .prj | Pen_DigitalData_1 | nomeada | — | sem equivalente na type lib |
| `Pen_DocString_0` | String |  | gravada no .prj | Pen_DocString_0 | nomeada | — | sem equivalente na type lib |
| `Pen_DocString_1` | String |  | gravada no .prj | Pen_DocString_1 | nomeada | — | sem equivalente na type lib |
| `Pen_EnableCalc_0` | Boolean |  | gravada no .prj | Pen_EnableCalc_0 | nomeada | — | sem equivalente na type lib |
| `Pen_EnableCalc_1` | Boolean |  | gravada no .prj | Pen_EnableCalc_1 | nomeada | — | sem equivalente na type lib |
| `Pen_EnableHighLimit_0` | Boolean |  | gravada no .prj | Pen_EnableHighLimit_0 | nomeada | — | sem equivalente na type lib |
| `Pen_EnableHighLimit_1` | Boolean |  | gravada no .prj | Pen_EnableHighLimit_1 | nomeada | — | sem equivalente na type lib |
| `Pen_EnableLowLimit_0` | Boolean |  | gravada no .prj | Pen_EnableLowLimit_0 | nomeada | — | sem equivalente na type lib |
| `Pen_EnableLowLimit_1` | Boolean |  | gravada no .prj | Pen_EnableLowLimit_1 | nomeada | — | sem equivalente na type lib |
| `Pen_EU_0` | String |  | gravada no .prj | Pen_EU_0 | nomeada | — | sem equivalente na type lib |
| `Pen_EU_1` | String |  | gravada no .prj | Pen_EU_1 | nomeada | — | sem equivalente na type lib |
| `Pen_HighlightMaxGapTime_0` | Boolean |  | gravada no .prj | Pen_HighlightMaxGapTime_0 | nomeada | — | sem equivalente na type lib |
| `Pen_HighlightMaxGapTime_1` | Boolean |  | gravada no .prj | Pen_HighlightMaxGapTime_1 | nomeada | — | sem equivalente na type lib |
| `Pen_HighLimit_0` | Double |  | gravada no .prj | Pen_HighLimit_0 | nomeada | — | sem equivalente na type lib |
| `Pen_HighLimit_1` | Double |  | gravada no .prj | Pen_HighLimit_1 | nomeada | — | sem equivalente na type lib |
| `Pen_LimitPenBkColor_0` | Long |  | gravada no .prj | Pen_LimitPenBkColor_0 | nomeada | — | sem equivalente na type lib |
| `Pen_LimitPenBkColor_1` | Long |  | gravada no .prj | Pen_LimitPenBkColor_1 | nomeada | — | sem equivalente na type lib |
| `Pen_LimitPenColor_0` | Long |  | gravada no .prj | Pen_LimitPenColor_0 | nomeada | — | sem equivalente na type lib |
| `Pen_LimitPenColor_1` | Long |  | gravada no .prj | Pen_LimitPenColor_1 | nomeada | — | sem equivalente na type lib |
| `Pen_LineStyle_0` | Long |  | gravada no .prj | Pen_LineStyle_0 | nomeada | — | sem equivalente na type lib |
| `Pen_LineStyle_1` | Long |  | gravada no .prj | Pen_LineStyle_1 | nomeada | — | sem equivalente na type lib |
| `Pen_LowLimit_0` | Double |  | gravada no .prj | Pen_LowLimit_0 | nomeada | — | sem equivalente na type lib |
| `Pen_LowLimit_1` | Double |  | gravada no .prj | Pen_LowLimit_1 | nomeada | — | sem equivalente na type lib |
| `Pen_MaxGapTime_0` | Double |  | gravada no .prj | Pen_MaxGapTime_0 | nomeada | — | sem equivalente na type lib |
| `Pen_MaxGapTime_1` | Double |  | gravada no .prj | Pen_MaxGapTime_1 | nomeada | — | sem equivalente na type lib |
| `Pen_MaxGapTimeColor_0` | Long |  | gravada no .prj | Pen_MaxGapTimeColor_0 | nomeada | — | sem equivalente na type lib |
| `Pen_MaxGapTimeColor_1` | Long |  | gravada no .prj | Pen_MaxGapTimeColor_1 | nomeada | — | sem equivalente na type lib |
| `Pen_MaxGapTimeStyle_0` | Long |  | gravada no .prj | Pen_MaxGapTimeStyle_0 | nomeada | — | sem equivalente na type lib |
| `Pen_MaxGapTimeStyle_1` | Long |  | gravada no .prj | Pen_MaxGapTimeStyle_1 | nomeada | — | sem equivalente na type lib |
| `Pen_Name_0` | String |  | gravada no .prj | Pen_Name_0 | nomeada | — | sem equivalente na type lib |
| `Pen_Name_1` | String |  | gravada no .prj | Pen_Name_1 | nomeada | — | sem equivalente na type lib |
| `Pen_PenType_0` | Long |  | gravada no .prj | Pen_PenType_0 | nomeada | — | sem equivalente na type lib |
| `Pen_PenType_1` | Long |  | gravada no .prj | Pen_PenType_1 | nomeada | — | sem equivalente na type lib |
| `Pen_PenWidth_0` | Long |  | gravada no .prj | Pen_PenWidth_0 | nomeada | — | sem equivalente na type lib |
| `Pen_PenWidth_1` | Long |  | gravada no .prj | Pen_PenWidth_1 | nomeada | — | sem equivalente na type lib |
| `Pen_PointStyle_0` | Long |  | gravada no .prj | Pen_PointStyle_0 | nomeada | — | sem equivalente na type lib |
| `Pen_PointStyle_1` | Long |  | gravada no .prj | Pen_PointStyle_1 | nomeada | — | sem equivalente na type lib |
| `Pen_ScaleXProp_0` | String |  | gravada no .prj | Pen_ScaleXProp_0 | nomeada | — | sem equivalente na type lib |
| `Pen_ScaleXProp_1` | String |  | gravada no .prj | Pen_ScaleXProp_1 | nomeada | — | sem equivalente na type lib |
| `Pen_ScaleYProp_0` | String |  | gravada no .prj | Pen_ScaleYProp_0 | nomeada | — | sem equivalente na type lib |
| `Pen_ScaleYProp_1` | String |  | gravada no .prj | Pen_ScaleYProp_1 | nomeada | — | sem equivalente na type lib |
| `Pen_ScanValue_0` | Double |  | gravada no .prj | Pen_ScanValue_0 | nomeada | — | sem equivalente na type lib |
| `Pen_ScanValue_1` | Double |  | gravada no .prj | Pen_ScanValue_1 | nomeada | — | sem equivalente na type lib |
| `Pen_ShowAverage_0` | Boolean |  | gravada no .prj | Pen_ShowAverage_0 | nomeada | — | sem equivalente na type lib |
| `Pen_ShowAverage_1` | Boolean |  | gravada no .prj | Pen_ShowAverage_1 | nomeada | — | sem equivalente na type lib |
| `Pen_ShowBadPoints_0` | Boolean |  | gravada no .prj | Pen_ShowBadPoints_0 | nomeada | — | sem equivalente na type lib |
| `Pen_ShowBadPoints_1` | Boolean |  | gravada no .prj | Pen_ShowBadPoints_1 | nomeada | — | sem equivalente na type lib |
| `Pen_ShowMinMax_0` | Boolean |  | gravada no .prj | Pen_ShowMinMax_0 | nomeada | — | sem equivalente na type lib |
| `Pen_ShowMinMax_1` | Boolean |  | gravada no .prj | Pen_ShowMinMax_1 | nomeada | — | sem equivalente na type lib |
| `Pen_UseTimeStamp_0` | Boolean |  | gravada no .prj | Pen_UseTimeStamp_0 | nomeada | — | sem equivalente na type lib |
| `Pen_UseTimeStamp_1` | Boolean |  | gravada no .prj | Pen_UseTimeStamp_1 | nomeada | — | sem equivalente na type lib |
| `Pen_Visible_0` | Boolean |  | gravada no .prj | Pen_Visible_0 | nomeada | — | sem equivalente na type lib |
| `Pen_Visible_1` | Boolean |  | gravada no .prj | Pen_Visible_1 | nomeada | — | sem equivalente na type lib |
| `Pen_XField_0` | String |  | gravada no .prj | Pen_XField_0 | nomeada | — | sem equivalente na type lib |
| `Pen_XField_1` | String |  | gravada no .prj | Pen_XField_1 | nomeada | — | sem equivalente na type lib |
| `Pen_XLink_0` | String |  | gravada no .prj | Pen_XLink_0 | nomeada | — | sem equivalente na type lib |
| `Pen_XLink_1` | String |  | gravada no .prj | Pen_XLink_1 | nomeada | — | sem equivalente na type lib |
| `Pen_YField_0` | String |  | gravada no .prj | Pen_YField_0 | nomeada | — | sem equivalente na type lib |
| `Pen_YField_1` | String |  | gravada no .prj | Pen_YField_1 | nomeada | — | sem equivalente na type lib |
| `Pen_YLink_0` | String |  | gravada no .prj | Pen_YLink_0 | nomeada | — | sem equivalente na type lib |
| `Pen_YLink_1` | String |  | gravada no .prj | Pen_YLink_1 | nomeada | — | sem equivalente na type lib |
| `PenCount` | Long |  | gravada no .prj | PenCount | nomeada | — | sem equivalente na type lib |
| `PositionProp_#` | Long |  | gravada no .prj | PositionProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `RefLineColor_#` | Long |  | gravada no .prj | RefLineColor_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `RefLineStyle_#` | Long |  | gravada no .prj | RefLineStyle_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `RefLineValue_#` | Double |  | gravada no .prj | RefLineValue_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `RefLineVisible_#` | Boolean |  | gravada no .prj | RefLineVisible_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `RefLineWidth_#` | Long |  | gravada no .prj | RefLineWidth_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `ScaleEnableTextColor_#` | Boolean |  | gravada no .prj | ScaleEnableTextColor_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `ScaleTypeProp_#` | Long |  | gravada no .prj | ScaleTypeProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `ShowGridProp_#` | Boolean |  | gravada no .prj | ShowGridProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `ShowHeader` | Boolean |  | gravada no .prj | ShowHeader | nomeada | — | sem equivalente na type lib |
| `Strikethrough` | Boolean |  | gravada no .prj | Strikethrough | nomeada | — | sem equivalente na type lib |
| `TickSpacing_#` | Double |  | gravada no .prj | TickSpacing_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `TickSpacingUnit_#` | Long |  | gravada no .prj | TickSpacingUnit_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `TimeRangeProp_#` | Double |  | gravada no .prj | TimeRangeProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `TimeUnitProp_#` | Long |  | gravada no .prj | TimeUnitProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `Underline` | Boolean |  | gravada no .prj | Underline | nomeada | — | sem equivalente na type lib |
| `UsePenEuAsTitle_#` | Boolean |  | gravada no .prj | UsePenEuAsTitle_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `VisibleProp_#` | Boolean |  | gravada no .prj | VisibleProp_# | nomeada | — | sem equivalente na type lib (família: 3) |
| `Weight` | Integer |  | gravada no .prj | Weight | nomeada | — | sem equivalente na type lib |
| `XCursorPos_0` | Double |  | gravada no .prj | XCursorPos_0 | nomeada | — | sem equivalente na type lib |
| `XCursorPos_1` | Double |  | gravada no .prj | XCursorPos_1 | nomeada | — | sem equivalente na type lib |
| `XQueryName_0` | String |  | gravada no .prj | XQueryName_0 | nomeada | — | sem equivalente na type lib |
| `XQueryName_1` | String |  | gravada no .prj | XQueryName_1 | nomeada | — | sem equivalente na type lib |
| `YCursorPos_0` | Double |  | gravada no .prj | YCursorPos_0 | nomeada | — | sem equivalente na type lib |
| `YCursorPos_1` | Double |  | gravada no .prj | YCursorPos_1 | nomeada | — | sem equivalente na type lib |

**Métodos:** `LoadData()`; `ResetConfig(Flags Variant)`; `CopyConfig(Sourcechart _DE3Chart, Flags Variant)`; `FitAll(FitStyle Variant)`; `FitPen(Pen Variant, FitStyle Variant)`; `ZoomOut()`; `ZoomIn()`; `ShowCursors()`; `ClearPenMarks()`

**Eventos:** `OnCursorChange()`; `OnLegendClick(Row Int, Col Int, RowData Int)`; `OnQueryFinish()`

### Enumerações de E3Chart

- **CursorType**: SelectedPen=0, AllPens=1
- **DataSourceTypes**: TYP_REALTIMEVAR=0, TYP_HISTVAR=1, TYP_REALHISTVAR=2, TYP_AUTOMATIC=3
- **ELegendBorderStyle**: lbsFlat=0, lbsRaised=1, lbsSunken=2, lbsEtched=3, lbsBump=4
- **ELineStyle**: LS_SOLID=0, LS_DASH=1, LS_DOT=2, LS_DASHDOT=3, LS_DASHDOTDOT=4, LS_NULL=5
- **EnumAxisPosition**: axpLeft=0, axpRight=1, axpTop=2, axpBottom=3
- **EnumAxisType**: eExtraAxis=0, eHorMain=1, eVerMain=2, eAutoAxis=3
- **EnumColumns**: clName=0, clTagX=1, clTagY=2, clTagXValue=3, clTagYValue=4, clDescription=5, clColor=6, clStatus=7, clScaleX=8, clScaleY=9, clAverageY=10, clMinY=11, clMaxY=12, clXBegin=13, clXEnd=14, clDiffX=15, clDiffY=16, clYBegin=17, clYEnd=18, clEU=19, clScaleYMax=20, clScaleYMin=21
- **EnumE3ChartType**: CS_XY=0, CS_YTIME=1, CS_YINSTANT=2
- **EnumFitStyle**: fitBoth=0, fitVertical=1, fitHorizontal=2
- **enumGridStyle**: SOLID=0, DASH=1, DOT=2, DASHDOT=3, DASHDOTDOT=4, INVISIBLE=5
- **EnumLegendPos**: lgTop=0, lgLeft=1, lgBottom=2, lgRight=3
- **EnumScaleType**: atNumberScale=0, atLastPeriod=1, atPeriod=2
- **EnumTimeUnit**: tuSeconds=0, tuMinutes=1, tuHours=2, tuDays=3, tuWeeks=4, tuMonths=5, tuYears=6
- **ERenderQuality**: rqDefault=0, rqNormal=1, rqHighQuality=2
- **LineStyles**: ST_LINES=0, ST_POINTS=1, ST_LINEPOINTS=2, ST_SOLID=3
- **MouseModeEnum**: MouseModeZoom=0, MouseModePan=1, MouseModePanH=2, MouseModeSearch=3, MouseModeCursors=4
- **SearchStyles**: PointNearest=0, LinearInterpolation=1, PointPrevious=2
- **TextAlignStyles**: taLeft=0, taRight=1, taCenter=2
- **Units**: UN_DAY=0, UN_HOR=1, UN_MIN=2, UN_SEG=3, UN_UNITS=4

---

## E3Browser

Arquivo `E3Browse.dll` · versão 3.2 · LIBID `{B1C4B931-1906-46EB-854C-269E10E0D3EE}` · E3Browser ActiveX

Classes: [E3Browser](#e3browser-e3browser)

<a id="e3browser-e3browser"></a>
### E3Browser

- CLSID `{4F0B5740-FB93-405E-AF6B-3F634B662103}` · interface `_DE3Browser` · eventos `_DE3BrowserEvents`
- Objeto de tela (gráfico): **sim** · usada nos projetos/libs: 4 instâncias em 2 arquivo(s)
- E3Browser Control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `GridBkColor` | OLE_COLOR | RW | type lib | GridBkColor | nomeada | white (RGB(255, 255, 255)) | Determines the background color for the data area of this object. The default value of this property is white (RGB(255, 255, 255)). This property corresponds to the E3Browser background color option on the Colors tab of this object's Properties Window. |
| `ToolbarBkColor` | OLE_COLOR | RW | type lib | ToolbarBkColor | nomeada | the color RGB(240, 240, 240) | Specifies the background color of the toolbar of this object. The default value of this property is the color RGB(240, 240, 240). This property corresponds to the Status bar background color option on the Colors tab of this object's Properties Window. |
| `ToolbarForeColor` | OLE_COLOR | RW | type lib | ToolbarForeColor | nomeada | black (RGB(0, 0, 0)) | Specifies the foreground color of the toolbar of this object. The default value of this property is black (RGB(0, 0, 0)). This property corresponds to the Status bar text color option on the Colors tab of this object's Properties Window. |
| `GridLineColor` | OLE_COLOR | RW | type lib | GridLineColor | nomeada | silver (RGB(192, 192, 192)) | Determines the color for the lines of the data grid of this object. The default value of this property is silver (RGB(192, 192, 192)). This property corresponds to the Grid line color option on the Colors tab of this object's Properties Window. |
| `TextColor` | OLE_COLOR | RW | type lib | TextColor | nomeada | black (RGB(0, 0, 0)) | Specifies the color of the text of this object. The default value of this property is black (RGB(0, 0, 0)). This property corresponds to the Cell text color option on the Colors tab of this object's Properties Window. |
| `TextBkColor` | OLE_COLOR | RW | type lib | TextBkColor | nomeada | white (RGB(255, 255, 255)) | Specifies the background color for data cells of this object. The default value of this property is white (RGB(255, 255, 255)). This property corresponds to the Cell background color option on the Colors tab of this object's Properties Window. |
| `FixedBkColor` | OLE_COLOR | RW | type lib | FixedBkColor | nomeada | the color RGB(240, 240, 240) | Specifies a background color for the header of this object. The default value of this property is the color RGB(240, 240, 240). This property corresponds to the Header background color option on the Colors tab of this object's Properties Window. |
| `FixedTextColor` | OLE_COLOR | RW | type lib | FixedTextColor | nomeada | black (RGB(0, 0, 0)) | Specifies the color of the header of this object. The default value of this property is black (RGB(0, 0, 0)). This property corresponds to the Header text color option on the Colors tab of this object's Properties Window. |
| `TitleTipTextColor` | OLE_COLOR | RW | type lib | TitleTipTextColor | nomeada | black (RGB(0, 0, 0)) | Specifies the color of the text of the tip of this object. The default value of this property is black (RGB(0, 0, 0)). This property corresponds to the Cell tip text color option on the Colors tab of this object's Properties Window. |
| `TitleTipBkColor` | OLE_COLOR | RW | type lib | TitleTipBkColor | nomeada | white (RGB(255, 255, 225)) | Specifies the background color of the text of the tip of this object. The default value of this property is white (RGB(255, 255, 225)). This property corresponds to the Cell tip background color option on the Colors tab of this object's Properties Window. |
| `ToolbarFont` | Font | RW | type lib | — | não gravada nomeada | the Arial font | Determines the font used on texts of the toolbar of this object. This property cannot be used in scripts or Links, and is configured only via Elipse E3 Studio. The default value of this property is the Arial font. Please check topic Font for more information about the sub-properties of this property… |
| `GridFont` | Font | RW | type lib | — | não gravada nomeada | the Arial font | Determines the font used on texts of the data area of this object. The default value of this property is the Arial font. This property cannot be used in scripts or Links, and is configured only via Elipse E3 Studio. Please check topic Font for more information about the sub-properties of this proper… |
| `FixedRowFont` | Font | RW | type lib | — | não gravada nomeada | the Arial font | Determines the font of the text used on the header row of this object. This property cannot be used in scripts or Links, and is configured only via Elipse E3 Studio. The default value of this property is the Arial font. Please check topic Font for more information about the sub-properties of this pr… |
| `ColumnWidth` | Long | RW | type lib | ColumnWidth | nomeada | — | Determines the width of columns of this object, in pixels. |
| `FixedColumnWidth` | Long | RW | type lib | FixedColumnWidth | nomeada | 30 | Determines the width of the first column of this object, in pixels. The default value of this property is 30. |
| `RowHeight` | Long | RW | type lib | RowHeight | nomeada | 20 | Defines the height of rows of this object, in pixels. The default value of this property is 20. |
| `FixedRowHeight` | Long | RW | type lib | FixedRowHeight | nomeada | 20 | Determines the height, in pixels, of the header row of this object. The default value of this property is 20. |
| `GridLinesType` | enumGLType | RW | type lib | GridLinesType | nomeada | — | Determines the type of lines to be drawn on the data grid of this object. Possible values for this property are 0 - GLNone: No grid lines, 1 - GLHorz: Only horizontal grid lines, 2 - GLVert: Only vertical grid lines, or 3 - GLBoth: Horizontal and vertical grid lines (default). |
| `ColumnTextAlignment` | enumTextAlignment | RW | type lib | ColumnTextAlignment | nomeada | — | Determines the alignment of text of this object's columns. Possible values for this property are 0: taAlignLeft (default), 1: taAlignCenter, or 2: taAlignRight. When selecting a value for this property, all values with the same alignment on the Text Alignment column of the list of fields on the Quer… |
| `AllowColumnResize` | Boolean | RW | type lib | ColumnResize (apelido confirmado) | nomeada | — | Enables or disables the configuration of the size of grid's columns, at run time. If this property is set to False, the size of columns is fixed and cannot be modified. |
| `AllowRowResize` | Boolean | RW | type lib | RowResize (apelido confirmado) | nomeada | — | Enables or disables the configuration of the size of grid's rows, at run time. If this property is set to False, the size of rows is fixed and cannot be modified. |
| `RefreshTime` | Long | RW | type lib | RefreshTime | nomeada | — | Specifies a Query's refresh time relative to the database. By using this property, users can check data updates on the related Historic, referring to a specific time, in milliseconds. When this property is equal to 0 (zero), there are no updates and data remains unchanged. The value of this property… |
| `SelectRow` | Boolean | RW | type lib | SelectRow | nomeada | — | Establishes the possibility of selecting rows of this object. If this property is set to True, users can select rows. Otherwise, users cannot select rows. |
| `CurSel` | Long | RW | type lib | — | não gravada nomeada | — | Indicates the current position of this object's cursor, that is, the index of the row in which the cursor is positioned. |
| `SourceQuery` | String | RW | type lib | SourceQuery | nomeada | — | Contains a reference to the Query object to which this object is linked. 190 View To change the Query of this object via scripts, in case the new Query modifies the fields from the original Query, in addition to changing this property, users must use the RetrieveE3QueryFields and Requery methods. |
| `Fields` | IFieldCollection | R | type lib | — | não gravada nomeada | empty | Returns the Collection of Fields of this object, which contains a list of all fields of a table, allowing a reference using the items of this Collection. This is a read-only property. The default value of this property is empty. The next script contains an example of using this property. Sub E3Brows… |
| `E3Query` | Object | R | type lib | — | não gravada nomeada | — | Returns the Query object of this object, for accessing this object's properties. This is a read-only property. |
| `HeaderWordWrap` | Boolean | RW | type lib | HeaderWordWrap | nomeada | False | This property applies a line break on the text of the header of columns of this object, allowing to display the full text of a column's name. That line break is applied only where there is a space, a tab, or a forced line break on the text. Configuring this property in True does not change the value… |
| `HeaderTextAlignment` | enumBrowserHeaderAlignment | RW | type lib | HeaderAlignment (apelido confirmado) | nomeada | — | Determines the alignment of the text of the header of columns of this object. Possible values for this property are 0: bhaLeft (default), 1: bhaCenter, 2: bhaRight, or 3: bhaFollowColumn. When selecting the bhaFollowColumn option, the text of column headers is aligned as specified on the Text Alignm… |
| `AllowHeaderSort` | Boolean | RW | type lib | AllowHeaderSort | nomeada | True | Enables or disables sorting by the header of this object's columns at run time. The default value of this property is True. |
| `SortColumn` | Long | RW | type lib | — | não gravada nomeada | -1 (minus one), that is, uses the sorting order … | Indicates the column used for sorting on this object. The default value of this property is -1 (minus one), that is, uses the sorting order of the Query that provides data. Configuring this property with a value less than 1 (one) or greater than the number of columns removes the sorting order of thi… |
| `SortOrder` | enumSortOrderType | RW | type lib | — | não gravada nomeada | — | Indicates the sorting order of data based on the column indicated in the SortColumn property. Possible values for this property are 0 - SONoSort: Without sorting order (default), 1 - SOAsc: In ascending order, or 2 - SODesc: In descending order. NOTES This property is only available at run time. Con… |
| `ShowToolbar` | Boolean | RW | type lib | ShowToolbar | nomeada | True | Shows or hides the toolbar of this object. The default value of this property is True. |
| `RightClickRefresh` | Boolean | RW | type lib | RightClickRefresh | nomeada | True | Indicates whether a right-click on this object causes a refresh in the Query. If this property is set to False, a right-click on this object only selects the indicated cell. The default value of this property is True. |
| `X` | Double | RW | base gráfica | — | binária (x1 do retângulo) | — | This property defines an object's left horizontal coordinate, in Himetric units. |
| `Y` | Double | RW | base gráfica | — | binária (y1 do retângulo) | — | This property defines an object's upper vertical coordinate, in Himetric units. |
| `Width` | Double | RW | base gráfica | — | binária (x2 − x1) | — | Determines an object's width, in Himetric units. |
| `Height` | Double | RW | base gráfica | — | binária (y2 − y1) | — | Determines an object's height. |
| `Angle` | ULong | RW | base gráfica | Angle | nomeada (cabeçalho) | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | base gráfica | Layer | nomeada (cabeçalho) | — | Camada (0xFFFFFFFF = todas) |
| `Visible` | Boolean | RW | base gráfica | Visible | nomeada (cabeçalho) | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | Boolean | RW | base gráfica | Enabled | nomeada (cabeçalho) | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | Boolean | RW | base gráfica | TabStop | nomeada (cabeçalho) | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Tip` | String | RW | base gráfica | Tip | nomeada (cabeçalho) | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_ExtentX` | Long |  | gravada no .prj | _ExtentX | nomeada | — | sem equivalente na type lib |
| `_ExtentY` | Long |  | gravada no .prj | _ExtentY | nomeada | — | sem equivalente na type lib |
| `_StockProps` | Long |  | gravada no .prj | _StockProps | nomeada | — | sem equivalente na type lib |
| `_Version` | Long |  | gravada no .prj | _Version | nomeada | — | sem equivalente na type lib |
| `Charset` | Integer |  | gravada no .prj | Charset | nomeada | — | sem equivalente na type lib |
| `ColWidth#` | Long |  | gravada no .prj | ColWidth# | nomeada | — | sem equivalente na type lib (família: 12) |
| `FieldBkColor#` | Long |  | gravada no .prj | FieldBkColor# | nomeada | — | sem equivalente na type lib (família: 12) |
| `FieldColor#` | Long |  | gravada no .prj | FieldColor# | nomeada | — | sem equivalente na type lib (família: 12) |
| `FieldFormat#` | String |  | gravada no .prj | FieldFormat# | nomeada | — | sem equivalente na type lib (família: 12) |
| `FieldName#` | String |  | gravada no .prj | FieldName# | nomeada | — | sem equivalente na type lib (família: 12) |
| `FieldTextAlignment#` | Long |  | gravada no .prj | FieldTextAlignment# | nomeada | — | sem equivalente na type lib (família: 12) |
| `FieldVisible#` | Boolean |  | gravada no .prj | FieldVisible# | nomeada | — | sem equivalente na type lib (família: 12) |
| `FieldWidth#` | Long |  | gravada no .prj | FieldWidth# | nomeada | — | sem equivalente na type lib (família: 12) |
| `Italic` | Boolean |  | gravada no .prj | Italic | nomeada | — | sem equivalente na type lib |
| `NColumns` | Long |  | gravada no .prj | NColumns | nomeada | — | sem equivalente na type lib |
| `NFields` | Long |  | gravada no .prj | NFields | nomeada | — | sem equivalente na type lib |
| `Strikethrough` | Boolean |  | gravada no .prj | Strikethrough | nomeada | — | sem equivalente na type lib |
| `Underline` | Boolean |  | gravada no .prj | Underline | nomeada | — | sem equivalente na type lib |
| `Weight` | Integer |  | gravada no .prj | Weight | nomeada | — | sem equivalente na type lib |

**Métodos:** `AboutBox()`; `ClearFields()`; `RetrieveE3QueryFields()`; `Requery()`; `GetColumnValue(Index Long)`; `Refresh()`

**Eventos:** `KeyDown(KeyCode Integer, Shift Integer)`; `Click()`; `DblClick()`; `KeyPress(KeyAscii Integer)`; `KeyUp(KeyCode Integer, Shift Integer)`; `MouseDown(Button Integer, Shift Integer, x OLE_XPOS_PIXELS, y OLE_YPOS_PIXELS)`; `MouseMove(Button Integer, Shift Integer, x OLE_XPOS_PIXELS, y OLE_YPOS_PIXELS)`; `MouseUp(Button Integer, Shift Integer, x OLE_XPOS_PIXELS, y OLE_YPOS_PIXELS)`; `OnDrawRow(Selected Boolean, Line Long, RowTextColor Variant, RowBackColor Variant)`; `OnFormatCell(Column Long, FieldName String, OriginalValue Variant, FormattedValue Variant)`

### Enumerações de E3Browser

- **enumBrowserHeaderAlignment**: bhaLeft=0, bhaCenter=1, bhaRight=2, bhaFollowColumn=3
- **enumCursorLocation**: clServer=0, clClient=1, clCached=2
- **enumCursorType**: ctKeyset=0, ctStatic=1, ctDynamic=2
- **enumGLType**: GLnone=0, GLHorz=1, GLVert=2, GLBoth=3
- **enumSortOrderType**: SONoSort=0, SOAsc=1, SODesc=2
- **enumTextAlignment**: taAlignLeft=0, taAlignCenter=1, taAlignRight=2

---

## E3Sys

Arquivo `E3Sys.dll` · versão 1.1 · LIBID `{318FE5A0-3319-11D4-8E8A-525400E657A3}` · E3Sys Library 1.1

Classes: [AgSimple](#e3sys-agsimple), [AlarmFilter](#e3sys-alarmfilter), [AnalogBind](#e3sys-analogbind), [AnimationBind](#e3sys-animationbind), [AppFilesNode](#e3sys-appfilesnode), [AppXQuery](#e3sys-appxquery), [BindExpert](#e3sys-bindexpert), [ClientsNode](#e3sys-clientsnode), [DBAccessConnection](#e3sys-dbaccessconnection), [DBMySQLConnection](#e3sys-dbmysqlconnection), [DBOracleConnection](#e3sys-dboracleconnection), [DBPostgresConnection](#e3sys-dbpostgresconnection), [DBSqlConnection](#e3sys-dbsqlconnection), [DomainNode](#e3sys-domainnode), [E3FileCollection](#e3sys-e3filecollection), [E3Query](#e3sys-e3query), [E3QueryCollection](#e3sys-e3querycollection), [E3QueryField](#e3sys-e3queryfield), [E3StudioApplication](#e3sys-e3studioapplication), [E3UaNodeId](#e3sys-e3uanodeid), [Event](#e3sys-event), [Events](#e3sys-events), [EventStatus](#e3sys-eventstatus), [ExtArea](#e3sys-extarea), [ExtControl](#e3sys-extcontrol), [ExtFile](#e3sys-extfile), [ExtItem](#e3sys-extitem), [GroupNode](#e3sys-groupnode), [GroupsNode](#e3sys-groupsnode), [LibFileNode](#e3sys-libfilenode), [LibFilesNode](#e3sys-libfilesnode), [LicenseCounterNode](#e3sys-licensecounternode), [LicenseNode](#e3sys-licensenode), [LinePrinter](#e3sys-lineprinter), [Links](#e3sys-links), [LocalServerNode](#e3sys-localservernode), [MeasurementColors](#e3sys-measurementcolors), [MultiSourceBind](#e3sys-multisourcebind), [MultiSourceRow](#e3sys-multisourcerow), [PkgFileNode](#e3sys-pkgfilenode), [PkgFilesNode](#e3sys-pkgfilesnode), [PrjFileNode](#e3sys-prjfilenode), [PrjFilesNode](#e3sys-prjfilesnode), [Project](#e3sys-project), [RemoteDomainNode](#e3sys-remotedomainnode), [RemoteDomainServersNode](#e3sys-remotedomainserversnode), [RemoteDomainSessionNode](#e3sys-remotedomainsessionnode), [RemoteDomainsNode](#e3sys-remotedomainsnode), [RemoteServerNode](#e3sys-remoteservernode), [RuntimeFolder](#e3sys-runtimefolder), [SecurityNode](#e3sys-securitynode), [ServerApplicationE3](#e3sys-serverapplicatione3), [ServerNode](#e3sys-servernode), [ServersNode](#e3sys-serversnode), [StudioSessionNode](#e3sys-studiosessionnode), [StudiosNode](#e3sys-studiosnode), [TableBind](#e3sys-tablebind), [TableBindRow](#e3sys-tablebindrow), [UserEvent](#e3sys-userevent), [UserNode](#e3sys-usernode), [UsersNode](#e3sys-usersnode), [ViewerSessionNode](#e3sys-viewersessionnode), [ViewersNode](#e3sys-viewersnode)

<a id="e3sys-agsimple"></a>
### AgSimple

- CLSID `{1CC935C2-4C20-11D4-8E8A-525400E657A3}` · interface `IAgSimple`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 530580 instâncias em 35 arquivo(s)
- Simple Aggregate Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Source` | String | RW | type lib | Source | nomeada | — | Returns/sets link source |
| `Property` | String | RW | type lib | Property | nomeada | — | Returns/sets the property name it is linked to |
| `Type` | BindStyle | R | type lib | — | não gravada nomeada | — | Returns link type |
| `BiDirectional` | Boolean | RW | type lib | — | não gravada nomeada | — | BiDirectional This property returns True when a Link is Bidirectional and False when a Link is Reverse or Simple. |
| `Reverse` | Boolean | RW | type lib | Reverse | nomeada | — | True if the connection is reverse |
| `BiDir` | ULong |  | gravada no .prj | BiDir | nomeada | — | sem equivalente na type lib |

<a id="e3sys-alarmfilter"></a>
### AlarmFilter

- CLSID `{4557A510-256D-48A9-A66D-20BCEE2AF042}` · interface `IAlarmFilter`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- AlarmFilter control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `AlarmServer` | BSTRALARMLINK | RW | type lib | — | — | — | Name of a unique Alarm Server on an application. |
| `AreaFilter` | String | RW | type lib | — | — | an empty String, that is, no filtering by area | Controls visible alarm areas on an Alarm Filter. If its value is not an empty String, it displays events whose Area names start with the indicated text. For example, if this property is equal to "Ana", it displays Area alarms such as "Analog.Production" or "Analysis", but not "Digital.Analysis" or "… |
| `CustomFilter` | String | RW | type lib | — | — | — | Allows informing a customized filter for alarms, as an expression. The next table describes all fields available for use on this filter expression. Available fields for the CustomFilter property FIELD DATA TYPE DESCRIPTION Acked Boolean Indicates whether a message was already acknowledged AckRequire… |
| `FilterType` | AlarmFilterType | RW | type lib | — | — | — | Performs the alarm filters. Possible values for this property are 1 - OnlyAlarms: Displays only alarms (default), 2 - OnlyEvents: Displays only events, or 3 - AlarmsAndEvents: Displays both alarms and events. |
| `ShowMediumPriority` | Boolean | RW | type lib | — | — | True | If this property is set to True, displays alarms with a Medium severity. The default value of this property is True. |
| `ShowLowPriority` | Boolean | RW | type lib | — | — | True | If this property is set to True, displays alarms with a Low severity. The default value of this property is True. |
| `ShowHighPriority` | Boolean | RW | type lib | — | — | True | If this property is set to True, displays alarms with a High severity. The default value of this property is True. |
| `ShowCriticalPriority` | Boolean | RW | type lib | — | — | True | If this property is set to True, displays alarms with a Critical severity. The default value of this property is True. |
| `SimpleAreaFilter` | Boolean | RW | type lib | — | — | — | When this property is set to True, the behavior of filtering by Alarm Area names is based only on the coincidence of the initial part of a name. When this property is set to False, this behavior considers the entire Area name, but allows 284 Server Objects using wildcard characters and multiple area… |
| `PrimarySortField` | String | RW | type lib | — | — | "EventTime" | Determines a primary field for sorting events on an Alarm Filter. Please check all available fields on Elipse E3 User's Manual. Default value of this property is "EventTime". When this property is an empty String, the SecondarySortField, ThirdSortField, and FourthSortField properties have no effect. |
| `PrimarySortAscending` | Boolean | RW | type lib | — | — | False | When this property is set to False, the sort order of events by the primary field is in descending order. Otherwise, the sort order is in ascending order. The default value of this property is False. |
| `SecondarySortField` | String | RW | type lib | — | — | an empty String | Determines a secondary field for sorting events on an Alarm Filter. Please check all available fields on Elipse E3 User's Manual. The default value of this property is an empty String. This property has no effect when the PrimarySortField property is configured with an empty String. |
| `SecondarySortAscending` | Boolean | RW | type lib | — | — | False | When this property is set to True, the sort order of events by a secondary field is in ascending order. Otherwise, it is descending. The default value of this property is False. |
| `ThirdSortField` | String | RW | type lib | — | — | an empty String | Determines a third field for sorting events on an Alarm Filter. Please check all available fields on Elipse E3 User's Manual. The default value of this property is an empty String. This property has no effect when the PrimarySortField or SecondarySortField properties are configured with an empty Str… |
| `ThirdSortAscending` | Boolean | RW | type lib | — | — | False | When this property is set to False, the sort order of events by a third field is in descending order. Otherwise, it is ascending. The default value of this property is False. |
| `FourthSortField` | String | RW | type lib | — | — | an empty String | Determines a fourth field for sorting events on an Alarm Filter. Please check all available fields on Elipse E3 User's Manual. The default value of this property is an empty String. This property has no effect when the PrimarySortField, SecondarySortField, or ThirdSortField properties are configured… |
| `FourthSortAscending` | Boolean | RW | type lib | — | — | False | When this property is set to False, the sort order of events by a fourth field is in descending order. Otherwise, it is ascending. The default value of this property is False. |
| `AlarmCount` | Long | R | type lib | — | — | — | Determines the number of alarms on an Alarm Filter. This is a read-only property. |
| `ActiveAlarms` | Long | R | type lib | — | — | — | Determines the number of active alarms on an Alarm Filter. This is a read-only property. |
| `ActiveNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of unacknowledged alarms on an Alarm Filter. This is a read-only property. |
| `ActiveCritNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of unacknowledged alarms with a Critical severity on an Alarm Filter. This is a read-only property. |
| `ActiveHighNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of unacknowledged alarms with a High severity on an Alarm Filter. This is a read-only property. |
| `ActiveMedNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of unacknowledged alarms with a Medium severity on an Alarm Filter. This is a read-only property. Server Objects 279 |
| `ActiveLowNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of unacknowledged alarms with a Low severity on an Alarm Filter. This is a read-only property. |
| `ActiveCritAlarms` | Long | R | type lib | — | — | — | Indicates the number of active alarms with a Critical severity on an Alarm Filter. This is a read-only property. |
| `ActiveHighAlarms` | Long | R | type lib | — | — | — | Indicates the number of active alarms with a High severity on an Alarm Filter. This is a read-only property. |
| `ActiveMedAlarms` | Long | R | type lib | — | — | — | Indicates the number of active alarms with a Medium severity on an Alarm Filter. This is a read-only property. |
| `ActiveLowAlarms` | Long | R | type lib | — | — | — | Indicates the number of active alarms with a Low severity on an Alarm Filter. This is a read-only property. |
| `InactiveNACKAlarms` | Long | R | type lib | — | — | — | Determines the number of inactive and unacknowledged alarms on an Alarm Filter. This is a read-only property. |
| `InactiveCritNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of inactive and unacknowledged alarms with a Critical severity on an Alarm Filter. This is a read- only property. |
| `InactiveHighNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of inactive and unacknowledged alarms with a High severity on an Alarm Filter. This is a read- only property. |
| `InactiveMedNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of inactive and unacknowledged alarms with a Medium severity on an Alarm Filter. This is a read-only property. |
| `InactiveLowNACKAlarms` | Long | R | type lib | — | — | — | Indicates the number of inactive and unacknowledged alarms with a Low severity on an Alarm Filter. This is a read- only property. |
| `Events` | IEventStatusCollection | R | type lib | — | — | — | Returns a collection of Events on an Alarm Filter. This is a read-only property. For more information about the collection returned by this property, please check topic Collection of Events. The next script contains an example of using this property. Sub CommandButton1_Click() For Each evt In Screen… |
| `Connections` | IAlarmConnectionCollection | R | type lib | — | — | — | Returns a collection of Connections on an Alarm Filter. This is a read-only property. For more information about the collection returned by this property, please check topic Collection of Connections. |
| `Filters` | IConnectionFilterCollection | R | type lib | — | — | — | Returns a collection of Filters on an Alarm Filter. This is a read-only property. For more information about the collection returned by this property, please check topic Collection of Filters. |

**Métodos:** `GetEventByIndex(Index UInt)`

<a id="e3sys-analogbind"></a>
### AnalogBind

- CLSID `{3ACDEDBE-A66B-49EB-AB53-A7773D97D0F9}` · interface `IAnalogBind`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 11 instâncias em 2 arquivo(s)
- AnalogBind Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Source` | String | RW | type lib | Source | nomeada | — | Returns/sets link source |
| `Property` | String | RW | type lib | Property | nomeada | — | Returns/sets the property name it is linked to |
| `Type` | BindStyle | R | type lib | — | não gravada nomeada | — | Returns link type |
| `SrcHiValue` | Double | RW | type lib | SrcHiValue | nomeada | — | SrcHiValue This property specifies the highest value reached by the source. The next script contains an example of using this property. Sub SrcHiValue_ValueChange() On Error Resume Next Dim Bind Set Bind = Screen.Item("ScrollBar1").Links.Item("Value") Screen.Item("ScrollBar2").Max = Value If Bind Is… |
| `SrcLoValue` | Double | RW | type lib | SrcLoValue | nomeada | — | SrcLoValue This property specifies the lowest value reached by the source. The next script contains an example of using this property. Programming in Elipse E3 45 Sub SrcLoValue_ValueChange() On Error Resume Next Dim Bind Set Bind = Screen.Item("ScrollBar1").Links.Item("Value") Screen.Item("ScrollBa… |
| `DstHiValue` | Double | RW | type lib | DstHiValue | nomeada | — | DstHiValue This property specifies the highest value reached by the property. The next script contains an example of using this property. Sub DstHiValue_ValueChange() On Error Resume Next Dim Bind Set Bind = Screen.Item("ScrollBar1").Links.Item("Value") Screen.Item("ScrollBar1").Max = Value If Bind … |
| `DstLoValue` | Double | RW | type lib | DstLoValue | nomeada | — | DstLoValue This property specifies the lowest value reached by the property. The next script contains an example of using this property. Sub DstLoValue_ValueChange() On Error Resume Next Dim Bind Set Bind = Screen.Item("ScrollBar1").Links.Item("Value") Screen.Item("ScrollBar1").Min = Value If Bind I… |
| `Color` | ULong |  | gravada no .prj | Color | nomeada | — | sem equivalente na type lib |

<a id="e3sys-animationbind"></a>
### AnimationBind

- CLSID `{22E4B7E4-E838-492A-820A-E05190C0A01A}` · interface `IAnimationBind`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 371 instâncias em 12 arquivo(s)
- AnimationBind Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Source` | String | RW | type lib | Source | nomeada | — | Returns/sets link source |
| `Property` | String | RW | type lib | — | não gravada nomeada | — | Returns/sets the property name it is linked to |
| `Type` | BindStyle | R | type lib | — | não gravada nomeada | — | Returns link type |
| `OnValue` | Variant | RW | type lib | OnValue | nomeada | — | OnValue This property specifies the value a property assumes when source's expression returns True. The next script contains an example of using this property. Sub OnValue_Click() On Error Resume Next Dim Value If Application.ShowPickColor_ (Value, ForegroundColor, 400, 300) Then Dim Bind Set Bind =… |
| `OffValue` | Variant | RW | type lib | OffValue | nomeada | — | OffValue This property specifies the value a property assumes when source's expression returns False. The next script contains an example of using this property. Sub OffValue_Click() On Error Resume Next Dim Value If Application.ShowPickColor_ (Value, ForegroundColor, 400, 300) Then Dim Bind Set Bin… |
| `BlinkOn` | Boolean | RW | type lib | BlinkOn | nomeada | — | BlinkOn When this property is set to True, the connected property alternates periodically between values of OnValue and BlinkOnValue properties, in case the source returns True. The next script contains an example of using this property. Sub BlinkOn_Change() On Error Resume Next Dim Bind Set Bind = … |
| `BlinkOff` | Boolean | RW | type lib | BlinkOff | nomeada | — | BlinkOff When this property is set to True, the connected property alternates periodically between values of OffValue and BlinkOffValue properties, in case the source returns False. The next script contains an example of using this property. Sub BlinkOff_Change() On Error Resume Next Dim Bind Set Bi… |
| `BlinkOnValue` | Variant | RW | type lib | BlinkOnValue | nomeada | — | BlinkOnValue This property specifies an alternative value the property assumes periodically when source's expression returns True and the BlinkOn property is set to True. The next script contains an example of using this property. Sub BlinkOnValue_Click() On Error Resume Next Dim Value If Applicatio… |
| `BlinkOffValue` | Variant | RW | type lib | BlinkOffValue | nomeada | — | BlinkOffValue This property specifies an alternative value the property assumes periodically when source's expression returns False and the BlinkOff property is set to True. The next script contains an example of using this property. Sub BlinkOffValue_Click() On Error Resume Next Dim Value If Applic… |
| `OnProperty` | String |  | gravada no .prj | OnProperty | nomeada | — | sem equivalente na type lib |
| `Version` | ULong |  | gravada no .prj | Version | nomeada | — | sem equivalente na type lib |

<a id="e3sys-appfilesnode"></a>
### AppFilesNode

- CLSID `{151E7DC4-B39F-4FA8-B46C-1F0A61EF6190}` · interface `IAppFilesNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- AppFiles Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-appxquery"></a>
### AppXQuery

- CLSID `{AC88CF6C-31B3-4A33-8252-EBBFF8622E3D}` · interface `IAppXQuery`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- AppXQuery object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Script` | String | RW | type lib | — | — | — | Source code of the script to be executed by this Query. |
| `DefaultObjectPath` | String | RW | type lib | — | — | — | Path of an object to be used as the default root object of this Query. If this property is not defined, the default root object is the Query Application Hierarchy object itself. |

**Métodos:** `VerifyXQuery(pvarOutErrors Variant)`; `RunXQuery(RootObjectOrPath Variant, pvarOutErrors Variant)`

<a id="e3sys-bindexpert"></a>
### BindExpert

- CLSID `{2BCDADBE-A66B-49EB-AB53-A7773D97D0F9}` · interface `IBindExpert`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- BindExpert Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Source` | String | RW | type lib | — | — | — | Returns/sets link source |
| `Property` | String | RW | type lib | — | — | — | Returns/sets the property name it is linked to |
| `Type` | BindStyle | R | type lib | — | — | — | Returns link type |

<a id="e3sys-clientsnode"></a>
### ClientsNode

- CLSID `{BB278D82-EAFB-43E1-B924-4E49B3A353C5}` · interface `IClientsNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- ClientsNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-dbaccessconnection"></a>
### DBAccessConnection

- CLSID `{BEED2462-30A0-11D4-8E8A-525400E658B2}` · interface `IDBAccessConnection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DBAccessConnection control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ConnectString` | String | RW | type lib | — | — | — | Connection String |
| `FilePath` | String | RW | type lib | — | — | — | File path |
| `UserName` | String | RW | type lib | — | — | — | Login String |
| `Password` | String | RW | type lib | — | — | — | Pwd String |
| `DBPassword` | String | RW | type lib | — | — | — | DB Password |

<a id="e3sys-dbmysqlconnection"></a>
### DBMySQLConnection

- CLSID `{AEBC2F55-78A5-4DE5-835B-7733623A2D7A}` · interface `IDBMySQLConnection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DBMySQLConnection control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Server` | String | RW | type lib | — | — | — | Address of a MySQL server. |
| `Port` | Long | RW | type lib | — | — | — | Number of the TCP/IP port used when connecting to a MySQL server. |
| `Database` | String | RW | type lib | — | — | — | Name of a database in a MySQL server. |
| `Login` | String | RW | type lib | — | — | — | Login name of a user of a database in a MySQL server. |
| `Password` | String | RW | type lib | — | — | — | Password of a user of a database in a MySQL server. |

<a id="e3sys-dboracleconnection"></a>
### DBOracleConnection

- CLSID `{ACDD7462-20A0-11D4-8E8A-525400E658B2}` · interface `IDBOracleConnection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DBOracleConnection control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ConnectString` | String | RW | type lib | — | — | — | Connection String |
| `UserName` | String | RW | type lib | — | — | — | Login String |
| `Password` | String | RW | type lib | — | — | — | Pwd String |
| `EnableTimestamp` | Boolean | RW | type lib | — | — | — | Enable timestamp type |
| `UseNativeProvider` | Boolean | RW | type lib | — | — | — | Use native provider |

<a id="e3sys-dbpostgresconnection"></a>
### DBPostgresConnection

- CLSID `{CE9674FF-204E-4585-B58A-E3776814FB40}` · interface `IDBPostgresConnection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DBPostgresConnection control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Server` | String | RW | type lib | — | — | — | Address of a PostgreSQL server. |
| `Port` | Long | RW | type lib | — | — | — | Number of the TCP/IP port used when connecting to a PostgreSQL server. |
| `Database` | String | RW | type lib | — | — | — | Name of a database in a PostgreSQL server. |
| `Login` | String | RW | type lib | — | — | — | Login name of a user of a database in a PostgreSQL server. |
| `Password` | String | RW | type lib | — | — | — | Password of a user of a database in a PostgreSQL server. 304 Server Objects |

<a id="e3sys-dbsqlconnection"></a>
### DBSqlConnection

- CLSID `{CCED8461-10A0-11D4-8E8A-525400E658B2}` · interface `IDBSqlConnection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 3 instâncias em 1 arquivo(s)
- DBSqlConnection control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Server` | String | RW | type lib | _Server (apelido confirmado) | nomeada | — | Server |
| `Catalog` | String | RW | type lib | — | não gravada nomeada | — | Catalog |
| `UserName` | String | RW | type lib | — | não gravada nomeada | — | Login String |
| `Password` | String | RW | type lib | _Pwd (apelido confirmado) | nomeada | — | Pwd String |
| `UseTransaction` | Boolean | RW | type lib | — | não gravada nomeada | — | Use Transaction |
| `NetLibrary` | SqlNetworkLibrary | RW | type lib | _NetLibrary (apelido confirmado) | nomeada | — | Returns/sets net library |
| `CustomConnectionString` | String | RW | type lib | _ConnString (apelido confirmado) | nomeada | — | Returns/sets the custom connection string |
| `UseCustomConnectionString` | Boolean | RW | type lib | _UseConnString (apelido confirmado) | nomeada | — | Enables/disables the custom connection string |
| `Provider` | SqlProvider | RW | type lib | _Provider (apelido confirmado) | nomeada | — | Returns/sets SQL provider |
| `_Cat` | String |  | gravada no .prj | _Cat | nomeada | — | sem equivalente na type lib |
| `_Log` | String |  | gravada no .prj | _Log | nomeada | — | sem equivalente na type lib |
| `_Trans` | Byte |  | gravada no .prj | _Trans | nomeada | — | sem equivalente na type lib |

<a id="e3sys-domainnode"></a>
### DomainNode

- CLSID `{006B9A90-4C41-4F73-8259-CCC89193B5FA}` · interface `IDomainNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- DomainNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `HotStandby` | Boolean | R | type lib | — | — | — | Returns True if the Hot-Standby mode is enabled in a Domain. This is a read-only property. |
| `FullPath` | String | R | type lib | — | — | — | Full path of a Domain file. This is a read-only property. 364 Server Objects |
| `Domain` | String | R | type lib | — | — | — | Friendly name of a Domain, configured in the Domain name item of the General group on the Properties tab of a Domain's configuration window. This is a read-only property. |
| `State` | EDomainState | R | type lib | — | — | — | Indicates the status of a Domain, local or remote. Possible values for this property are -1: Closed or without a Domain, 0: Stopped but loaded, 1: In Hot-Standby mode, or 2: Executing. This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`; `Refresh()`; `Stop()`

<a id="e3sys-e3filecollection"></a>
### E3FileCollection

- CLSID `{FF7E7E25-67DA-468A-B084-6DFF98733F06}` · interface `IE3FileCollection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- File collection object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Count` | Long | R | type lib | — | — | — | The count of Files |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-e3query"></a>
### E3Query

- CLSID `{0F87A305-5CC5-4C6B-8C7E-0FA31D46433A}` · interface `IE3Query` · eventos `DE3QueryEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 6 instâncias em 3 arquivo(s)
- E3Query object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `DataSource` | String | RW | type lib | DataSource | nomeada | — | Indicates a Database, Storage, or OPC UA Driver object used in a Query. |
| `Table` | String | RW | type lib | Table | nomeada | — | This property contains the tables to query. For example, Alarms is the alarms or events table. It corresponds to the argument of the FROM clause in the SQL code of a Query. |
| `Fields` | String | RW | type lib | Fields | nomeada | — | Text with the Fields to be viewed in a Query, separated by commas. It corresponds to the argument of the SELECT clause in a Query's SQL code. When blank (empty), it determines that a Query must display all Fields from a table. |
| `Where` | String | RW | type lib | Where | nomeada | — | Determines the condition of a Query that filters records from a table to view, that is, only records that match this condition are viewed. It corresponds to the WHERE clause in the SQL code of a Query. |
| `OrderBy` | String | RW | type lib | OrderBy | nomeada | — | Text corresponding to the argument of the ORDER BY clause in the SQL code of a Query. |
| `Having` | String | RW | type lib | Having | nomeada | — | Text corresponding to the argument of the HAVING clause in the SQL code of a Query. This property is commonly used with the GroupBy property. |
| `GroupBy` | String | RW | type lib | GroupBy | nomeada | — | Text corresponding to the argument of the GROUP BY clause in the SQL code of a Query. |
| `SQL` | String | RW | type lib | SQL | nomeada | — | Contains the SQL code specified for a Query. |
| `CursorLocation` | enumCursorLocation | RW | type lib | CursorLocation | nomeada | — | Defines the location where a Query is generated and handled, from a DBMS (Database Management System) point of view. Possible values for this property are 0 - clServer: Query is generated on a DBMS (server), 1 - clClient: Query is generated on a Server (client, default), or 2 - clCached: Equivalent … |
| `CursorType` | enumCursorType | RW | type lib | CursorType | nomeada | 0 (zero, ctKeyset) | Defines the type of a Query, according to the way data is viewed. The default value of this property is 0 (zero, ctKeyset). Possible values for this property are described on the next table. Available options for the CursorType property 0 - ctKeyset Any change in records initially returned by a Quer… |
| `DatabaseType` | DBSourceType | RW | type lib | — | não gravada nomeada | — | Defines the type of database server used in a Query. Possible values for this property are -1 - stUnknown: Undefined (default), 0 - stAccess: Access-type database, 1 - stOracle: Oracle-type database, 2 - stSqlServer: SQL Server-type database, 3 - stPostgreSQL: PostgreSQL-type database, or 4 - stMySQ… |
| `FunctionType` | FunctionType | RW | type lib | — | não gravada nomeada | — | This property is valid when a Storage object is the source of a Query, which is indicated by the DataSource property. It specifies a function that defines data generated by a Query. Some functions contain sub-functions, which can be indicated in the FunctionSubType property. This property can assume… |
| `FunctionSubType` | FunctionSubType | RW | type lib | HistSubType (apelido inferido) | nomeada | — | Specifies the subtype of the function indicated by the FunctionType property. Only the 1 (one, ftArchivedValue), 2 (two, ftTagAttribute), and 6 (six, ftCalculatedData) options have subtypes. For all other functions, this property assumes the value -1 (minus one, fsNoSubType). The next table shows al… |
| `IgnoreQuality` | Boolean | RW | type lib | Quality (apelido inferido) | nomeada | — | Allows indicating whether data with bad quality is included or not on the results of a Query. This property is only effective if a Query object is using a Storage object as its data source. |
| `QueryType` | E3QueryType | RW | type lib | QueryType | nomeada | — | Indicates the type of query to perform. Possible values for this property are the following: -1 - qtUndefined: The Query object initially tries to execute a query on a Database object. If it fails, then it tries to execute a query on a Storage object. This is the default value for Queries created in… |
| `UaNamespaceArray` | IUaNamespaceArray | R | type lib | — | não gravada nomeada | — | This property returns an object that is a Collection of OPC UA Namespaces, used by the Fields configured in a Query. This is a read-only property. 296 Server Objects |
| `UaQueryType` | UaQueryType | RW | type lib | UaRaw (apelido a confirmar) | nomeada | — | This is a read and write property that allows determining whether the type of a Query is Raw Data (0 - uqtRaw) or Processed Data (1 - uqtProcessed, default). In Elipse E3 Studio this is a read-only property. At run time it allows configuring the type of an OPC UA Query, but it only accepts writings … ⚠ manual: somente leitura |
| `QueryCacheMaxRows` | Long | RW | type lib | QueryCacheMaxRows | nomeada | 0 (zero, unlimited) | Maximum number of rows in cache for Queries whose CursorLocation property is configured with the value 2 (two, clCached) or if the Cached queries usage option on the Database group of the Properties tab of the Domain configuration window is configured as Enabled (globally). The default value of this… |
| `QueryCacheMaxKBytes` | Long | RW | type lib | QueryCacheMaxKBytes | nomeada | 256 | Maximum size, in kilobytes, that is stored in cache for Queries whose CursorLocation property is configured with the value 2 (two, clCached) or if the Cached queries usage option on the Database group of the Properties tab of the Domain configuration window is configured as Enabled (globally). The d… |
| `QueryCacheOverrideDomainConfig` | Boolean | RW | type lib | QueryCacheOverrideDomConfig (apelido confirmado) | nomeada | — | When this property is configured to False (default), a Query obeys the Domain configuration, the QueryCacheMaxKBytes and QueryCacheMaxRows properties are not considered and these values are defined in the Maximum query cache size (kilobytes) and Maximum query cache size (rows) options of that tab, r… |
| `Tip` | String | RW | cabeçalho (todo objeto) | Tip | nomeada | — | This property displays a pop-up text when the mouse pointer is briefly over an object at run time. |
| `Angle` | ULong | RW | cabeçalho (todo objeto) | Angle | nomeada | 0 (zero, no rotation) | This property defines a rotation angle in degrees, counter clockwise, that an object must be rotated. This also applies to child objects of that object, respecting rotation limitations of each child object. An object rotates according to its center, which can be edited during this rotation operation… |
| `Layer` | ULong | RW | cabeçalho (todo objeto) | Layer | nomeada | — | propriedade do cabeçalho gravada em todo objeto E3 |
| `Visible` | ULong | RW | cabeçalho (todo objeto) | Visible | nomeada | — | This property defines an object's visibility. If this property is configured as True, that object remains visible, as long as this object's parent object be visible and this object's Layer property is available on a Screen layer. |
| `Enabled` | ULong | RW | cabeçalho (todo objeto) | Enabled | nomeada | — | Enables or disables an object, that is, focus and response to user-generated events. If this property is set to True, an object can receive focus, respond to user-generated events, and it is accessible via scripts (default). Otherwise, users cannot interact with this object by using the mouse pointe… |
| `TabStop` | ULong | RW | cabeçalho (todo objeto) | TabStop | nomeada | — | This property determines how the TAB key is used in an application. If this property is set to True, users can use the TAB key. Otherwise, this key cannot be used. |
| `Name` | String | RW | framework | Name | nomeada | — | Identifies an object in an application. This property cannot be changed while this object is active. When changing this property, users must change all properties or scripts that use this object. It is not advisable to change this property at run time. The next characters are reserved and automatica… |
| `DocString` | String | RW | framework | DocString | nomeada | — | Free text that enables documenting an object's functionality or features by the project's programmers. The next script contains an example of using this property. Sub CommandButton1_Click() Docstring = "This button activates the system condenser." MsgBox Docstring |
| `_DefaultValue#` | Double, Date, String |  | gravada no .prj | _DefaultValue# | nomeada | — | sem equivalente na type lib (família: 13) |
| `_DefaultVar#` | String |  | gravada no .prj | _DefaultVar# | nomeada | — | sem equivalente na type lib (família: 13) |
| `_Query#.Column` | String |  | gravada no .prj | _Query#.Column | nomeada | — | sem equivalente na type lib (família: 10) |
| `_Query#.Table` | String |  | gravada no .prj | _Query#.Table | nomeada | — | sem equivalente na type lib (família: 10) |
| `_Query2.Criteria0.Op` | ULong |  | gravada no .prj | _Query2.Criteria0.Op | nomeada | — | sem equivalente na type lib |
| `_Query2.Criteria0.Operation` | String |  | gravada no .prj | _Query2.Criteria0.Operation | nomeada | — | sem equivalente na type lib |
| `_Query2.Criteria0.Value` | String |  | gravada no .prj | _Query2.Criteria0.Value | nomeada | — | sem equivalente na type lib |
| `_Query2.Criteria0.Variable` | Boolean |  | gravada no .prj | _Query2.Criteria0.Variable | nomeada | — | sem equivalente na type lib |
| `_QueryFieldCount` | UShort |  | gravada no .prj | _QueryFieldCount | nomeada | — | sem equivalente na type lib |
| `_TableName0` | String |  | gravada no .prj | _TableName0 | nomeada | — | sem equivalente na type lib |
| `DBSourceType` | ULong |  | gravada no .prj | DBSourceType | nomeada | — | sem equivalente na type lib |
| `DefaultValuesCount` | ULong |  | gravada no .prj | DefaultValuesCount | nomeada | — | sem equivalente na type lib |
| `Domain` | String |  | gravada no .prj | Domain | nomeada | — | sem equivalente na type lib |
| `EnableFields` | Boolean |  | gravada no .prj | EnableFields | nomeada | — | sem equivalente na type lib |
| `HistType` | ULong |  | gravada no .prj | HistType | nomeada | — | sem equivalente na type lib |
| `Query#.Alias` | String |  | gravada no .prj | Query#.Alias | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.Criteria` | String |  | gravada no .prj | Query#.Criteria | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.CriteriaCount` | ULong |  | gravada no .prj | Query#.CriteriaCount | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.Function` | String |  | gravada no .prj | Query#.Function | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.GroupBy` | Boolean |  | gravada no .prj | Query#.GroupBy | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.Output` | Boolean |  | gravada no .prj | Query#.Output | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.SortOrder` | ULong |  | gravada no .prj | Query#.SortOrder | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.SortType` | ULong |  | gravada no .prj | Query#.SortType | nomeada | — | sem equivalente na type lib (família: 10) |
| `Query#.VarType` | ULong |  | gravada no .prj | Query#.VarType | nomeada | — | sem equivalente na type lib (família: 10) |
| `TablesCount` | ULong |  | gravada no .prj | TablesCount | nomeada | — | sem equivalente na type lib |
| `UaNamespacesCount` | ULong |  | gravada no .prj | UaNamespacesCount | nomeada | — | sem equivalente na type lib |

**Métodos:** `SetVariableValue(VarName String, Value Variant)`; `GetE3QueryFields()`; `GetADORecordset()`; `GetAsyncADORecordset()`; `CancelAsyncADORecordset()`; `Execute(ImmediateExecute Boolean)`; `AddField(Name String, Table String)`; `AddTable(Name String)`; `RemoveField(FieldName String, Table String)`; `RemoveTable(TableName String)`; `AddStorageTag(Name String, FieldType Long)`; `RemoveStorageTag(Name String)`; `AddUaField(Name String, Alias String, Aggregate String)`; `RemoveUaField(Name String)`

**Eventos:** `OnAsyncQueryFinish(Recordset Object, Error Boolean)`

<a id="e3sys-e3querycollection"></a>
### E3QueryCollection

- CLSID `{CC61CD18-2FD0-408C-9980-6C76BDC8FD39}` · interface `IE3QueryCollection`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- E3Query Collection Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Count` | Long | R | type lib | — | — | — | Returns the number of Query Field objects on this Collection. This is a read-only property. |

**Métodos:** `Remove(Index Variant)`; `Item(Index Variant)`; `RefreshUaNodeIds()`

<a id="e3sys-e3queryfield"></a>
### E3QueryField

- CLSID `{3F17F375-5CD5-4C6B-8E7A-0FA31D46433A}` · interface `IE3QueryField`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- E3QueryField object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ColumnName` | String | RW | type lib | — | — | — | ColumnName Name of a column. This name must exist on the tables added to this Query. |
| `TableName` | String | RW | type lib | — | — | — | TableName Name of the table that a Field belongs. This table must have been added during the configuration of a Query. |
| `Alias` | String | RW | type lib | — | — | — | Alias Alias of this Field in a Query. |
| `Criteria` | String | RW | type lib | — | — | — | Criteria Filter applied to a Field. |
| `OrderBy` | String | RW | type lib | — | — | — | OrderBy Sort order of data in a Field. Valid values are "ASC" (ascending), "DESC" (descending), or an empty String (no sort order). Any other value means that a Field has no sort order. |
| `OrderNumber` | Long | RW | type lib | — | — | — | OrderNumber Order number of a Field relative to the other Fields forming the sort order of a Query. This value is only accepted as a number greater than 0 (zero) if a Field contains a sort type, defined by the OrderBy property. This value must be less or equal to the number of Fields forming the sor… |
| `Function` | String | RW | type lib | — | — | — | Function Function to which a Field can be passed as its parameter. |
| `GroupBy` | Boolean | RW | type lib | — | — | — | GroupBy When in True, indicates that a Field is part of a group. |
| `Visible` | Boolean | RW | type lib | — | — | — | Visible Indicates whether a Field is visible or not. |
| `UaNodeId` | IE3UaNodeId | RW | type lib | — | — | — | UaNodeId Returns an OPC UA Node Identifier-type object, with the configuration of a Node that identifies a Field from an OPC UA query on a certain OPC UA server. In Elipse E3 Studio this property is only represented by an icon, on the Id column of the configuration of Fields of a Query. This is a re… ⚠ manual: somente leitura |

<a id="e3sys-e3studioapplication"></a>
### E3StudioApplication

- CLSID `{11C1B832-46EA-4518-963E-756533F00F8E}` · interface `IE3StudioApplication`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- E3 Studio Application object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ProductVersionMajor` | Long | R | type lib | — | — | — | This property returns the major number of the installed version of Elipse E3 Studio. For example, if the installed version is 6.9.312, this property returns the value 6. This is a read-only property. |
| `ProductVersionMinor` | Long | R | type lib | — | — | — | This method returns the minor number of the installed version of Elipse E3 Studio. For example, if the installed version is 6.9.312, this property returns the value 9. This is a read-only property. |
| `ProductVersionBuild` | Long | R | type lib | — | — | — | This property returns the build number of the installed version of Elipse E3 Studio. For example, if the installed version is 6.9.312, this property returns the value 312. This is a read-only property. |
| `ProductString` | String | R | type lib | — | — | — | This property returns a String containing the product's name and the installed version of Elipse E3 Studio, such as "Elipse E3 6.9.312" or "Elipse E3 (64-bits) 6.9.312". This is a read-only property. Server Objects 277 |

**Métodos:** `GetObject(ObjectPath String)`; `Trace(MessageText String, LogTimeStamp Boolean, BreakLine Boolean)`; `RenameFolder(FullOldName String, NewName String)`; `CreatePRJ(PrjName String)`; `CreateFile(PrjName String, ClassName String, FileName String, Folder String, RunWizard Boolean, OpenView Boolean)`; `DeleteFile(PrjName String, FileName String, Folder String)`; `CreateFolder(PrjName String, FolderName String, ParentFolder String)`; `ListFiles(FileClass String, Domain String)`; `Verify(OutputFile String, ObjectLink String, FixQuestionsDefault Long)`; `BlockUndo()`; `ShowFilePicker(Open Boolean, FileName Variant, Extension String, Flags Long, Filter String)`

<a id="e3sys-e3uanodeid"></a>
### E3UaNodeId

- CLSID `{5502E25E-6936-4F30-AF4F-6708A72602F4}` · interface `IE3UaNodeId`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- E3UaNodeId object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `NamespaceIndex` | Long | RW | type lib | — | — | — | NamespaceIndex A read-and-write property identifying to which Namespace this Identifier refers. This index must be between 0 (zero) and the number of Namespaces minus 1 (one) in a server. When defining a Field in a Query, the index refers to the OPC UA Namespaces Collection defined in a Query object… |
| `Type` | UaNodeIdType | RW | type lib | — | — | — | Type A read-and-write property determining the type of identifier this object uses. Possible values for this property are 0 - nitNumeric: Identifier is a number (LONG), 1 - nitString: Identifier is a String, 2 - nitGUID: Identifier is a GUID-type (Globally Unique Identifier) String, or 3 - nitOpaque… |
| `Numeric` | Long | RW | type lib | — | — | — | Numeric A read-and-write property identifying this object, in case the Type property is equal to 0 (zero, nitNumeric). If the Type property is different from 0 (zero), reading this property returns an error. Writing to this property always forces the Type property to change to 0 (zero). Setting this… |
| `String` | String | RW | type lib | — | — | — | String A read-and-write property identifying this object, in case the Type property is equal to 1 (one, nitString). If the Type property is different from 1 (one), reading this property returns an error. Writing to this property always forces the Type property to change to 1 (one). An empty String i… |
| `GUID` | String | RW | type lib | — | — | — | GUID A read-and-write property identifying this object, in case the Type property is equal to 2 (two, nitGUID). If the Type property is different from 2 (two), reading this property returns an error. Writing to this property always forces the Type property to change to 2 (two). The value of this pro… |
| `Opaque` | String | RW | type lib | — | — | — | Opaque A read-and-write property identifying this object, in case the Type property is equal to 3 (three, nitOpaque). The value of this property is an array of bytes, that is, a String of characters not necessarily valid or printable. If the Type property is different from 3 (three), reading this pr… |

<a id="e3sys-event"></a>
### Event

- CLSID `{333B63D3-60C2-4450-BADE-35DC76F003FA}` · interface `IEvent`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Event object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Returns the name of this Event on the Collection of Events. This is a read-only property. ⚠ manual: somente leitura |

**Métodos:** `AddScript(bstrCode String)`; `RemoveAll()`

<a id="e3sys-events"></a>
### Events

- CLSID `{BB7F35A7-86FD-48F8-AA7B-97932835A4ED}` · interface `IEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Event collection object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Count` | Int | R | type lib | — | — | — | Returns the number of child objects, or items, of a collection of Events. This property works together with the Item method. If a collection does not contain child objects, the returned value is 0 (zero). This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`; `AddUserEvent(Name String, Link String, Type EUserEventType, ScanTime ULong, ChangeOnDisconnect Boolean)`; `RemoveUserEvent(Name String)`

<a id="e3sys-eventstatus"></a>
### EventStatus

- CLSID `{FF0A8402-6851-4C45-B824-EDD251779335}` · interface `IEventStatus`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Event status object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `EventTime` | Date | R | type lib | — | — | — | Date and time of Alarm Source's value at the moment of this Event, in local computer's time. This is a read-only property. |
| `EventTimeUTC` | Date | R | type lib | — | — | — | Date and time of Alarm Source's value at the moment of this Event, adjusted to UTC (Coordinated Universal Time) format. In applications created in versions previous to version 7.0, this property corresponds to the value of the EventTime property without timezone adjustment. For more information, ple… |
| `InTime` | Date | R | type lib | — | — | — | Stores value's date and time of the moment when it enters the alarm condition. This is a read-only property. |
| `OutTime` | Date | R | type lib | — | — | — | Stores value's date and time of the moment in which it leaves the alarm condition, or zero (12/30/1899) while this Alarm still did not leave the active condition. This is a read-only property. |
| `AckTime` | Date | R | type lib | — | — | — | Stores Elipse E3's date and time of the moment this Event is acknowledged, or zero (12/30/1899) while this Event is not acknowledged. For Events that do no ask for acknowledgment, this property assumes Elipse E3's date and time of the moment this Event is activated. This is a read-only property. |
| `CurrentValue` | Double | R | type lib | — | — | — | Determines the value of the Alarm Source, converted to Double, at the moment of this Event. For other Events this property's value is always 0 (zero). This is a read-only property. |
| `ActorID` | String | R | type lib | — | — | — | Name of the operator who acknowledged this Event. This is a read-only property and its value can be: Elipse E3 Viewer's logged-in user, when acknowledgment is performed on an E3Alarm, or "No user" if there is no logged-in user "System", when acknowledgment is automatic, that is, for Events that ask … |
| `Area` | String | R | type lib | — | — | — | For Alarm Events, this is the name of the Area to which the Alarm Source belongs. This is a read-only property. |
| `AlarmSourceName` | String | R | type lib | — | — | — | Contains the name of an Alarm Source. This is a read-only property. |
| `FullAlarmSourceName` | String | R | type lib | — | — | — | Stores the Alarm Source's full path, including Areas, name of Alarm Configurations, and possible Folders where it can be inserted, such as "Folder1.AlarmConfig1.Area1.AlarmSource1". This is a read-only property. 178 View |
| `ConditionName` | String | R | type lib | — | — | — | Name of a condition, if this is an Alarm Event. Possible values for this property are Dead Band: Dead Band-type Alarm Source, Digital: Digital-type Alarm Source, Discrete: Discrete-type Alarm Source, Level: Analog-type Alarm Source, or RateOfChange: Rate of Change-type Alarm Source. If this Event is… |
| `EventCategory` | String | R | type lib | — | — | — | Event's category. For Alarms, possible value for this property are Dead Band: Dead Band-type Alarm Source, Digital: Digital-type Alarm Source, Discrete: Discrete-type Alarm Source, Level: Analog-type Alarm Source, or RateOfChange: Rate of Change-type Alarm Source. This is a read-only property. |
| `EventType` | String | R | type lib | — | — | — | Event's type. For Alarm Events, this is always "Condition". This is a read-only property. |
| `Message` | String | R | type lib | — | — | — | This is the text configured on the Alarm Source. This is a read-only property. |
| `Quality` | String | R | type lib | — | — | — | Quality of Alarm Source's value at the moment of this Event. This is a read-only property. Possible values for this property are 0 - 63: Bad quality, 64 - 127: Uncertain quality, 128 - 191: Undefined value, or 192 - 255: Good quality. If this Event is not an Alarm, this property is equal to an empty… |
| `Source` | String | R | type lib | — | — | — | For Alarm Events, informs an expression used to evaluate Alarm conditions. This is a read-only property. |
| `SubConditionName` | String | R | type lib | — | — | — | Name of a subcondition, if it is an Alarm Event. Possible values for this property are DB: Dead Band alarm, DIG: Digital alarm, ROC: Rate of Change alarm, LOLO: Analog alarm on a Very Low range, LO: Analog alarm on a Low range, HI: Analog alarm on a High range, or HIHI: Analog alarm on a Very High r… |
| `FormattedValue` | String | R | type lib | — | — | — | Displays the formatted value of the Alarm Source that goes to this Event. This is a read-only property. |
| `UserField[Index Variant]` | Variant | R | type lib | — | — | — | This property receives an index or the name of a User Field from the Collection of User Fields of an Alarm Area, that is, the UserFields property, and returns its corresponding object. For more information about the object returned by this property, please check topic Alarm's User Fields. This is a … |
| `Severity` | EAlarmSeverity | R | type lib | — | — | — | This is the value of severity configured on the Alarm Source. Possible values for this property are -2: Critical, 0: High, 1: Medium, or 2: Low. This is a read-only property. |
| `Acked` | Boolean | R | type lib | — | — | — | Informs whether this Event was acknowledged (True) or not (False). This is a read-only property. |
| `AckRequired` | Boolean | R | type lib | — | — | — | Determines an automatic (False) or manual (True) acknowledgment of this Event. This is a read-only property. |
| `ConditionActive` | Boolean | R | type lib | — | — | — | Indicates whether the Alarm Source is in Alarm (True) or not (False). This is a read-only property. |
| `Enabled` | Boolean | R | type lib | — | — | — | Determines whether this Alarm's verification is enabled (True) or not (False). This is a read-only property. |
| `EventCLSID` | String | R | type lib | — | — | — | Unique identifier for this Event's lifespan. When a new Event occurs in a Source, a new EventCLSID is generated. Thus, this Event keeps this CLSID on the database, while it does not leave the list of active and not acknowledged Events. This is a read-only property. |
| `ActiveSource` | Long | R | type lib | — | — | — | Active Measurement Source of the Alarm Source at the moment of this Event. This is a read-only property. |
| `DomainName` | String | R | type lib | — | — | — | Returns the Domain name of this Event's Connection. This name corresponds to the Domain column on the list of available Connections on an E3Alarm's Connections tab. This is a read-only property. |
| `Unbound` | Boolean | R | type lib | — | — | — | Indicates whether this Event is not bound to an Alarm Source. This is a read-only property. |
| `Deleted` | Boolean | R | type lib | — | — | — | Indicates whether this Event was removed or not. This is a read-only property. |
| `AllowShelving` | Boolean | R | type lib | — | — | — | Indicates whether this Alarm or Event can be shelved or not. This is a read-only property. |
| `Shelved` | Boolean | R | type lib | — | — | — | Indicates whether this Alarm or Event was shelved or not. This is a read-only property. |
| `ShelvedTime` | Date | R | type lib | — | — | — | Stores the date and time of the moment this Alarm or Event is shelved. This is a read-only property. |
| `ShelvedOutTime` | Date | R | type lib | — | — | — | Stores the date and time of the moment this Alarm or Event is unshelved, or zero (12/30/1899) while this Alarm or Event has not been unshelved. This is a read-only property. |
| `ShelveDuration` | Long | R | type lib | — | — | — | Time, in minutes, this Alarm or Event remained shelved. This is a read-only property. |
| `ShelveMaxDuration` | Long | R | type lib | — | — | — | Maximum time, in minutes, this Alarm or Event can remain shelved. This is a read-only property. |
| `ShelveCount` | Long | R | type lib | — | — | — | Number of times this Alarm or Event was shelved. This is a read-only property. |
| `ShelveMaxCount` | Long | R | type lib | — | — | — | Maximum number of times this Alarm or Event can be shelved. This is a read-only property. |
| `ShelveActorID` | String | R | type lib | — | — | — | Name of the operator who shelved this Alarm or Event. This is a read-only property and its value can be the user logged on Elipse E3 Viewer, when shelving is performed on an E3Alarm, "No user" if there is no logged-on user, or "System" when shelving is automatic, that is, for Alarms or Events that a… |
| `ShelveReason` | String | R | type lib | — | — | — | Reason why this Alarm or Event was shelved. This is a read-only property. |
| `E3TimeStamp` | Date | R | type lib | — | — | — | Date and time this Event occurred. This is a read-only property. |
| `AlarmState` | EAlarmState | R | type lib | — | — | — | Indicates the current status of an Alarm. Possible values for this property are 1: Alarm left its alarm condition and was acknowledged, 2: Alarm active and needs acknowledgment, 3: Alarm in active condition and acknowledged, 4: Alarm in inactive condition and needs acknowledgment, 5: Alarm suppresse… |
| `ShelvedExpirationTime` | Date | R | type lib | — | — | — | Date and time this Alarm or Event is programmed to leave its shelving condition. This is a read-only property. |
| `OutOfService` | Boolean | R | type lib | — | — | — | Identifies whether an Alarm was suppressed using the Out-of-Service type. ⚠ type lib: somente leitura |
| `OutOfServiceTime` | Date | R | type lib | — | — | — | Stores the date an time in which an Alarm was suppressed using the Out-of-Service type. ⚠ type lib: somente leitura |
| `ReturnToServiceTime` | Date | R | type lib | — | — | — | Stores the date and time in which an Alarm suppressed using the Out-of-Service type returned to a normal operation. ⚠ type lib: somente leitura |
| `OutOfServiceReason` | String | R | type lib | — | — | — | Reason why an Alarm was suppressed using the Out-of-Service type by an operator. ⚠ type lib: somente leitura |
| `OutOfServiceActorID` | String | R | type lib | — | — | — | Operator that performed the suppression of an Alarm using the Out-of-Service type. ⚠ type lib: somente leitura |

<a id="e3sys-extarea"></a>
### ExtArea

- CLSID `{22E1B2FE-B979-476C-BE81-C21DD6265CC3}` · interface `IExtArea` · eventos `DContainerEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Extended Item with Alarm Area behavior control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Returns/sets the name of the object |
| `DocString` | String | RW | type lib | — | — | — | Returns/sets the object documentation string |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Application` | Object | R | type lib | — | — | — | Returns the current application object |
| `Count` | Int | R | type lib | — | — | — | Returns the number of children of object |
| `PathName` | String | R | type lib | — | — | — | Full object path name |
| `Links` | ILinks | R | type lib | — | — | — | Collection of object links |
| `ObjectEvents` | IEvents | R | type lib | — | — | — | Collection of object events |
| `PathVolume` | String | R | type lib | — | — | — | Full file name of the volume (.PRJ or .LIB) where this object is stored |
| `PathContainer` | String | R | type lib | — | — | — | Full name of the folder or unit that contains this object |
| `IsAlarmArea` | Boolean | RW | type lib | — | — | — | True if the object has Alarm Area behavior |
| `IsObjectActive` | Boolean | R | type lib | — | — | — | True if the object is activated |
| `AlarmVerify` | Boolean | RW | type lib | — | — | — | Enables/disables area alarm checking |
| `Alarm` | Boolean | R | type lib | — | — | — | Reports if this area has at least one active alarm |
| `ActiveAlarms` | Long | R | type lib | — | — | — | Total number of active alarms |
| `ActiveCritAlarms` | Long | R | type lib | — | — | — | Total number of critical severity active alarms |
| `ActiveHighAlarms` | Long | R | type lib | — | — | — | Total number of high severity active alarms |
| `ActiveMedAlarms` | Long | R | type lib | — | — | — | Total number of medium severity active alarms |
| `ActiveLowAlarms` | Long | R | type lib | — | — | — | Total number of low severity active alarms |
| `ActiveNACKAlarms` | Long | R | type lib | — | — | — | Total number of unacknowledged alarms (both active and inactive) |
| `ActiveCritNACKAlarms` | Long | R | type lib | — | — | — | Total number of critical severity unacknowledged alarms (both active and inactive) |
| `ActiveHighNACKAlarms` | Long | R | type lib | — | — | — | Total number of high severity unacknowledged alarms (both active and inactive) |
| `ActiveMedNACKAlarms` | Long | R | type lib | — | — | — | Total number of medium severity unacknowledged alarms (both active and inactive) |
| `ActiveLowNACKAlarms` | Long | R | type lib | — | — | — | Total number of low severity unacknowledged alarms (both active and inactive) |
| `InactiveNACKAlarms` | Long | R | type lib | — | — | — | Total number of inactive unacknowledged alarms |
| `InactiveCritNACKAlarms` | Long | R | type lib | — | — | — | Total number of critical severity inactive unacknowledged alarms |
| `InactiveHighNACKAlarms` | Long | R | type lib | — | — | — | Total number of high severity inactive unacknowledged alarms |
| `InactiveMedNACKAlarms` | Long | R | type lib | — | — | — | Total number of medium severity inactive unacknowledged alarms |
| `InactiveLowNACKAlarms` | Long | R | type lib | — | — | — | Total number of low severity inactive unacknowledged alarms |
| `UserFields` | IAlarmUserFieldsCollection | R | type lib | — | — | — | Retrieves the collection of user fields |
| `SuppressedAlarms` | Long | R | type lib | — | — | — | Total number of suppressed alarms |
| `ShelvedAlarms` | Long | R | type lib | — | — | — | Total number of shelved alarms |
| `SuppressedByDesignAlarms` | Long | R | type lib | — | — | — | Total number of suppressed by design alarms |
| `OutOfServiceAlarms` | Long | R | type lib | — | — | — | Total number of out of service alarms |

**Métodos:** `Item(ItemId Variant)`; `AddObject(ClassName String, Activate Boolean, ObjectName String)`; `DeleteObject(ChildName String)`; `Activate()`; `Deactivate()`; `GetChildObject(ObjectPath String)`; `Context(ContextName String)`; `RunEvent(EventName String, Arguments Array de Variant)`; `RunProcedure(ProcedureName String, Arguments Array de Variant)`

**Eventos:** `OnStartRunning()`; `OnStopRunning()`

<a id="e3sys-extcontrol"></a>
### ExtControl

- CLSID `{0CB75AF2-3320-11D4-8E8A-525400E657A3}` · interface `IExtControl` · eventos `DContainerEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Extended Control control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Returns/sets the name of the object |
| `DocString` | String | RW | type lib | — | — | — | Returns/sets the object documentation string |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Application` | Object | R | type lib | — | — | — | Returns the current application object |
| `Count` | Int | R | type lib | — | — | — | Returns the number of children of object |
| `PathName` | String | R | type lib | — | — | — | Full object path name |
| `Links` | ILinks | R | type lib | — | — | — | Collection of object links |
| `ObjectEvents` | IEvents | R | type lib | — | — | — | Collection of object events |
| `PathVolume` | String | R | type lib | — | — | — | Full file name of the volume (.PRJ or .LIB) where this object is stored |
| `PathContainer` | String | R | type lib | — | — | — | Full name of the folder or unit that contains this object |
| `IsAlarmArea` | Boolean | RW | type lib | — | — | — | True if the object has Alarm Area behavior |
| `IsObjectActive` | Boolean | R | type lib | — | — | — | True if the object is activated |
| `Tip` | String | RW | type lib | — | — | — | Returns/sets tip text of the object |
| `Angle` | Long | RW | type lib | — | — | — | Returns/sets the angle of object |
| `X` | Double | RW | type lib | — | — | — | Returns/sets the distance between the left edge of an object and the left edge of screen |
| `Y` | Double | RW | type lib | — | — | — | Returns/sets the distance between the top edge of an object and the top edge of screen |
| `Width` | Double | RW | type lib | — | — | — | Returns/sets the width of object |
| `Height` | Double | RW | type lib | — | — | — | Returns/sets the height of object |
| `Layer` | Long | RW | type lib | — | — | — | Returns/sets the layer of object |
| `Visible` | Boolean | RW | type lib | — | — | — | True if object is visible |
| `Enabled` | Boolean | RW | type lib | — | — | — | True if object is enabled |
| `TabStop` | Boolean | RW | type lib | — | — | — | Returns/sets the tabStop of object |
| `Screen` | Object | R | type lib | — | — | — | Returns the parent screen of object |
| `Frame` | Object | R | type lib | — | — | — | Returns the parent frame of object |
| `MouseOver` | Boolean | R | type lib | — | — | — | True if the mouse pointer is over the object |
| `MouseOverChild` | Boolean | R | type lib | — | — | — | True if the mouse pointer is over the object or a child |
| `HasFocus` | Boolean | R | type lib | — | — | — | True if the object has keyboard focus |
| `FlipHorizontal` | Boolean | RW | type lib | — | — | — | True if the object is flipped over the horizontal axis |
| `FlipVertical` | Boolean | RW | type lib | — | — | — | True if the object is flipped over the vertical axis |

**Métodos:** `Item(ItemId Variant)`; `AddObject(ClassName String, Activate Boolean, ObjectName String)`; `DeleteObject(ChildName String)`; `Activate()`; `Deactivate()`; `GetChildObject(ObjectPath String)`; `Context(ContextName String)`; `RunEvent(EventName String, Arguments Array de Variant)`; `RunProcedure(ProcedureName String, Arguments Array de Variant)`; `SetFocus()`; `BringToFront()`; `SendToBack()`; `FitObject(ScreenFillPercentage Long)`

**Eventos:** `OnStartRunning()`; `OnStopRunning()`

<a id="e3sys-extfile"></a>
### ExtFile

- CLSID `{2DB45AE1-3320-11D4-8E8A-525400E657A3}` · interface `IExtFile`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Extended File control

**Métodos:** `Save()`

<a id="e3sys-extitem"></a>
### ExtItem

- CLSID `{0CB75AE2-3320-11D4-8E8A-525400E657A3}` · interface `IExtItem` · eventos `DContainerEvents`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Extended Item control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Returns/sets the name of the object |
| `DocString` | String | RW | type lib | — | — | — | Returns/sets the object documentation string |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Application` | Object | R | type lib | — | — | — | Returns the current application object |
| `Count` | Int | R | type lib | — | — | — | Returns the number of children of object |
| `PathName` | String | R | type lib | — | — | — | Full object path name |
| `Links` | ILinks | R | type lib | — | — | — | Collection of object links |
| `ObjectEvents` | IEvents | R | type lib | — | — | — | Collection of object events |
| `PathVolume` | String | R | type lib | — | — | — | Full file name of the volume (.PRJ or .LIB) where this object is stored |
| `PathContainer` | String | R | type lib | — | — | — | Full name of the folder or unit that contains this object |
| `IsAlarmArea` | Boolean | RW | type lib | — | — | — | True if the object has Alarm Area behavior |
| `IsObjectActive` | Boolean | R | type lib | — | — | — | True if the object is activated |

**Métodos:** `Item(ItemId Variant)`; `AddObject(ClassName String, Activate Boolean, ObjectName String)`; `DeleteObject(ChildName String)`; `Activate()`; `Deactivate()`; `GetChildObject(ObjectPath String)`; `Context(ContextName String)`; `RunEvent(EventName String, Arguments Array de Variant)`; `RunProcedure(ProcedureName String, Arguments Array de Variant)`

**Eventos:** `OnStartRunning()`; `OnStopRunning()`

<a id="e3sys-groupnode"></a>
### GroupNode

- CLSID `{26ADEAB4-AED9-48DB-8F46-A3DB394A7958}` · interface `IGroupNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- GroupNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Type` | EUserGroupType | R | type lib | — | — | — | Type Indicates the type of a group. Possible values for this property are 0: Elipse E3 group or 1: Windows group. This is a read-only property. Access to this property is only allowed to users with permission to configure users and groups. For more information, please check topic Security - Users on… |

**Métodos:** `Item(ItemId Variant)`; `AddToGroup(GroupName String)`; `RemoveFromGroup(GroupName String)`

<a id="e3sys-groupsnode"></a>
### GroupsNode

- CLSID `{24876058-102C-41EB-BB18-852F5FF32F67}` · interface `IGroupsNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- GroupsNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`; `CreateGroup(Name String, Type EUserGroupType)`; `RemoveGroup(Name String)`; `GroupExists(Name String)`

<a id="e3sys-libfilenode"></a>
### LibFileNode

- CLSID `{1DB09F17-22D5-41CF-9D87-ACEA21EF334A}` · interface `ILibFileNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- LibFile Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `PathVolume` | String | R | type lib | — | — | — | PathVolume Full path of a library file. This is a read-only property. |
| `FileVersionMaj` | Long | R | type lib | — | — | — | FileVersionMaj Contains the major version number of a library file, available on the Version Report window of Elipse E3 Studio. This is a read-only property. |
| `FileVersionMin` | Long | R | type lib | — | — | — | FileVersionMin Contains the minor version number of a library file, available on the Version Report window of Elipse E3 Studio. This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-libfilesnode"></a>
### LibFilesNode

- CLSID `{FF098477-E60C-4F47-AD91-25327528252F}` · interface `ILibFilesNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- LibFiles Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-licensecounternode"></a>
### LicenseCounterNode

- CLSID `{22C98E45-7488-4DE8-8C69-7E7992D1D239}` · interface `ILicenseCounterNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- LicenseCounterNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `IsUnlimited` | Boolean | R | type lib | — | — | — | Indicates whether the current License Type is unlimited, that is, the value of the Limit property is not used. This is a read-only property. |
| `Limit` | Long | R | type lib | — | — | — | Indicates the limit of licenses for the current License Type or -1 (minus one) if the current License Type is unlimited. This is a read-only property. |
| `Used` | Long | R | type lib | — | — | — | Indicates the total number of licenses already consumed by the current License Type. This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-licensenode"></a>
### LicenseNode

- CLSID `{FF8CFAA0-D07D-45EB-B662-550EFBF37A5F}` · interface `ILicenseNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- LicenseNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `ID` | String | R | type lib | — | — | — | Returns the unique identifier of the protection device of the current license or an empty String if Elipse E3 is in Demonstration mode. This is a read-only property. |
| `IsDemo` | Boolean | R | type lib | — | — | — | Indicates whether the current license is in Demonstration mode, that is, no valid license was found. This is a read- only property. |
| `MaxRuntime` | Long | R | type lib | — | — | — | Indicates the maximum time allowed for executing a Domain, in minutes. This is a read-only property. |
| `ExpireDate` | Date | R | type lib | — | — | — | Indicates the expiration date of the current license or 0 (zero) if the current license does not have an expiration date. This is a read-only property. |
| `DeviceType` | Long | R | type lib | — | — | — | Indicates the type of device of the current license. Possible values for this property are 0: Not found, 1: HASP, 2: TimeHasp, or 3: Softkey. This is a read-only property. |
| `VersionRange` | String | R | type lib | — | — | — | Indicates the range of versions allowed for the current license, such as "4.7-5.0", that is, the current license can be used between versions 4.7 and 5.0. This is a read-only property. |
| `DbAvailable` | Boolean | R | type lib | — | — | — | Indicates whether the current license allows using the Database feature. This is a read-only property. |
| `ReportsAvailable` | Boolean | R | type lib | — | — | — | Indicates whether the current license allows using the Section Report feature. This is a read-only property. |
| `OpcClientAvailable` | Boolean | R | type lib | — | — | — | Indicates whether the current license allows using an OPC DA Client. This is a read-only property. |
| `UaClientAvailable` | Boolean | R | type lib | — | — | — | Indicates whether the current license allows using an OPC UA Client. This is a read-only property. Server Objects 369 |
| `TrendAnalysisAvailable` | Boolean | R | type lib | — | — | — | Indicates whether the current license allows using the TrendAnalysis feature. This is a read-only property. |
| `ErrorMessage` | String | R | type lib | — | — | — | Returns the error message related to the current license or an empty String if there is no error message, which is the default value. This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-lineprinter"></a>
### LinePrinter

- CLSID `{8383B867-3655-4F21-B00B-7C9A83889A13}` · interface `ILinePrinter`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- LinePrinter control

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `PrinterName` | String | RW | type lib | — | — | an empty String, that is, the Line Printer objec… | Name of the printer used by the Line Printer object. The default value of this property is an empty String, that is, the Line Printer object uses Windows default printer. NOTES If this property is configured with an empty String and the UseDefaultPrinter property is configured as False, printing is … |
| `UseDefaultPrinter` | Boolean | RW | type lib | — | — | True | Configures the Line Printer object to use Windows default printer. The default value of this property is True. NOTES If this property is configured as False and the PrinterName property is configured with an empty String, users cannot print and the PrinterStatus property returns the value 0 (zero, p… |
| `PrinterStatus` | PrinterStatus | R | type lib | — | — | — | Indicates the status of the printer selected for the Line Printer object. This is a read-only property. Possible values for this property are 0 - psUnknown: Unknown status (default), 1 - psOffline: Printer is not available, 2 - psError: An error occurred during the printing, or 3 - psReady: Printer … |
| `MaxPendingLines` | Long | RW | type lib | — | — | 1000 | Maximum number of lines pending for printing. If the printer queue reaches this value and more lines are sent, by using the Write method, a script error is generated and the line sent is discarded. The default value of this property is 1000. |

**Métodos:** `Write(Val String)`

<a id="e3sys-links"></a>
### Links

- CLSID `{221C08C0-0438-4CED-9F25-12FEBC822D1E}` · interface `ILinks`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Link collection object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Count` | Int | R | type lib | — | — | — | The count of links |

**Métodos:** `Item(ItemId Variant)`; `CreateLink(Property String, Source String, BindType BindStyle)`; `RemoveLink(Property String)`

<a id="e3sys-localservernode"></a>
### LocalServerNode

- CLSID `{666D562D-879A-4B6B-A472-B90C87CFDD7C}` · interface `ILocalServerNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- LocalServerNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Disabled` | Boolean | RW | type lib | — | — | — | True if this server is in maintenance mode |
| `ServerName` | String | R | type lib | — | — | — | Returns the server alias in the Domain configuration |
| `NetworkAddress` | String | R | type lib | — | — | — | Returns the server network address (name) |
| `FailuresWeight` | Long | R | type lib | — | — | — | Returns the total numeric weight of server active failures |
| `State` | EDomainState | R | type lib | — | — | — | Returns the server state for this server |
| `IsCandidate` | Boolean | R | type lib | — | — | — | Returns True if this server is ready to run the Domain |
| `IsIoActive` | Boolean | R | type lib | — | — | — | Returns True if this server has I/O Drivers running |
| `IsPrioritySet` | Boolean | R | type lib | — | — | — | Returns True is this server was set to run the Domain |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-measurementcolors"></a>
### MeasurementColors

- CLSID `{02980B02-3425-45E6-8974-0F09E24E4B95}` · interface `IMeasurementColors`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- MeasurementColors

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ColorNormal` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets the color used to display good quality values |
| `ColorBad` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets the color used to display bad quality values |
| `ColorAlarm` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets the color used to display values in alarm |
| `ColorNAck` | ECO_COLOR | RW | type lib | — | — | — | Returns/sets the color used to display unacknowledged alarm values |
| `BlinkNormal` | Boolean | RW | type lib | — | — | — | Returns/sets whether the normal color blinks |
| `BlinkBad` | Boolean | RW | type lib | — | — | — | Returns/sets whether the bad color blinks |
| `BlinkAlarm` | Boolean | RW | type lib | — | — | — | Returns/sets whether the alarm color blinks |
| `BlinkNAck` | Boolean | RW | type lib | — | — | — | Returns/sets whether the unacknowledged alarm color blinks |

<a id="e3sys-multisourcebind"></a>
### MultiSourceBind

- CLSID `{BBD1846B-3265-4E0A-8F20-82A8992E4580}` · interface `IMultiSourceBind`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 13 instâncias em 2 arquivo(s)
- MultiSourceBind Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Source` | String | RW | type lib | Source | nomeada | — | Returns/sets link source |
| `Property` | String | RW | type lib | — | não gravada nomeada | — | Returns/sets the property name it is linked to |
| `Type` | BindStyle | R | type lib | — | não gravada nomeada | — | Returns link type |
| `Count` | Int | R | type lib | Count | nomeada | — | Count This property returns the number of Rows on the Multisource Links table. This is a read-only property. |
| `AdviseAll` | Boolean | RW | type lib | AdviseAll | nomeada | True | AdviseAll This property keeps all Links on the Multisource Links table in Advise (active) mode. The default value of this property is True. For applications created in previous versions, this property is set to False, for compatibility reasons. |
| `Max#` | Double |  | gravada no .prj | Max# | nomeada | — | sem equivalente na type lib (família: 4) |
| `Min#` | Double |  | gravada no .prj | Min# | nomeada | — | sem equivalente na type lib (família: 4) |
| `OnProperty` | String |  | gravada no .prj | OnProperty | nomeada | — | sem equivalente na type lib |
| `Source#` | String |  | gravada no .prj | Source# | nomeada | — | sem equivalente na type lib (família: 4) |

**Métodos:** `InsertRow(InsertAtRow Int)`; `RemoveRow(Row Int)`; `Item(ItemId Variant)`

<a id="e3sys-multisourcerow"></a>
### MultiSourceRow

- CLSID `{EEF93D78-70C4-4FFF-B85E-87984A446770}` · interface `IMultiSourceRow`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- MultiSourceRow Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Min` | Double | RW | type lib | — | — | — | Min This property specifies the minimum interval for a Link value indicated by the Source property. |
| `Max` | Double | RW | type lib | — | — | — | Max This property specifies the maximum interval for a Link value indicated by the Source property. |
| `Source` | String | RW | type lib | — | — | — | Source This property specifies a Multisource Link Row's source, which can be the name of another application object or a more complex expression accessing several objects. |

<a id="e3sys-pkgfilenode"></a>
### PkgFileNode

- CLSID `{763429C9-9EFF-407F-A524-228136766691}` · interface `IPkgFileNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- PkgFile Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `PathVolume` | String | R | type lib | — | — | — | PathVolume Full path of a library package file. This is a read-only property. |
| `FileVersionMaj` | Long | R | type lib | — | — | — | FileVersionMaj Contains the major version number of a library package file, available on the Version Report window of Elipse E3 Studio. This is a read-only property. |
| `FileVersionMin` | Long | R | type lib | — | — | — | FileVersionMin Contains the minor version number of a library package file, available on the Version Report window of Elipse E3 Studio. This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-pkgfilesnode"></a>
### PkgFilesNode

- CLSID `{DE7E054E-B990-4CAA-8EC2-DB9804859428}` · interface `IPkgFilesNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- PkgFiles Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-prjfilenode"></a>
### PrjFileNode

- CLSID `{D45C0C0B-FE73-4CC2-AFE8-21D8904C29B3}` · interface `IPrjFileNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- PrjFile Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `PathVolume` | String | R | type lib | — | — | — | PathVolume Full path of a project file. This is a read-only property. 366 Server Objects |
| `FileVersionMaj` | Long | R | type lib | — | — | — | FileVersionMaj Contains the major version number of a project file, available on the Version Report window of Elipse E3 Studio. This property returns -1 (minus one) if a project file is disabled or 0 (zero) if there is an error loading a project file. This is a read-only property. |
| `FileVersionMin` | Long | R | type lib | — | — | — | FileVersionMin Contains the minor version number of a project file, available on the Version Report window of Elipse E3 Studio. This is a read-only property. |
| `Enabled` | Boolean | RW | type lib | — | — | — | Enabled Allows enabling or disabling a project file. |
| `DocString` | String | R | type lib | — | — | — | DocString Returns the DocString property of a project file. This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-prjfilesnode"></a>
### PrjFilesNode

- CLSID `{44987E3F-5253-48B9-AC2F-68DC649CB801}` · interface `IPrjFilesNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- PrjFiles Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-project"></a>
### Project

- CLSID `{9F8A633D-2FD2-4984-A677-6EEB72BE1D93}` · interface `IProject`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- E3 Project Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `DocString` | String | RW | type lib | — | — | — | Project documentation string |

<a id="e3sys-remotedomainnode"></a>
### RemoteDomainNode

- CLSID `{BBB8768E-C2FA-4C0A-8AF4-D7FA5C921EA1}` · interface `IRemoteDomainNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- RemoteDomainNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Connected` | Boolean | R | type lib | — | — | — | Connected Indicates whether there is an established connection at the moment with any remote server, primary or secondary. ⚠ type lib: somente leitura |
| `DomainFile` | String | R | type lib | — | — | — | DomainFile Indicates the name of the Domain file configured for a remote Domain. ⚠ type lib: somente leitura |
| `ServerAddress` | String | R | type lib | — | — | — | ServerAddress Indicates the address of the main remote server for a remote Domain or an empty String if the main server is disabled. ⚠ type lib: somente leitura |
| `BackupAddress` | String | R | type lib | — | — | — | BackupAddress Indicates the address of the secondary remote server for a remote Domain or an empty String if the secondary remote server is disabled. ⚠ type lib: somente leitura |
| `LastError` | String | R | type lib | — | — | — | LastError Diagnostic message about the reason for a connection failure with the main server or an empty String if there is an active connection. ⚠ type lib: somente leitura |
| `LastErrorBackup` | String | R | type lib | — | — | — | LastErrorBackup Diagnostic message about the reason for a connection failure with the secondary server or an empty String if there is an active connection. 368 Server Objects ⚠ type lib: somente leitura |
| `ActiveServer` | String | R | type lib | — | — | — | ActiveServer Indicates the name of the remote server with an active connection, if the connection is established, or an empty String if the remote server is not connected. ⚠ type lib: somente leitura |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-remotedomainserversnode"></a>
### RemoteDomainServersNode

- CLSID `{99A7F1A2-85F3-42D7-A813-68C71EBFCB69}` · interface `IRemoteDomainServersNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- RemoteDomainServersNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-remotedomainsessionnode"></a>
### RemoteDomainSessionNode

- CLSID `{FFB036CD-5107-4E4C-A12B-113BE75B1843}` · interface `ISessionNodeBase2`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- RemoteDomainSessionNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Machine` | String | R | type lib | — | — | — | Returns the client machine name |
| `Address` | String | R | type lib | — | — | — | Returns the IPv4 address of the client |
| `User` | String | R | type lib | — | — | — | Returns the login name of current user |
| `Version` | String | R | type lib | — | — | — | Returns the product version on the client machine |
| `StartTime` | Date | R | type lib | — | — | — | Returns the start-time of current session |
| `ReadOnly` | Boolean | R | type lib | — | — | — | Returns TRUE if the session is currently in read-only mode |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-remotedomainsnode"></a>
### RemoteDomainsNode

- CLSID `{445FB738-6604-4F17-B0F0-CC57ACF07AE1}` · interface `IRemoteDomainsNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- RemoteDomainsNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-remoteservernode"></a>
### RemoteServerNode

- CLSID `{BBE549D5-DFB5-412C-8328-6E7DA4E8954B}` · interface `IRemoteServerNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- RemoteServerNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Disabled` | Boolean | RW | type lib | — | — | — | True if this server is in maintenance mode |
| `ServerName` | String | R | type lib | — | — | — | Returns the server alias in the Domain configuration |
| `NetworkAddress` | String | R | type lib | — | — | — | Returns the server network address (name) |
| `FailuresWeight` | Long | R | type lib | — | — | — | Returns the total numeric weight of server active failures |
| `State` | EDomainState | R | type lib | — | — | — | Returns the server state for this server |
| `IsCandidate` | Boolean | R | type lib | — | — | — | Returns True if this server is ready to run the Domain |
| `IsIoActive` | Boolean | R | type lib | — | — | — | Returns True if this server has I/O Drivers running |
| `IsPrioritySet` | Boolean | R | type lib | — | — | — | Returns True is this server was set to run the Domain |
| `DomainState` | EDomainState | R | type lib | — | — | — | Returns the Domain state for this Server |
| `Ping` | Boolean | R | type lib | — | — | — | Returns True if Ping is succeeding for this Server |
| `Online` | Boolean | R | type lib | — | — | — | Returns True if there is a connection to this Server |
| `Connection` | String | R | type lib | — | — | — | Returns the current connection status |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-runtimefolder"></a>
### RuntimeFolder

- CLSID `{AAAD84E8-05F0-46CF-BB64-78FB37174BEA}` · interface `IRuntimeFolder`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- Runtime folder object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns the name of the folder |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the folder |
| `Application` | Object | R | type lib | — | — | — | Returns the current Application object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of server children of folder |
| `PathName` | String | R | type lib | — | — | — | Full folder path name |

**Métodos:** `Item(ItemId Variant)`; `Save()`

<a id="e3sys-securitynode"></a>
### SecurityNode

- CLSID `{8495B150-3999-42D6-8899-270C81CA8222}` · interface `ISecurityNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- SecurityNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-serverapplicatione3"></a>
### ServerApplicationE3

- CLSID `{268610B1-2966-47C2-879A-C5BB6C914F22}` · interface `IServerApplicationE3`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- ServerApplicationE3 Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `ProductVersionMajor` | Long | R | type lib | — | — | — | This property returns the major number of the installed version of a Server. For example, if the installed version is 6.9.312, this property returns the value 6. This is a read-only property. |
| `ProductVersionMinor` | Long | R | type lib | — | — | — | This method returns the minor number of the installed version of a Server. For example, if the installed version is 6.9.312, this property returns the value 9. This is a read-only property. |
| `ProductVersionBuild` | Long | R | type lib | — | — | — | This property returns the build number of the installed version of a Server. For example, if the installed version is 6.9.312, this property returns the value 312. This is a read-only property. |
| `ProductString` | String | R | type lib | — | — | — | This property returns a String containing the product's name and the installed version of a Server, such as "Elipse E3 6.9.312" or "Elipse E3 (64-bits) 6.9.312". This is a read-only property. |
| `Name` | String | R | type lib | — | — | — | Returns the name of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of the server |

**Métodos:** `GetObject(ObjectPath String)`; `Trace(MessageText String, LogTimeStamp Boolean, BreakLine Boolean)`; `ReportFailure(FailureName String, FailureDescription String, FailureWeight Long)`; `ClearFailure(FailureName String)`; `AckFailure(FailureName String)`; `TrackEvent(EventMessage String, EventComment String, EventTimestamp Date)`; `LoadReport(ReportName String)`; `Item(ItemId Variant)`; `Save()`; `E3GetActor()`; `IsUserMemberOfGroup(GroupName String, UserName String)`

<a id="e3sys-servernode"></a>
### ServerNode

- CLSID `{33B005EB-4308-4FF3-83E3-EA90A985D16A}` · interface `IServerNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- ServerNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `ProductString` | String | R | type lib | — | — | — | Returns a server's product name and version, such as "Elipse E3 6.9.312". This is a read-only property. |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-serversnode"></a>
### ServersNode

- CLSID `{3342150E-DB36-40FD-A289-596836E84F57}` · interface `IServersNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- ServersNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-studiosessionnode"></a>
### StudioSessionNode

- CLSID `{77DC92FF-5ED6-4F5E-98C0-61891C444A80}` · interface `ISessionNodeBase`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- StudioSessionNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Machine` | String | R | type lib | — | — | — | Returns the client machine name |
| `Address` | String | R | type lib | — | — | — | Returns the IPv4 address of the client |
| `User` | String | R | type lib | — | — | — | Returns the login name of current user |
| `Version` | String | R | type lib | — | — | — | Returns the product version on the client machine |
| `StartTime` | Date | R | type lib | — | — | — | Returns the start-time of current session |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-studiosnode"></a>
### StudiosNode

- CLSID `{EEB35132-94FF-40F8-BCD4-F692016B3F01}` · interface `IStudiosNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- StudiosNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-tablebind"></a>
### TableBind

- CLSID `{B9A88108-6301-4BC4-9DE2-B4462B4C3CCE}` · interface `ITableBind`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: 99225 instâncias em 33 arquivo(s)
- TableBind Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Source` | String | RW | type lib | Source | nomeada | — | Returns/sets link source |
| `Property` | String | RW | type lib | — | não gravada nomeada | — | Returns/sets the property name it is linked to |
| `Type` | BindStyle | R | type lib | — | não gravada nomeada | — | Returns link type |
| `Count` | Int | R | type lib | Count | nomeada | — | Count This property informs the number of rows on the Table Links table. This is a read-only property. |
| `blink#` | ULong |  | gravada no .prj | blink# | nomeada | — | sem equivalente na type lib (família: 14) |
| `blinkValue#` | Integer, Long, Double, String |  | gravada no .prj | blinkValue# | nomeada | — | sem equivalente na type lib (família: 14) |
| `max#` | Double |  | gravada no .prj | max# | nomeada | — | sem equivalente na type lib (família: 14) |
| `min#` | Double |  | gravada no .prj | min# | nomeada | — | sem equivalente na type lib (família: 14) |
| `OnProperty` | String |  | gravada no .prj | OnProperty | nomeada | — | sem equivalente na type lib |
| `value#` | Integer, Long, Double, String, Boolean |  | gravada no .prj | value# | nomeada | — | sem equivalente na type lib (família: 14) |

**Métodos:** `InsertRow(InsertAtRow Int)`; `RemoveRow(Row Int)`; `Item(ItemId Variant)`

<a id="e3sys-tablebindrow"></a>
### TableBindRow

- CLSID `{09EEDAD8-111F-4A07-A68D-D9EC4A4E9E8A}` · interface `ITableBindRow`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- TableBindRow Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Min` | Double | RW | type lib | — | — | — | Min This property specifies the lowest source value for a Table Row. The next example applies to the Max property and to this property. Sub CommandButton1_Click() Set Bind = _ Screen.Item("Rectangle1").Links.Item("ForegroundColor") Set Line1 = Bind.Item(1) Line1.Min = 0 Line1.Max = 20 Set Line2 = Bi… |
| `Max` | Double | RW | type lib | — | — | — | Max This property specifies the highest source value for a Table Row. |
| `Value` | Variant | RW | type lib | — | — | — | Value This property specifies the value the property assumes when the source is within the specified Row's interval. The next script contains an example of using this property. Sub CommandButton1_Click() Dim Color ' Picks a color Application.ShowPickColor Color, 0, 100, 100 Screen.Item("Rectangle1")… |
| `Blink` | Boolean | RW | type lib | — | — | — | Blink This property determines that when the source is within this Row's interval, the property alternates periodically between values established in the Value and BlinkValue properties. The next script contains an example of using this property. Sub CheckBox1_Click() Screen.Item("Rectangle1").Links… |
| `BlinkValue` | Variant | RW | type lib | — | — | — | BlinkValue This property specifies an alternative (blinking) value the property assumes when source is within the specified Row's interval and the Blink property is set to True. The next script contains an example of using this property. Sub CommandButton1_Click() Dim Color ' Picks a color Applicati… |

<a id="e3sys-userevent"></a>
### UserEvent

- CLSID `{CC25A2CB-18FF-432B-B121-3524FE19A22A}` · interface `IUserEvent`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- User Event object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | RW | type lib | — | — | — | Returns/sets the name of the event |
| `Link` | String | RW | type lib | — | — | an empty String | Text with the expression evaluated in a User Event. The default value of this property is an empty String. |
| `Type` | EUserEventType | RW | type lib | — | — | — | Indicates a type of User Event. Possible values for this property are 0 - uetOnEvent: this User Event triggers whenever the value of the expression changes from False to True (default), 1 - uetWhileTrue: this User Event triggers periodically while the value of the expression is equal to True, or 2 -… |
| `ScanTime` | ULong | RW | type lib | — | — | 1000, or one second | Time, in milliseconds, referring to the repetition period of this User Event. This property only applies to User Events whose Type property is equal to 1 (one, uetWhileTrue). The default value of this property is 1000, or one second. |
| `ChangeOnDisconnect` | Boolean | RW | type lib | — | — | False | Indicates whether a disconnection is handled as a change in the value of the expression indicated in the Link property. This property only applies to User Events whose Type property is equal to 2 (two, uetOnValueChanged). The default value of this property is False. |

**Métodos:** `AddScript(bstrCode String)`; `RemoveAll()`

<a id="e3sys-usernode"></a>
### UserNode

- CLSID `{26DBC379-C8FC-4B76-B73B-B21217BBEE77}` · interface `IUserNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- UserNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Type` | EUserGroupType | R | type lib | — | — | — | Type Returns the authentication type of a user. Possible values for this property are 0: Elipse E3 user or 1: Windows user. This is a read-only property. |
| `FullName` | String | RW | type lib | — | — | — | FullName Returns or configures the full name of a user. Access to this property is only allowed to users with permission to configure users and groups. If the user is an administrator, writing access to this property is only allowed to administrators. For more information, please check topic Securit… |
| `Password` | String | W | type lib | — | — | — | Password Configures the password of a user. This is a write-only property. Access to this property is only allowed to users with permission to configure users and groups. If the user is an administrator, writing access to this property is only allowed to administrators. For more information, please … |
| `IsAdministrator` | Boolean | RW | type lib | — | — | — | IsAdministrator Returns or configures whether a user is an administrator. Access to this property is only allowed to users with permission to configure users and groups. Writing access to this property is only allowed to administrators. For more information, please check topic Security - Users on El… |

**Métodos:** `Item(ItemId Variant)`; `AddToGroup(GroupName String)`; `RemoveFromGroup(GroupName String)`

<a id="e3sys-usersnode"></a>
### UsersNode

- CLSID `{7B296332-130D-416C-AB5F-B70A0912045E}` · interface `IUsersNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- UsersNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`; `CreateUser(Name String, Type EUserGroupType, IsAdmin Boolean, FullName String, Password String)`; `RemoveUser(Name String)`; `UserExists(Name String)`

<a id="e3sys-viewersessionnode"></a>
### ViewerSessionNode

- CLSID `{DDBA2E86-81B8-4766-9AA7-144CCE1CFDCF}` · interface `ISessionNodeBase2`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- ViewerSessionNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |
| `Machine` | String | R | type lib | — | — | — | Returns the client machine name |
| `Address` | String | R | type lib | — | — | — | Returns the IPv4 address of the client |
| `User` | String | R | type lib | — | — | — | Returns the login name of current user |
| `Version` | String | R | type lib | — | — | — | Returns the product version on the client machine |
| `StartTime` | Date | R | type lib | — | — | — | Returns the start-time of current session |
| `ReadOnly` | Boolean | R | type lib | — | — | — | Returns TRUE if the session is currently in read-only mode |

**Métodos:** `Item(ItemId Variant)`

<a id="e3sys-viewersnode"></a>
### ViewersNode

- CLSID `{22D71E27-1818-4AF8-BE6C-44C8E3446F5F}` · interface `IViewersNode`
- Objeto de tela (gráfico): **não** · usada nos projetos/libs: não observada
- ViewersNode Object

| Propriedade | Tipo | Acesso | Origem | Nome no .prj | Persistência | Padrão (manual) | Descrição |
|---|---|:--:|---|---|---|---|---|
| `Name` | String | R | type lib | — | — | — | Returns/sets the name of the object |
| `Parent` | Object | R | type lib | — | — | — | Returns the parent of the object |
| `Count` | Long | R | type lib | — | — | — | Returns the number of children of object |

**Métodos:** `Item(ItemId Variant)`

### Enumerações de E3Sys

- **AlarmConnectionStatus**: eNotConnected=0, eConnected=1, eEFilterNotConfigured=2, eEServerNotConfigured=3, eEUnexpected=4, eUnknownStatus=5
- **AlarmFilterType**: OnlyAlarms=1, OnlyEvents=2, AlarmsAndEvents=3
- **BindStyle**: bsSimple=0, bsSimpleBiDir=1, bsAnalog=2, bsAnimation=3, bsTable=4, bsReverse=5, bsMultiSource=6
- **DBSourceType**: stUnknown=-1, stAccess=0, stOracle=1, stSqlServer=2, stPostgreSQL=3, stMySQL=4
- **E3QueryType**: qtUndefined=-1, qtDBServer=0, qtStorage=1, qtOpcUa=2
- **EAckOnClick**: ACKNONE=0, ACKCLICK=1, ACKDBCLK=2
- **EAlarmSeverity**: asCritical=-2, asInvalid=-1, asHigh=0, asMedium=1, asLow=2
- **EAlarmState**: stNormal=1, stUnacked=2, stAcked=3, stNormalUnacked=4, stShelved=5, stSuppressedByDesign=6, stOutOfService=7, stNoAckRequired=8, stEvent=9, stTrack=10
- **EDomainState**: stClosed=-1, stStopped=0, stStandBy=1, stRunning=2
- **EExposeToOpc**: eeUseParentConfig=0, eeExpose=1, eeExposeAsReadOnly=2, eeDontExpose=3
- **EFieldID**: AF_NONE=0, AF_ACKREQUIRED=1, AF_ACKED=2, AF_ACTORID=3, AF_CHANGEMASK=4, AF_CONDITIONNAME=5, AF_CONDITIONACTIVE=6, AF_COOKIE=7, AF_ENABLED=8, AF_EVENTCATEGORY=9, AF_EVENTTYPE=10, AF_MESSAGE=11, AF_QUALITY=12, AF_SEVERITY=13, AF_SOURCE=14, AF_SUBCONDITIONNAME=15, AF_EVENTTIME=16, AF_EVENTTIMEUTC=17, AF_CV=18, AF_AREA=19, AF_ALARMSOURCENAME=20, AF_INTIME=21, AF_OUTTIME=22, AF_ACKTIME=23, AF_FULLSOURCENAME=24, AF_FORMATTEDVALUE=25, AF_ACTIVESOURCE=26, AF_DOMAINNAME=27, AF_UNBOUND=28, AF_DELETED=29, AF_ALLOWSHELVING=30, AF_SHELVED=31, AF_SHELVEDTIME=32, AF_SHELVEDOUTTIME=33, AF_SHELVEDURATION=34, AF_SHELVEMAXDURATION=35, AF_SHELVECOUNT=36, AF_SHELVEMAXCOUNT=37, AF_SHELVEREASON=38, AF_SHELVEACTORID=39, AF_E3TIMESTAMP=40, AF_SUPPRESSED=41, AF_SUPPRESSEDTIME=42, AF_ALARMSTATE=43, AF_SHELVEDEXPIRATIONTIME=44, AF_OUTOFSERVICE=45, AF_OUTOFSERVICETIME=46, AF_RETURNTOSERVICETIME=47, AF_OUTOFSERVICEREASON=48, AF_OUTOFSERVICEACTORID=49, AF_USERFIELDFIRST=1000
- **enumCursorLocation**: clServer=0, clClient=1, clCached=2
- **enumCursorType**: ctKeyset=0, ctStatic=1, ctDynamic=2
- **EUserEventType**: uetOnEvent=0, uetWhileTrue=1, uetOnValueChanged=2
- **EUserFieldValueSource**: evsInherited=0, evsLink=1, evsForcedValue=2
- **EUserGroupType**: eugtE3=0, eugtWindows=1
- **FunctionSubType**: fsNoSubType=-1, fsPreviousArchivedValue=0, fsInterpolatedArchivedValue=1, fsNextArchivedValue=2, fsExactArchivedValue=3, fsTagAttributeDescription=0, fsTagAttributeSource=1, fsTagAttributeType=2, fsTagAttributeEU=3, fsTagAttributeLowEng=4, fsTagAttributeHiEng=5, fsTagAttributeDeadBand=6, fsTagAttributeDeadBandUnit=7, fsTagAttributeMinRecTime=8, fsTagAttributeMaxRecTime=9, fsTagAttributeSize=10, fsTagAttributeVARTYPE=11, fsTagAttributeScanTime=12, fsTotalCalculatedData=0, fsMinimumCalculatedData=1, fsMaximumCalculatedData=2, fsStandardCalculatedData=3, fsRangeCalculatedData=4, fsAverageCalculatedData=5, fsMeanCalculatedData=6
- **FunctionType**: ftNoFunction=-1, ftLastValue=0, ftArchivedValue=1, ftTagAttribute=2, ftCompressedDataNValues=3, ftCompressedDataStartEndTime=4, ftSampledData=5, ftCalculatedData=6
- **PowerSourceType**: stNone=-1, stActiveSource=0, stScada=1, stOperator=2, stCCLink=3, stBilling=4, stCalculated=5, stDatabase=6, stTopologyProcessor=100, stPowerFlow=101, stStateEstimator=102, stLoadShedding=103, stDistLoadModelling=104, stSelfHealing=105, stExternalReader=106
- **PrinterStatus**: psUnknown=0, psOffline=1, psError=2, psReady=3
- **SqlNetworkLibrary**: nlDefault=0, nlNamedPipes=1, nlTcpIp=2, nlSpxIpx=3, nlBanyanVines=4, nlMultiProtocol=5
- **SqlProvider**: SQLOLEDB=1, MSOLEDBSQL=2
- **UaNodeIdType**: nitNumeric=0, nitString=1, nitGUID=2, nitOpaque=3
- **UaQueryType**: uqtRaw=0, uqtProcessed=1
- **WaterSourceType**: wstNone=-1, wstActiveSource=0, wstScada=1, wstOperator=2, wstCCLink=3, wstBilling=4, wstCalculated=5, wstDatabase=6, wstTopologyProcessor=100, wstExternalReader=106
