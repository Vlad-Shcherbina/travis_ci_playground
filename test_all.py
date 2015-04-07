from __future__ import print_function
import sys
import logging

import nose
from hypothesis import given, assume

N = 41


def example_test():
    pass


@given(int)
def test_square_is_even(x):
    assume(x % 2 == 0)
    logging.info('x = {}'.format(x))
    assert x ** 2 % 2 == 0, x


def test_skipped():
    raise nose.SkipTest('zzz')
    

if __name__ == '__main__':
    print(sys.version)
    argv = sys.argv + [
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',
        '--rednose',
        ]
    nose.run_exit(argv=argv)
