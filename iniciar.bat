@echo off
setlocal
set "APP_ROOT=%~dp0"
set "PYTHONPATH=%APP_ROOT%src"
if not exist "%APP_ROOT%.venv\Scripts\python.exe" (
  echo Ambiente virtual ausente. Consulte README.md para instalar.
  pause
  exit /b 1
)
"%APP_ROOT%.venv\Scripts\python.exe" -m engineering_copilot_studio.main
