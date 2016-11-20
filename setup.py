from setuptools import setup
from itertools import imap, ifilter
from ast import parse

if __name__ == '__main__':
    package_name = 'vagrant2json'

    with open(package_name + '.py') as f:
        __author__, __version__ = imap(
            lambda buf: next(imap(lambda e: e.value.s, parse(buf).body)),
            ifilter(lambda line: line.startswith('__version__') or line.startswith('__author__'), f)
        )

    setup(
        name=package_name,
        author=__author__,
        version=__version__,
        test_suite='tests',
        py_modules=[package_name]
    )
