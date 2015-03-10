class Ls(list):
    def reverse(self, *args, **kwargs):
        super.reverse(*args, **kwargs)
        return self


def ls(*args, **kwargs):
    return list(*args, **kwargs)

