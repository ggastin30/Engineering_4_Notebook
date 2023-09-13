import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

Seconds = 10 # Starts at 10 seconds
Bpress = 0 # Button presses

Button = digitalio.DigitalInOut(board.GP16) 
Rled = digitalio.DigitalInOut(board.GP0) # Sets the pin of the green LED
Gled = digitalio.DigitalInOut(board.GP1) # Sets the pin of the red LED
Button.direction = digitalio.Direction.INPUT # Pin is using input
Rled.direction = digitalio.Direction.OUTPUT # Pin is using output
Gled.direction = digitalio.Direction.OUTPUT # Pin is using output
Button.pull = digitalio.Pull.UP # Button has normal amount set at 3 volts

pwm = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50) # create a PWMOut object on Pin A2.
my_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500) # Define the servo


while True:
    if Bpress < 1: # If it's not pressed
        if Button.value == False: # If pressed
            Bpress = 1 # Go to countdown
    else:
        my_servo.angle = 0 # Servo angle goes to 0
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
            my_servo.angle = 179 # 180 glitches the servo
            Seconds = 10 # Reset values for new loop
            Bpress = 0 # Resest button