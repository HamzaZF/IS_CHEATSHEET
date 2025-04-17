#!/usr/bin/env python3
import time
from gpiozero import MCP3008, PWMLED

def pwm_led_with_pot():
    """
    Controls a PWM LED (GPIO 21) brightness with MCP3008 pot.
    """
    pot = MCP3008(channel=0)
    led = PWMLED(21)

    print("PWM LED brightness controlled by potentiometer. Press CTRL+C to exit.")
    try:
        led.source = pot.values
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program terminated!")

if __name__ == '__main__':
    pwm_led_with_pot()
