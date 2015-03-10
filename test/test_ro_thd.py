class TestRoThd(ro.ro_unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.o = ro.cells.ro_thr.RoThr()

    def test_ro_thd(self, *args, **kwargs):
        def lamb(*args, **kwargs):
            sleep(1)
            out.out('sleep finish')

        t = ro_thr(lamb)
        t.join



