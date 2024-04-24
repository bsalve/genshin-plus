@echo off
setlocal

set "SCRIPT_DIR=%~dp0"

call "%SCRIPT_DIR%\.venv\Scripts\activate" & pythonw "%SCRIPT_DIR%\claim_dailies.py"

endlocal