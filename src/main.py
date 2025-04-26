class Calculator(): 
    def Add(self, val):
        if val == "":
            return 0
        
        v = val.split(',')
        return int(v[0])
    
        
