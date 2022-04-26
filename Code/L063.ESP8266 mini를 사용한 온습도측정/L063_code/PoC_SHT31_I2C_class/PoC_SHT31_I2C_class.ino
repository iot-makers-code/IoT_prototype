/*************************************************** 
  This is an example for the SHT31-D Humidity & Temp Sensor

  Designed specifically to work with the SHT31-D sensor from Adafruit
  ----> https://www.adafruit.com/products/2857

  These sensors use I2C to communicate, 2 pins are required to  
  interface
 ****************************************************/
 
#include <Arduino.h>
#include "AnHiveSHT31Class.h"

void setup() {
  Serial.begin(115200);
  AnHiveSHT31.setup();
}


void loop() {
	AnHiveSHT31.loop();
}
