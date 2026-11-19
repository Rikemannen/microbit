run = False

def on_button_pressed_a():
    global run
    run = not run
    print("Switched, now " + str(run))

def on_forever():
    if run:
        led.toggle_all()
    basic.pause(10)

input.on_button_pressed(Button.A, on_button_pressed_a)
basic.forever(on_forever)
