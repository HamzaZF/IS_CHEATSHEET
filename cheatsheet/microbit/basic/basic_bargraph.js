// bargraph.js
let level = 0
basic.forever(() => {
    level = Math.randomRange(0, 100)
    led.plotBarGraph(level, 100)
    basic.pause(500)
})
