import ro_unittest
import socket

import sh

class TestBash(ro_unittest.TestCase):
    def setUp(self, *args):
        self.o = bash

    def test_port_is_listened(self, *args):
        sv = socket.socket()
        port = 23333
        sv.bind(('localhost', port))
        result = self.o.port_is_listened(port)
        self.assertFalse(result)
