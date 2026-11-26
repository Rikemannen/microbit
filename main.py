def mode():
    global dice
    dice = not dice
    print(dice)
input.on_button_pressed(Button.A, mode)

def clear():
    basic.clear_screen()
input.on_button_pressed(Button.B, clear)

def rps_func():
    global hand
    hand = randint(1, 3)
    print("number: " + ("" + str(hand)))
    if hand == 1:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
    elif hand == 2:
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

def dice_func():
    global num
    num = randint(1, 6)
    if num == 1:
        basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    elif num == 2:
        basic.show_leds("""
        . . . . .
        . . . # .
        . . . . .
        . # . . .
        . . . . .
        """)
    elif num == 3:
        basic.show_leds("""
        . . . . .
        . # . . .
        . . # . .
        . . . # .
        . . . . .
        """)
    elif num == 4:
        basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
    elif num == 5:
        basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """)
    else:
        basic.show_leds("""
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        """)

def on_gesture_shake():
    if dice:
        dice_func()
    else:
        rps_func()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

hand = 0
num = 0
dice = False