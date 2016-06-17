from setuptools import setup, find_packages
from os import path
import re

def read(*relpath):
    with open(path.join(path.dirname(__file__), *relpath)) as fp:
        return fp.read()

def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['']([^'']*)['']''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)

setup(
    name='toolwrapper',
    version=get_version('toolwrapper.py'),
    description='A base class for wrapping text-processing tools',
    long_description=read('README.rst'),
    url='https://bitbucket.org/luismsgomes/toolwrapper',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='Other/Proprietary License',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Filters',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='subprocess text tool wrapper',
    py_modules= ['toolwrapper'],
)
