@echo off
title LightX Mobile Automation Runner
echo ========================================================
echo       LIGHTX MOBILE AUTOMATION SUITE (ANDROID & IOS)
echo ========================================================
echo 1. Activating Virtual Environment...
call venv\Scripts\activate.bat

echo 2. Running Mobile Test Suites (Android + iOS + Cross-Platform)...
python -m pytest -v -s --html=reports/mobile_report.html --self-contained-html

echo ========================================================
echo 3. Opening Mobile HTML Execution Report in Browser...
echo ========================================================
start reports\mobile_report.html
pause
