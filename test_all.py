from __future__ import print_function
import sys

import nose


N = 42


def example_test():
    assert N % 2 == 0


if __name__ == '__main__':
    print(sys.version)
    argv = sys.argv + [
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',
        ]
    nose.run_exit(argv=argv)
