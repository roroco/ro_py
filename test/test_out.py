from out import Out
from ro import ro.unittest


class TestOut(ro.ro_unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.o = Out()

    def test_out(self, *args):
        self.o.out('smth')
