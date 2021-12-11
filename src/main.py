import time
from dataclasses import dataclass, field
from signal import pause
from typing import List

from gpiozero import Button

from muscle_fuck import MuscleFuck


@dataclass
class OnRaspberry:
    mf: MuscleFuck = MuscleFuck()
    scoreboard: List[float] = field(default_factory=lambda: [])
    is_running: float = field(default=False)
    start: float = field(default_factory=lambda: time.time())
    program: List[str] = field(default_factory=lambda: [])

    def _display_scoreboard(self) -> None:
        if not self.scoreboard:
            print("Welcome to this contest")
        else:
            self.scoreboard.sort()
            for i, t in enumerate(self.scoreboard):
                print(f"Your score is {t}: rank {i+1}")

    def run(self) -> None:
        def button1_pressed() -> None:
            print(">", end="")
            self.program.append(">")

        def button2_pressed() -> None:
            print("<", end="")
            self.program.append("<")

        def button3_pressed() -> None:
            print("+", end="")
            self.program.append("+")

        def button4_pressed() -> None:
            print("-", end="")
            self.program.append("-")

        def button5_pressed() -> None:
            print(".", end="")
            self.program.append(".")

        def button6_pressed() -> None:
            print(",", end="")
            self.program.append(",")

        def button7_pressed() -> None:
            print("[", end="")
            self.program.append("[")

        def button8_pressed() -> None:
            print("]", end="")
            self.program.append("]")

        def button9_pressed() -> None:
            if self.is_running:
                self._display_scoreboard()
                self.start = time.time()
                self.program = []
            else:
                self.scoreboard.append(time.time() - self.start)
                self.mf.run_from_program("".join(self.program))
            self.is_running = not self.is_running

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
    ras = OnRaspberry()
    ras.run()
