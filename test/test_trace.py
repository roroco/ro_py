from ro import ro.unittest
from test.test_helper import *

class TestRoTrace(ro.ro_unittest.TestCase):
    def setUp(self, *args):
        self.o = ro_trace

    def test_last_frame(self, *args, **kws):
        r = self.o.last_frame()
        result = r.file
        self.assertEqual(__file__, result)
