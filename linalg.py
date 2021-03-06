import numpy as np

hash = {}


def psevdodiv(a, b, z):
    global hash
    if hash.get(z):
        if hash[z].get(a):
            if hash[z][a].get(b):
                return hash[z][a][b]
            else:
                if a % b != 0:
                    for k in range(z):
                        if a == b * k % z:
                            hash[z][a][b] = k
                            return k
                else:
                    k = a // b
                    hash[z][a][b] = k
                    return k

        else:
            if a % b != 0:
                for k in range(z):
                    if a == b * k % z:
                        hash[z][a] = {b: k}
                        return k
            else:
                k = a // b
                hash[z][a] = {b: k}
                return k
    else:
        if a % b != 0:
            for k in range(z):
                if a == b * k % z:
                    hash[z] = {a: {b: k}}
                    return k
        else:
            k = a // b
            hash[z] = {a: {b: k}}
            return k

def psevdodivarr(a, b, z):
    for i in a:
        i = psevdodiv(i, b, z)
    return a


def check_ker_matrix(matrix, kernel, z):
    mul = np.matmul(matrix, kernel.transpose()) % z
    # return mul
    return np.all(mul == 0)


# def get_solution(ker_matrix, z=7):
#     zero = ker_matrix[np.all(ker_matrix[:, :len(ker_matrix[0])/2] == 0, axis=1)]
#     kernel = zero[:, len(ker_matrix/2):len(ker_matrix[0])]
#     solution = kernel[kernel[:, 0] != 0]
#     b = solution[0][0]
#     x = psevdodiv(1, b, z)
#     monic_pol = (solution[0] * x) % z
#     # print(monic_pol)
#     return monic_pol


# def kernel(matrix, z=13):
#     # z = 7
#     # matrix = np.asarray([[-1, -1, 2, 0],
#     #                      [1, 4, 0, 0],
#     #                      [-1, 1, 1, 0],
#     #                      [-4, -4, 1, 0]])
#
#     matrix_t = matrix.transpose()
#     # matrix_t = matrix
#     u_matrix = np.eye(len(matrix_t))
#     ker_matrix = np.concatenate((matrix_t, u_matrix), axis=1)
#     ker_matrix = ker_matrix % z
#     ind_row = 0
#     print()
#
#     for col in range(len(matrix[0])):
#         print('Step for {} column'.format(col))
#         for row in range(ind_row, len(matrix)):
#             # Pivoting
#             if ker_matrix[row][col]:
#                 ker_matrix[[ind_row, row]] = ker_matrix[[row, ind_row]]
#                 break
#
#         b = ker_matrix[ind_row][col]
#         print("b is ", b)
#         x = psevdodiv(1, b, z)
#         if x:
#             ker_matrix = ker_matrix * x
#         else:
#             ker_matrix = ker_matrix * 1
#         # print("x is ", x)
#
#         ker_matrix %= z
#         print(ker_matrix)
#
#         for row in range(ind_row + 1, len(matrix)):
#             # ax + b = 0 mod(z)
#             # ax = -b mod(z)
#             b = (-1) * ker_matrix[row][col]
#
#             # x = -b/a mod(z)
#             x = psevdodiv(b % z, ker_matrix[ind_row][col], z)
#
#             # b = ax + b
#             ker_matrix[row] += x * ker_matrix[ind_row]
#
#         # ker_matrix %= z
#         print('Matrix after step\n {}'.format(ker_matrix))
#         # print(ker_matrix)
#         ind_row += 1
#
#     # print('__________________')
#     # print('Final matrix')
#     ker_matrix %= z
#
#     print("\nKernel matrix is\n", ker_matrix)
#
#     zero = ker_matrix[np.all(ker_matrix[:, :len(matrix)] == 0, axis=1)]
#     kernel = zero[:, len(matrix):len(ker_matrix[0])]
#     print(kernel)
#     solution = kernel[kernel[:, len(matrix)-1] != 0]
#     print(solution)
#
#     b = solution[0][len(matrix)-1]
#     x = psevdodiv(1, b, z)
#     solution[0] = np.flip(solution[0])
#     print(solution[0])
#     monic_pol = (solution[0] * x) % z
#     print(solution[0])
#
#     return monic_pol.astype(int)


def kernel(matrix, z=13):
    # z = 7
    # matrix = np.asarray([[-1, -1, 2, 0],
    #                      [1, 4, 0, 0],
    #                      [-1, 1, 1, 0],
    #                      [-4, -4, 1, 0]])

    matrix_t = matrix.transpose()
    # matrix_t = matrix
    u_matrix = np.eye(len(matrix_t), dtype=int)
    ker_matrix = np.concatenate((matrix_t, u_matrix), axis=1)
    ker_matrix = ker_matrix % z
    ind_row = 0
    print()

    for col in range(len(matrix[0])):
        print('Step for {} column'.format(col))
        #         first_element_idx = ind_row
        #         if not ker_matrix[ind_row][col]:
        for row in range(ind_row, len(matrix)):
            # Pivoting
            if ker_matrix[row][col]:
                #                 print(ker_matrix[row][col])
                ker_matrix[[ind_row, row]] = ker_matrix[[row, ind_row]]
                #                 print("Есть ненулевой элемент")
                # есть ненулевой элемент в столбце
                flag = True
                break
            else:
                # только нулевые элементы в столбце
                flag = False

        if flag:
            #             ind_row -= 1
            print("Есть ненулевой элемент")
            b = ker_matrix[ind_row][col]
            print("b is ", b)
            x = psevdodiv(1, b%z, z)
            if x:
                ker_matrix[ind_row] = ker_matrix[ind_row] * x
            else:
                ker_matrix[ind_row] = ker_matrix[ind_row] * 1
            # print("x is ", x)

            # ker_matrix %= z
            # print(ker_matrix)

            for row in range(ind_row + 1, len(matrix)):
                # ax + b = 0 mod(z)
                # ax = -b mod(z)
                b = (-1) * ker_matrix[row][col]

                # x = -b/a mod(z)
                x = psevdodiv(b % z, ker_matrix[ind_row][col]%z, z)

                # b = ax + b
                ker_matrix[row] += x * ker_matrix[ind_row]

            # ker_matrix %= z
            print('Matrix after step\n {}'.format(ker_matrix))
            # print(ker_matrix)
            ind_row += 1

        ker_matrix %= z

    # print('__________________')
    # print('Final matrix')
    ker_matrix %= z

    print("\nKernel matrix is\n", ker_matrix)

    zero = ker_matrix[np.all(ker_matrix[:, :len(matrix)] == 0, axis=1)]
    kernel = zero[:, len(matrix):len(ker_matrix[0])]
    print(kernel)
    # 2
    # solution = kernel[kernel[:, len(matrix) - 1] != 0]
    # 1
    solution = kernel[kernel[:, 0] != 0]
    print(solution)

    # 2
    # b = solution[0][len(matrix) - 1]
    # 1
    b = solution[0][0]
    x = psevdodiv(1, b%z, z)
    # 2
    # solution[0] = np.flip(solution[0])
    print(solution[0])
    monic_pol = (solution[0] * x) % z
    print(solution[0])

    return monic_pol.astype(int)


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
