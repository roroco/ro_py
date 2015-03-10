from os import path


def rt(*args, **kwargs):
    return path.join(path.realpath("."), *args, **kwargs)

if __name__ == '__main__':
    r = rt('ex')
    print("r:" + r.str())
