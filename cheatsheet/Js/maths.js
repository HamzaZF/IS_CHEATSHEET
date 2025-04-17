// math_cheatsheet.js
let x = 3.7

let rounded    = Math.round(x)       // ↪ Round x to the nearest integer (4)
let floored    = Math.floor(x)       // ↪ Round x down to the next integer (3)
let ceiled     = Math.ceil(x)        // ↪ Round x up to the next integer (4)
let absolute   = Math.abs(-x)        // ↪ Absolute value of x (3.7)
let power      = Math.pow(2, 3)      // ↪ 2⁸ = 8
let root       = Math.sqrt(16)       // ↪ Square root of 16 (4)
let randFloat  = Math.random()       // ↪ Random float in [0,1)
let minVal     = Math.min(5, 10, -3) // ↪ Smallest of the list (-3)
let maxVal     = Math.max(5, 10, -3) // ↪ Largest of the list (10)
let signOf     = Math.sign(-42)      // ↪ Sign of -42: -1
let ln         = Math.log(Math.E)    // ↪ Natural log of e (1)
let expOf      = Math.exp(2)         // ↪ e² ≈ 7.389
let sine       = Math.sin(Math.PI/2) // ↪ Sine of π/2 radians (1)
let cosine     = Math.cos(0)         // ↪ Cosine of 0 radians (1)
let tangent    = Math.tan(Math.PI/4) // ↪ Tangent of π/4 (1)

// Utility: random integer between min and max (inclusive)
function randomRange(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min
}
let rndInt     = randomRange(0, 9999) // ↪ e.g. 0–9999
