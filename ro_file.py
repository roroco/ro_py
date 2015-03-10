def read(file, *args, **kwargs):
    open(file, 'r').read()


def write(file, ctn, *args, **kwargs):
    open(file, 'w').write(ctn)
