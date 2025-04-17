// string_cheatsheet.js
let s = " Hello, MakeCode! "

let len        = s.length                       // ↪ Number of characters
let charAt1    = s.charAt(1)                    // ↪ Character at index 1 ("H")
let sub        = s.substr(1, 5)                 // ↪ 5‑char substring from index 1 ("Hello")
let idx        = s.indexOf("Make")              // ↪ Starting index of "Make" (7)
let lower      = s.toLowerCase()                // ↪ All lowercase (" hello, makecode! ")
let upper      = s.toUpperCase()                // ↪ All UPPERCASE (" HELLO, MAKECODE! ")
let trimmed    = s.trim()                       // ↪ Remove edges ("Hello, MakeCode!")
let parts      = trimmed.split(", ")            // ↪ Split into ["Hello", "MakeCode!"]
let replaced   = s.replace("Make", "Code")      // ↪ Replace first "Make" → "Code"
let replacedAll= s.replaceAll("e", "3")         // ↪ Replace all "e" → "3"
let concatenated = trimmed.concat(" Rocks")     // ↪ "Hello, MakeCode! Rocks"
let includesMC  = s.includes("MC")              // ↪ true if "MC" appears
let startsWithSpace = s.startsWith(" ")         // ↪ true if s begins with a space
let endsWithBang   = s.endsWith("!")            // ↪ true if s ends with "!"
let repeated   = trimmed.repeat(2)              // ↪ The string twice
let padStart   = trimmed.padStart(20, "*")      // ↪ Left‑pad up to length 20
let padEnd     = trimmed.padEnd(20, "*")        // ↪ Right‑pad up to length 20
