from polynom import Polynom, Poly


def main():
    p = Poly(str(input()))
    s = Poly(str(input()))

    #print(s)
    print(p+s)
    print(p-s)
    print(p*s)

if __name__ == '__main__':
    main()
