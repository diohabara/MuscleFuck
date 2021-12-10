import time
from typing import List

from gpiozero import Button
from muscle_fuck import MuscleFuck


def main() -> None:
    def display_time() -> None:
        if not time_list:
            print("Welcome to this contest")
        else:
            time_list.sort()
            for i, t in enumerate(time_list):
                print(f"{t} ranked in {i+1}")

    print("Start")
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
    start: float
    time_list: List[float] = []

    while True:
        if button9.is_pressed:
            if is_running:
                display_time()
                start = time.time()
            else:
                time_list.append(time.time() - start)
                start = 0.0
                mf.run_from_program("".join(program))
                program = []
            is_running = not is_running
        if button1.is_pressed:
            print("1")
            program.append(">")
        if button2.is_pressed:
            print("2")
            program.append("<")
        if button3.is_pressed:
            print("3")
            program.append("+")
        if button4.is_pressed:
            print("4")
            program.append("-")
        if button5.is_pressed:
            print("5")
            program.append(".")
        if button6.is_pressed:
            print("6")
            program.append(",")
        if button7.is_pressed:
            print("7")
            program.append("[")
        if button8.is_pressed:
            print("8")
            program.append("]")


if __name__ == "__main__":
    main()
