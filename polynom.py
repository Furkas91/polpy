import numpy as np


class Polynom:
    z = 0

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
    z = 5

    def __init__(self, values):
        if isinstance(values, str):
            values = values.replace(' ', '')
            values = values.replace('-', "+-")
            values = values.replace("-x", "-1x")
            # print(values)
            mas = values.split('+')
            # print(mas)
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
                # print(f"{i}x^{v}")
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
        if len(self.koefs) == 0:
            values = "0"
        return values

    def __eq__(self, other):
        if isinstance(other, Poly):
            return len(self.koefs) == len(other.koefs)
        elif isinstance(other, int):
            return len(self.koefs) == other

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
        return Poly(h).ringz()

    def __sub__(self, other):
        c = Poly(other.koefs.copy())
        for i in c.koefs:
            c.koefs[i] *= -1
        r = self + c
        return r.ringz()

    def __mul__(self, other):
        h = {}
        for i in self.koefs:
            for j in other.koefs:
                if h.get(i + j):
                    h[i + j] += self.koefs[i] * other.koefs[j]
                else:
                    h[i + j] = self.koefs[i] * other.koefs[j]
        return Poly(h).ringz()

    def __divmod__(self, other):
        # division function that only works on a prime remainder ring
        # initiate internal variables
        r = Poly(self.koefs.copy())
        d = Poly(other.koefs.copy())
        q = Poly({})
        # main cycle division
        while True:
            # if r=0, then division finished with reminder = 0
            if r == 0:
                break
            # check degrees reminder's and divider's
            kr = r.deg()
            kd = d.deg()
            i = kr - kd
            if i < 0:
                break
            j = 1
            # find suitable multiplier for this step
            for j in range(self.z):
                if r.koefs[kr] == d.koefs[kd] * j % self.z:
                    break
                # i don't know what that condition mean
                elif j == self.z - 1:
                    print("attention")
                    return Poly({0: 0}), Poly({0: 0})
            # creating monom from quotient
            kq = Poly({i: j})
            #print(kq)
            # add monom to quotient
            q += kq
            # computing the reminder
            r = r - d * kq
        return q, r

    def __floordiv__(self, other):
        return self.__divmod__(other)[0]

    def __mod__(self, other):
        return self.__divmod__(other)[1]

    def __pow__(self):
        # TODO: write an algorithm for exponentiation
        pass

    def ringz(self):
        if self.z:
            cr = Poly(self.koefs.copy())
            for i in cr.koefs:
                #print(self.koefs[i])
                self.koefs[i] %= self.z
                #print(f"= {self.koefs[i]} mod {self.z}")
                if self.koefs[i] == 0:
                    self.koefs.pop(i)
        return self

    def deg(self):
        return sorted(self.koefs, reverse=True)[0]

    def normalize(self):
        pass

    def gcd(self, other):
        a = Poly(self.koefs.copy())
        b = Poly(other.koefs.copy())

        while len(b.koefs) > 0:
            a, b = b, a % b
            #print(f"a = {a}\nb = {b}")
        return a

    def gcdsup(self, other):
        if other == 0:
            #print(other)
            return self, Poly({0: 1}), Poly({})
        else:
            #print(f"self {self}\n other {other} \n mod {self % other}")
            d, x, y = other.gcdsup(self % other)
            return d, y, x - y * (self // other)

    def gcdex(self, other):
        a = Poly(self.koefs.copy())
        b = Poly(other.koefs.copy())
        return a.gcdsup(b)

    def derivative(self):
        h = {}
        for i in self.koefs:
            if i > 0:
                h[i - 1] = self.koefs[i] * i
        return Poly(h).ringz()

    def squarefree(self):
        # TODO: write to basic square free algorithm
        from factors import Factors
        p = Poly(self.koefs.copy())
        f = Factors([])
        deg = 1
        while p.deg() != 0:
            g = p.derivative()
            print(f" g = {g}")
            gx = p.gcd(g)
            print(f" gx = {gx}")
            tx = p // gx
            print(f" tx = {tx}")
            fx = gx.gcd(tx)
            print(f" fx = {fx}")
            if fx.deg() > 0:
                mon = tx // fx
            else:
                mon = tx
            print(f" mon = {mon}")
            f.multipliers.append((mon, f"^{deg}"))
            p = gx
            print(deg)
            deg += 1
        return f