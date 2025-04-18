#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def rgb_led_control():
    """
    Controls three LEDs (11,13,15) via buttons (12,16,18).
    """
    led = 11
    but = 36

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(but, GPIO.IN, pull_up_down=GPIO.PUD_UP)


    print("RGB LED control via buttons. Press CTRL+C to exit.")
    try:
        while True:
            # print("LED state: ", GPIO.input(led))
            # print("Button state: ", GPIO.input(but))
            GPIO.output(led, not GPIO.input(but))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program terminated!")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    rgb_led_control()
