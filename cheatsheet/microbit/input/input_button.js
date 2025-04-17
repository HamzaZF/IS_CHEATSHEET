// input_buttons.js
// Display which button was pressed: A, B, or both (A+B)

input.onButtonPressed(Button.A, () => {
    basic.clearScreen()
    basic.showString("A")
})

input.onButtonPressed(Button.B, () => {
    basic.clearScreen()
    basic.showString("B")
})

input.onButtonPressed(Button.AB, () => {
    basic.clearScreen()
    basic.showString("A+B")
})
