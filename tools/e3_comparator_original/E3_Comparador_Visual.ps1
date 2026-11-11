<#
.SYNOPSIS
  Retorno visual (protótipo) do comparador de projetos Elipse E3: abas Adicionado / Removido / Modificado.

.DESCRIPTION
  Exibe os resultados gerados por comparar.py (logs\comparacao_*.json) e permite disparar novas comparações.
  Nada é gravado nos .prj.

    -Modo Gui      (padrão) janela Windows Forms
    -Modo Console  resumo em texto

.EXAMPLE
  .\E3_Comparador_Visual.ps1
  .\E3_Comparador_Visual.ps1 -Modo Console
#>
[CmdletBinding()]
param(
    [ValidateSet('Gui', 'Console')][string]$Modo = 'Gui',
    [string]$PastaLogs,
    [switch]$SelfTest,
    [string]$Screenshot,
    [string[]]$TesteAB,
    [string[]]$TesteLote,
    [string]$TesteExt = 'prj'
)
$ErrorActionPreference = 'Stop'
$Script:Raiz = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $PastaLogs) { $PastaLogs = Join-Path $Script:Raiz 'logs' }
Add-Type -AssemblyName System.Web.Extensions
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

function Read-Json([string]$Caminho) {
    $ser = New-Object System.Web.Script.Serialization.JavaScriptSerializer
    $ser.MaxJsonLength = [int]::MaxValue; $ser.RecursionLimit = 200
    return $ser.DeserializeObject([System.IO.File]::ReadAllText($Caminho, [System.Text.Encoding]::UTF8))
}

function Get-Resultados([string]$Pasta) {
    # último .json de comparação de cada projeto (pelo caminho do projeto novo)
    $mapa = @{}
    if (Test-Path $Pasta) {
        Get-ChildItem -Path $Pasta -Filter 'comparacao_*.json' -File | Sort-Object LastWriteTime | ForEach-Object {
            try { $r = Read-Json $_.FullName; if ($r.ContainsKey('tabelas')) { $mapa[$r['meta']['novo']] = @{ Arquivo = $_.FullName; Dados = $r } } } catch { }
        }
    }
    return $mapa
}

function Get-Python {
    foreach ($c in 'py', 'python', 'python3') {
        $cmd = Get-Command $c -ErrorAction SilentlyContinue
        if ($cmd) { if ($c -eq 'py') { return @($cmd.Source, '-3') } else { return @($cmd.Source) } }
    }
    throw 'Python não encontrado no PATH.'
}

$ColsAdd = @('Projeto', 'Tipo de nó', 'Nó', 'Objeto', 'Classe', 'Observação')
$ColsMod = @('Projeto', 'Tipo de nó', 'Nó', 'Objeto', 'Classe', 'Tipo de alteração', 'Propriedade', 'De', 'Para', 'Detalhe')

function New-Tabela($colunas, $linhas, $projeto) {
    $t = New-Object System.Data.DataTable
    foreach ($c in $colunas) { [void]$t.Columns.Add($c, [string]) }
    foreach ($l in $linhas) {
        if ($projeto -and $l[0] -ne $projeto) { continue }
        $v = New-Object 'object[]' $colunas.Count
        for ($i = 0; $i -lt $colunas.Count; $i++) { $v[$i] = if ($i -lt $l.Count -and $null -ne $l[$i]) { [string]$l[$i] } else { '' } }
        [void]$t.Rows.Add($v)
    }
    return , $t
}

# ------------------------------------------------------------------------------------ console
function Show-Console($mapa) {
    Write-Host ''
    Write-Host '=== COMPARAÇÃO DE PROJETOS E3 ===' -ForegroundColor Cyan
    if ($mapa.Count -eq 0) { Write-Host "Nenhum resultado em $PastaLogs (rode comparar.py)." -ForegroundColor DarkYellow; return }
    Write-Host ('{0,-18} {1,8} {2,8} {3,8} {4,10}' -f 'Projeto', 'Adicion.', 'Removid.', 'Modific.', 'Itens alt.') -ForegroundColor Yellow
    foreach ($k in ($mapa.Keys | Sort-Object)) {
        $r = $mapa[$k].Dados; $t = $r['tabelas']
        Write-Host ('{0,-18} {1,8} {2,8} {3,8} {4,10}' -f (Split-Path $k -Leaf), $t['adicionado'].Count, $t['removido'].Count, $t['modificado'].Count, $r['resumo']['itens_alterados'])
    }
    $k = ($mapa.Keys | Sort-Object | Select-Object -First 1); $r = $mapa[$k].Dados
    Write-Host ''; Write-Host ("Exemplo - {0}: horário da análise {1} -> {2}" -f (Split-Path $k -Leaf), $r['meta']['analise_inicio'], $r['meta']['analise_fim'])
    $r['tabelas']['modificado'] | Select-Object -First 12 | ForEach-Object { Write-Host ('  {0} | {1} | {2}: de {3} para {4}' -f $_[3], $_[4], $_[6], $_[7], $_[8]) }
}

