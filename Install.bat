@echo off
set VERSION=1.2.0
set INSTALL_DIR=%USERPROFILE%\PyHub
set TMP_ZIP=%TEMP%\pyhub.zip

echo Installing PyHub v%VERSION%...

:: Create install directory
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Downloading PyHub v%VERSION%...
powershell -Command "Invoke-WebRequest https://github.com/SebCodesHere/PyHub/archive/refs/tags/v%VERSION%.zip -OutFile '%TMP_ZIP%'"

echo Extracting...
powershell -Command "Expand-Archive -Path '%TMP_ZIP%' -DestinationPath '%TEMP%' -Force"

echo Copying files...
xcopy /E /I /Y "%TEMP%\PyHub-%VERSION%\*" "%INSTALL_DIR%\"

echo Installing dependencies...
python -m pip install --user pyfiglet requests speedtest-cli colorama

echo Creating pyhub command...
echo @echo off > "%INSTALL_DIR%\pyhub.bat"
echo python "%INSTALL_DIR%\pyhub.py" %%* >> "%INSTALL_DIR%\pyhub.bat"

:: Add to PATH if not already
setx PATH "%PATH%;%INSTALL_DIR%" >nul

echo.
echo PyHub v%VERSION% installed!
echo Restart your terminal and run:
echo pyhub
pause