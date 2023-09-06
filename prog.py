import numpy as np


def matrix(A, B):
    num = len(A)

    if num == 1:
        return np.array([[A[0][0] * B[0][0]]])

    spl = num // 2
    A11 = A[:spl, :spl]
    A12 = A[:spl, spl:]
    A21 = A[spl:, :spl]
    A22 = A[spl:, spl:]
    B11 = B[:spl, :spl]
    B12 = B[:spl, spl:]
    B21 = B[spl:, :spl]
    B22 = B[spl:, spl:]

    P1 = matrix(A11, np.subtract(B12, B22))
    P2 = matrix(np.add(A11, A12), B22)
    P3 = matrix(np.add(A21, A22), B11)
    P4 = matrix(A22, np.subtract(B21, B11))
    P5 = matrix(np.add(A11, A22), np.add(B11, B22))
    P6 = matrix(np.subtract(A12, A22), np.add(B21, B22))
    P7 = matrix(np.subtract(A11, A21), np.add(B11, B12))

    C11 = np.subtract(np.add(np.add(P5, P4), P6), P2)
    C12 = np.add(P1, P2)
    C21 = np.add(P3, P4)
    C22 = np.subtract(np.subtract(np.add(P5, P1), P3), P7)

    C = np.zeros((n, n))
    C[:spl, :spl] = C11
    C[:spl, spl:] = C12
    C[spl:, :spl] = C21
    C[spl:, spl:] = C22

    return C


n = 2
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = matrix(A, B)
print(result)