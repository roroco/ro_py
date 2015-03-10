from ro_str import RoStr
from ro import ro.unittest


class TestRoStr(ro.ro_unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.o = RoStr()

    def test_ro_msg(self, *args, **kwargs):
        result = ro_msg("word", "word2")
        self.assertEqual(result, "word word2")
