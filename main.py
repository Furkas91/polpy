from polynom import Polynom

def main():
    s = Polynom(str(input()))
    p = Polynom(str(input()))
    print(p*s)
    print(p+s)
    print(p-s)

if __name__ == '__main__':
    main()
