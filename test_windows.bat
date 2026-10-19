@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
 echo Run run_windows.bat first to install the environment.
 pause
 exit /b 1
)
.venv\Scripts\python.exe -m pytest -q
pause
