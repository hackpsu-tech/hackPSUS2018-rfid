@echo off
set /P location=Please enter your location: 
if "%location%"=="" GOTO Error
python ping.py ws://localhost:5000/v1/pi 10 pings.csv %location%
GOTO End
:Error
echo A location must be entered
:End
pause