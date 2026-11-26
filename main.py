def on_gesture_shake():
    global hand, oldhand
    while hand == oldhand:
        hand = randint(1, 3)
    print("number: " + str(hand))
    if hand == 0:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif hand == 1:
        basic.show_leds("""
            . . . # #
            . # # # #
            . # # # .
            # # # # .
            # # . . .
            """)
    else:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            # # . # #
            # # . # #
            """)
    oldhand = hand
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

oldhand = 0
hand = 0