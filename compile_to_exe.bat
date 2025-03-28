@echo off
:: Ensure PyInstaller is installed in the current Python environment
echo Checking if PyInstaller is installed...
python -m pip show pyinstaller >nul 2>&1
if %errorlevel% neq 0 (
    echo PyInstaller is not installed. Installing it now...
    python -m pip install pyinstaller
)

:: Compile the Python file into an executable
echo Compiling the game into an executable...
python -m PyInstaller --onefile --noconsole --name PlatformerGame platformer.py

:: Move the compiled executable to the current directory
if exist dist\PlatformerGame.exe (
    move dist\PlatformerGame.exe PlatformerGame.exe
    echo Compilation successful! The executable is saved as "PlatformerGame.exe".
) else (
    echo Compilation failed. Please check the PyInstaller output for details.
)

:: Clean up build artifacts
rmdir /s /q build >nul 2>&1
del /q PlatformerGame.spec >nul 2>&1
rmdir /s /q dist >nul 2>&1

pause
