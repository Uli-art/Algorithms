import numpy as np


def find_inverse_matrix(A_inverse, x, i, n):
    l = np.array(A_inverse) @ np.array(x)
    if l[i] == 0:
        raise Exception
    l_i = l[i]
    l[i] = -1
    l = np.array(l) * (-1/l_i)
    Q = np.eye(n)
    for j in range(0, n):
        Q[j][i] = l[j]
    E = np.zeros(shape=(n, n))
    for j in range(0, n):
        for k in range(0, n):
            if i == j:
                E[j][k] = Q[j][i] * A_inverse[i][k]
                continue
            E[j][k] = Q[j][j] * A_inverse[j][k] + Q[j][i] * A_inverse[i][k]
    return E


def main_phase_of_simplex_method(c, A, x, B):
    A_B = A[:, B]
    A_B_inv = np.linalg.inv(A_B)
    while True:
        c_B = [c[i] for i in B]
        u_T = c_B @ A_B_inv
        delta = u_T @ A - c
        if all(n >= 0 for n in delta):
            return x, B
        j_0 = next((n for n in range(len(delta)) if delta[n] < 0), None)
        A_j_0 = A[:, j_0]
        z = A_B_inv @ A_j_0
        tetta = [np.inf] * len(z)
        for i in range(len(z)):
            if z[i] > 0:
                tetta[i] = x[B[i]] / z[i]
        tetta_0 = min(tetta)
        if tetta_0 == np.inf:
            raise Exception("целевой функционал задачи (1) не ограничен сверху на множестве допустимых планов")
        k = tetta.index(tetta_0)
        j_0_star = B[k]
        B[k] = j_0
        x[j_0] = tetta_0
        for i in range(len(B)):
            if i != k:
                x[B[i]] = x[B[i]] - tetta_0 * z[i]
        x[j_0_star] = 0
        A_B_inv = find_inverse_matrix(A_B_inv, A_j_0, k, len(A_B_inv[0]))


def first_phase_of_simplex_method(c, A, b):
    n = len(A[0])
    m = len(A)
    for i in range(len(b)):
        if b[i] < 0:
            b[i] = -1 * b[i]
            A[i] = [-n for n in A[i]]
    c_tilda = [0] * n + [-1] * m
    A_tilda = np.concatenate((A, np.eye(m)), axis=1)
    x_tilda = [0] * n + b
    B_tilda = [i for i in range(n , n + m )]
    opt_plan, B = main_phase_of_simplex_method(c_tilda, A_tilda, x_tilda, B_tilda)
    if not all(opt_plan[n] == 0 for n in range(n + 1, n + m - 1)):
        raise Exception("Задача не совместна")
    dop_plan = opt_plan[0:n]
    while True:
        if all(el <= n for el in B):
            return dop_plan, B
        A_B = A_tilda[:, B]
        A_B_inv = np.linalg.inv(A_B)
        j_k = max(B)
        k = B.index(j_k)
        change = False
        for j in range(0, n):
            if j not in B:
                l = A_B_inv @ A_tilda[:, j]
                if l[k] != 0:
                    B[k] = j
                    change = True
                    break
        if not change:
            i = j_k - n
            A = np.delete(A, i, axis=0)
            del b[i]
            del B[k]
            A_tilda = np.delete(A_tilda, i, axis=0)

