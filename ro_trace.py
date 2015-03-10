import inspect
import re
import os
import traceback
import copy

import ls
import ro_str


def cur_frame(*args):
    return inspect.getframeinfo(inspect.currentframe().f_back)


def cur_lineno(*args):
    return cur_frame().lineno


def cur_file(*args):
    return cur_frame().filename


def cur_filename(*args):
    return os.path.basename(cur_file())


# don't rename to Trace, pydev use trace by default, you can't never override trace mod
class RoTrace:
    def last_frame_not_in(self, *file_shorts, **kwargs):
        return self.parse(file_shorts)

    def build_file_shorts(self, *args, **kwargs):
        file_shorts = args
        return flatten([file_shorts, __file__, "kernel.py", "pydevd.*.py$", '<string>'])

    def last_frame(self, *args, **kwargs):
        return self.parse(*args, **kwargs)

    class LastFrame:
        def __init__(self, file, lineno, func_name):
            self.file = file
            self.lineno = lineno
            self.func_name = func_name
            self.location = ro_str(file, ":", lineno)
            self.simple_location = ro_str(os.path.basename(file), ":", lineno)

        def __repr__(self, *args, **kwargs):
            return repr(self.__dict__)


    def parse(self, *_file_shorts):
        frames = traceback.extract_stack()
        frames.reverse()
        backtrace = frames

        file_shorts = self.build_file_shorts(_file_shorts)

        for _attrs in backtrace:
            attrs = copy.copy(_attrs)
            file = attrs[0]
            lineno = attrs[1]
            func_name = attrs[2]

            def lamb(file_short, **kwargs):
                return not re.search(file_short, file)

            if all(map(lamb, file_shorts)):
                return RoTrace.LastFrame(file, lineno, func_name)


def last_frame_not_in(*args, **kwargs):
    return RoTrace().last_frame_not_in(*args, **kwargs)


def last_func_name_not_in(*args, **kwargs):
    return last_frame_not_in(*args, **kwargs).func_name


def last_frame(*args, **kwargs):
    r = RoTrace().last_frame()
    return RoTrace().last_frame()


def last_func_name(*args, **kwargs):
    r = last_frame().func_name
    return r


def last_loaction(*args, **kwargs):
    return last_frame().location


def last_location_not_in(*args, **kwargs):
    return last_frame_not_in(*args, **kwargs).location


def last_simple_location_not_in(*args, **kwargs):
    return last_frame_not_in(*args, **kwargs).simple_location

