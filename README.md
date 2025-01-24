# Empty project for kata

only pytest in deps

## Install Python (on Ubuntu)

```sh
sudo apt install python3 python3-venv python-pytest
```

## How to setup environment

```sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
``` 

```sh
pip freeze > requirements.txt
```

## Run tests

```sh
pytest . -vv
```

## Tips

### Parametrized tests
```python
@pytest.mark.parametrize("test_input, expected", [
    ("Bob", "Hello, Bob.")
])
def test(test_input, expected):
    pass
```

### How to handle exceptions
```python

def test_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```
