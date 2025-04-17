let lightState = 0

input.onButtonPressed(Button.A, () => {
    if (lightState == 1) {
        lightState = 0
    } else {
        lightState = 1
    }
    pins.digitalWritePin(DigitalPin.P0, lightState)
    basic.showNumber(lightState)
})

lightState = 0
pins.digitalWritePin(DigitalPin.P0, lightState)
basic.showIcon(IconNames.Yes)
