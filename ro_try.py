from time import sleep

from ro.cells.timeout import timeout
import out
from ro_str import msg
import ro_str
from ro.cells import out
from determination import *


class RoTry:
    def __init__(self, delay=None, *args, **kwargs):
        if delay == None:
            delay = 10
        self.delay = delay

    def errs(self, *args):
        if not hasattr(self, "_errs"):
            self._errs = []
        return self._errs

    def last_err(self, *args):
        if not hasattr(self, "_last_err"):
            self._last_err = None
        return self._last_err


    def until(self, func):
        @timeout(self.delay)
        def lamb():
            out.out(msg('try', ro_str(self.delay, "s"), 'until', func))
            while 1:
                try:
                    if func():
                        break
                except Exception as e:
                    if not self.last_err() == e:
                        out.out(e)
                    self.errs() << e
                sleep(0.1)


def ro_try(smth, *args, **kwargs):
    if is_func(smth):
        return RoTry().until(smth)
    if isinstance(smth, int):
        return RoTry(smth).until


