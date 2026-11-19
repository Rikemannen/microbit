def on_forever():
    led.toggle_all()
    basic.pause(10)
basic.forever(on_forever)
