import time

import out

from ro_thr import Thr

import out


def slp(delay=None, *args, **kwargs):
    if delay == None:
        out.out("sleep forever in", Thr.cur())
        while 1:
            pass
    time.sleep(delay)



