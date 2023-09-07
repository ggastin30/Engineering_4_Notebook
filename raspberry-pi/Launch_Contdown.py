import board
import time
Seconds = 10 # Starts at 10 seconds

while True:
    if Seconds > 0: # When it is counting down
        print("T minus", Seconds) # Prints to serial monitor
        time.sleep(1) # Pause 1 second
        Seconds = Seconds - 1 # Decreases the value of seconds by 1
    else: # Once it reaches 0
        print("LIFTOFF") # Prints to serial monitor
        time.sleep(1) # Pause 1 second
