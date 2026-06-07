@echo off
chcp 65001 > nul
cls

echo.
echo  ==========================================
echo   StreamChat Simulator
echo   Made with Claude.ai by Mahomed
echo  ==========================================
echo.
echo   Controller : http://localhost:8080/controller.html
echo   OBS Overlay: http://localhost:8080/overlay.html
echo.
echo   Do not close this window while recording!
echo   To stop: CTRL+C
echo.
echo  ==========================================
echo.

cd /d "%~dp0"
start "" "http://localhost:8080/controller.html"
python server.py
pause
