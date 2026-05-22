"""
Problem: 304. Range Sum Query 2D - Immutable
Link: https://leetcode.com/problems/range-sum-query-2d-immutable/

Author: Mrunal Nirajkumar Shah
Date: 22 May, 2026

Time Complexity: O(n^2)
Space Complexity: O(1) like only we define sum, matrix is input.
"""

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        storing matrix in NumMatrix class
        """
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        using nested for loop to calculate each value of the matrix.
        """
        
        sum = 0

        for i in range(row1, row2 + 1, 1):
            for j in range(col1, col2 + 1, 1):
                sum += self.matrix[i][j]

        return sum


def main():
    numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(numMatrix.sumRegion(2, 1, 4, 3))
    print(numMatrix.sumRegion(1, 1, 2, 2))
    print(numMatrix.sumRegion(1, 2, 2, 4))

if __name__ == "__main__":
    main()
