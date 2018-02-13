@echo off

rem get the location that the user wants entered into the first cell
set /P location=Please enter your location: 
if "%location%"=="" GOTO Error

rem run the python script.  update ws://localhost:5000/v1/pi to the server address
python ping.py ws://localhost:5000/v1/pi 10 pings.csv %location%
GOTO End

:Error
echo A location must be entered
:End
pause
