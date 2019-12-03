from cython_pure_python_package import Person


def test_person_hello():
    assert Person().hello() == "hello"
