class Calculator(): 
    def Add(self, val):
        if val == "":
            return 0
        
        v = val.split(',')

        return sum(int(v_) for v_ in v)
