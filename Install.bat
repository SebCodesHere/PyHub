@echo off
SETLOCAL

echo Installing PyHub v1.1.0...

:: Paths
set REPO=https://github.com/SebCodesHere/PyHub
set INSTALL_DIR=%USERPROFILE%\PyHub
set TMP_ZIP=%TEMP%\pyhub.zip

:: Make install folder
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Download main branch zip
powershell -Command "Invoke-WebRequest '%REPO%/archive/refs/heads/main.zip' -OutFile '%TMP_ZIP%'"

:: Extract zip
powershell -Command "Expand-Archive -Path '%TMP_ZIP%' -DestinationPath '%TEMP%' -Force"

:: Copy files to install folder
xcopy /E /I /Y "%TEMP%\PyHub-main\*" "%INSTALL_DIR%\"

:: Install Python dependencies
python -m pip install --user pyfiglet requests speedtest-cli colorama

:: Create pyhub.bat launcher in a folder in PATH
set LAUNCHER=%USERPROFILE%\AppData\Local\Microsoft\WindowsApps\pyhub.bat
echo @echo off > "%LAUNCHER%"
echo python "%INSTALL_DIR%\pyhub.py" %%* >> "%LAUNCHER%"

echo.
echo PyHub installed!
echo Open a new terminal and run:
echo pyhub

ENDLOCAL
pause