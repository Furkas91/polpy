from factors import Factors
from polynom import Polynom, Poly


def main():
    Poly.z = 0
    p = Poly("112x^4+58x^3-31x^2+107x-66")
    print(p.factorize())
    #p = Poly("x^2+9x+9")
    #d = Poly("8x^2+12x+10")
    #h = Poly("2x^2+5x+5")
#
    ## f = p.berlekamp()
    #for i in p.enumeration(d):
    #    print(i[0], i[1])
    #for i in h.naturaltoint():
    #    print(i)
    # s = Poly(str(input()))
    # Poly.z = 7
    # print(p.expand().derivative())
    # print(s)
    # p.ringz()
    # print(p)
    # s = p.squarefree()
    # print(s)
    # print(s.expand())
    # print(p-s)
    # print(p*s)
    # print(p.gcd(s))
    # s = Poly("x^2")
    # gced = p.gcdex(s)
    # print(gced[0])
    # print(gced[1])
    # print(gced[2])
    # h1 = gced[1]//Poly({0: 9})
    # h2 = gced[2]//Poly({0: 9})
    # print(f"{h1} + {h2}={gced[0]}")
    # print(Poly("7x+8")//Poly("7"))


if __name__ == '__main__':
    main()
