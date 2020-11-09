from polynom import Poly


class Factors():
    def __init__(self, values):
        #print(values)
        if isinstance(values, str):
            self.multipliers = []
            values = values[1:].split('(')
            #print(values)
            for val in values:
                val = val.split(')')
                #print(val)
                if val[1]:
                    self.multipliers.append((Poly(val[0]),val[1]))
                else:
                    self.multipliers.append((Poly(val[0]), ""))
        else:
            self.multipliers = values

    def __str__(self):
        fts = ""
        for mul in self.multipliers:
            fts += f"({mul[0].__str__()}){mul[1]}"
        return fts

    def expand(self):
        p = Poly({0: 1})
        for mul in self.multipliers:
            if mul[1].replace("^", ""):
                for i in range(int(mul[1].replace("^", ""))):
                    p *= mul[0]
            else:
                p *= mul[0]
        return p