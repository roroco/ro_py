import ro_kls
import ro_unittest


class TestKls(ro_unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.o = ro_kls.Kls()

    class C(RoKls):
        def at(self, *args):
            return self._attr("default val")

    def test__attr(self, *args):
        result = TestKls.C().at()
        self.assertEqual(result, "default val")

