class RoStr(str):
    def init(self, *args, **kwargs):
        if not 'seperator' in kwargs:
            kwargs['seperator'] = ""

        return kwargs['seperator'].join(map(str, args))


def ro_str(*args, **kwargs):
    return RoStr().init(*args, **kwargs)


def msg(*args, **kwargs):
    return RoStr().init(*args, seperator=" ")

