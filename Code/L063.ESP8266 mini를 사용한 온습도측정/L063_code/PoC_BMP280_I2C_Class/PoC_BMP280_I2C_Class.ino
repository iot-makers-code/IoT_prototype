#include "AnHiveBMP280Class.h"

void setup() {
  Serial.begin(115200);
  AnHiveBMP280.setup();
}

void loop() {
  AnHiveBMP280.loop();
  
  delay(2000);
}
