import board
import time
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import digitalio
import math

displayio.release_displays()

# OLED = 0x3d, MPU = 0x68
sda_pin = board.GP14 #Sets the sda pin
scl_pin = board.GP15 #Sets the scl pin
i2c = busio.I2C(scl_pin, sda_pin) # Connects the sda and scl to i2c

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP3) # Connect OLED to i2c
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # Define OLED
splash = displayio.Group() # create the display group

Led = digitalio.DigitalInOut(board.GP0) # Set LED pin
Led.direction = digitalio.Direction.OUTPUT # Pin is using output

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Sets up the MPU
title = "ANGULAR VELOCITY" # add title block to display group
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # the order of this command is (font, text, text color, and location)
splash.append(text_area)   
display.show(splash)

while True:
   
    Xaccel = mpu.acceleration[0] #Reads the X acceleration
    Yaccel = mpu.acceleration[1]
    Zaccel = mpu.acceleration[2]

    #print(f"X acceleration:{Xaccel}") # Prints the X acceleration
    #print(f"Y acceleration:{Yaccel}")
    #print(f"Z acceleration:{Zaccel}")
    print(" ") # Create a space between the prints

    text_area.text = f"ANGULAR VELOCITY: \n X:{round(mpu.gyro[0],3)} \n Y:{round(mpu.gyro[1],3)} \n Z:{round(mpu.gyro[2],3)}" 

    if abs(Zaccel) < 1: # If Z is 90 degrees from parallel
        Led.value = True # Turn LED on
        time.sleep(.1) # Pause so there isn't too much data
    else:
        Led.value = False # Turn LED off
        time.sleep(.1) # Pause so there isn't too much data
