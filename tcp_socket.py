import socket


class TcpSocket:
    def cnn(host, port, *args):
        s = socket.socket()
        s.connect(host, port)
        return s


def tcp_socket(*args):
    TcpSocket().cnn(*args)
