#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def read_button():
    """
    Reads the input from a button on pin 12 (pull‑up).
    """
    butPin = 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print("Reading button state. Press CTRL+C to exit.")
    try:
        while True:
            state = "released" if GPIO.input(butPin) else "pressed"
            print(f"Button {state}!")
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("Program terminated!")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    read_button()
