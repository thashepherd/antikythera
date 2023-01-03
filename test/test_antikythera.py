import pytest
from main import Antikythera, Rotor

def test_add_rotor():
    # Create an Antikythera puzzle with 3 rotors, 3 layers, and 3 columns
    puzzle = Antikythera(3, 3, 3, 15)

    # Create a Rotor with 3 layers and 3 columns
    rotor = Rotor({
        0: [1, 2, 3],
        1: [4, 5, 6],
        2: [7, 8, 9]
    })

    # Add the rotor to the puzzle
    puzzle.add_rotor(rotor)

    # Check that the rotor has been added to the puzzle
    assert puzzle.rotors == [rotor]

def test_add_rotor_exception():
    # Create an Antikythera puzzle with 3 rotors, 3 layers, and 3 columns
    puzzle = Antikythera(3, 3, 3, 15)

    # Create a Rotor with 3 layers and 4 columns
    rotor = Rotor({
        0: [1, 2, 3, 4],
        1: [5, 6, 7, 8],
        2: [9, 10, 11, 12]
    })

    # Try to add the rotor to the puzzle
    with pytest.raises(Exception) as excinfo:
        puzzle.add_rotor(rotor)

    # Check that the exception has the correct message
    assert str(excinfo.value) == "Added rotor has 4 columns but this puzzle is set for 3"

def test_add_rotor_max_rotors():
    # Create an Antikythera puzzle with 3 rotors, 3 layers, and 3 columns
    puzzle = Antikythera(3, 3, 3, 15)

    # Create 3 Rotors with 3 layers and 3 columns
    rotor1 = Rotor({
        0: [1, 2, 3],
        1: [4, 5, 6],
        2: [7, 8, 9]
    })
    rotor2 = Rotor({
        0: [10, 11, 12],
        1: [13, 14, 15],
        2: [16, 17, 18]
    })
    rotor3 = Rotor({
        0: [19, 20, 21],
        1: [22, 23, 24],
        2: [25, 26, 27]
    })

    # Add the rotors to the puzzle
    puzzle.add_rotor(rotor1)
    puzzle.add_rotor(rotor2)
    puzzle.add_rotor(rotor3)

    # Check that the rotors have been added to the puzzle
    assert puzzle.rotors == [rotor1, rotor2, rotor3]

def test_add_rotor_exception_too_many_rotors():
    # Create an Antikythera puzzle with 3 rotors, 3 layers, and 3 columns
    puzzle = Antikythera(3, 3, 3, 15)

    # Create 3 Rotors with 3 layers and 3 columns
    rotor1 = Rotor({
        0: [1, 2, 3],
        1: [4, 5, 6],
        2: [7, 8, 9]
    })
    rotor2 = Rotor({
        0: [10, 11, 12],
        1: [13, 14, 15],
        2: [16, 17, 18]
    })
    rotor3 = Rotor({
        0: [19, 20, 21],
        1: [22, 23, 24],
        2: [25, 26, 27]
    })

    # Add the rotors to the puzzle
    puzzle.add_rotor(rotor1)
    puzzle.add_rotor(rotor2)
    puzzle.add_rotor(rotor3)

    # Try to add an additional rotor to the puzzle
    with pytest.raises(Exception) as excinfo:
        puzzle.add_rotor(rotor1)

    # Check that the exception has the correct message
    assert str(excinfo.value) == "Cannot add more rotors: 3 rotors are already present"

