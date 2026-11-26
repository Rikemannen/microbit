input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    while (hand == oldhand) {
        hand = randint(1, 3)
    }
    console.log("number: " + ("" + hand))
    if (hand == 0) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (hand == 1) {
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
    
    oldhand = hand
})
let oldhand = 0
let hand = 0
