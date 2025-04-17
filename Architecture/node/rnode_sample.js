// Customizable Settings
let HANDSHAKE_COMMAND = "handshake";      // The handshake command sent from the transmitter.
let ENROLL_COMMAND_PREFIX = "enrol=";       // Prefix for enrollment messages.
let RADIO_GROUP = 8;                        // Radio group number.
let RADIO_TRANSMIT_POWER = 7;               // Radio transmit power.
let RANDOM_WAIT_MIN = 100;                  // Minimum random wait time in milliseconds.
let RANDOM_WAIT_MAX = 9900;                 // Maximum random wait time in milliseconds.

// Global Variables for State and Data
let state = 0;
let commandKey = "";
let commandValue = "";
let randomWaitPeriod = 0;
let buffer: string[] = [];

// Define a type for command specifications
type CommandSpec = {
    key: string,
    value: string,
    action: () => void
};

// Array of commands with their specifications.
// You can add, remove, or modify commands here.
let commands: CommandSpec[] = [
    {
        key: "sensor",
        value: "temp",
        action: function () {
            randomWait();
            // Sends a response with current temperature.
            radio.sendString(control.deviceName() + "=" + input.temperature());
            basic.showString("T");
        }
    },
    // Add another command example if needed.
    {
        key: "sensor",
        value: "light",
        action: function () {
            randomWait();
            // Example action for a light sensor (replace with actual sensor reading if available).
            let lightLevel = input.lightLevel();
            radio.sendString(control.deviceName() + "=" + lightLevel);
            basic.showString("L");
        }
    }
];

// Radio Message Reception Handler
radio.onReceivedString(function (receivedString: string) {
    if (receivedString == HANDSHAKE_COMMAND) {
        basic.showString("H");
        if (state == 0) {
            state = 1;
            randomWait();
            // Send enrollment message using the custom prefix.
            radio.sendString(ENROLL_COMMAND_PREFIX + control.deviceName());
        }
    } else {
        basic.showString("R");
        if (state == 1) {
            // Split the received message into command key and command value.
            buffer = receivedString.split('=');
            commandKey = buffer[0];
            commandValue = buffer[1];

            // Iterate over the array to see if there is a matching command.
            for (let i = 0; i < commands.length; i++) {
                // If both key and value match, execute the corresponding action.
                if (commands[i].key == commandKey && commands[i].value == commandValue) {
                    commands[i].action();
                    break;  // Stop after the first match.
                }
            }
        }
    }
});

// Function to introduce a random wait period to mitigate message collisions.
function randomWait (): void {
    randomWaitPeriod = Math.randomRange(RANDOM_WAIT_MIN, RANDOM_WAIT_MAX);
    basic.pause(randomWaitPeriod);
}

// Button A displays the latest command key/value received.
input.onButtonPressed(Button.A, function () {
    basic.showString("[" + commandKey + "=" + commandValue + "]");
});

// Button A+B displays the device name.
input.onButtonPressed(Button.AB, function () {
    basic.showString("DN:" + control.deviceName());
});

// Radio Setup and Initialization
radio.setGroup(RADIO_GROUP);
radio.setTransmitSerialNumber(true);
radio.setTransmitPower(RADIO_TRANSMIT_POWER);

// Show an icon on startup to indicate that the device is ready.
basic.showIcon(IconNames.Yes);

// An empty forever loop to keep the program running.
basic.forever(function () {
    // Additional repetitive tasks can be added here if necessary.
});
