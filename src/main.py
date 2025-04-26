class NegativeError(Exception): ...
class Calculator(): 
    def Add(self, val):
        if val == "":
            return 0
        
        v = val.split(',')
        res = 0
        for v_ in v:
            if '-' in v_:
                raise NegativeError
            res += int(v_)
        return res
