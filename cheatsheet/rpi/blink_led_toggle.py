#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def blink_led_toggle():
    """
    Toggles an LED connected to pin 11 every second.
    """
    ledPin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)

    print("Blinking LED indefinitely. Press CTRL+C to exit.")
    ledStatus = True
    GPIO.output(ledPin, ledStatus)

    try:
        while True:
            time.sleep(1)
            ledStatus = not ledStatus
            GPIO.output(ledPin, ledStatus)
    except KeyboardInterrupt:
        print("Program terminated!")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    blink_led_toggle()
