// pin_serial.js
// Micro:bit pin‑based serial cheatsheet

// Redirect RX to P0 and TX to P1 at 115200 baud
serial.redirect(
    SerialPin.P0,
    SerialPin.P1,
    BaudRate.BaudRate115200
)

// Send a line of text over pins
serial.writeLine("Hello, pins!")

// Send a number
serial.writeNumber(456)

// Send a key/value pair
serial.writeValue("humi", 80)

// Read incoming data terminated by newline on pins
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), () => {
    let line = serial.readLine()
    basic.showString(line)    // or process as needed
})