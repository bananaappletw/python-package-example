# python-package-example [![Build Status](https://travis-ci.com/bananaappletw/python-package-example.svg?branch=master)](https://travis-ci.com/bananaappletw/python-package-example)

Collection of minimal examples of python package

## Overview

### Interface

All the examples provide Person class with instance method hello()

    class Person:
    def hello(self):
        return 'hello'

    from xxx_package import Person
    Person().hello()

### [pure python package](./pure-python-package/)

pure python implementation

### [cython pure cpp package](./cython-pure-cpp-package/)

pure cpp implementation
package is compiled into single .so file

### [cython pure python package](./cython-pure-python-package/)

pure python implementation
package is compiled into single .so file

### [swig python package](./swig-python-package/)

pure cpp implementation
package is compiled into single .so file

## Personal opinion

### C/C++ Extension

I perfer [Cython](https://cython.org/) to other implementations

It's more flexible than [swig](http://www.swig.org/)

[swig](http://www.swig.org/) currently have limited C++11 standard support

For example, smart pointer

Only shared_ptr supported

Besides, there is a slight difference between c++ and python

For example, you want to access property `name` from Person class

Cython

use C++ getter to access private member and encapsulated as Python property

    cdef class Person:
    cdef CPPPerson *thisptr
    def __cinit__(self):
        self.thisptr = new CPPPerson()
    @property
    def name(self):
        return self.thisptr.getName().decode()

Swig

interface directly inherit from c++ class, need to do something nasty

### Test

For the test, [tox](https://tox.readthedocs.io/en/latest/) and [pytest](https://docs.pytest.org/en/latest/)

[tox](https://tox.readthedocs.io/en/latest/) create virtualenv then install the package and test.

Suitable for C/C++ Extension

### distutils vs setuptools

Use setuptools instead
