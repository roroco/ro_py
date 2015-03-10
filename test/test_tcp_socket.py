import ro_unittest

from test_helper import *


class TestTcpSocket(ro_unittest.TestCase):
    def setUp(self, *args):
        self.o = ro.tcp_socket.TcpSocket()

    def test_start(self, *args):
        TcpServer().until("localhost", 23333)
        self.o.cnn("localhost", 23333)
