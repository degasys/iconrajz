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
