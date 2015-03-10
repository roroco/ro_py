from ro_try import RoTry
from ro import ro.unittest


class TestRoTry(ro.ro_unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.o = RoTry()

    def test_ro_try(self, *args, **kwargs):
        smth = 0

        @ro_thr
        def lamb(*args, **kwargs):
            sleep(0.1)
            smth = 1

        @ro_try(5)
        def smth_is_one(*args, **kwargs):
           return smth






