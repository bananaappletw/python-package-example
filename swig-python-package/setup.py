from setuptools import setup, Extension, find_packages, find_namespace_packages
from setuptools.command.build_py import build_py


class BuildPy(build_py):
    def run(self):
        self.run_command('build_ext')
        super(build_py, self).run()


modules = [Extension('_swig_python_package',
                     swig_opts=['-c++', '-modern',
                                '-Isrc/swig_python_package/include', '-py3'],
                     sources=['src/swig_python_package/swig_python_package.i',
                              'src/swig_python_package/person.cpp'],
                     include_dirs=['src/swig_python_package/include'],
                     extra_compile_args=['-std=c++11']
                     )]

for e in modules:
    e.cython_directives = {'language_level': "3"}

setup(name='swig_python_package',
      version='0.1',
      ext_modules=modules,
      packages=find_packages('src'),
      package_dir={'': 'src'},
      python_requires='>=3.6',
      cmdclass={'build_py': BuildPy}
      )
