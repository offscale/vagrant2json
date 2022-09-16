from ast import parse
from itertools import ifilter, imap

from setuptools import setup

if __name__ == "__main__":
    package_name = "vagrant2json"

    with open(package_name + ".py") as f:
        __author__, __version__ = imap(
            lambda buf: next(imap(lambda e: e.value.s, parse(buf).body)),
            ifilter(
                lambda line: line.startswith("__version__")
                or line.startswith("__author__"),
                f,
            ),
        )

    setup(
        name=package_name,
        author=__author__,
        version=__version__,
        test_suite="tests",
        py_modules=[package_name],
    )
