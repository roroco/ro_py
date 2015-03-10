import os
from os import path
from flatten import *
from ls import *
import ro
import re


def flatten_file_ls(ls, *args, **kwargs):
    l = []
    for d in ls:
        prefix = d[0]
        for fn in d[2]:
            l.append(path.join(prefix, fn))

    return l


def find(d, *res, **kwargs):
    l = flatten_file_ls(ls(os.walk(d)))
    l2 = []
    for e in l:
        all_true = True
        for r in res:
            all_true = (all_true and re.search(r, e) is not None)
        if all_true:
            l2.append(e)
    return l2


def ff(d, *res, **kwargs):
    l = []
    for e in find(d, *res, **kwargs):
        if path.isfile(e):
            l.append(e)
    return l


def fd(d, *res, **kwargs):
    l = []
    for e in find(d, *res, **kwargs):
        if path.isdir(e):
            l.append(e)
    return l


if __name__ == '__main__':
    r = find(ro.rt("test"))
    print("r:" + str(r))
