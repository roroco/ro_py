import os


def fork(func, *args, **kwargs):
    pid = os.fork()
    if pid > 0:
        child = pid
    else:
        func(*args, **kwargs)
    return pid


def waitpid(pid, *args, **kwargs):
    os.waitpid(pid, 0, *args, **kwargs)
