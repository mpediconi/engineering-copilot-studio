$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$candidates = @(
    (Join-Path $root '.venv\Scripts\python.exe'),
    (Join-Path $env:USERPROFILE 'AppData\Local\Programs\Python\Python313\python.exe'),
    (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python313\python.exe'),
    (Get-Command python -ErrorAction SilentlyContinue).Source
)
$python = $null
foreach ($candidate in $candidates) {
    if (-not $candidate -or -not (Test-Path -LiteralPath $candidate)) { continue }
    $version = & $candidate -c 'import sys; print(int(sys.version_info >= (3, 12)))'
    if ($LASTEXITCODE -eq 0 -and $version -eq '1') {
        $python = $candidate
        break
    }
}
if (-not $python) { throw 'Instale Python 3.12 ou superior. Consulte README.md.' }
& $python -c 'import PySide6, openpyxl, olefile'
if ($LASTEXITCODE -ne 0) { throw 'Instale as dependencias com: python -m pip install -e .' }
$env:PYTHONPATH = Join-Path $root 'src'
& $python -m engineering_copilot_studio.main
