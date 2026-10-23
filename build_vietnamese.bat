@echo off
setlocal
chcp 65001 > nul
cd /d "%~dp0"

echo ========================================================
echo   Biên dịch kịch bản Kichikuou Rance (Unicode/Tiếng Việt)
echo ========================================================
echo.

set "COMPILER=.\xsys35c_tools\xsys35c.exe"
if not exist "%COMPILER%" (
    where xsys35c.exe >nul 2>&1
    if not errorlevel 1 (
        set "COMPILER=xsys35c.exe"
    ) else (
        echo [LỖI] Không tìm thấy trình biên dịch xsys35c.exe!
        echo Vui lòng đảm bảo xsys35c.exe nằm trong thư mục xsys35c_tools\ hoặc trong PATH.
        echo.
        pause
        exit /b 1
    )
)

echo Đang biên dịch mã nguồn từ thư mục src/...
"%COMPILER%" --project=src/xsys35c.cfg --outdir=.
if errorlevel 1 (
    echo.
    echo [LỖI] Quá trình biên dịch thất bại!
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================================
echo   [THÀNH CÔNG] Đã tạo KICHIKUSA.ALD và System39.ain mới!
echo ========================================================
echo.
pause