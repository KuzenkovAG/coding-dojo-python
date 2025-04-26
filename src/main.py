class RomeNumber:
    Values = {
        1:"I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
        4: "IV",
        9: "IX",
        90: "XC",
        400: "CD",
        900: "CM",
    }
    def get(self, value):
        if v := self.Values.get(value):
            return v 
        
        digits = []
        while value > 0:
            r = value % 10
            digits.append(r)
            value = int(value/10)

        for i in range(len(digits)):
            digits[i] = digits[i] * 10**i

        return digits[0] * self.Values.get(1)

    #     return [self._sum(v_) for v_ in digits.reverse()].join()
    
    # def _sum(self, value):
    #     if 

