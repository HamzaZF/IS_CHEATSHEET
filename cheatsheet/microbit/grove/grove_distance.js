basic.forever(() => {
    let d = grove.measureInCentimeters(DigitalPin.P1)
    basic.showNumber(d)
    basic.pause(1000)
})
