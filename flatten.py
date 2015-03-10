class Flatten:
    def __init__(self, *args, **kws):
        self.l = []

    def flatten(self, o, **kwargs):
        for _o in o:
            if self.is_iter(_o):
                self.flatten(_o)
            else:
                self.l.append(_o)
        return self.l


    def is_iter(self, o, *args):
        return hasattr(o, '__iter__')


def flatten(*args, **kwargs):
    return Flatten().flatten(*args, **kwargs)
