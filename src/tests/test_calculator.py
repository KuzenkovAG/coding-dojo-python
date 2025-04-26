from main import Calculator

def test_Add():
    assert 0 == Calculator().Add("")

def test_add_number():
    assert 1 == Calculator().Add("1")
