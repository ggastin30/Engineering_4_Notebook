import board
import time
Seconds = 10

while True:
    if Seconds > 0:
        print("T minus", Seconds)
        time.sleep(1)
        Seconds = Seconds - 1
    else:
        print("LIFTOFF")
        time.sleep(1)
