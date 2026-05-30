"""
Problem: 36. Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/

Author: Mrunal Nirajkumar Shah
Date: 23 May, 2026

Time Complexity: O(n^2 + O(m) + O(o) + O(p))
Space Complexity: O(m + o + p)
where n^2 is 9x9 sudoku matrix, m is length of ROWS,
o is length of COLS, and p is length of BOXES 
"""

from typing import List

class Solution:
    """
    Input will be 9x9 sudoku board
    Output will be True or False if either sudoku rules are followed, or not.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Initialize ROWS, COLS, and BOXES for validation. use nested loop to store each element in
        all of the three: ROWS, COLS and BOXES based on index as we have to check if rows are okay,
        cols are okay and boxes 3x3 is also okay (no number repetation). Later use set to check if
        all this arrays have duplicates, if not than return True else False.
        """
        ROWS = [[] for _ in range(9)]
        COLS = [[] for _ in range(9)]
        BOXES = [[] for _ in range(9)]

        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == ".":
                    continue

                ROWS[i].append(col)
                COLS[j].append(col)

                box_index = (i // 3) * 3 + (j // 3)
                BOXES[box_index].append(col)

        # VALIDATE ROWS
        for row in ROWS:
            val_set = set()

            for num in row:
                if num in val_set:
                    return False
                val_set.add(num)
        
        # VALIDATE COLS
        for col in COLS:
            val_set = set()

            for num in col:
                if num in val_set:
                    return False
                val_set.add(num)
        
        # VALIDATE BOXES
        for box in BOXES:
            val_set = set()

            for num in box:
                if num in val_set:
                    return False
                val_set.add(num)
        
        return True



def main():
    list_boards = [
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]],

        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]],
    ]

    list_outputs = [
        True,
        False
    ]

    solve = Solution()

    results = []
    for board in list_boards:
        results.append(solve.isValidSudoku(board))

    # TEST
    for result, output in zip(results, list_outputs):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()