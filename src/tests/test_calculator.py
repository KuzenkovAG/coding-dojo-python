import pytest

from main import RomeNumber


@pytest.mark.parametrize(
    "test_input, "
    "expected", [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
    ],
)
def test_simple(
        test_input,
        expected,
):
    assert expected == RomeNumber().get(test_input)
