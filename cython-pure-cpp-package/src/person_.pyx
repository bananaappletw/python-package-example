from libcpp.string cimport string
cdef extern from "person.hpp":
    cdef cppclass CPPPerson "Person":
        CPPPerson()
        string hello()

cdef class Person:
    cdef CPPPerson *thisptr
    def __cinit__(self):
        self.thisptr = new CPPPerson()
    def __dealloc__(self):
        del self.thisptr
    def hello(self):
        return self.thisptr.hello().decode()
