import logging
import sys
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class MuscleFuck:
    program: str = ""
    program_ptr: int = field(default=0)
    memory: List[int] = field(default_factory=lambda: [0] * 3000)
    memory_ptr: int = field(default=0)
    output: List[str] = field(default_factory=lambda: [""] * 3000)
    output_ptr: int = field(default=0)
    stack_count: int = field(default=0)
    brace_mapping: Dict[int, int] = field(default_factory=lambda: {})

    def __del__(self) -> None:
        print("")

    def run_from_program(self, program: str) -> str:
        self.program = program
        self.brace_mapping = self._create_brace_mapping(program)
        while self.program_ptr < len(self.program):
            self._read_char(self.program[self.program_ptr])
            self.program_ptr += 1
        return "".join(self.output)

    def run_from_file(self, file_path: str) -> str:
        with open(file_path, "r") as f:
            program: List[str] = [
                self._fuck_filter(program_line) for program_line in f.readlines()
            ]
            self.run_from_program("".join(program))
        return "".join(self.output)

    def reset(self) -> None:
        self.program = ""
        self.memory, self.output = [0] * 30, [""] * 30
        self.program_ptr, self.memory_ptr, self.output_ptr = 0, 0, 0
        self.stack_count = 0

    def _err(self, message: str) -> None:
        logging.exception(message)

    def _fuck_filter(self, code: str) -> str:
        return "".join(
            filter(lambda x: x in [">", "<", "+", "-", ".", ",", "[", "]"], code)
        )

    def _create_brace_mapping(self, code: str) -> Dict[int, int]:
        temp_bracestack: List[int] = []
        brace_mapping: Dict[int, int] = {}
        for position, command in enumerate(code):
            if command == "[":
                temp_bracestack.append(position)
            if command == "]":
                start = temp_bracestack.pop()
                brace_mapping[start] = position
                brace_mapping[position] = start
        return brace_mapping

    def _read_char(self, ch: str) -> None:
        if ch == ">":
            self.memory_ptr += 1
            if len(self.memory) <= self.memory_ptr:
                self._err(f"Out of array: {self.memory_ptr=}")
        elif ch == "<":
            self.memory_ptr -= 1
            if self.memory_ptr < 0:
                self._err(f"Out of array: {self.memory_ptr=}")
        elif ch == "+":
            self.memory[self.memory_ptr] += 1
        elif ch == "-":
            self.memory[self.memory_ptr] -= 1
        elif ch == ".":
            self.output[self.output_ptr] = chr(self.memory[self.memory_ptr])
            self.output_ptr += 1
        elif ch == ",":
            self.memory[self.memory_ptr] = ord(sys.stdin.read(1))
        elif ch == "[":
            if self.memory[self.memory_ptr] == 0:
                self.program_ptr = self.brace_mapping[self.program_ptr]
        elif ch == "]":
            if self.memory[self.memory_ptr] != 0:
                self.program_ptr = self.brace_mapping[self.program_ptr]
        else:
            self._err(f"Does not accept this character: {ch=}")
