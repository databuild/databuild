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


def has_lib(libname):
    platform_name = os.uname()[0]
    if platform_name == 'Darwin':
        try:
            output = subprocess.check_output(['ld', '-l%s' % libname], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            output = exc.output
        return ('library not found' not in output.decode('utf8'))
    if platform_name == 'Linux':
        try:
            output = subprocess.check_output(['ldconfig', '-p'], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as exc:
            output = exc.output
        return libname in output.decode('utf8')


requirements = read('requirements.txt').splitlines()

pypi_requirements = [req for req in requirements if not req.startswith('http')]
dependency_links = [req for req in requirements if req.startswith('http')]

WITHLUA = os.environ.get('WITHLUA', has_lib('lua'))
if WITHLUA:
    lua_requirements = read('lua-requirements.txt').splitlines()

    pypi_requirements.extend([req for req in lua_requirements if not req.startswith('http')])
    dependency_links.extend([req for req in lua_requirements if req.startswith('http')])


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
    url='https://github.com/fcurella/databuild',
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
