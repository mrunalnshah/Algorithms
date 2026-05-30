"""
Problem: 304. Range Sum Query 2D - Immutable
Link: https://leetcode.com/problems/range-sum-query-2d-immutable/

Author: Mrunal Nirajkumar Shah
Date: 22 May, 2026

Time Complexity: O(n^2) + O(5)
Space Complexity: O(n^2 + 5)
where n^2 is the matrix.
"""

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        Using Prefix Sum to calculate a new matrix sumMatrix where
        each [row][col] is total sum of its top above and top left side making 
        a rectange of sum for each element.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        # + 1 in ROWS and COLS is to create a 0 layer above and left of matrix.
        self.sumMatrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Using the sumMatrix to calculate the sum of the boundary.
        """
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.sumMatrix[row2][col2]
        above = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1 - 1]
        topLeft = self.sumMatrix[row1 - 1][col1 - 1]

        sum = bottomRight - above - left + topLeft

        return sum

def main():
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(numMatrix.sumRegion(2, 1, 4, 3))
    print(numMatrix.sumRegion(1, 1, 2, 2))
    print(numMatrix.sumRegion(1, 2, 2, 4))

if __name__ == "__main__":
    main()