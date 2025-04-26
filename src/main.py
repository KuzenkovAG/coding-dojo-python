class NegativeError(Exception): ...
class Calculator(): 
    def Add(self, val):
        if val == "":
            return 0

        for s in ("\n", ";"):
            val = val.replace(s, ',')

        v = val.split(',')
        res = 0
        for v_ in v:
            if '-' in v_:
                raise NegativeError
            if (v__ := int(v_)) > 1000:
                continue
            res += v__

        return res
