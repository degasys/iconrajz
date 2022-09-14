def on_button_pressed_a():
    basic.show_string("Hello Ali!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_icon(IconNames.SAD)
    basic.pause(500)
    basic.show_icon(IconNames.HAPPY)
    basic.pause(500)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_string("Hello Béla!")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_arrow(ArrowNames.NORTH)
basic.pause(200)
basic.show_arrow(ArrowNames.EAST)
basic.pause(200)
basic.show_arrow(ArrowNames.SOUTH)
basic.pause(200)
basic.show_arrow(ArrowNames.WEST)

def on_forever():
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . # # # .
                . . # . .
    """)
    basic.pause(500)
    basic.show_leds("""
        . . # . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.pause(500)
    basic.show_leds("""
        . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
    """)
    basic.pause(500)
    basic.clear_screen()
    basic.pause(200)
basic.forever(on_forever)
