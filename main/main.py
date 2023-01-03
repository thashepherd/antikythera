from antikythera import Antikythera, Rotor

# This puzzle is made of a number of rotors, each having columns of numbers radiating out from the center.
# Each rotor has an equal number of columns. Columns are represented as a List[Optional[int]]. Columns may have 'holes' or be missing entirely.
# The index of the Dict[int, List[Optional[int]]] below represents the position of the column.
# 'None' in this object represents a column with a hole in it, i.e. that the number needs to be read from the rotor below this one.
# Rotors are added from the top down.
# The objective of the puzzle is to rotate the rotors until each column adds up to 42.

ant = Antikythera(5, 12, 42)
ant.add_rotor(Rotor({}))
