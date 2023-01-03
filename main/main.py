# This puzzle is made of a number of rotors, each having columns of numbers radiating out from the center.
# Each rotor has an equal number of columns. Columns are represented as a List[Optional[int]]. Columns may have 'holes' or be missing entirely.
# The index of the Dict[int, List[Optional[int]]] below represents the position of the column.
# 'None' in this object represents a column with a hole in it, i.e. that the number needs to be read from the rotor below this one.
# Rotors are added from the top down.
# The objective of the puzzle is to rotate the rotors until each column adds up to 42.

from antikythera import Antikythera, Rotor

# Set up the specific puzzle I got for Christmas
ant = Antikythera(5, 4, 12, 42)
ant.add_rotor(Rotor({0: [15, None, 8, None, 3, None, 6, None, 10, None, 7, None]}))
ant.add_rotor(
    Rotor(
        {
            0: [6, 17, 7, 3, None, 6, None, 11, 11, 6, 11, None],
            1: [12, None, 4, None, 7, 15, None, None, 14, None, 9, None],
        }
    )
)
ant.add_rotor(
    Rotor(
        {
            0: [8, 9, 13, 9, 7, 13, 21, 17, 4, 5, None, 7],
            1: [None, 21, 6, 15, 4, 9, 18, 11, 26, 14, 1, 12],
            2: [None, 5, None, 10, None, 8, None, 22, None, 16, None, 9],
        }
    )
)
ant.add_rotor(
    Rotor(
        {
            0: [7, None, 9, None, 7, 14, 11, None, 8, None, 16, None],
            1: [9, None, 2, 3, 6, None, 14, 12, 9, None, 9, 2],
            2: [3, 26, 6, None, 2, 13, 9, None, 3, 20, 3, 12],
            3: [1, None, 9, None, 12, None, 6, None, 10, None, 10, None],
        }
    )
)
ant.add_rotor(
    Rotor(
        {
            0: [14, 11, 14, 14, 11, 14, 11, 14, 11, 11, 14, 11],
            1: [8, 9, 10, 11, 12, 13, 14, 15, 4, 5, 6, 7],
            2: [3, 3, 14, 14, 21, 21, 9, 9, 4, 4, 6, 6],
            3: [2, 5, 10, 7, 16, 8, 7, 8, 8, 3, 4, 12],
        }
    )
)
print(ant.rotors[1].rotated_contents[0])
print(ant.rotors[1].rotated_contents[1])
print(ant.to_str())
print("ROTATING")
ant.rotors[0].rotate()
print(ant.to_str())

print(ant.rotors[1].to_str())
ant.rotors[1].rotate()
ant.rotors[1].rotate()
ant.rotors[1].rotate()
ant.rotors[1].rotate()
ant.rotors[1].rotate()
ant.rotors[1].rotate()
ant.rotors[1].rotate()
print(ant.rotors[1].to_str())
ant.solve()
