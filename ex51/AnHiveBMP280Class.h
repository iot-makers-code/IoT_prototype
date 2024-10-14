#ifndef AnHiveBMP280Class_H
#define AnHiveBMP280Class_H

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>

class AnHiveBMP280Class {
   private:
     Adafruit_BMP280 *bmp // use I2C interface
     Adafruit_Sensor *bmp_temp
     Adafruit_Sensor *bmp_pressure
float temperature
float pressure
   public:
     void setup() {
       //Serial.begin(115200);
       Serial.println(F(" \n \nBMP280 Sensor event test"));

       bmp = new Adafruit_BMP280(); // use I2C interface
       bmp_temp = bmp->getTemperatureSensor();
       bmp_pressure = bmp->getPressureSensor();


       if (!bmp->begin(BMP280_ADDRESS_ALT, BMP280_CHIPID)) {
         //if (!bmp->begin()) {
         Serial.println(F("Could not find a valid BMP280 sensor, check wiring or "
                          "Try a different address!"));
         while (1) delay(10);
       }

       /* Default settings from datasheet. */
       bmp->setSampling(
               Adafruit_BMP280::MODE_NORMAL,/* Operating Mode. */
               Adafruit_BMP280::SAMPLING_X2, /* Temp. oversampling */
               Adafruit_BMP280::SAMPLING_X16, /* Pressure oversampling */
               Adafruit_BMP280::FILTER_X16, /* Filtering. */
               Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */

       bmp_temp->printSensorDetails();
     }

     void read() {
       sensors_event_t temp_event, pressure_event
       bmp_temp->getEvent(&temp_event);
    temperature = temp_event.temperature
   
       bmp_pressure->getEvent(&pressure_event);
       pressure = pressure_event.pressure
     }

     float getTemperature() {
       sensors_event_t event
       bmp_temp->getEvent(&event);
       return (float)event.temperature
     }
     float getPressure() {
       sensors_event_t event
       bmp_pressure->getEvent(&event);
       return (float)event.temperature
     }

     void loop() {
       sensors_event_t temp_event, pressure_event
       bmp_temp->getEvent(&temp_event);
       bmp_pressure->getEvent(&pressure_event);

       Serial.print(F("Temperature = "));
       Serial.print(temp_event.temperature);
       Serial.println(" *C");

       Serial.print(F("Pressure = "));
       Serial.print(pressure_event.pressure);
       Serial.println(" hPa");

       Serial.println();
       //delay(2000);
     }
};

AnHiveBMP280Class AnHiveBMP280

#endif //#ifndef AnHiveBMP280Class_H

@PoC_BMP280_I2C_Class.ino

#include "AnHiveBMP280Class.h"

void setup() {
   Serial.begin(115200);
   AnHiveBMP280.setup();
}

void loop() {
   AnHiveBMP280.loop();
  
   delay(2000);
}

