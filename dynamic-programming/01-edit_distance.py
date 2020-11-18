"""

Date: November 18, 2020

Dynamic Programming solution for the edit distance problem written in Python 

"""


class EditDistance:
    """
    Use : 

    """

    def __init__(self):
        self.__prepare__()

    def __prepare__(self, N=0, M=0):
        self.dp = [[-1 for y in range(0, M) for x in range(0, N)]]

    def __solve_DP(self, x, y):
        if x == -1:
            return y+1
        if y == -1:
            return x+1
