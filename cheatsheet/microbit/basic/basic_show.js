// display.js
// 1) Show a custom 5×5 LED frame
basic.showLeds(`
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
`)
basic.pause(500)         // Wait 0.5 seconds

// 2) Show the built‑in heart icon
basic.showIcon(IconNames.Heart)
basic.pause(500)         // Wait 0.5 seconds

// 3) Scroll the text “HI” across the display
basic.showString("HI")
basic.pause(500)         // Wait 0.5 seconds

// 4) Finally, show the number 42
basic.showNumber(42)
