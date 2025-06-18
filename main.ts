input.onButtonPressed(Button.B, function () {
    result = result + 1
    if (number_1 + number_2 == result) {
        basic.clearScreen()
        music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Entertainer), music.PlaybackMode.InBackground)
        basic.showString("" + (result))
        basic.pause(5000)
        number_1 = randint(1, 9)
        number_2 = randint(1, 9)
        result = 0
    }
})
let result = 0
let number_2 = 0
let number_1 = 0
number_1 = randint(1, 9)
number_2 = randint(1, 9)
result = 0
basic.forever(function () {
    basic.showString("" + (number_1))
    basic.showLeds(`
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        `)
    basic.showString("" + (number_2))
})
