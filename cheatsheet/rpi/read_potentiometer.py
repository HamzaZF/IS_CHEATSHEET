#!/usr/bin/env python3
import time
from gpiozero import MCP3008

def read_potentiometer():
    """
    Reads a potentiometer on channel 0 of an MCP3008 ADC.
    """
    pot = MCP3008(channel=0)
    print("Reading potentiometer value. Press CTRL+C to exit.")
    try:
        while True:
            print(f"Pot value: {pot.value:.2f}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Program terminated!")

if __name__ == '__main__':
    read_potentiometer()
