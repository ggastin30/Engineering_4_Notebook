import board
import time
import adafruit_mpu6050
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()

# OLED = 0x3d, MPU = 0x68
sda_pin = board.GP14 #Sets the sda pin
scl_pin = board.GP15 #Sets the scl pin
i2c = busio.I2C(scl_pin, sda_pin) # Connects the sda and scl to i2c

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP3) # Connect OLED to i2c
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) # Define OLED
splash = displayio.Group() # create the display group
title = "ANGULAR VELOCITY" # add title block to display group
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5) # the order of this command is (font, text, text color, and location)
splash.append(text_area)    
display.show(splash)

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) # Sets up the MPU

while True:
   

    time.sleep(.1) # Pause so there isn't too much data
