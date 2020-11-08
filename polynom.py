import numpy as np


class Polynom:
    z = np.NaN

    def __init__(self, values):
        if isinstance(values, str):
            values = values.replace(' ', '')
            values = values.replace('-', "+-")
            mas = values.split('+')
            self.koefs = np.zeros(10, np.int8)
            for k in mas:
                if 'x' in k:
                    q = k.split('x^')
                    if k[-1] == 'x':
                        i = 1
                    else:
                        i = int(q[-1])
                    if k[0] == 'x':
                        v = 1
                    else:
                        v = int(q[0].split('x')[0])
                else:
                    i = 0
                    v = int(k)
                self.koefs[i] += v
        else:
            # print(values)
            self.koefs = values

    def __str__(self):
        values = ""
        for i in range(9, 0, -1):
            if self.koefs[i] != 0:
                if values:
                    values += '+'
                if i == 1:
                    st = ""
                else:
                    st = f"^{i}"
                if self.koefs[i] == 1:
                    v = ""
                else:
                    v = f"{self.koefs[i]}"
                values += f"{v}x{st}"
        if self.koefs[0] != 0:
            values += f"+{self.koefs[0]}"
        return values.replace("+-", "-")

    def __add__(self, other):
        return Polynom(self.koefs + other.koefs)

    def __sub__(self, other):
        return Polynom(self.koefs - other.koefs)

    def __mul__(self, other):
        mul = np.zeros(20, np.int8)
        for i in range(10):
            mul += np.insert(np.zeros(10, np.int8), i, self.koefs[i] * other.koefs)
        return Polynom(mul)


class Poly:
    z = np.NaN

    def __init__(self, values):
        if isinstance(values, str):
            values = values.replace(' ', '')
            values = values.replace('-', "+-")
            mas = values.split('+')
            self.koefs = {}
            for k in mas:
                if 'x' in k:
                    q = k.split('x^')
                    if k[-1] == 'x':
                        i = 1
                    else:
                        i = int(q[-1])
                    if k[0] == 'x':
                        v = 1
                    else:
                        v = int(q[0].split('x')[0])
                else:
                    i = 0
                    v = int(k)
                if self.koefs.get(i):
                    self.koefs[i] += v
                else:
                    self.koefs[i] = v
        else:
            # print(values)
            self.koefs = values

    def __str__(self):
        values = ""
        # print(self.koefs)
        for i in sorted(self.koefs, reverse=True):
            if self.koefs[i] > 0:
                if values:
                    values += '+'
            else:
                values += '-'
            if i == 1:
                st = ""
            else:
                st = f"^{i}"
            if abs(self.koefs[i]) == 1:
                v = ""
            else:
                v = f"{abs(self.koefs[i])}"
            if i != 0:
                values += f"{v}x{st}"
            else:
                values += f"{abs(self.koefs[i])}"
        return values

    def __add__(self, other):
        h = {}
        # TODO: add optimized queue
        for i in self.koefs:
            h[i] = self.koefs[i]
        for i in other.koefs:
            if h.get(i):
                h[i] += other.koefs[i]
            else:
                h[i] = other.koefs[i]
        return Poly(h)

    def __sub__(self, other):
        # TODO: optimize that function, it has a lot of iterations
        c = Poly(other.koefs.copy())
        for i in c.koefs:
            c.koefs[i] *= -1
        r = self + c
        cr = self + c
        for i in cr.koefs:
            if r.koefs[i] == 0:
                r.koefs.pop(i)
        return r

    def __mul__(self, other):
        h = {}
        for i in self.koefs:
            for j in other.koefs:
                if h.get(i + j):
                    h[i + j] += self.koefs[i] * other.koefs[j]
                else:
                    h[i + j] = self.koefs[i] * other.koefs[j]
        return Poly(h)
