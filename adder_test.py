

import adder

def test_no_carry():
    a = [1,2,3]
    b = [7,2,0]
    c = [8,4,3]
    assert adder.add(a, b) == c

def test_rightmost_carry():
    a = [1,2,3]
    b = [7,2,9]
    c = [8,5,2]
    assert adder.add(a, b) == c

def test_lefttmost_carry():
    a = [9,2,3]
    b = [7,2,0]
    c = [1,6,4,3]
    assert adder.add(a, b) == c

def test_a_longer():
    a = [1,0,0,0,1,2,3]
    b = [7,2,0]
    c = [1,0,0,0,8,4,3]
    assert adder.add(a, b) == c

def test_a_longer():
    a = [1,2,3]
    b = [1,0,0,0,7,2,0]
    c = [1,0,0,0,8,4,3]
    assert adder.add(a, b) == c

def test_add_fn():
    assert adder._add_digit(1,2) == (0, 3)
    assert adder._add_digit(1,0) == (0, 1)
    assert adder._add_digit(0,0) == (0, 0)
    assert adder._add_digit(9,9) == (1, 8)
