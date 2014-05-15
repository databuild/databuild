import os
import subprocess
from setuptools import setup, find_packages

VERSION = "0.0.1"


def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''


requirements = read('requirements.txt').splitlines()

pypi_requirements = [req for req in requirements if not req.startswith('http')]
dependency_links = [req for req in requirements if req.startswith('http')]

tests_requirements = read('test-requirements.txt').splitlines()

# Temporary fix until tablib gets released
subprocess.call(["pip", "install", "--quiet", "https://github.com/kennethreitz/tablib/archive/f6cd89c76cb8f025114e208caa8965d3d0196ae7.zip"])

# Temporary fix until unicodecsv gets released
subprocess.call(["pip", "install", "--quiet", "https://github.com/jdunck/python-unicodecsv/archive/13a300d82d8002e1db141540830e10f3c8dd7606.zip"])

setup(
    name="databuild",
    version=VERSION,
    description="a build tool for data",
    long_description=read('README.rst'),
    url='https://github.com/databuild/databuild',
    license='BSD',
    author='Flavio Curella',
    author_email='flavio.curella@gmail.com',
    packages=find_packages(exclude=['tests']),
    scripts=['bin/data-build.py'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    install_requires=pypi_requirements,
    dependency_links=dependency_links,
    tests_require=tests_requirements,
)
