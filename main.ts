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
