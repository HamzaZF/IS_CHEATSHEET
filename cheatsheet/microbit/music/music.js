// music.js

// 1) Play a single tone: Middle C (262 Hz) for a whole beat
music.playTone(262, music.beat(BeatFraction.Whole))
basic.pause(500)

// 2) Play a C major scale with half‑beats
const scale = [262, 294, 330, 349, 392, 440, 494, 523]
for (let note of scale) {
    music.playTone(note, music.beat(BeatFraction.Half))
    basic.pause(50)
}

// 3) Play the built‑in "Birthday" melody once
music.beginMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.Once)
basic.pause(2000)

// 4) Adjust volume and tempo, then play a custom melody string
music.setVolume(180)      // Volume range: 0–255
music.setTempo(120)       // Tempo in BPM
music.playMelody("C5 B A G F E D C ", 120)

// 5) Rest for a whole beat, then disable the speaker
music.rest(music.beat(BeatFraction.Whole))
basic.pause(500)
music.setBuiltInSpeakerEnabled(false)

// Signal completion
basic.showString("Done")
