from main import Calculator

def test_Add():
    assert 0 == Calculator().Add("")

def test_add_number():
    assert 1 == Calculator().Add("1")

def test_sum_numbers():
    assert 2 == Calculator().Add("1,1")
