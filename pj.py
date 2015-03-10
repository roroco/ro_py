import os
import sys


def env(key, *args):
    try:
        return os.environ[key]
    except KeyError  as e:
        return None


def ro_stage(*args):
    if env(ro_stage_key()) == None:
        set_env(ro_stage_key(), 'dev')
    return env(ro_stage_key())


def set_env(key, val, *args):
    os.environ[key] = val


def in_prod(*args):
    return env[ro_stage_key()] == 'prod'


def set_test(*args, **kwargs):
    set_env(ro_stage_key(), 'test')


def set_dev(*args, **kwargs):
    set_env(ro_stage_key(), 'dev')


def in_dev(*args):
    return ro_stage() == 'dev'


def in_test(*args):
    return env(ro_stage_key()) == 'test'


def ro_stage_key(*args):
    return "RO_STAGE"


def home(*args):
    return os.path.join(os.environ["HOME"], *args)


def rb_projs(*args):
    return os.path.join(home(), "Dropbox/rb-projs", *args)


def py_projs(*args):
    return os.path.join(home(), "Dropbox/py-projs", *args)

