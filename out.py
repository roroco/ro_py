from ro_str import msg
import ro_trace


class Out:
    def out(self, *args, **kwargs):
        s = msg(*args, **kwargs)
        loc = ro_trace.last_simple_location_not_in(__file__)
        print(msg(s, " ---- ", loc))


def out(*args, **kwargs):
    Out().out(*args, **kwargs)
