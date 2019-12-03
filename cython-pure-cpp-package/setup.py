from setuptools import setup, Extension


modules = [Extension("cython_pure_cpp_package",
                           ['src/person_.pyx', 'src/person.cpp'],
                           include_dirs=['src/include'],
                           language="c++",
                           extra_compile_args=['-std=c++17']
                           )]
for e in modules:
    e.cython_directives = {'language_level': "3"}

setup(
    name="cython_pure_cpp_package",
    version="0.0.1",
    ext_modules=modules,
    python_requires='>=3.6',
    setup_requires=[
        'setuptools>=18.0',
        'cython',
        ]
)

