// input_gestures.js
// Respond to common micro:bit gestures with icons

input.onGesture(Gesture.Shake, () => {
    basic.clearScreen()
    basic.showIcon(IconNames.Surprised)   // 🤯
})

input.onGesture(Gesture.TiltLeft, () => {
    basic.clearScreen()
    basic.showArrow(ArrowNames.West)      // ←
})

input.onGesture(Gesture.TiltRight, () => {
    basic.clearScreen()
    basic.showArrow(ArrowNames.East)      // →
})

input.onGesture(Gesture.LogoUp, () => {
    basic.clearScreen()
    basic.showArrow(ArrowNames.North)     // ↑
})

input.onGesture(Gesture.LogoDown, () => {
    basic.clearScreen()
    basic.showArrow(ArrowNames.South)     // ↓
})
