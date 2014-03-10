import os
from setuptools import setup, find_packages
from setuptools.command.install import install

import subprocess

VERSION = "0.0.1"

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

requirements = read('requirements').splitlines()
tests_requirements = read('test-requirements').splitlines()

class DataBuildInstall(install):

    def run(self):
        subprocess.call('make all')
        install.run(self)


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
    cmdclass={
        'install': DataBuildInstall,
    },
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
    install_requires=requirements,
    tests_require=tests_requirements,
)
