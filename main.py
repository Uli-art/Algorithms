from functions import *
from duplex_simplex_method import *
from transport import *

if __name__ == '__main__':
    # Lab_1 -------------------------------------------------------------------------------------------------
    # A = [[1, -1, 0], [0, 1, 0], [0, 0, 1]]
    # A_inverse = [[1, 1, 0], [0, 1, 0], [0, 0, 1]]
    # x = [1, 0, 1]
    # i = 2
    # n = 3
    #
    # A = [[1, 0, 5], [2, 1, 6], [3, 4, 0]]
    # A_inverse = [[-24, 20, -5], [18, -15, 4], [5, -4, 1]]
    # x = [2, 2, 2]
    # i = 1
    # n = 3
    # try:
    #     print(find_inverse_matrix(A_inverse, x, i, n))
    # except Exception:
    #     print("Irreversible")

    # Lab_2 -------------------------------------------------------------------------------------------------
    # A = np.array([
    #     [-1, 1, 1, 0, 0],
    #     [1, 0, 0, 1, 0],
    #     [0, 1, 0, 0, 1]
    # ])
    # c = [1, 1, 0, 0, 0]
    # b = [1, 3, 2]
    # x = [0, 0, 1, 3, 2]
    # B = [2, 3, 4]
    # try:
    #     print(main_phase_of_simplex_method(c, A, x, B))
    # except Exception as e:
    #     print(e)

    # Lab_3 -------------------------------------------------------------------------------------------------
    # A = np.array([
    #     [1, 1, 1],
    #     [2, 2, 2]
    # ])
    # c = [1, 0, 0]
    # b = [-1, -1]
    #
    # try:
    #     print(first_phase_of_simplex_method(c, A, b))
    # except Exception as e:
    #     print(e)

    # Lab_4 -------------------------------------------------------------------------------------------------
    # A = np.array([
    #     [-2, -1, -4, 1, 0],
    #     [-2, -2, -2, 0, 1]
    # ])
    # c = [-4, -3, -7, 0, 0]
    # b = [-1, -1.5]
    # B = [3, 4]

    # try:
    #     print(duplex_simplex_method(c, A, b, B))
    # except Exception as e:
    #     print(e)

    # Lab_5 -------------------------------------------------------------------------------------------------
    # a = np.array([100, 300, 300])
    # b = np.array([300, 200, 200])
    # c = np.array([[8, 4, 1],
    #               [8, 4, 3],
    #               [9, 7, 5]])

    a = np.array([50, 50, 100])
    b = np.array([40, 90, 70])
    c = np.array([[2, 5, 3],
                  [4, 3, 2],
                  [5, 1, 2]])

    ans = transportation_problem(a, b, c)
    print(f"X = {ans[0]}\nB = {ans[1]}")



