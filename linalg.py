import numpy as np


def psevdodiv(a, b, z):
    for k in range(z):
        if a == b * k % z:
            return k


def psevdodivarr(a, b, z):
    for i in a:
        i = psevdodiv(i, b, z)
    return a


def kernel():
    z = 7
    a = np.asarray([[-1, -1, 2, 0],
                    [1, 4, 0, 0],
                    [-1, 1, 1, 0],
                    [-4, 3, 1, 0]])

    for i in range(len(a)):
        for k in range(len(a)):
            if i != k:
                for j in range(0, z):
                    if (a[k][i] + a[i][i] * j) % z == 0:
                        x = a[k]
                        a[k] = (a[k] + a[i] * j) % z
                        print(f"{a[k]} = {x} + {a[i]}*{j}%{z}")
                        break

    print(a)


def ToReducedRowEchelonForm(M):
    # if not M: return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i], M[r] = M[r], M[i]
        lv = M[r][lead]
        M[r] = psevdodivarr(M[r], lv, 7)
        print(f"{lead} row {r} = {M[r]}")
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = (M[i]-M[r]*lv) % 7
        lead += 1


mtx = np.asarray([
                    [1, 1, 3, 3],
                    [0, 2, 1, 6],
                    [0, 0, 5, 1],
                    [0, 2, 6, 0]])

ToReducedRowEchelonForm(mtx)

for rw in mtx:
    print(', '.join((str(rv) for rv in rw)))

# for i in range(7):
#    for j in range(7):
#        f = 0
#        for k in range(7):
#            if i == j*k%7:
#                print(f"{i}/{j}={k}")
#                f = 1
#        if f == 0:
#            print(f"her tam {i} na {j} ne delitsya")
# kernel()
