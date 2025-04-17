// ================= Customization Variables =================

// String commands and prefixes
let HANDSHAKE_COMMAND = "handshake";          // Expected handshake received from serial.
let RADIO_HANDSHAKE_COMMAND = "handshake";      // Handshake command to broadcast via radio.
let ENROLL_PREFIX = "enrol=";                   // Prefix in enrollment responses from micro:bit devices.
let SERIAL_CMD_PREFIX = "cmd:";                 // Prefix for any command coming from the serial port.
let SENSOR_CMD_PREFIX = "cmd:sensor=";          // Specific prefix for sensor commands.

// Timing constants (in milliseconds)
let HANDSHAKE_TIMEOUT = 10 * 1000;              // Time to wait for enrolling devices.
let COMMAND_TIMEOUT = 10 * 1000;                // Time to wait for sensor command responses.

// Radio and serial configuration variables
let RADIO_GROUP = 8;
let RADIO_TRANSMIT_POWER = 7;

// ================= Global Variables =================

let state = 0;                // 0: Initial, 1: Handshake ongoing, 2: Waiting for new commands, 3: Processing sensor command.
let handshakeStartTime = 0;
let commandStartTime = 0;
let data = "";
let buffer: string[] = [];
let microbitDevices: string[] = [];
let sensorValues: string[] = [];
let response = "";

// ================= Serial Data Reception Handler =================

serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    data = serial.readLine();
    
    // Process a handshake command from the serial interface
    if (data == HANDSHAKE_COMMAND) {
        if (state == 0) {
            state = 1;
            radio.sendString(RADIO_HANDSHAKE_COMMAND);
            handshakeStartTime = input.runningTime();
        }
    }
    // Process any command that includes the SERIAL_CMD_PREFIX
    else if (data.includes(SERIAL_CMD_PREFIX)) {
        if (state == 2) {
            // For sensor commands, change state to 3 and prepare to gather sensor values.
            if (data.includes(SENSOR_CMD_PREFIX)) {
                state = 3;
                commandStartTime = input.runningTime();
                sensorValues = [];
            }
            // Split the command string and forward the command payload via radio.
            buffer = data.split(':');
            radio.sendString("" + buffer[1]);
        }
    }
});

// ================= Radio Data Reception Handler =================

radio.onReceivedString(function (receivedString: string) {
    // Process enrollment messages from micro:bit devices
    if (receivedString.includes(ENROLL_PREFIX)) {
        if (state == 1) {
            buffer = receivedString.split('=');
            microbitDevices.push(buffer[1]);
        }
    }
    // Process sensor data responses
    else if (receivedString.includes('=')) {
        if (state == 3) {
            sensorValues.push(receivedString);
        }
    }
});

// ================= Initialization =================

// Set up radio and serial parameters
radio.setGroup(RADIO_GROUP);
radio.setTransmitSerialNumber(true);
radio.setTransmitPower(RADIO_TRANSMIT_POWER);
serial.redirectToUSB();

// Show an icon at startup to indicate readiness
basic.showIcon(IconNames.Yes);

// ================= Main Loop =================

basic.forever(function () {
    basic.showNumber(state);  // Display the current state for debugging.

    if (state == 1) {  // Handshake state: waiting for device enrollment to complete.
        if (input.runningTime() - handshakeStartTime > HANDSHAKE_TIMEOUT) {
            state = 2;
            response = "";
            // Build a comma-separated response of enrolled micro:bit device names.
            for (let microbitDevice of microbitDevices) {
                if (response.length > 0) {
                    response = response + "," + microbitDevice;
                } else {
                    response = microbitDevice;
                }
            }
            serial.writeLine(ENROLL_PREFIX + response);
        }
    } else if (state == 3) {  // Sensor command state: collecting sensor values.
        if (input.runningTime() - commandStartTime > COMMAND_TIMEOUT) {
            response = "";
            // Build a comma-separated response of all sensor values received.
            for (let sensorValue of sensorValues) {
                if (response.length > 0) {
                    response = response + "," + sensorValue;
                } else {
                    response = sensorValue;
                }
            }
            serial.writeLine(response);
            state = 2;
        }
    }
});
