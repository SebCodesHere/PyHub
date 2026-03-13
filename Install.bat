@echo off
setlocal

:: === Config ===
:: Change this to match your GitHub tag (numeric tags like 1.2.0)
set "VERSION=1.2.0"

:: Paths
set "INSTALL_DIR=%USERPROFILE%\PyHub-%VERSION%"
set "ZIP_URL=https://github.com/SebCodesHere/PyHub/archive/refs/tags/%VERSION%.zip"
set "ZIP_PATH=%TEMP%\pyhub.zip"

echo Installing PyHub %VERSION%...

:: Download the zip archive
powershell -Command "Write-Host 'Downloading PyHub...'; Invoke-WebRequest -Uri '%ZIP_URL%' -OutFile '%ZIP_PATH%'"

:: Check if download succeeded
if not exist "%ZIP_PATH%" (
    echo ERROR: Failed to download PyHub zip. Check the VERSION variable or your internet connection.
    pause
    exit /b 1
)

:: Extract the zip
powershell -Command "Write-Host 'Extracting...'; Expand-Archive -Path '%ZIP_PATH%' -DestinationPath '%INSTALL_DIR%' -Force"

:: Remove the zip
del "%ZIP_PATH%"

:: Create a launcher script for pyhub
set "LAUNCHER=%USERPROFILE%\pyhub.cmd"
echo @echo off > "%LAUNCHER%"
echo python "%INSTALL_DIR%\PyHub-%VERSION%\pyhub.py" %%* >> "%LAUNCHER%"

:: Add launcher folder to PATH if not already
setx PATH "%USERPROFILE%;%PATH%"

echo.
echo PyHub v%VERSION% installed!
echo You can now run "pyhub" from anywhere.
pause