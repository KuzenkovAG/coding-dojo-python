import pytest


@pytest.mark.parametrize("test_input, expected", [
    ("Bob", "Hello, Bob.")
])
def test(test_input, expected):
    pass


def test_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
