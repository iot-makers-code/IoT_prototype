import smbus2
import time

bus = smbus2.SMBus(1)
bus.write_i2c_block_data(0x44, 0x22, [0x36])
while True:
     time.sleep(0.5)
     
     data = bus.read_i2c_block_data(0x44, 0x00, 6)
     temp_r = data[0] * 256 + data[1]
     temp = round(-45 + (175 * temp_r / 65535.0),1)
     humidity = round(100 * (data[3] * 256 + data[4]) / 65535.0,1)
     
     print("Temperature: %.2fC" %temp)
     print("Humidity: %.2f%%RH" %humidity)

