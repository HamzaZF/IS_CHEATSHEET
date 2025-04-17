#!/usr/bin/env python3
import time
import board
from adafruit_bme280 import basic as adafruit_bme280

def read_bme280():
    """
    Reads Temperature, Pressure, Humidity from a BME280 via I2C.
    """
    i2c = board.I2C()
    sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c)
    print("Reading BME280 data. Press CTRL+C to exit.")
    try:
        while True:
            print(f"Temp = {sensor.temperature:.3f} °C")
            print(f"Pres = {sensor.pressure:.2f} hPa")
            print(f"Hum  = {sensor.humidity:.2f} %")
            print('---------------------------')
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated!")

if __name__ == '__main__':
    read_bme280()
