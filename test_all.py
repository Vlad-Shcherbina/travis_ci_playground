from __future__ import print_function
import sys
import logging

import nose
from hypothesis import given, assume
import numpy

N = 41


def example_test():
    pass


# @given(int)
# def test_square_is_even(x):
#     assume(x % 2 == 0)
#     logging.info('x = {}'.format(x))
#     assert x ** 2 % 2 == 0, x


def test_skipped():
    raise nose.SkipTest('zzz')
    
    
def test_numpy():
    xs = numpy.array([0, 10, 0, 20, 0])
    nz, = xs.nonzero()
    assert numpy.array_equal(nz, numpy.array([1, 3]))
    

if __name__ == '__main__':
    print(sys.version)
    argv = sys.argv + [
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',
        '--rednose',
        ]
    nose.run_exit(argv=argv)
