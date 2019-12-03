from setuptools import setup, find_namespace_packages

setup(
    name="pure_python_package",
    version="0.0.1",
    python_requires='>=3',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src')
)
