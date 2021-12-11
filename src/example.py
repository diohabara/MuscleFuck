from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

button1 = Button(2)
button2 = Button(6)
button3 = Button(13)
button4 = Button(19)
button5 = Button(26)

button1.when_pressed = say_hello
button2.when_pressed = say_hello
button3.when_pressed = say_hello
button4.when_pressed = say_hello
button5.when_pressed = say_hello

pause()
