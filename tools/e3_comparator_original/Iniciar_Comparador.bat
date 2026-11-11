@echo off
rem Abre o visualizador do comparador de projetos E3 (janela com abas Adicionado / Removido / Modificado)
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0E3_Comparador_Visual.ps1"
