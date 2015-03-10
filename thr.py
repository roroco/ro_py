import threading

import ro_trace


class Thr(threading.Thread):
    @staticmethod
    def cur(*args, **kwargs):
        threading.current_thread()

    @staticmethod
    def is_main(*args, **kwargs):
        threading.current_thread().name == "MainThread"


def thr(func, *args, **kwargs):
    name = ro_trace.last_location_not_in(__file__)
    thr = Thr(target=func, name=name, *args, **kwargs)
    thr.start()
    return thr
