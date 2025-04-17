#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def blink_led_for():
    """
    Blinks an LED connected to pin 11 for 50 cycles using GPIO.BOARD numbering.
    """
    ledPin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)

    print("Blinking LED for 50 cycles. Press CTRL+C to exit.")
    try:
        for _ in range(50):
            GPIO.output(ledPin, True)
            time.sleep(1)
            GPIO.output(ledPin, False)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program terminated!")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    blink_led_for()
