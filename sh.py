import socket

def port_is_listened(port, *args):
    try:
        sv = socket.socket()
        sv.connect(("localhost", port))
        sv.bind(("localhost", port))
        return True
    except socket.error as e:
        return False


def is_listened(*args, **kwargs):
    port_is_listened(*args, **kwargs)
