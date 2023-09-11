import board
import time
import digitalio

Seconds = 10 # Starts at 10 seconds
Bpress = 0 # Button presses

Button = digitalio.DigitalInOut(board.GP16)
Rled = digitalio.DigitalInOut(board.GP0) # Sets the pin of the green LED
Gled = digitalio.DigitalInOut(board.GP1) # Sets the pin of the red LED
Button.direction = digitalio.Direction.INPUT # Pin is using input
Rled.direction = digitalio.Direction.OUTPUT # Pin is using output
Gled.direction = digitalio.Direction.OUTPUT # Pin is using output
Button.pull = digitalio.Pull.UP # Button has normal amount set at 3 volts

while True:
    if Bpress < 1: # If it's not pressed
        if Button.value == False: # If pressed
            Bpress = 1 # Go to countdown
    else:
        Gled.value = False # Turn off green from previous loop
        if Seconds > 0: # When it is counting down
            print("T minus", Seconds) # Prints to serial monitor
            time.sleep(.5) # Pause 1/2 second
            Rled.value = True # Turn off Red
            time.sleep(.5) # Pause 1/2 second
            Rled.value = False # Turn off Red
            Seconds = Seconds - 1 # Decreases the value of seconds by 1
        else: # Once it reaches 0
            print("LIFTOFF") # Prints to serial monitor
            Gled.value = True # Turn on Green
            if Button.value == False: # If pressed
                Seconds = 10 # Reset values for new loop
                Bpress = 0