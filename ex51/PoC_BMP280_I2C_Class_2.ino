#include "AnHiveScanI2CClass.h"

void setup() {
Serial.begin(115200);
while (!Serial);

AnHiveScanI2C.setup();
/*
byte x = AnHiveScanI2C.checkEnvSensor();
if (x == BME680) Serial.println("BME680 used");
if (x == SHT31) Serial.println("SHT31 used");
*/
} // end of void setup()

void loop() {
   AnHiveScanI2C.loop();
} // end of void loop()

