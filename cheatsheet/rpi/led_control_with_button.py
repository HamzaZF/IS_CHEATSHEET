#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def led_control_with_button():
    """
    LED on pin 11 follows button on pin 12: on when pressed, off when released.
    """
    ledPin, butPin = 11, 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print("LED control via button. Press CTRL+C to exit.")
    try:
        while True:
            GPIO.output(ledPin, not GPIO.input(butPin))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program terminated!")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    led_control_with_button()
