let run = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    run = !run
    console.log("Switched, now " + ("" + run))
})
basic.forever(function on_forever() {
    if (run) {
        led.toggleAll()
    }
    
    basic.pause(10)
})
