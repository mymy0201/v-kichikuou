@echo off
setlocal
chcp 65001 > nul
cd /d "%~dp0"

echo ========================================================
echo   Biên dịch kịch bản Kichikuou Rance (Unicode/Tiếng Việt)
echo ========================================================
echo.
echo Đang biên dịch mã nguồn từ thư mục src/...
.\xsys35c_tools\xsys35c.exe --project=src/xsys35c.cfg --outdir=.
if errorlevel 1 (
    echo.
    echo [LỖI] Quá trình biên dịch thất bại!
    pause
    exit /b 1
)

echo.
echo ========================================================
echo   [THÀNH CÔNG] Đã tạo KICHIKUSA.ALD và System39.ain mới!
echo ========================================================
echo.
pause