# ------------------------------------------------------------------------------------ GUI
function New-Grid {
    $g = New-Object System.Windows.Forms.DataGridView
    $g.Dock = 'Fill'; $g.ReadOnly = $true; $g.AllowUserToAddRows = $false; $g.RowHeadersVisible = $false; $g.SelectionMode = 'FullRowSelect'
    $g.AutoSizeColumnsMode = 'None'; $g.BackgroundColor = [System.Drawing.Color]::White; $g.BorderStyle = 'None'
    $g.AlternatingRowsDefaultCellStyle.BackColor = [System.Drawing.Color]::FromArgb(246, 248, 251)
    return $g
}

function Show-Gui {
    $mapa = Get-Resultados $PastaLogs
    $form = New-Object System.Windows.Forms.Form
    $form.Text = 'Comparador de Projetos E3 - Visual (protótipo)'; $form.Size = New-Object System.Drawing.Size(1320, 800)
    $form.StartPosition = 'CenterScreen'; $form.Font = New-Object System.Drawing.Font('Segoe UI', 9)

    $barra = New-Object System.Windows.Forms.FlowLayoutPanel; $barra.Dock = 'Top'; $barra.Height = 42; $barra.Padding = New-Object System.Windows.Forms.Padding(6, 6, 6, 0)
    $btnAB = New-Object System.Windows.Forms.Button; $btnAB.Text = 'Comparar A × B…'; $btnAB.AutoSize = $true
    $btnLote = New-Object System.Windows.Forms.Button; $btnLote.Text = 'Comparar lote (pastas)…'; $btnLote.AutoSize = $true
    $btnRec = New-Object System.Windows.Forms.Button; $btnRec.Text = 'Recarregar'; $btnRec.AutoSize = $true
    $btnXls = New-Object System.Windows.Forms.Button; $btnXls.Text = 'Abrir Excel'; $btnXls.AutoSize = $true
    $btnPasta = New-Object System.Windows.Forms.Button; $btnPasta.Text = 'Abrir pasta de logs'; $btnPasta.AutoSize = $true
    $lblSt = New-Object System.Windows.Forms.Label; $lblSt.AutoSize = $true; $lblSt.Padding = New-Object System.Windows.Forms.Padding(10, 6, 0, 0); $lblSt.Text = 'Pronto.'
    $barra.Controls.AddRange(@($btnAB, $btnLote, $btnRec, $btnXls, $btnPasta, $lblSt))

    $filtro = New-Object System.Windows.Forms.FlowLayoutPanel; $filtro.Dock = 'Top'; $filtro.Height = 36; $filtro.Padding = New-Object System.Windows.Forms.Padding(6, 4, 6, 0)
    $cbProj = New-Object System.Windows.Forms.ComboBox; $cbProj.DropDownStyle = 'DropDownList'; $cbProj.Width = 190
    $cbTipo = New-Object System.Windows.Forms.ComboBox; $cbTipo.DropDownStyle = 'DropDownList'; $cbTipo.Width = 220
    $lbB = New-Object System.Windows.Forms.Label; $lbB.Text = 'buscar:'; $lbB.AutoSize = $true; $lbB.Padding = New-Object System.Windows.Forms.Padding(8, 5, 0, 0)
    $txtB = New-Object System.Windows.Forms.TextBox; $txtB.Width = 300
    $lblCont = New-Object System.Windows.Forms.Label; $lblCont.AutoSize = $true; $lblCont.Padding = New-Object System.Windows.Forms.Padding(12, 5, 0, 0)
    $filtro.WrapContents = $false
    $filtro.Controls.AddRange(@($cbProj, $cbTipo, $lbB, $txtB, $lblCont))

    $info = New-Object System.Windows.Forms.TextBox; $info.Multiline = $true; $info.ReadOnly = $true; $info.Dock = 'Top'; $info.Height = 92
    $info.Font = New-Object System.Drawing.Font('Consolas', 9.5); $info.BackColor = [System.Drawing.Color]::White

    $detalhe = New-Object System.Windows.Forms.TextBox; $detalhe.Multiline = $true; $detalhe.ReadOnly = $true; $detalhe.Dock = 'Bottom'; $detalhe.Height = 92
    $detalhe.ScrollBars = 'Vertical'; $detalhe.Font = New-Object System.Drawing.Font('Consolas', 9.5); $detalhe.BackColor = [System.Drawing.Color]::FromArgb(250, 250, 240)

    $tabs = New-Object System.Windows.Forms.TabControl; $tabs.Dock = 'Fill'
    $gAdd = New-Grid; $gRem = New-Grid; $gMod = New-Grid
    $tpAdd = New-Object System.Windows.Forms.TabPage 'Adicionado'; $tpAdd.Controls.Add($gAdd)
    $tpRem = New-Object System.Windows.Forms.TabPage 'Removido'; $tpRem.Controls.Add($gRem)
    $tpMod = New-Object System.Windows.Forms.TabPage 'Modificado'; $tpMod.Controls.Add($gMod)
    $tabs.TabPages.AddRange(@($tpAdd, $tpRem, $tpMod))
    $form.Controls.Add($tabs); $form.Controls.Add($detalhe); $form.Controls.Add($info); $form.Controls.Add($filtro); $form.Controls.Add($barra)

    $TopN = 100          # linhas exibidas por aba (desempenho); totais e Excel/logs continuam completos
    $estado = @{ Mapa = $mapa; Proc = $null; Tmp = $null; Tab = @{}; Dados = @{ add = @(); rem = @(); mod = @() }; Carregando = $false }
    $larg = @{ 'Projeto' = 80; 'Tipo de nó' = 85; 'Nó' = 170; 'Objeto' = 230; 'Classe' = 130; 'Observação' = 100; 'Tipo de alteração' = 105; 'Propriedade' = 150; 'De' = 190; 'Para' = 190; 'Detalhe' = 200 }

    $aplicar = {
        if ($estado.Carregando) { return }
        $proj = if ($cbProj.SelectedIndex -gt 0) { $cbProj.SelectedItem } else { $null }
        $tipo = if ($cbTipo.SelectedIndex -gt 0) { [string]$cbTipo.SelectedItem } else { $null }
        $busca = $txtB.Text.Trim()
        $tot = @{}
        # cada aba mostra no maximo $TopN linhas (as primeiras que passam nos filtros); os totais contam TODAS as linhas
        foreach ($par in @(@('add', $gAdd, $ColsAdd, @(2, 3, 4)), @('rem', $gRem, $ColsAdd, @(2, 3, 4)), @('mod', $gMod, $ColsMod, @(2, 3, 4, 6, 7, 8)))) {
            $chave = $par[0]; $cols = $par[2]; $camposBusca = $par[3]
            $t = New-Object System.Data.DataTable
            foreach ($c in $cols) { [void]$t.Columns.Add($c, [string]) }
            $n = 0
            foreach ($l in $estado.Dados[$chave]) {
                if ($proj -and $l[0] -ne $proj) { continue }
                if ($chave -eq 'mod' -and $tipo -and $l[5] -ne $tipo) { continue }
                if ($busca) {
                    $ok = $false
                    foreach ($i in $camposBusca) { if ($i -lt $l.Count -and $l[$i] -and ([string]$l[$i]).IndexOf($busca, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) { $ok = $true; break } }
                    if (-not $ok) { continue }
                }
                $n++
                if ($t.Rows.Count -lt $TopN) {
                    $v = New-Object 'object[]' $cols.Count
                    for ($i = 0; $i -lt $cols.Count; $i++) { $v[$i] = if ($i -lt $l.Count -and $null -ne $l[$i]) { [string]$l[$i] } else { '' } }
                    [void]$t.Rows.Add($v)
                }
            }
            $tot[$chave] = $n; $estado.Tab[$chave] = $t
            $par[1].DataSource = $t
            foreach ($c in $par[1].Columns) { $c.Width = $(if ($larg.ContainsKey($c.Name)) { $larg[$c.Name] } else { 120 }) }
        }
        $tpAdd.Text = 'Adicionado (top {0} de {1})' -f $estado.Tab['add'].Rows.Count, $tot['add']
        $tpRem.Text = 'Removido (top {0} de {1})' -f $estado.Tab['rem'].Rows.Count, $tot['rem']
        $tpMod.Text = 'Modificado (top {0} de {1})' -f $estado.Tab['mod'].Rows.Count, $tot['mod']
        $lblCont.Text = 'Total {0} / {1} / {2} · tela: top {3} por aba · Excel tem tudo' -f $tot['add'], $tot['rem'], $tot['mod'], $TopN
        # resumo do projeto selecionado
        $linhas = @()
        foreach ($k in ($estado.Mapa.Keys | Sort-Object)) {
            $nome = Split-Path $k -Leaf
            if ($proj -and $nome -ne $proj) { continue }
            $r = $estado.Mapa[$k].Dados; $m = $r['meta']; $s = $r['resumo']
            if ($proj) {
                $linhas += "Antigo: $($m['antigo'])"; $linhas += "Novo  : $($m['novo'])"
                $linhas += "Horário da análise: $($m['analise_inicio'])  ->  $($m['analise_fim'])"
                $linhas += "Itens alterados: $($s['itens_alterados'])  (objetos alterados $($s['objetos_alterados']), adicionados $($s['objetos_adicionados']), removidos $($s['objetos_removidos']), movidos $($s['objetos_renomeados_ou_movidos']); propriedades de->para $($s['propriedades_alteradas']))"
            }
        }
        if (-not $proj) { $linhas = @("Todos os projetos ($($estado.Mapa.Count)). Selecione um projeto para ver horários e totais.", "Pasta de logs: $PastaLogs") }
        $info.Text = ($linhas -join "`r`n")
    }

    $carregar = {
        $estado.Carregando = $true
        $estado.Mapa = Get-Resultados $PastaLogs
        $a = New-Object System.Collections.ArrayList; $rm = New-Object System.Collections.ArrayList; $md = New-Object System.Collections.ArrayList
        foreach ($k in ($estado.Mapa.Keys | Sort-Object)) { $t = $estado.Mapa[$k].Dados['tabelas']; $a.AddRange(@($t['adicionado'])); $rm.AddRange(@($t['removido'])); $md.AddRange(@($t['modificado'])) }
        $bib = @($md | Where-Object { $_[5] -eq 'Biblioteca' }); $md2 = @($md | Where-Object { $_[5] -ne 'Biblioteca' }) + $bib       # bibliotecas por último
        $estado.Dados = @{ add = $a.ToArray(); rem = $rm.ToArray(); mod = $md2 }
        $cbProj.Items.Clear(); [void]$cbProj.Items.Add('(todos os projetos)')
        foreach ($k in ($estado.Mapa.Keys | Sort-Object)) { [void]$cbProj.Items.Add((Split-Path $k -Leaf)) }
        $cbProj.SelectedIndex = 0
        $tipos = @{}; foreach ($l in $estado.Dados['mod']) { $tipos[[string]$l[5]] = 1 }
        $cbTipo.Items.Clear(); [void]$cbTipo.Items.Add('(todos os tipos de alteração)'); foreach ($k in ($tipos.Keys | Sort-Object)) { [void]$cbTipo.Items.Add($k) }; $cbTipo.SelectedIndex = 0
        $estado.Carregando = $false
        & $aplicar
        $lblSt.Text = "Carregado: $($estado.Mapa.Count) projeto(s) de $PastaLogs"
    }

    $gMod.Add_CellFormatting({ param($s, $e)
            if ($e.RowIndex -lt 0) { return }
            $t = $s.Rows[$e.RowIndex].Cells['Tipo de alteração'].Value
            if ($t -eq 'Geometria') { $e.CellStyle.BackColor = [System.Drawing.Color]::FromArgb(227, 240, 255) }
            elseif ($t -eq 'Movido' -or $t -eq 'Renomeado') { $e.CellStyle.BackColor = [System.Drawing.Color]::FromArgb(240, 232, 250) }
            elseif ($t -like 'Campo binário*') { $e.CellStyle.BackColor = [System.Drawing.Color]::FromArgb(255, 240, 220) }
        })
    foreach ($g in @($gAdd, $gRem)) {
        $g.DefaultCellStyle.SelectionBackColor = [System.Drawing.Color]::FromArgb(40, 120, 70)
    }
    $gAdd.DefaultCellStyle.ForeColor = [System.Drawing.Color]::FromArgb(25, 100, 45)
    $gRem.DefaultCellStyle.ForeColor = [System.Drawing.Color]::FromArgb(160, 35, 30)

    $mostrarDetalhe = { param($s, $e)
        if ($s.CurrentRow -eq $null) { return }
        $c = $s.CurrentRow.Cells; $l = @()
        foreach ($col in $s.Columns) { $v = $c[$col.Name].Value; if ($v) { $l += ('{0}: {1}' -f $col.Name, $v) } }
        $detalhe.Text = $l -join "`r`n"
    }
    foreach ($g in @($gAdd, $gRem, $gMod)) { $g.Add_SelectionChanged($mostrarDetalhe) }
    $cbProj.Add_SelectedIndexChanged($aplicar); $cbTipo.Add_SelectedIndexChanged($aplicar); $debounce = New-Object System.Windows.Forms.Timer; $debounce.Interval = 450; $debounce.Add_Tick({ $debounce.Stop(); & $aplicar }); $txtB.Add_TextChanged({ $debounce.Stop(); $debounce.Start() })
    $btnRec.Add_Click({ & $carregar })
    $btnPasta.Add_Click({ if (Test-Path $PastaLogs) { Start-Process explorer.exe $PastaLogs } })
    $btnXls.Add_Click({
            $x = Get-ChildItem -Path $PastaLogs -Filter 'comparacao_*.xlsx' -File -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
            if ($x) { Start-Process $x.FullName } else { [System.Windows.Forms.MessageBox]::Show('Nenhum .xlsx encontrado.') | Out-Null }
        })

    # execução assíncrona do comparador
    $timer = New-Object System.Windows.Forms.Timer; $timer.Interval = 700
    $iniciar = { param($args2)
        if ($estado.Proc -and -not $estado.Proc.HasExited) { [System.Windows.Forms.MessageBox]::Show('Já existe uma comparação em andamento.') | Out-Null; return }
        $py = Get-Python; $estado.Tmp = [System.IO.Path]::GetTempFileName()
        $estado.Proc = Start-Process -FilePath $py[0] -ArgumentList ((@($py | Select-Object -Skip 1) + @('-u', (Join-Path $Script:Raiz 'comparar.py')) + $args2 + @('-o', $PastaLogs)) | ForEach-Object { if ($_ -match '\s') { '"' + $_ + '"' } else { $_ } }) -WindowStyle Hidden -PassThru -RedirectStandardOutput $estado.Tmp
        $null = $estado.Proc.Handle          # sem isso o ExitCode fica vazio apos o termino
        $btnAB.Enabled = $false; $btnLote.Enabled = $false; $lblSt.Text = 'Comparando…'; $timer.Start()
    }
    $timer.Add_Tick({
            if ($estado.Proc -and $estado.Proc.HasExited) {
                $timer.Stop(); $btnAB.Enabled = $true; $btnLote.Enabled = $true
                if ($estado.Proc.ExitCode -eq 0) { & $carregar; $tabs.SelectedTab = $tpMod } else {
                    $lblSt.Text = 'Falha na comparação.'; [System.Windows.Forms.MessageBox]::Show((Get-Content $estado.Tmp -Tail 15 -ErrorAction SilentlyContinue) -join "`n", 'Erro') | Out-Null }
            } elseif ($estado.Tmp -and (Test-Path $estado.Tmp)) { $u = Get-Content $estado.Tmp -Tail 1 -ErrorAction SilentlyContinue; if ($u) { $lblSt.Text = 'Comparando… ' + $u } }
        })
    $btnAB.Add_Click({
            $a = New-Object System.Windows.Forms.OpenFileDialog; $a.Title = 'Projeto ou biblioteca ANTIGO(A)'; $a.Filter = 'Projeto ou biblioteca E3 (*.prj;*.lib)|*.prj;*.lib|Todos os arquivos (*.*)|*.*'
            if ($a.ShowDialog() -ne 'OK') { return }
            $b = New-Object System.Windows.Forms.OpenFileDialog; $b.Title = 'Projeto ou biblioteca NOVO(A)'; $b.Filter = 'Projeto ou biblioteca E3 (*.prj;*.lib)|*.prj;*.lib|Todos os arquivos (*.*)|*.*'; $b.InitialDirectory = Split-Path $a.FileName
            if ($b.ShowDialog() -ne 'OK') { return }
            & $iniciar @($a.FileName, $b.FileName)
        })
    $btnLote.Add_Click({
            $a = New-Object System.Windows.Forms.FolderBrowserDialog; $a.Description = 'Pasta dos projetos ANTIGOS (ex.: temp-backups\04_Projects)'
            if ($a.ShowDialog() -ne 'OK') { return }
            $b = New-Object System.Windows.Forms.FolderBrowserDialog; $b.Description = 'Pasta dos projetos NOVOS (ex.: 04_Projects)'
            if ($b.ShowDialog() -ne 'OK') { return }
            $r = [System.Windows.Forms.MessageBox]::Show("Comparar BIBLIOTECAS (.lib)?`n`nSim = arquivos .lib das duas pastas`nNão = projetos .prj (Main, GC, Substations, GD)", 'Tipo de arquivo', 'YesNoCancel')
            if ($r -eq 'Cancel') { return }
            $extra = if ($r -eq 'Yes') { @('--ext', 'lib') } else { @() }
            & $iniciar (@('--lote', $a.SelectedPath, $b.SelectedPath) + $extra)
        })

    & $carregar
    if ($Screenshot) {
        $form.Show(); [System.Windows.Forms.Application]::DoEvents()
        $alvo = ($estado.Mapa.Keys | Where-Object { (Split-Path $_ -Leaf) -eq 'ufv_cfso.prj' } | Select-Object -First 1)
        foreach ($tp in @($tpMod, $tpAdd, $tpRem)) {
            $tabs.SelectedTab = $tp; [System.Windows.Forms.Application]::DoEvents()
            $bmp = New-Object System.Drawing.Bitmap $form.Width, $form.Height
            $form.DrawToBitmap($bmp, (New-Object System.Drawing.Rectangle 0, 0, $form.Width, $form.Height))
            $bmp.Save(($Screenshot -replace '\.png$', ("_{0}.png" -f $tp.Text.Split(' ')[0]))); $bmp.Dispose()
        }
        $form.Close(); return
    }
    if ($TesteAB -or $TesteLote) {
        $form.Show(); [System.Windows.Forms.Application]::DoEvents()
        if ($TesteAB) { & $iniciar @($TesteAB[0], $TesteAB[1]) } else { & $iniciar @('--lote', $TesteLote[0], $TesteLote[1], '--ext', $TesteExt) }
        $t0 = Get-Date
        while (((Get-Date) - $t0).TotalSeconds -lt 900) {
            [System.Windows.Forms.Application]::DoEvents(); Start-Sleep -Milliseconds 300
            if ($estado.Proc -and $estado.Proc.HasExited -and $btnAB.Enabled) { break }
        }
        Write-Host ("TESTE {0}: exit={1} | status='{2}' | projetos={3} adicionado={4} removido={5} modificado={6} | aba={7}" -f $(if ($TesteAB) { 'A x B' } else { 'LOTE' }), $estado.Proc.ExitCode, $lblSt.Text, $estado.Mapa.Count, $estado.Dados['add'].Count, $estado.Dados['rem'].Count, $estado.Dados['mod'].Count, $tabs.SelectedTab.Text)
        $form.Close(); return
    }
    if ($SelfTest) { Write-Host ("SelfTest OK: projetos={0} adicionado={1} removido={2} modificado={3}" -f $estado.Mapa.Count, $estado.Dados['add'].Count, $estado.Dados['rem'].Count, $estado.Dados['mod'].Count); $form.Dispose(); return }
    [void]$form.ShowDialog()
}

if ($Modo -eq 'Console') { Show-Console (Get-Resultados $PastaLogs) } else { Show-Gui }
