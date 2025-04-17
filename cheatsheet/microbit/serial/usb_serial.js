// usb_serial.js
// Micro:bit USB serial cheatsheet

// Force serial over USB (otherwise it’s the default on most editors)
serial.redirectToUSB()

// Send a line of text over USB
serial.writeLine("Hello, USB!")

// Send a number
serial.writeNumber(123)

// Send a key/value pair
serial.writeValue("temp", 25)

// Send multiple numbers
serial.writeNumbers([10, 20, 30])

// Read incoming data terminated by newline
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), () => {
    let line = serial.readLine()
    basic.showString(line)    // or process as needed
})
