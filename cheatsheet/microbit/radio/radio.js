// radio.js
// Comprehensive micro:bit radio API cheatsheet for MakeCode JS

// --- Basic Configuration ---
radio.setGroup(1)                          // Set radio group (0–255)
radio.setTransmitPower(7)                  // Set power level (0=min, 7=max)
radio.setTransmitSerialNumber(true)        // Include sender serial in packets
radio.setFrequencyBand(7)                  // (optional) set frequency band (0–83)

// --- Sending Data ---
radio.sendString("Hello")                // Send a short string (max 19 chars)
radio.sendNumber(123)                      // Send a number (32‑bit signed)
radio.sendValue("key", 456)              // Send a key/value pair (key max 8 chars)

// --- Receiving Data ---
radio.onReceivedString(msg => {
    // Received a string
    basic.showString("S:" + msg)
})
radio.onReceivedNumber(num => {
    // Received a number
    basic.showNumber(num)
})
radio.onReceivedValue((name, value) => {
    // Received key and value
    basic.showString(name + ":" + value)
})

// --- Received Packet Metadata ---
radio.onReceivedPacket(packet => {
    let strength = packet.signal;          // RSSI signal strength
    let serial  = packet.serial;          // Sender device serial number
    let time    = packet.time;            // Timestamp when received
    // Example display
    basic.showString("R:" + strength)
})

// --- Utility ---
radio.reset()                              // Reset the radio module
radio.powerOff()                           // Turn off radio to save power
radio.powerOn()                            // Turn radio back on after powerOff

// Note: Always use matching group and frequencies on all devices to communicate!
