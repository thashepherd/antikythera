from main.antikythera import Rotor


def test_rotate():
    # Test rotating a rotor with a single layer
    r = Rotor({0: [1, 2, 3, 4]})
    r.rotate()
    assert r.rotated_contents == {0: [2, 3, 4, 1]}
    r.rotate()
    assert r.rotated_contents == {0: [3, 4, 1, 2]}
    r.rotate()
    assert r.rotated_contents == {0: [4, 1, 2, 3]}

    # Test rotating a rotor with multiple layers
    r = Rotor({0: [1, 2, 3, 4], 1: [5, 6, 7, 8]})
    r.rotate()
    assert r.rotated_contents == {0: [2, 3, 4, 1], 1: [6, 7, 8, 5]}
    r.rotate()
    assert r.rotated_contents == {0: [3, 4, 1, 2], 1: [7, 8, 5, 6]}
    r.rotate()
    assert r.rotated_contents == {0: [4, 1, 2, 3], 1: [8, 5, 6, 7]}


def test_reset_rotation():
    # Test resetting a rotor with a single layer
    r = Rotor({0: [1, 2, 3, 4]})
    r.rotate()
    assert r.rotated_contents == {0: [2, 3, 4, 1]}
    r.reset_rotation()
    assert r.rotated_contents == {0: [1, 2, 3, 4]}

    # Test resetting a rotor with multiple layers
    r = Rotor({0: [1, 2, 3, 4], 1: [5, 6, 7, 8]})
    r.rotate()
    assert r.rotated_contents == {0: [2, 3, 4, 1], 1: [6, 7, 8, 5]}
    r.reset_rotation()
    assert r.rotated_contents == {0: [1, 2, 3, 4], 1: [5, 6, 7, 8]}
