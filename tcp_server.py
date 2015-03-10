import socket
from ro import sh


class TcpServer:
    def __init__(self, host, port, *args):
        self.host = host
        self.port = port

    def url(self, *args):
        if not hasattr(self, "_url"):
            self._url = self.host + ":" + self.port

    def start(self, blk=None, *args):
        sv = socket.socket()
        sv.bind()
        sv.listen(0)
        while 1:
            s, addr = sv.accept()
            blk(s)
        s.close()
        self.wait_until_start()


    def wait_until_start(self, *args):
        @ro_try
        def blk(*args):
            return bash.port_is_listened(self.port)

    def tcp_server(*args):
        TcpServer().start(*args)

