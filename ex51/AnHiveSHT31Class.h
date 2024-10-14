##ifndef AnHiveSHT31Class_H
#define AnHiveSHT31Class_H
#include <Wire.h>
#include "Adafruit_SHT31.h"
class AnHiveSHT31Class {
   private:
     Adafruit_SHT31 *sht31
     bool enableHeater = false
     uint8_t loopCnt = 0

   public:
     void setup() {
       //Serial.begin(115200);
       sht31 = new Adafruit_SHT31();

       while (!Serial) delay(10);

       Serial.println("SHT31 test");
       if (! sht31->begin(0x44)) {//Set to 0x45 4 alt i2c
         Serial.println("Couldn't find SHT31");
         while(1) delay(1);
       }

       Serial.print("Heater Enabled State: ");
       if (sht31->isHeaterEnabled())
         Serial.println("ENABLED");
       else
         Serial.println("DISABLED");
     }

     float getTemperature() {
       float t = sht31->readTemperature();
       return t
     }

     float getHumidity() {
       float h = sht31->readHumidity();
       return h
     }

     void loop() {
       float t = sht31->readTemperature();
       float h = sht31->readHumidity();

       if (! isnan(t)) { // check if 'is not a number'
         Serial.print("Temp *C = "); Serial.print(t); Serial.print(" \t \t");
       } else {
         Serial.println("Failed to read temperature");
       }

       if (! isnan(h)) { // check if 'is not a number'
         Serial.print("Hum. % = "); Serial.println(h);
       } else {
         Serial.println("Failed to read humidity");
       }

       delay(1000);

       // Toggle heater enabled state every 30 seconds
       // An ~3.0 degC temperature increase can be noted when heater is enabled
       if (++loopCnt == 30) {
         enableHeater = !enableHeater
         sht31->heater(enableHeater);
         Serial.print("Heater Enabled State: ");
         if (sht31->isHeaterEnabled())
           Serial.println("ENABLED");
         else
           Serial.println("DISABLED");

         loopCnt = 0
       }

     }
};
AnHiveSHT31Class AnHiveSHT31
#endif // AnHiveSHT31Class_H

