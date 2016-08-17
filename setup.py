from setuptools import setup
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)

setup(
    name='toolwrapper',
    version=get_version('src', 'toolwrapper.py'),
    description='A base class for wrapping text-processing tools',
    long_description=read('README.rst'),
    url='https://bitbucket.org/luismsgomes/toolwrapper',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Filters',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='subprocess text tool wrapper',
    package_dir={'': 'src'},
    py_modules=['toolwrapper'],
)
