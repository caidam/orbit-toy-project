from calc import add, subtract, multiply, divide, average, clamp


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    try:
        divide(1, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_average():
    assert average([1, 2, 3]) == 2.0
    assert average([10]) == 10.0


def test_average_empty():
    try:
        average([])
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(15, 0, 10) == 10
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10
