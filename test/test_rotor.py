from main.rotor import Rotor


def test_init():
    r = Rotor({})


def test_rotate():
    # Create a new Rotor with 3 layers and 3 columns
    rotor = Rotor({0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]})

    # Check that the rotor has the correct contents and rotation increment
    assert rotor.rotation_increment == 0
    assert rotor.rotated_contents == {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}

    # Rotate the rotor once
    rotor.rotate()

    # Check that the rotor's rotation increment has been incremented by 1 and that the rotated_contents have been updated
    assert rotor.rotation_increment == 1
    assert rotor.rotated_contents == {0: [2, 3, 1], 1: [5, 6, 4], 2: [8, 9, 7]}

    # Rotate the rotor three more times
    rotor.rotate()
    rotor.rotate()
    rotor.rotate()

    # Check that the rotor's rotation increment has been incremented by 3 and that the rotated_contents have been updated
    assert rotor.rotation_increment == 4
    assert rotor.rotated_contents == {0: [2, 3, 1], 1: [5, 6, 4], 2: [8, 9, 7]}


def test_reset_rotation():
    # Create a new Rotor with 3 layers and 3 columns
    rotor = Rotor({0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]})

    # Rotate the rotor four times
    rotor.rotate()
    rotor.rotate()
    rotor.rotate()
    rotor.rotate()

    # Check that the rotor's rotation increment has been incremented by 4 and that the rotated_contents have been updated
    assert rotor.rotation_increment == 4
    assert rotor.rotated_contents == {0: [2, 3, 1], 1: [5, 6, 4], 2: [8, 9, 7]}

    # Reset the rotation of the rotor
    rotor.reset_rotation()

    # Check that the rotation increment has been reset to 0 and that the rotated_contents have been reset to the original contents
    assert rotor.rotation_increment == 0
    assert rotor.rotated_contents == {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}

    # Check that the rotor has 3 columns
    assert rotor.num_columns() == 3


def test_reset_rotation():
    # Create a new Rotor with 3 layers and 3 columns
    rotor = Rotor({0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]})

    # Rotate the rotor four times
    rotor.rotate()
    rotor.rotate()
    rotor.rotate()
    rotor.rotate()

    # Check that the rotor's rotation increment has been incremented by 4 and that the rotated_contents have been updated
    assert rotor.rotation_increment == 4
    assert rotor.rotated_contents == {0: [2, 3, 1], 1: [5, 6, 4], 2: [8, 9, 7]}

    # Reset the rotation of the rotor
    rotor.reset_rotation()

    # Check that the rotation increment has been reset to 0 and that the rotated_contents have been reset to the original contents
    assert rotor.rotation_increment == 0
    assert rotor.rotated_contents == {0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]}


def test_num_columns():
    # Create a new Rotor with 3 layers and 3 columns
    rotor = Rotor({0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]})

    # Check that the rotor has 3 columns
    assert rotor.num_columns() == 3


def test_to_str():
    # Create a new Rotor with 3 layers and 3 columns
    rotor = Rotor({0: [1, 2, 3], 1: [4, 5, 6], 2: [7, 8, 9]})

    # Check that the to_str method returns the correct string representation of the rotor
    assert rotor.to_str() == (
        "Rotation increment: 0\n"
        "Layer 0: [1, 2, 3] \n"
        "Layer 1: [4, 5, 6] \n"
        "Layer 2: [7, 8, 9] \n"
    )
