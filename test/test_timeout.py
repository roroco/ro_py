from timeout import TimeoutErr
import timeout
from ro import ro.unittest


class TestTimeout(ro.ro_unittest.TestCase):
    def test_timeout_first(self, *args, **kwargs):
        @timeout(10)
        def lamb():
            pass

    def test_timeout2(self, *args, **kwargs):
        @self.assertRaisingErr(TimeoutErr)
        def lamb():
            @timeout(0.1)
            def lamb(*args, **kwargs):
                sleep(1)


