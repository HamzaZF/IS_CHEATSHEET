// pins.js

// --- Digital I/O ---
// Set digital pin P0 HIGH (1) or LOW (0)
pins.digitalWritePin(DigitalPin.P0, 1)
// Read digital state (0 or 1)
let digitalValue = pins.digitalReadPin(DigitalPin.P0)

// --- Analog (PWM) I/O ---
// Read analog value (0–1023) from pin P1
let analogValue = pins.analogReadPin(AnalogPin.P1)
// Write PWM value (0–1023) to pin P1
pins.analogWritePin(AnalogPin.P1, 512)

// --- Capacitive Touch ---
// Check if pin P3 is touched (true/false)
let touched = pins.touchIsPressed(DigitalPin.P3)

// --- Pulse Measurement ---
// Measure pulse width (microseconds) on P4
let pulseDuration = pins.pulseIn(
    DigitalPin.P4,      // the pin you’re listening on
    PulseValue.High,    // whether you’re measuring a HIGH pulse (1) or LOW pulse (0)
    1_000_000           // timeout in microseconds (1 000 000 µs = 1 s)
  )
  
// --- Serial on Pins ---
// Redirect serial TX/RX to P0/P1 at 115200 baud
serial.redirect(SerialPin.P0, SerialPin.P1, BaudRate.BaudRate115200)
