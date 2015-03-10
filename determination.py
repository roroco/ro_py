def have_val(smth, ele=None, **kwargs):
    if ele == None:
        if hasattr(smth, '__len__'):
            return smth.__len__() > 0

def is_func(smth,*args, **kwargs):
    hasattr(smth, '__call__')
