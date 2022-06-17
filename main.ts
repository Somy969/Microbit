input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    Grade = 80
    if (Grade >= 50) {
        basic.showString("Pass :)")
    } else if (Grade >= 90) {
        basic.showString("Excellent ☆")
    } else {
        basic.showString("Fail :'(")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    number += 1
    basic.showNumber(number)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    number = 0
    for (let index = 0; index < 11; index++) {
        basic.showNumber(number)
        number += 1
    }
})
let Grade = 0
let number = 0
basic.showString("Ahilla")
number = 0
