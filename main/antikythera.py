from typing import List

class Rotor:
    def __init__(self, contents):
        self.contents = contents


class Antikythera:
    num_rotors: int
    num_columns: int
    target_sum: int
    rotors: List[Rotor]

    def __init__(self, rotors: int, columns: int, sum: int):
        self.rotors = []
        self.num_rotors = rotors
        self.num_columns = columns
        self.target_sum = sum
        print(
            f"Creating a {self.num_rotors}-rotor puzzle with {self.num_columns} columns of numbers that sum up to {self.target_sum}."
        )

    def add_rotor(self, rotor: Rotor):
        self.rotors.append(rotor)
