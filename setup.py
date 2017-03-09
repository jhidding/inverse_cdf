#!/usr/bin/env python

from distutils.core import setup
# from distutils.command.build_clib import build_clib
from distutils.extension import Extension

try:
    from Cython.Build import cythonize
except ImportError:
    has_cython = False
else:
    has_cython = True

from os import path
from codecs import open


if has_cython:
    ext_modules = cythonize([Extension(
            "inverse_cdf.icdf",
            sources=["src/icdf.cc", "inverse_cdf/icdf.pyx"],
            language="c++")])
else:
    ext_modules = [Extension(
            "inverse_cdf.icdf",
            sources=["src/icdf.cc", "inverse_cdf/icdf.cpp"],
            language="c++")]

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='inverse_cdf',
    version='0.1.0',
    long_description=long_description,
    description="""Computes the inverse CDF from a PDF.""",
    license='Apache v2',
    author='Johan Hidding',
    author_email='j.hidding@esciencecenter.nl',
    url='https://github.com/jhidding/inverse_cdf',
    packages=['inverse_cdf'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics'],
    install_requires=['numpy'],
    extras_require={
        'develop': [
            'pytest', 'pytest-cov', 'pep8', 'pyflakes', 'cython'],
    },
    ext_modules=ext_modules
)
