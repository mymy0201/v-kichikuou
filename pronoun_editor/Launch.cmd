@echo off
setlocal
cd /d "%~dp0"
if exist "PronounStudio.exe" (
    start "" "PronounStudio.exe" %*
    exit /b 0
)
if exist "runtime\python.exe" (
    "runtime\python.exe" app.py %*
) else (
    py -3 app.py %*
)
if errorlevel 1 pause
