import ro_trace


class Kls:
    def set_attrs(self, *args, **kws):
        for k, v in kws.items():
            setattr(self, "_" + k, v)

    def _attr(self, default_val=None, *args, **kws):
        rt = ro_trace
        func_name = rt.last_func_name_not_in(__file__)
        attr_name = "_" + func_name
        if attr_name == "_attr":
            raise ValueError("you cannot set ins var meth name as 'attr', please use other name")
        if not hasattr(self, attr_name):
            setattr(self, attr_name, default_val)

        return getattr(self, attr_name)
