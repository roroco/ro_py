from time import sleep

from ro.cells.ro_thr import ro_thr


class TimeoutErr(Exception):
    pass


def timeout(delay, *args, **kwargs):
    finished = 0
    def lamb(*args, **kwargs):
        sleep(delay)
        if not finished:
            raise TimeoutErr

    t = ro_thr(lamb)

    def decorator(func):
        func()
        finished = 1


    return decorator

