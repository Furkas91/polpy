import numpy as np
import linalg as la
import itertools


class Polynom:
    z = 7

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


def to_hash(a):
    h = {}
    for i in range(len(a)):
        if a[i] != 0:
            h[len(a) - i - 1] = a[i]
    return h


class Poly:
    z = 13

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
            # print(kq)
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
                # print(self.koefs[i])
                self.koefs[i] %= self.z
                # print(f"= {self.koefs[i]} mod {self.z}")
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
            print(f"a = {a}\nb = {b}")
        return a

    def gcdsup(self, other):
        if other == 0:
            # print(other)
            return self, Poly({0: 1}), Poly({})
        else:
            # print(f"self {self}\n other {other} \n mod {self % other}")
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

    def to_nparray(self, n):
        k = np.zeros(n, np.int32)
        # print(self.koefs)
        for i in self.koefs:
            k[i] = self.koefs[i]
        return k

    def berlekamp(self):
        from factors import Factors
        self.ringz()
        print(self)
        f = Factors([])
        m = []
        for i in range(self.deg()):
            h = Poly({i * self.z: 1})
            # if i > 0:
            #     h = h + Poly({i * self.z -1: 1})
            r = h % self
            print(f"{h}/{self}={r}")
            print(r.to_nparray(self.deg()))
            m.append(r.to_nparray(self.deg()))
        Q = np.asarray(m).transpose()[::-1]
        for i in range(len(Q)):
            Q[i] = Q[i][::-1]
        # A = (Q - np.asarray([[1, 0, 0, 0],
        #                      [0, 1, 0, 0],
        #                      [0, 0, 1, 0],
        #                      [0, 0, 0, 1]])) % self.z
        print(m)
        print(Q)

        A = []
        for i in range(len(Q)):
            #print("A append: ", Q[i])
            A.append(Q[i] % self.z)
            A[i][i] -= 1
        A = np.asarray(A)
        # TODO: Add kernel function
        print(A)
        a = la.kernel(A)
        #a = np.asarray([0, 0, 0, 1])
        # a = [1, 5, 3, 0]
        g = Poly(to_hash(a)).ringz()
        print(f"g = {g}")
        for i in range(self.z):
            d = self.gcdex(g - Poly({0: i}))[0]
            #d = d // d.koefs[d.deg()]

            if d.deg() != 0:
                d = d // Poly({0: d.koefs[d.deg()]})
                f.multipliers.append((d, ""))
            print(f"d{i} = {d}")
        print(f)
        return f

    def henzel_lifting(self, k=2):
        f = self.berlekamp()
        g1 = f.multipliers[0][0]
        h1 = f.multipliers[1][0]
        for t in range(k - 1):
            d = (f - g1*h1)
            # TODO: finish that function
            pass

    def cartesian_product_itertools(self, arrays):
        return np.array(list(itertools.product(*arrays)))

    def devisors(self, N):
        D = np.array([-1, 1])
        d = 2
        while (d * d <= np.abs(N)):
            if N % d == 0:
                D = np.append(np.append(D, d), -d)
                d_new = N // d
                if d_new != d:
                    D = np.append(np.append(D, d_new), -d_new)
            d += 1

        D = np.append(np.append(D, N), -N)
        return np.unique(D)

    def kroneker(self):
        result_file = open('result.txt', 'w')
        result_set = set()
        result = np.array([])
        coefs = list(self.koefs)
        print("coefs is: ", coefs)
        p = np.poly1d(coefs)
        p0 = p(0)
        flag = False
        for i in range((len(coefs) - 1) // 2):
            if p(i) == 0:
                result_set.add(str(np.array([1, -i])))

        if len(result_set) == 0:
            U = self.devisors(p0).copy()
            for i in range(1, (len(coefs) - 1) // 2 + 1):
                M = self.devisors(p(i)).copy()
                U1 = np.array([])
                if i == 1:
                    U = self.cartesian_product_itertools([U, M])
                else:
                    U1 = self.cartesian_product_itertools([U, M])
                    U_new = np.array([np.append(U1[0][0], U1[0][1])])
                    for u in range(1, len(U1)):
                        new_u = np.array(np.append(U1[u][0], U1[u][1]))
                        U_new = np.append(U_new, [new_u], axis=0)
                    U = U_new.copy()
                for u in U:
                    vars = np.array(list(itertools.permutations(u)))
                    for coefs_u in vars:
                        res = np.polydiv(coefs, coefs_u)[1][0]
                        if res == 0.0:
                            result_set.add(str(coefs_u))
        result_file.write(str(result_set))
        result_file.close()
        return result
