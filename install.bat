@echo off
setlocal enabledelayedexpansion

set "VERSION=1.5.0"
set "REPO=https://github.com/SebCodesHere/PyHub"
set "INSTALL_DIR=%USERPROFILE%\PyHub"
set "ZIP_FILE=%TEMP%\pyhub.zip"

echo Installing PyHub %VERSION%...

:: 1. Create Install Directory
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: 2. Download PyHub using PowerShell
echo Downloading PyHub release %VERSION%...
powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%REPO%/archive/refs/tags/%VERSION%.zip' -OutFile '%ZIP_FILE%'"

if %ERRORLEVEL% NEQ 0 (
    echo Download failed.
    pause
    exit /b 1
)

:: 3. Extract using PowerShell
echo Extracting...
powershell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%TEMP%' -Force"

:: 4. Move files to Install Directory
xcopy /E /I /Y "%TEMP%\PyHub-%VERSION%\*" "%INSTALL_DIR%"

:: 5. Install Python Dependencies
echo Installing dependencies...
python -m pip install pyfiglet requests speedtest-cli colorama psutil

:: 6. Create the 'pyhub.bat' shim so it can be called as a command
echo @echo off > "%INSTALL_DIR%\pyhub.bat"
echo python "%INSTALL_DIR%\main.py" %%* >> "%INSTALL_DIR%\pyhub.bat"

:: 7. Add to PATH (User Level)
echo Adding PyHub to PATH...
setx PATH "%PATH%;%INSTALL_DIR%" >nul

echo.
echo ----------------------------------------------------
echo PyHub installed successfully!
echo.
echo IMPORTANT: Close this CMD window and open a NEW one.
echo Then simply type: pyhub
echo ----------------------------------------------------
pause