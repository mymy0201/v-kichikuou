@echo off
setlocal
pushd "%~dp0"
if not exist "save" mkdir "save"
"xsystem35.exe" -savedir "save" -playlist "playlist.txt"
set "release_exit=%ERRORLEVEL%"
popd
exit /b %release_exit%
