#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

def heart_rate_measurement():
    """
    Measures heart rate via interrupts on pin 16. LED on 40, button on 38 toggles.
    """
    heartPin, ledPin, butPin = 16, 40, 38
    count = 0; doCounting = False; startTime = 0.0
    measuring = False

    def callback(ch):
        nonlocal count, doCounting, startTime
        count += 1
        if not doCounting and count == 10:
            doCounting = True
            startTime = time.time()
            count = 0
        if doCounting and (time.time() - startTime) > 15:
            print(f"Heart rate: {count*4} bpm")
            startTime = time.time()
            count = 0

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(heartPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    print('Heart rate measurement running... Press CTRL+C to exit.')
    try:
        while True:
            if not GPIO.input(butPin):
                if not measuring:
                    GPIO.add_event_detect(heartPin, GPIO.RISING, callback=callback)
                    GPIO.output(ledPin, True)
                    measuring = True
                    count = 0; doCounting = False; startTime = time.time()
                    print('Started measuring...')
                else:
                    GPIO.remove_event_detect(heartPin)
                    GPIO.output(ledPin, False)
                    measuring = False
                    print('Stopped measuring...')
                time.sleep(0.2)
    except KeyboardInterrupt:
        print('Program terminated!')
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    heart_rate_measurement()
