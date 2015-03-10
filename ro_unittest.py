import unittest
import re

from ro.cells.timeout import timeout, TimeoutErr
from ro_str import msg


class TestCase(unittest.TestCase):
    def assertMatch(self, reg, st):
        if not re.match(reg, st):
            self.raise_err(reg, 'not match', st)

    def assertRunAtLeast(self, delay, *args, **kwargs):
        def decorator(func):
            try:
                @timeout
                def lamb():
                    func()

                raise AssertionError(msg('assert', func, 'run at least', delay + "s", 'but it exit unexpectly'))
            except TimeoutErr as e:
                return 1

        return decorator


    def assertHaveVal(self, smth, *args, **kwargs):
        if not have_val(smth, *args, **kwargs):
            self.raise_err(smth, "have not", *args, **kwargs)

    def assertRaisingErr(self, err_kls, *args, **kwargs):
        def decorator(func):
            try:
                func()
                self.raise_err()
            except Exception as e:
                if isinstance(e, err_kls):
                    return 1
                else:
                    self.raise_err("assert raise", err_kls, 'but raise', e)

        return decorator


    def raise_err(self, *args, **kwargs):
        msg = msg(*args, **kwargs)
        location = ro_trace.last_location_not_in(__file__)
        if have_val(msg):
            raise AssertionError(msg(msg, ", raised in", location))
        msg()

    pass


