import time
from signal import pause
from typing import List

from gpiozero import Button
from muscle_fuck import MuscleFuck

is_running = False
start: float
program: List[str] = []


def main() -> None:
    mf = MuscleFuck()
    time_list: List[float] = []

    def display_time() -> None:
        if not time_list:
            print("Welcome to this contest")
        else:
            time_list.sort()
            for i, t in enumerate(time_list):
                print(f"You score {t} ranked in {i+1}")

    def button1_pressed() -> None:
        print(">")
        program.append(">")

    def button2_pressed() -> None:
        print("<")
        program.append("<")

    def button3_pressed() -> None:
        print("+")
        program.append("+")

    def button4_pressed() -> None:
        print("-")
        program.append("-")

    def button5_pressed() -> None:
        print(".")
        program.append(".")

    def button6_pressed() -> None:
        print(",")
        program.append(",")

    def button7_pressed() -> None:
        print("[")
        program.append("[")

    def button8_pressed() -> None:
        print("]")
        program.append("]")

    def button9_pressed() -> None:
        global start
        global program
        global is_running
        if is_running:
            display_time()
            start = time.time()
            program = []
        else:
            time_list.append(time.time() - start)
            mf.run_from_program("".join(program))
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
