@echo off
chcp 65001 > nul
cls

echo.
echo  ╔══════════════════════════════════════════════╗
echo  ║         StreamChat Simulator                                ║
echo  ║         Made with Claude.ai by MahSomething                 ║
echo  ╚══════════════════════════════════════════════╝
echo.
echo  ─────────────────────────────────────────────
echo   Select your language / Selecione o idioma
echo  ─────────────────────────────────────────────
echo.
echo   [1]  Português  🇧🇷
echo   [2]  English    🇺🇸
echo   [3]  Français   🇫🇷
echo.
choice /c 123 /n /m "  Choose (1/2/3): "

if errorlevel 3 set LANG=fr
if errorlevel 2 set LANG=en
if errorlevel 1 set LANG=pt

cls
echo.
echo  ╔══════════════════════════════════════════════╗
echo  ║         StreamChat Simulator                 ║
echo  ║         Made with Claude.ai by Mahomed       ║
echo  ╚══════════════════════════════════════════════╝
echo.

if "%LANG%"=="pt" (
  echo   Servidor iniciado com sucesso!
  echo.
  echo   Controlador : http://localhost:8080/controller.html?lang=pt
  echo   Overlay OBS : http://localhost:8080/overlay.html
  echo.
  echo   Nao feches esta janela enquanto gravares!
  echo   Para parar: CTRL+C
)
if "%LANG%"=="en" (
  echo   Server started successfully!
  echo.
  echo   Controller  : http://localhost:8080/controller.html?lang=en
  echo   OBS Overlay : http://localhost:8080/overlay.html
  echo.
  echo   Do not close this window while recording!
  echo   To stop: CTRL+C
)
if "%LANG%"=="fr" (
  echo   Serveur demarré avec succès!
  echo.
  echo   Contrôleur  : http://localhost:8080/controller.html?lang=fr
  echo   Overlay OBS : http://localhost:8080/overlay.html
  echo.
  echo   Ne fermez pas cette fenêtre pendant l'enregistrement!
  echo   Pour arrêter: CTRL+C
)

echo.
echo  ─────────────────────────────────────────────
echo.

cd /d "%~dp0"

:: Abrir browser automaticamente com o idioma escolhido
start "" "http://localhost:8080/controller.html?lang=%LANG%"

python server.py
pause
