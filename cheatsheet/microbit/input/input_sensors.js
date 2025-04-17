// sensor_data.js
// micro:bit sensor input cheatsheet—just the input calls

input.temperature()                   // °C
input.lightLevel()                    // 0–255 ambient light
input.compassHeading()                // 0–359° compass
input.acceleration(Dimension.X)       // X‑axis accel (mg)
input.acceleration(Dimension.Y)       // Y‑axis accel (mg)
input.acceleration(Dimension.Z)       // Z‑axis accel (mg)
input.acceleration(Dimension.Strength)// Combined accel strength (mg)
input.rotation(Rotation.Pitch)        // Pitch angle (°)
input.rotation(Rotation.Roll)         // Roll angle (°)
