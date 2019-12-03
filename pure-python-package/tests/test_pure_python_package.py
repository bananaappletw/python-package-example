from pure_python_package import Person


def test_hello():
    assert Person().hello() == 'hello'
