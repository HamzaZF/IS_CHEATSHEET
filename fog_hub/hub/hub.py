import time
import random
import serial
import RPi.GPIO as GPIO
import requests
import json
import paho.mqtt.client as mqtt
import _thread as thread

from hub_config import *
from hub_db_utils import insert_reading, get_unsent, mark_sent
from hub_config import COMMANDS


def send_command(cmd: str):
    ser.write(f"{cmd}\n".encode())


def wait_response() -> str:
    return ser.readline().decode('utf-8').strip()


def sensor_hub_thread():
    global ser
    ser = serial.Serial(
        port=SERIAL_PORT,
        baudrate=BAUDRATE,
        timeout=SERIAL_TIMEOUT
    )
    print(f"rhub: Listening on {SERIAL_PORT}... Press CTRL+C to exit")

    # Handshaking
    send_command('handshake')
    resp = ''
    while not resp:
        resp = wait_response()
        print(f"rhub handshake: {resp}")
        time.sleep(0.1)

    parts = resp.split('=', 1)
    if len(parts) > 1 and parts[1]:
        devices = parts[1].split(',')
        for d in devices:
            print(f"rhub: Connected to micro:bit device {d}...")
        while True:
            time.sleep(POLL_INTERVAL)
            cmd = f"cmd:{COMMANDS['read']}"
            send_command(cmd)
            raw = ''
            while not raw:
                raw = wait_response()
                time.sleep(0.1)
            readings = raw.split(',')
            for entry in readings:
                device, value = entry.split('=')
                print(f"rhub: {entry}")
                insert_reading(device, value)


def cloud_relay_thread():
    uri = CLOUD_BASE_URI.rstrip('/') + '/' + CLOUD_ENDPOINT
    headers = {'Content-Type':'application/json'}
    mark_sql = SQL['mark_sent'].format(table=TABLE_NAME)

    while True:
        time.sleep(RELAY_INTERVAL)
        print("Relaying data to cloud server...")
        rows = get_unsent()
        for row in rows:
            row_id, dev, val, ts = row
            print(f"Relaying id={row_id}; devicename={dev}; {SENSOR_FIELD}={val}; timestamp={ts}")
            payload = {'devicename': dev, SENSOR_FIELD: val, 'timestamp': ts}
            requests.put(uri, headers=headers, data=json.dumps(payload))
            mark_sent(row_id)


def on_message(client, userdata, msg):
    cmd = msg.payload.decode()
    print(f"Command received: {cmd}")
    # if cmd == COMMANDS['act_on']:
    #     GPIO.output(GPIO_PIN, True)
    # else:
    #     GPIO.output(GPIO_PIN, False)


def actuator_listener_mqtt_thread():
    client = mqtt.Client(f"{MQTT_CLIENT_ID}{random.randint(0,10000)}")
    client.connect(MQTT_BROKER, MQTT_PORT)
    client.subscribe(MQTT_TOPIC)
    client.on_message = on_message
    client.loop_forever()


def init():
    return
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(GPIO_PIN, GPIO.OUT)
    # GPIO.output(GPIO_PIN, False)


def main():
    init()
    thread.start_new_thread(sensor_hub_thread, ())
    thread.start_new_thread(cloud_relay_thread, ())
    thread.start_new_thread(actuator_listener_mqtt_thread, ())
    print("Program running... Press CTRL+C to exit")

    while True:
        try:     
            time.sleep(0.1)
        except RuntimeError as error:
            print('Error: {}'.format(error.args[0]))
        except Exception as error:
            print('Error: {}'.format(error.args[0]))
        except KeyboardInterrupt:
            if ser.is_open:
                ser.close()
            GPIO.cleanup()
            print('Program terminating...')
            break


if __name__ == '__main__':
    main()
