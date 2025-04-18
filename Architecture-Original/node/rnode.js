radio.onReceivedString(function (receivedString) {
    if (receivedString == "handshake") {
        //basic.showString("H")
        if (state == 0) {
            state = 1
            radio.sendString("enrol=" + control.deviceName())
        }
    } else {
        if (state == 1) {
            buffer = receivedString.split("=")
            commandKey = buffer[0]
            commandValue = buffer[1]
            if (commandKey == "sensor") {
                //basic.showString("S")
                if (commandValue == "temp") {
                    radio.sendString("" + control.deviceName() + "=" + pins.analogReadPin(AnalogPin.P0))
                    // radio.sendString("" + control.deviceName() + "=" + input.temperature())
                }
            }
        }
    }
})
let commandValue = ""
let commandKey = ""
let buffer: string[] = []
let state = 0
radio.setGroup(8)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    basic.showNumber(state)
    // led.plotBarGraph(
    //     pins.analogReadPin(AnalogPin.P0),
    //     650
    // )
})
