from setuptools import setup, Extension

import os
import sys
import setuptools
import glob

__version__ = '0.0.2'

# with open("README.md", "r") as readme_file:
#     readme = readme_file.read()

extra_compile_args_dict = {
    'linux' : ['-w', '-ftemplate-backtrace-limit=0', '-std=c++11'],
    'linux2' : ['-w', '-ftemplate-backtrace-limit=0', '-std=c++11'],
    'darwin' : ['-w', '-ftemplate-backtrace-limit=0', '-std=c++11', '-stdlib=libc++'],
}

ext_modules = [
  Extension(
    "_atomic_depth",
    glob.glob('src/*.cc'),
    include_dirs = [ 'src', 'lib/pybind11/include'],
    language = 'c++',
    extra_compile_args = extra_compile_args_dict[sys.platform],
    extra_link_args = ['-lz'],
    define_macros = [('DOCTEST_CONFIG_DISABLE', None)]
  )
]

setup(
    name = 'atomic_depth',
    version = __version__,
    author = 'Brian Coventry',
    author_email = 'bcov@uw.edu',
    description = 'Atomic Depth',
    packages = ['atomic_depth'],
    package_dir={'atomic_depth': 'atomic_depth'},
    package_data={},
    ext_modules = ext_modules,
    install_requires = ['numpy', 'pybind11'],
    include_package_data=True,
    zip_safe = False,
    # long_description=readme,
    long_description_content_type='text/markdown',
    # url="https://github.com/atom-moyer/getpy",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: C++',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix'
    ],
)
