import unittest
from find import *
import re
from proc import *
from os import path


def run_test(test, *args, **kwargs):
    d = path.dirname(test)
    fn = path.basename(test)
    argv = ['discover', "-s", d, '-p', fn, '-f']
    print(' '.join(['py -m unittest'] + argv))
    unittest.main(argv=['python -m unittest'] + argv)


def run_all_tests(*args, **kwargs):
    tests = ff(ro.rt('test'), re.compile('test\_.*\.py$'))
    for test in tests:
        pid = fork(run_test, test)
        waitpid(pid)


if __name__ == '__main__':
    run_all_tests()
