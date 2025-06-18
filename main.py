def on_button_pressed_b():
    global result
    result = result + 1
    if number_1 + number_2 == result:
        music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_icon(IconNames.YES)
        basic.show_icon(IconNames.YES)
        basic.show_icon(IconNames.YES)
        result = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

result = 0
number_2 = 0
number_1 = 0
number_1 = 1
number_2 = 2
result = 0

def on_forever():
    basic.show_leds("""
        . # # . .
        . . # . .
        . . # . .
        . . # . .
        . # # # .
        """)
    basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        . # # # .
        . . . # .
        . . # . .
        . # . . .
        . # # # .
        """)
basic.forever(on_forever)
