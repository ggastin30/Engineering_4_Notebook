#type:ignore
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

with open("/data.csv", "a") as datalog: #When Data Mode is Active
    while True:
        time_elapsed = time.monotonic()
        Xaccel = mpu.acceleration[0] #Reads the X acceleration
        Yaccel = mpu.acceleration[1]
        Zaccel = mpu.acceleration[2]

        if abs(Zaccel) < 1: # If Z is 90 degrees from parallel
            Led.value = True # Turn LED on
            Tilted = True # Say if it's tilted
        else:
            Led.value = False # Turn LED off
            Tilted = False # Say if it's not tilted
           
        datalog.write(f"{time_elapsed},{Xaccel},{Yaccel},{Zaccel},{Tilted}\n") #Put the data into a chart

        Led.value = True # LED cycle
        time.sleep(.5)
        Led.value = False

        datalog.flush() # Save the data
        time.sleep(.1)