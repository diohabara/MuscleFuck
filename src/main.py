import time
from signal import pause
from typing import List

from gpiozero import Button
from muscle_fuck import MuscleFuck


def main() -> None:
    mf = MuscleFuck()
    program: List[str] = []
    is_running = False
    start: float
    time_list: List[float] = []

    def display_time() -> None:
        if not time_list:
            print("Welcome to this contest")
        else:
            time_list.sort()
            for i, t in enumerate(time_list):
                print(f"{t} ranked in {i+1}")

    def button1_pressed() -> None:
        print("1")
        program.append(">")

    def button2_pressed() -> None:
        print("2")
        program.append("<")

    def button3_pressed() -> None:
        print("3")
        program.append("+")

    def button4_pressed() -> None:
        print("4")
        program.append("-")

    def button5_pressed() -> None:
        print("5")
        program.append(".")

    def button6_pressed() -> None:
        print("6")
        program.append(",")

    def button7_pressed() -> None:
        print("7")
        program.append("[")

    def button8_pressed() -> None:
        print("8")
        program.append("]")

    def button9_pressed() -> None:
        nonlocal start
        nonlocal program
        nonlocal is_running
        if is_running:
            display_time()
            start = time.time()
        else:
            time_list.append(time.time() - start)
            start = 0.0
            mf.run_from_program("".join(program))
            program = []
        is_running = not is_running

    button1 = Button(5)
    button2 = Button(6)
    button3 = Button(13)
    button4 = Button(19)
    button5 = Button(26)
    button6 = Button(12)
    button7 = Button(16)
    button8 = Button(20)
    button9 = Button(21)

    button1.when_pressed = button1_pressed
    button2.when_pressed = button2_pressed
    button3.when_pressed = button3_pressed
    button4.when_pressed = button4_pressed
    button5.when_pressed = button5_pressed
    button6.when_pressed = button6_pressed
    button7.when_pressed = button7_pressed
    button8.when_pressed = button8_pressed
    button9.when_pressed = button9_pressed
    print("Start")
    pause()


if __name__ == "__main__":
    main()
