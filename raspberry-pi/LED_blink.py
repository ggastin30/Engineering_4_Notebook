#type: ignore
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP1)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    time.sleep(0.5)