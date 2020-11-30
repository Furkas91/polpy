import numpy as np


def psevdodiv(a, b, z):
    for k in range(z):
        if a == b * k % z:
            return k


def psevdodivarr(a, b, z):
    for i in a:
        i = psevdodiv(i, b, z)
    return a


def check_ker_matrix(matrix, kernel, z):
    mul = np.matmul(matrix, kernel.transpose()) % z
    # return mul
    return np.all(mul == 0)


def get_solution(ker_matrix, z=7):
    zero = ker_matrix[np.all(ker_matrix[:, :len(ker_matrix[0])/2] == 0, axis=1)]
    kernel = zero[:, len(ker_matrix/2):len(ker_matrix[0])]
    solution = kernel[kernel[:, 0] != 0]
    b = solution[0][0]
    x = psevdodiv(1, b, z)
    monic_pol = (solution[0] * x) % z
    # print(monic_pol)
    return monic_pol


def kernel(matrix, z=7):
    # z = 7
    # matrix = np.asarray([[-1, -1, 2, 0],
    #                      [1, 4, 0, 0],
    #                      [-1, 1, 1, 0],
    #                      [-4, -4, 1, 0]])

    matrix_t = matrix.transpose()
    u_matrix = np.eye(len(matrix_t))
    ker_matrix = np.concatenate((matrix_t, u_matrix), axis=1)
    ker_matrix = ker_matrix % z
    ind_row = 0

    for col in range(len(matrix[0])):
        # print('Step for {} column'.format(col))
        for row in range(ind_row, len(matrix)):
            # Pivoting
            if ker_matrix[row][col]:
                ker_matrix[[ind_row, row]] = ker_matrix[[row, ind_row]]
                break

        for row in range(ind_row + 1, len(matrix)):
            # ax + b = 0 mod(z)
            # ax = -b mod(z)
            b = (-1) * ker_matrix[row][col]

            # x = -b/a mod(z)
            x = psevdodiv(b % z, ker_matrix[ind_row][col], z)

            # b = ax + b
            ker_matrix[row] += x * ker_matrix[ind_row]

        # ker_matrix %= z
        # print('Matrix after {} step'.format(col))
        # print(ker_matrix)
        ind_row += 1

    # print('__________________')
    # print('Final matrix')
    ker_matrix %= z
    # print(ker_matrix)
    return ker_matrix


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
                M[i] = (M[i] - M[r] * lv) % 7
        lead += 1


mtx = np.asarray([[1, 1, 3, 3],
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
