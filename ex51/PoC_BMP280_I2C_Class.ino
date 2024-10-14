#include <Arduino.h>
#include "AnHiveSHT31Class.h"

void setup() {
   Serial.begin(115200);
   AnHiveSHT31.setup();
}

void loop() {
AnHiveSHT31.loop();
}

