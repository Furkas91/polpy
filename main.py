from factors import Factors
from polynom import Polynom, Poly

def main():
    p = Poly(str(input()))
    p.berlekamp()
    #s = Poly(str(input()))
    #Poly.z = 7
    #print(p.expand().derivative())
    #print(s)
    #p.ringz()
    #print(p)
    #s = p.squarefree()
    #print(s)
    #print(s.expand())
    #print(p-s)
    #print(p*s)
    #print(p.gcd(s))
    #gced = p.gcdex(s)
    #print(gced[0])
    #print(gced[1])
    #print(gced[2])


if __name__ == '__main__':
    main()