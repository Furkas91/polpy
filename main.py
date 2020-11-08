from polynom import Polynom, Poly


def main():
    p = Poly(str(input()))
    s = Poly(str(input()))

    #print(s)
    #print(p+s)
    #print(p-s)
    #print(p*s)
    print(p.gcd(s))
    gced = p.gcdex(s)
    print(gced[0])
    print(gced[1])
    print(gced[2])

if __name__ == '__main__':
    main()
