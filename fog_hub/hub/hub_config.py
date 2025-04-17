# Configuration Constants
DB_NAME = '../sensor.db'
TABLE_NAME = 'sensor'
SENSOR_FIELD = 'value'
SERIAL_PORT = '/dev/ttyACM0'
BAUDRATE = 115200
SERIAL_TIMEOUT = 1
SENSOR_TYPE = 'light'
POLL_INTERVAL = 1
CLOUD_BASE_URI = 'http://169.254.53.99:5000/'
CLOUD_ENDPOINT = 'api/record'
RELAY_INTERVAL = 10
MQTT_BROKER = 'broker.emqx.io'
MQTT_PORT = 1883
MQTT_TOPIC = '/sensor/actuator'
MQTT_CLIENT_ID = 'python-mqtt-'
GPIO_PIN = 11
ON_CMD = 'on'

# SQL Templates
SQL = {
    'insert':    "INSERT INTO {table} (devicename, {field}, timestamp) VALUES (?, ?, datetime('now','localtime'))",
    'retrieve':  "SELECT id, devicename, {field}, timestamp FROM {table} WHERE tocloud = 0",
    'mark_sent': "UPDATE {table} SET tocloud = 1 WHERE id = ?"
}

# Command mappings
COMMANDS = {
    'read':   f"sensor={SENSOR_TYPE}",
    'act_on': ON_CMD,
    'act_off':'off'
}