%USERPROFILE%\AppData\Local\Arduino15\packages\esp8266\hardware\esp8266\3.0.2/tools/upload.py --chip esp8266 --port COM4 --baud 921600 --before default_reset --after hard_reset write_flash 0x0 C:\Users\AnHive\AppData\Local\Temp\arduino_build_533228/envSensor_01.ino.bin

REM copy /y %USERPROFILE%\AppData\Local\Temp\arduino_build_533228\envSensor_01.ino.bin D:\source\P02_emshive\envSensor_01\.

%USERPROFILE%\AppData\Local\Arduino15\packages\esp8266\hardware\esp8266\3.0.2\tools\upload.py --chip esp8266 --port COM4 --baud 921600 write_flash 0x200000 %USERPROFILE%\AppData\Local\Temp\arduino_build_533228/envSensor_01.mklittlefs.bin

REM  copy /y %USERPROFILE%\AppData\Local\Temp\arduino_build_533228\envSensor_01.mklittlefs.bin D:\source\P02_emshive\envSensor_01\.