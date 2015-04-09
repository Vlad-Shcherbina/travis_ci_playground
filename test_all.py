from __future__ import print_function
import sys
import logging

import nose
import numpy

import cpp
cpp.build_extensions()
from cpp import sample


N = 41


def example_test():
    pass


def test_skipped():
    raise nose.SkipTest('zzz')


def test_numpy():
    xs = numpy.array([0, 10, 0, 20, 0])
    nz, = xs.nonzero()
    assert numpy.array_equal(nz, numpy.array([1, 3]))


def test_swig():
    assert sample.N == 42
    assert sample.square_float(2) == 4.0
    assert sample.reverse([1, 2, 3]) == (3, 2, 1)

    hz = sample.Hz()
    hz.a = 1
    hz.b = 'b'
    hz2 = sample.Hz(hz)
    hz.a = 7
    assert str(hz) == 'Hz(7, b)'
    assert str(hz2) == 'Hz(1, b)'


if __name__ == '__main__':
    print(sys.version)
    argv = sys.argv + [
        '--verbose', '--with-doctest',
        '--logging-level=DEBUG',
        '--rednose',
        ]
    nose.run_exit(argv=argv)
