@echo off
setlocal enabledelayedexpansion

:: --- Configuration ---
set "VERSION=1.5.1"
set "REPO=https://github.com/SebCodesHere/PyHub"
set "INSTALL_DIR=%USERPROFILE%\PyHub"
set "ZIP_FILE=%TEMP%\pyhub.zip"

echo ----------------------------------------------------
echo           PyHub %VERSION% Windows Installer
echo ----------------------------------------------------

:: 1. Create Install Directory
if not exist "%INSTALL_DIR%" (
    echo [+] Creating folder: %INSTALL_DIR%
    mkdir "%INSTALL_DIR%"
)

:: 2. Download PyHub using PowerShell
echo [+] Downloading PyHub from GitHub...
powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri '%REPO%/archive/refs/tags/%VERSION%.zip' -OutFile '%ZIP_FILE%'"

if %ERRORLEVEL% NEQ 0 (
    echo [!] Download failed. Check your internet connection.
    pause
    exit /b 1
)

:: 3. Extract using PowerShell
echo [+] Extracting files...
powershell -Command "Expand-Archive -Path '%ZIP_FILE%' -DestinationPath '%TEMP%' -Force"

:: 4. Move files to Install Directory
echo [+] Installing files to %INSTALL_DIR%...
xcopy /E /I /Y "%TEMP%\PyHub-%VERSION%\*" "%INSTALL_DIR%" >nul

:: 5. Install Python Dependencies
echo [+] Checking Python dependencies...
python -m pip install pyfiglet requests speedtest-cli colorama psutil --quiet

:: 6. Create the 'pyhub.bat' shim (Points to pyhub.py)
echo @echo off > "%INSTALL_DIR%\pyhub.bat"
echo python "%INSTALL_DIR%\pyhub.py" %%* >> "%INSTALL_DIR%\pyhub.bat"

:: 7. Add to PATH (PowerShell Method)
echo [+] Registering 'pyhub' command in System PATH...
powershell -Command "$currentPath = [Environment]::GetEnvironmentVariable('Path', 'User'); if ($currentPath -notlike '*%INSTALL_DIR%*') { [Environment]::SetEnvironmentVariable('Path', $currentPath + ';%INSTALL_DIR%', 'User') }"

echo.
echo ----------------------------------------------------
echo SUCCESS: PyHub has been installed!
echo.
echo 1. CLOSE THIS CMD WINDOW.
echo 2. Open a NEW CMD window.
echo 3. Type 'pyhub' to start.
echo ----------------------------------------------------
pause