@echo off

:: Check if Python 3.9 is installed
py -3.9 --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python 3.9 not found. !!!...
    echo Download the executable from https://www.python.org/downloads/release/python-390/
)

:: Create a virtual environment named 'my_venv'
py -3.9 -m venv .venv

:: Activate the virtual environment
.\.venv\Scripts\activate

echo "Environment setup complete! You are now in the '.venv' virtual environment."
