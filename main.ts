input.onButtonPressed(Button.A, function () {
    basic.showString("happy chanukkah")
    pins.digitalWritePin(DigitalPin.P5, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P3, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P4, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P6, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P7, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P8, 1)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P9, 1)
    basic.pause(10000)
    pins.digitalWritePin(DigitalPin.P5, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P3, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P4, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P6, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P7, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P8, 0)
    basic.pause(200)
    pins.digitalWritePin(DigitalPin.P9, 0)
})
input.onGesture(Gesture.SixG, function () {
	
})
input.onSound(DetectedSound.Loud, function () {
    basic.showString("thank you chayalim")
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    pins.digitalWritePin(DigitalPin.P1, 0)
    pins.digitalWritePin(DigitalPin.P2, 0)
    pins.digitalWritePin(DigitalPin.P3, 0)
    pins.digitalWritePin(DigitalPin.P4, 0)
    pins.digitalWritePin(DigitalPin.P5, 0)
    pins.digitalWritePin(DigitalPin.P6, 0)
    pins.digitalWritePin(DigitalPin.P7, 0)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
    pins.digitalWritePin(DigitalPin.P6, 0)
    pins.digitalWritePin(DigitalPin.P7, 0)
    pins.digitalWritePin(DigitalPin.P8, 0)
    pins.digitalWritePin(DigitalPin.P9, 0)
})
input.onButtonPressed(Button.B, function () {
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P2, 1)
    pins.digitalWritePin(DigitalPin.P3, 1)
    pins.digitalWritePin(DigitalPin.P4, 1)
    pins.digitalWritePin(DigitalPin.P5, 1)
    pins.digitalWritePin(DigitalPin.P6, 1)
    pins.digitalWritePin(DigitalPin.P7, 1)
    pins.digitalWritePin(DigitalPin.P8, 1)
    pins.digitalWritePin(DigitalPin.P9, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P1, 1)
    pins.digitalWritePin(DigitalPin.P3, 1)
    pins.digitalWritePin(DigitalPin.P5, 1)
    pins.digitalWritePin(DigitalPin.P7, 1)
    pins.digitalWritePin(DigitalPin.P9, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P2, 1)
    pins.digitalWritePin(DigitalPin.P4, 1)
})
input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index < 10; index++) {
        music.play(music.createSoundExpression(WaveShape.Sine, 5000, 2811, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        for (let index = 0; index < 10; index++) {
            music.play(music.createSoundExpression(WaveShape.Square, 5000, 4894, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        }
        music.play(music.createSoundExpression(WaveShape.Sawtooth, 5000, 2877, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        for (let index = 0; index < 10; index++) {
            music.play(music.createSoundExpression(WaveShape.Noise, 5000, 4073, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        }
    }
    if (input.buttonIsPressed(Button.AB)) {
        music.stopAllSounds()
    }
})
input.onGesture(Gesture.ThreeG, function () {
    for (let index = 0; index < 10; index++) {
        music.play(music.createSoundExpression(WaveShape.Sine, 5000, 2811, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        for (let index = 0; index < 10; index++) {
            music.play(music.createSoundExpression(WaveShape.Square, 5000, 4894, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        }
        music.play(music.createSoundExpression(WaveShape.Sawtooth, 5000, 2877, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        for (let index = 0; index < 10; index++) {
            music.play(music.createSoundExpression(WaveShape.Noise, 5000, 4073, 255, 255, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
        }
    }
    if (input.buttonIsPressed(Button.AB)) {
        music.stopAllSounds()
    }
})
