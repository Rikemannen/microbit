input.onButtonPressed(Button.A, function mode() {
    
    dice = !dice
    console.log(dice)
})
input.onButtonPressed(Button.B, function clear() {
    basic.clearScreen()
})
function rps_func() {
    
    hand = randint(1, 3)
    console.log("number: " + ("" + ("" + hand)))
    if (hand == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (hand == 2) {
        basic.showLeds(`
            . . . # #
            . # # # #
            . # # # .
            # # # # .
            # # . . .
            `)
    } else {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            `)
    }
    
}

function dice_func() {
    
    num = randint(1, 6)
    if (num == 1) {
        basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        `)
    } else if (num == 2) {
        basic.showLeds(`
        . . . . .
        . . . # .
        . . . . .
        . # . . .
        . . . . .
        `)
    } else if (num == 3) {
        basic.showLeds(`
        . . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . .
        `)
    } else if (num == 4) {
        basic.showLeds(`
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        `)
    } else if (num == 5) {
        basic.showLeds(`
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        `)
    } else {
        basic.showLeds(`
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `)
    }
    
}

input.onGesture(Gesture.Shake, function on_gesture_shake() {
    if (dice) {
        dice_func()
    } else {
        rps_func()
    }
    
})
let hand = 0
let num = 0
let dice = false
