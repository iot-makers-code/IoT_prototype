// --------------------------------------
// Scan and Identify I2C devices by farmerkeith
// Last update 9 July 2019
// Based on i2c_scanner Version 6
//
// This sketch tests all standard 7-bit addresses
// Devices with higher bit address might not be seen properly.
//
// Recognised devices are listed as their device type

#include "AnHiveScanI2CClass.h"

void setup() {
	Serial.begin(115200);
	while (!Serial);             // Leonardo: wait for serial monitor
	
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
