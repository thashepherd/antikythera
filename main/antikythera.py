from typing import Dict, List, Optional
import time


class Rotor:
    _contents: Dict[int, List[Optional[int]]]

    rotation_increment: int = 0
    rotated_contents: Dict[int, List[Optional[int]]]

    def __init__(self, contents: Dict[int, List[Optional[int]]]):
        for layer in contents:
            assert len(contents[layer]) == len(contents[0])

        self._contents = contents
        self.rotated_contents = self._contents.copy()

    def num_columns(self) -> int:
        return len(self._contents[0])

    def rotate(self):
        self.rotation_increment += 1
        for layer in self.rotated_contents.keys():
            self.rotated_contents[layer] = (
                self.rotated_contents[layer][1:] + self.rotated_contents[layer][:1]
            )

    def reset_rotation(self):
        self.rotation_increment = 0
        self.rotated_contents = self._contents.copy()

    def to_str(self) -> str:
        result_str = f"Rotation increment: {self.rotation_increment}\n"
        for layer in self.rotated_contents:
            result_str += f"Layer {layer}: {self.rotated_contents[layer]} \n"
        return result_str


class Antikythera:
    num_rotors: int
    num_columns: int
    num_layers: int
    target_sum: int
    rotors: List[Rotor]

    def __init__(self, rotors: int, layers: int, columns: int, sum: int):
        self.rotors = []
        self.num_rotors = rotors
        self.num_layers = layers
        self.num_columns = columns
        self.target_sum = sum
        print(
            f"Creating a {self.num_rotors}-rotor puzzle with {self.num_columns} columns of {self.num_layers} layers of numbers that sum up to {self.target_sum}."
        )

    def add_rotor(self, rotor: Rotor):
        if rotor.num_columns() != self.num_columns:
            raise Exception(
                f"Added rotor has {rotor.num_columns()} columns but this puzzle is set for {self.num_columns}"
            )
        self.rotors.append(rotor)

    def reset_rotors(self):
        for rotor in self.rotors:
            rotor.reset_rotation()

    def read_column(self, column_index: int) -> int:
        column: list[int] = []
        for layer in range(0, self.num_layers):
            for rotor in self.rotors:
                if not layer in rotor.rotated_contents.keys():
                    continue
                if rotor.rotated_contents[layer][column_index]:
                    column.append(rotor.rotated_contents[layer][column_index])
                    break
        assert len(column) == self.num_layers
        return column

    def is_solved(self) -> bool:
        if sum(self.read_column(0)) == self.target_sum:
            for col in range(1, self.num_columns):
                if not sum(self.read_column(col)) == self.target_sum:
                    return False
            return True
        return False

    permutations: int = 0

    def _solve(self, rotor) -> bool:
        self.permutations += 1
        if self.is_solved():
            return True

        if rotor > 0:
            for inc in range(self.num_columns):
                self.rotors[rotor].rotate()
                if self._solve(rotor - 1):
                    return True

        return False

    def solve(self):
        if len(self.rotors) != self.num_rotors:
            raise Exception(
                f"Cannot solve puzzle: {self.num_rotors} rotors specified but {len(self.rotors)} are present"
            )

        tic = time.perf_counter()
        self._solve(rotor=self.num_rotors - 1)
        toc = time.perf_counter()

        print(
            f"Solution found in {toc-tic:0.4f}s at permutation {self.permutations}:\n{self.to_str()}"
        )

    def to_str(self):
        result_str = ""
        for col in range(self.num_columns):
            column = self.read_column(col)
            result_str += f"Column {col}: {column} = {sum(column)}\n"
        return result_str
