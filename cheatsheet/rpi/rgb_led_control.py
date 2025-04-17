#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def rgb_led_control():
    """
    Controls three LEDs (11,13,15) via buttons (12,16,18).
    """
    leds = {'red':11, 'green':13, 'blue':15}
    buts = {'red':12, 'green':16, 'blue':18}

    GPIO.setmode(GPIO.BOARD)
    for pin in leds.values():
        GPIO.setup(pin, GPIO.OUT)
    for pin in buts.values():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print("RGB LED control via buttons. Press CTRL+C to exit.")
    try:
        while True:
            for color in leds:
                GPIO.output(leds[color], not GPIO.input(buts[color]))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program terminated!")
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    rgb_led_control()
