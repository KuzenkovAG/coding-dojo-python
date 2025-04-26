class RomeNumber:
    Values = {
        1: "I",
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

    @staticmethod
    def get(value):
        result = ''
        for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                                 'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
            result += value // arabic * roman
            value %= arabic
        return result
