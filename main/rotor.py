from typing import Dict, List, Optional


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
