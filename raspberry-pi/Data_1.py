import board
import time
import adafruit_mpu6050
import busio
import digitalio

sda_pin = board.GP14 #Sets the sda pin
scl_pin = board.GP15 #Sets the scl pin
i2c = busio.I2C(scl_pin, sda_pin) # Connects the sda and scl to i2c

Led = digitalio.DigitalInOut(board.GP0) # Set LED pin
Led.direction = digitalio.Direction.OUTPUT # Pin is using output

mpu = adafruit_mpu6050.MPU6050(i2c) # Sets up the MPU

while True:
    Xaccel = mpu.acceleration[0] #Reads the X acceleration
    Yaccel = mpu.acceleration[1]
    Zaccel = mpu.acceleration[2]

    print(f"X acceleration:{Xaccel}") # Prints the X acceleration
    print(f"Y acceleration:{Yaccel}")
    print(f"Z acceleration:{Zaccel}")
    print(" ") # Create a space between the prints

    if abs(Zaccel) < 1: # If Z is 90 degrees from parallel
        Led.value = True # Turn LED on
        time.sleep(.1) # Pause so there isn't too much data
    else:
        Led.value = False # Turn LED off
        time.sleep(.1) # Pause so there isn't too much data