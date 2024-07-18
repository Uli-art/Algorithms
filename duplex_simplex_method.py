import numpy as np


def duplex_simplex_method(c, A, b, B):
    while True:
        n = len(c)
        A_B = A[:, B]
        A_B_inv = np.linalg.inv(A_B)
        c_B = [c[i] for i in B]
        y = c_B @ A_B_inv
        ae_B = A_B_inv @ b
        ae = []
        for i in range(n):
            if i in B:
                ae.append(ae_B[B.index(i)])
            else:
                ae.append(0)
        if all(el >= 0 for el in ae):
            return ae
        ae_j = [i for i, x in enumerate(ae) if x < 0][0]
        k = B.index(ae_j)
        delta_y = A_B_inv[k]
        mu = {}
        for i in range(n):
            if i not in B:
                A_j = delta_y @ A[:, i]
                mu[i] = A_j
        if all(el >= 0 for el in mu.values()):
            raise Exception("Задача не совместна")
        sigma = {}
        for index, el in mu.items():
            if el < 0:
                j = index
                sigma_j = (c[j] - A[:, j].transpose() @ y) / el
                sigma[index] = sigma_j
        sigma_0 = min(sigma.values())
        j_0 = list(sigma.keys())[list(sigma.values()).index(sigma_0)]
        B[k] = j_0
