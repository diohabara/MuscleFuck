import time
from typing import Dict, List

from gpiozero import Button

from muscle_fuck import MuscleFuck


def main() -> None:
    def display_time() -> None:
        # TODO: display time and run-length distance
        print("hello")

    # TODO: fill in the buttons' IDs
    button1 = Button(5)
    button2 = Button(6)
    button3 = Button(13)
    button4 = Button(19)
    button5 = Button(26)
    button6 = Button(12)
    button7 = Button(16)
    button8 = Button(20)
    button9 = Button(21)

    mf = MuscleFuck()
    program: List[str] = []
    is_running = False

    while True:
        if button9.is_pressed:
            if is_running:
                display_time()
            else:
                mf.run_from_program("".join(program))
                program = []
            is_running = not is_running
        if button1.is_pressed:
            program.append(">")
        if button2.is_pressed:
            program.append("<")
        if button3.is_pressed:
            program.append("+")
        if button4.is_pressed:
            program.append("-")
        if button5.is_pressed:
            program.append(".")
        if button6.is_pressed:
            program.append(",")
        if button7.is_pressed:
            program.append("[")
        if button8.is_pressed:
            program.append("]")


if __name__ == "__main__":
    main()
