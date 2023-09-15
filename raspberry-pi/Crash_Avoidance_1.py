import board
import time
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    Xaccel = mpu.acceleration[0]
    Yaccel = mpu.acceleration[1]
    Zaccel = mpu.acceleration[2]

    print(f"X acceleration:{Xaccel}")
    print(f"Y acceleration:{Yaccel}")
    print(f"Z acceleration:{Zaccel}")
    print(" ")

    time.sleep(.1)
