"""Daily Challenge #3.

~~~I am Neo from the Matrix~~~
Given an m x n binary matrix mat, return the number of special
positions in mat. A position (i, j) is called special if
mat[i][j] == 1 and all other elements in row i and column j are 0
(rows and columns are 0-indexed).

Case:
    1. mat = [[1, 0, 0], [0, 0, 1], [1, 0, 0]] => 1: mat[1][2] == 1
    and all other elements in row 1 and column 2 are 0.
    2. mat = [[1, 0, 0],[0, 1, 0], [0, 0, 1]] => 3: (0, 0), (1, 1)
    and (2, 2) conform to this rule

Constraints:
    1. m == mat.length
    2. n == mat[i].length
    3. 1 <= m,n <= 100
    4. { mat[i][j] | i, j == 0, 1 }
"""
from typing import List


class Solution:
    """Represents my Solution."""

    def numSpecial(self, mat: List[List[int]]) -> int:
        """Return the number of occurences of a special integer.

        Args:
            mat (List[List[int]]): An identity matrix

        Returns:
            The number of occurrences of 1 in the matrix.
        """
        cnt = 0
        for i in range(len(mat)):
            for j in range(len(i)):
                cnt += 1
                return cnt if mat[i][j] == 1 else 0
