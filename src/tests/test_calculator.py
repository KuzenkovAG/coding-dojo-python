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

        (4, "IV"),
        (9, "IX"),
        (90, "XC"),
        (400, "CD"),
        (900, "CM"),

        (2, "II"),
        (7, "VII"),
        (390, "CCCXC"),
    ],
)
def test_simple(
        test_input,
        expected,
):
    assert expected == RomeNumber().get(test_input)
