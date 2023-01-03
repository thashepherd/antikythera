from antikythera import Antikythera, Rotor

ant = Antikythera(5, 12, 42)
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
            2: [3, 26, 6, None, 2, 13, 9, None, 17, 19, 3, 12],
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
for rotor in ant.rotors:
    print(rotor.to_str())

ant.rotors[0].rotate()
ant.rotors[2].rotate()
ant.rotors[2].rotate()
for rotor in ant.rotors:
    print(rotor.to_str())
