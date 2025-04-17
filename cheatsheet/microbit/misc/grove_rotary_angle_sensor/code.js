let value = 0

basic.showIcon(IconNames.Yes)

basic.forever(function () {
    value = pins.analogReadPin(AnalogPin.P0)
    led.plotBarGraph(value, 1023)
    if (value < 512) {
        pins.digitalWritePin(DigitalPin.P1, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    basic.pause(10)
})
