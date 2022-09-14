input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("Hello Ali!")
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showIcon(IconNames.Sad)
    basic.pause(500)
    basic.showIcon(IconNames.Happy)
    basic.pause(500)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("Hello Béla!")
})
basic.showArrow(ArrowNames.North)
basic.pause(200)
basic.showArrow(ArrowNames.East)
basic.pause(200)
basic.showArrow(ArrowNames.South)
basic.pause(200)
basic.showArrow(ArrowNames.West)
basic.forever(function on_forever() {
    basic.showLeds(`
        . . # . .
                . # # # .
                # . # . #
                . # # # .
                . . # . .
    `)
    basic.pause(500)
    basic.showLeds(`
        . . # . .
                . # # # .
                # # # # #
                . # # # .
                . . # . .
    `)
    basic.pause(500)
    basic.showLeds(`
        . . # . .
                . . # . .
                # # # # #
                . . # . .
                . . # . .
    `)
    basic.pause(500)
    basic.clearScreen()
    basic.pause(200)
})
