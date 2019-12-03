from setuptools import setup, Extension

extensions = [
    Extension("cython_pure_python_package", ["src/cython_pure_python_package.pyx"])
]

for e in extensions:
    e.cython_directives = {'language_level': "3"}

setup(
    name="cython_pure_python_package",
    version="0.0.1",
    python_requires='>=3',
    ext_modules=extensions,
    setup_requires=[
        'setuptools>=18.0',
        'cython',
    ]
)
