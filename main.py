def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Grade
    Grade = 80
    if Grade >= 50:
        basic.show_string("Pass :)")
    elif Grade >= 90:
        basic.show_string("Excellent ☆")
    else:
        basic.show_string("Fail :'(")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global number
    number += 1
    basic.show_number(number)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global number
    number = 0
    for index in range(11):
        basic.show_number(number)
        number += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Grade = 0
number = 0
basic.show_string("Ahilla")
number = 0