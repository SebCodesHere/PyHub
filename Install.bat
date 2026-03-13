@echo off
setlocal

:: === Config ===
set "VERSION=1.2.0"
set "INSTALL_DIR=%USERPROFILE%\PyHub-%VERSION%"
set "ZIP_URL=https://github.com/SebCodesHere/PyHub/archive/refs/tags/%VERSION%.zip"
set "ZIP_PATH=%TEMP%\pyhub.zip"

echo Installing PyHub %VERSION%...

:: Download the zip
powershell -Command "Invoke-WebRequest -Uri '%ZIP_URL%' -OutFile '%ZIP_PATH%'"

:: Extract the zip
powershell -Command "Expand-Archive -Path '%ZIP_PATH%' -DestinationPath '%INSTALL_DIR%' -Force"

:: Remove zip
del "%ZIP_PATH%"

:: Add to PATH (user scope)
setx PATH "%PATH%;%INSTALL_DIR%\PyHub-%VERSION%-1.2.0"

echo.
echo PyHub %VERSION% installed in %INSTALL_DIR%
echo Add %INSTALL_DIR% to your PATH if you want to run 'pyhub' from anywhere.

pause