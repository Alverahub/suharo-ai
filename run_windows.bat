@echo off
setlocal
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  echo Creating Python virtual environment...
  py -m venv .venv || goto error
)
echo Installing project dependencies...
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt || goto error
if not exist .env copy .env.example .env >nul
echo Starting Ada and Adi at http://127.0.0.1:8000
.venv\Scripts\python.exe -m uvicorn backend.main:app --reload
exit /b 0
:error
echo Setup failed. Check that Python 3.10+ is installed and available as py.
pause
exit /b 1
