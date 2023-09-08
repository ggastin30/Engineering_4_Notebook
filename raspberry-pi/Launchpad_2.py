import board
import time
import digitalio
Seconds = 10 # Starts at 10 seconds
Rled = digitalio.DigitalInOut(board.GP0) # Sets the pin of the green LED
Gled = digitalio.DigitalInOut(board.GP1) # Sets the pin of the red LED
Rled.direction = digitalio.Direction.OUTPUT # Pin is using output
Gled.direction = digitalio.Direction.OUTPUT # Pin is using output

while True:
    if Seconds > 0: # When it is counting down
        print("T minus", Seconds) # Prints to serial monitor
        time.sleep(.5) # Pause 1/2 second
        Rled.value = True
        time.sleep(.5) # Pause 1/2 second
        Rled.value = False
        Seconds = Seconds - 1 # Decreases the value of seconds by 1
    else: # Once it reaches 0
        print("LIFTOFF") # Prints to serial monitor
        Gled.value = True
        time.sleep(1) # Pause 1 second
       
