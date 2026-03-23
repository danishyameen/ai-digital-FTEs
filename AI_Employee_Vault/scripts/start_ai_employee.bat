@echo off
REM start_ai_employee.bat - Start the AI Employee Bronze Tier system
REM 
REM This script starts both the Filesystem Watcher and Orchestrator
REM in separate background processes.
REM
REM Usage: 
REM   Option 1: Double-click this file
REM   Option 2: Run from any directory: full\path\to\scripts\start_ai_employee.bat

echo ================================================
echo   AI Employee Bronze Tier - Starting...
echo ================================================
echo.

REM Get the directory where this batch file is located
set SCRIPT_DIR=%~dp0
set VAULT_DIR=%SCRIPT_DIR%..

echo Script Directory: %SCRIPT_DIR%
echo Vault Directory: %VAULT_DIR%
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.13+
    pause
    exit /b 1
)

echo Python found!
python --version
echo.

REM Install watchdog if not already installed
echo Checking for watchdog...
pip show watchdog >nul 2>&1
if errorlevel 1 (
    echo Installing watchdog...
    pip install watchdog
) else (
    echo watchdog already installed.
)
echo.

REM Start Filesystem Watcher
echo Starting Filesystem Watcher...
start "AI Employee - Filesystem Watcher" cmd /k "cd /d %SCRIPT_DIR% && python filesystem_watcher.py %VAULT_DIR%"

REM Wait a moment for watcher to start
timeout /t 2 /nobreak >nul

REM Start Orchestrator
echo Starting Orchestrator...
start "AI Employee - Orchestrator" cmd /k "cd /d %SCRIPT_DIR% && python orchestrator.py %VAULT_DIR%"

echo.
echo ================================================
echo   AI Employee Bronze Tier is now running!
echo ================================================
echo.
echo Two windows have been opened:
echo   1. Filesystem Watcher - monitors Inbox folder
echo   2. Orchestrator - triggers Claude Code
echo.
echo To test the system:
echo   1. Create a text file in the Inbox folder
echo   2. Watch the logs for processing updates
echo.
echo To stop: Close both terminal windows
echo ================================================
echo.
pause
