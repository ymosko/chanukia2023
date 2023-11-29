def on_button_pressed_a():
    basic.show_string("happy chanukkah")
    pins.digital_write_pin(DigitalPin.P5, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P2, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P3, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P4, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P6, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P7, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P8, 1)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(10000)
    pins.digital_write_pin(DigitalPin.P5, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P3, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P4, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P6, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P7, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P8, 0)
    basic.pause(200)
    pins.digital_write_pin(DigitalPin.P9, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_six_g():
    pass
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_sound_loud():
    basic.show_string("thank you chayalim")
    basic.clear_screen()
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_ab():
    music.stop_all_sounds()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P2, 1)
    pins.digital_write_pin(DigitalPin.P3, 1)
    pins.digital_write_pin(DigitalPin.P4, 1)
    pins.digital_write_pin(DigitalPin.P5, 1)
    pins.digital_write_pin(DigitalPin.P6, 1)
    pins.digital_write_pin(DigitalPin.P7, 1)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(500)
    pins.digital_write_pin(DigitalPin.P1, 1)
    pins.digital_write_pin(DigitalPin.P3, 1)
    pins.digital_write_pin(DigitalPin.P5, 1)
    pins.digital_write_pin(DigitalPin.P7, 1)
    pins.digital_write_pin(DigitalPin.P9, 1)
    basic.pause(500)
    pins.digital_write_pin(DigitalPin.P2, 1)
    pins.digital_write_pin(DigitalPin.P4, 1)
    pins.digital_write_pin(DigitalPin.P6, 1)
    pins.digital_write_pin(DigitalPin.P8, 1)
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 0)
    pins.digital_write_pin(DigitalPin.P3, 0)
    pins.digital_write_pin(DigitalPin.P4, 0)
    pins.digital_write_pin(DigitalPin.P5, 0)
    pins.digital_write_pin(DigitalPin.P6, 0)
    pins.digital_write_pin(DigitalPin.P7, 0)
    pins.digital_write_pin(DigitalPin.P8, 0)
    pins.digital_write_pin(DigitalPin.P9, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    for index in range(10):
        music.play(music.create_sound_expression(WaveShape.SINE,
                5000,
                2811,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        for index2 in range(10):
            music.play(music.create_sound_expression(WaveShape.SQUARE,
                    5000,
                    4894,
                    255,
                    255,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_sound_expression(WaveShape.SAWTOOTH,
                5000,
                2877,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        for index3 in range(10):
            music.play(music.create_sound_expression(WaveShape.NOISE,
                    5000,
                    4073,
                    255,
                    255,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.UNTIL_DONE)
    if input.button_is_pressed(Button.AB):
        music.stop_all_sounds()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_three_g():
    for index4 in range(10):
        music.play(music.create_sound_expression(WaveShape.SINE,
                5000,
                2811,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        for index5 in range(10):
            music.play(music.create_sound_expression(WaveShape.SQUARE,
                    5000,
                    4894,
                    255,
                    255,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.UNTIL_DONE)
        music.play(music.create_sound_expression(WaveShape.SAWTOOTH,
                5000,
                2877,
                255,
                255,
                500,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
        for index6 in range(10):
            music.play(music.create_sound_expression(WaveShape.NOISE,
                    5000,
                    4073,
                    255,
                    255,
                    500,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LINEAR),
                music.PlaybackMode.UNTIL_DONE)
    if input.button_is_pressed(Button.AB):
        music.stop_all_sounds()
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)
