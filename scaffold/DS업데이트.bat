@echo off
chcp 65001 >nul
cd /d "%~dp0"
python update_ds.py || py update_ds.py
echo.
pause
