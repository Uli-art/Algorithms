from itertools import product
from copy import deepcopy
from collections import Counter
import numpy as np


def balance_condition(a, b, c):
    diff = sum(a) - sum(b)
    if diff > 0:
        new_b = np.append(b, diff)
        new_a = a
        new_c = np.append(c, [[0] * c.shape[0]], axis=1)
    elif diff < 0:
        new_b = b
        new_a = np.append(a, -diff)
        new_c = np.append(c, [[0] * c.shape[1]], axis=0)
    else:
        new_a = a
        new_b = b
        new_c = c
    return new_a, new_b, new_c


def north_west_corner(a, b):
    m, n = len(a), len(b)
    X = np.zeros((m, n))
    B = []
    i, j = 1, 1
    while not (i == m and a[i - 1] == 0 and j == n and b[i - 1] == 0):
        B.append((i, j))

        diff = min(a[i - 1], b[j - 1])
        X[i - 1][j - 1] = diff
        b[j - 1] -= diff
        a[i - 1] -= diff

        if a[i - 1] == 0:
            if i + 1 <= m:
                i += 1
        if b[j - 1] == 0:
            if j + 1 <= n:
                j += 1
    return X, B


def potential_method(X, B, c):
    m, n = len(c), len(c[0])
    i_s = list(range(1, m + 1))
    j_s = list(range(1, n + 1))
    all_positions = list(product(i_s, j_s))

    while True:
        sys = [[0 for i in range(m + n)] for j in range(m + n)]
        c_vals = [0 for i in range(m + n)]
        for step, (i, j) in enumerate(B):
            sys[step][i - 1] = 1
            sys[step][m + j - 1] = 1
            c_vals[step] = c[i - 1][j - 1]
        sys[-1][0] = 1
        c_vals[-1] = 0
        sol = np.linalg.solve(sys, c_vals)
        u = sol[:m]
        v = sol[m:]
        non_basis_positions = [pair for pair in all_positions if pair not in B]

        optimal = True
        new_base_i, new_base_j = None, None
        for i, j in non_basis_positions:
            if not u[i - 1] + v[j - 1] <= c[i - 1][j - 1]:
                optimal = False
                new_base_i, new_base_j = i, j
                break

        if optimal:
            return X, B

        B.append((new_base_i, new_base_j))
        B_temp = deepcopy(B)
        while True:
            i_list = [i for (i, j) in B_temp]
            j_list = [j for (i, j) in B_temp]

            i_counter = Counter(i_list)
            j_counter = Counter(j_list)

            i_del = [i for i in i_counter if i_counter[i] < 2]
            j_del = [j for j in j_counter if j_counter[j] < 2]

            if not i_del and not j_del:
                break
            B_temp = [(i, j) for (i, j) in B_temp if i not in i_del
                      and j not in j_del]

        B_copy = deepcopy(B_temp)
        plus, minus = [], []
        plus.append(B_copy.pop())

        while B_copy:
            if len(plus) > len(minus):
                for index, (i, j) in enumerate(B_copy):
                    if plus[-1][0] == i or plus[-1][1] == j:
                        minus.append(B_copy.pop(index))
                        break
            else:
                for index, (i, j) in enumerate(B_copy):
                    if minus[-1][0] == i or minus[-1][1] == j:
                        plus.append(B_copy.pop(index))
                        break

        signs = [(pair, '+') if pair in plus else (pair, '-') for pair in B_temp]

        minuses = [X[i - 1][j - 1] for (i, j), sign in signs if sign == '-']
        theta = min(minuses)

        for (i, j), sign in signs:
            if sign == '+':
                X[i - 1][j - 1] += theta
            else:
                X[i - 1][j - 1] -= theta

        i_del, j_del = None, None
        for (i, j) in B:
            if X[i - 1][j - 1] == 0:
                i_del, j_del = i, j
                break
        B.remove((i_del, j_del))


def transportation_problem(a, b, c):
    a, b, c = balance_condition(a, b, c)
    X, B = north_west_corner(a, b)
    X, B = potential_method(X, B, c)
    return X, B
