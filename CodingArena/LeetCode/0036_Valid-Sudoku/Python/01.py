"""
Author: Mrunal Nirajkumar Shah
Date  : 11th February, 2026

LeetCode: 36. Valid Sudoku

Solution Description:
O(1) because Sudoku is fixed size 9x9 = 81
Time Complexity: O(1) - GENERALIZED: O(N^2)
Space Complexity: O(1) - GENERALIZED: O(N) ~ O(N^2)
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_matrix = [[] for _ in range(9)]
        for i in range(9):
            rule_col_num = []
            rule_row_num = []
            for j in range(9):
                if board[i][j] in rule_col_num and board[i][j] != '.':
                    return False
                else:
                    if board[i][j] != '.':
                        rule_col_num.append(board[i][j])

                if board[j][i] in rule_row_num and board[j][i] != '.':
                    return False
                else:
                    if board[j][i] != '.':
                        rule_row_num.append(board[j][i])


                if board[i][j] != '.':
                    box_index = (i // 3) * 3 + (j // 3)
                    sub_matrix[box_index].append(board[i][j])

        for numbers in sub_matrix:
            memory = {}
            for number in numbers:
                if number in memory:
                    return False
                else:
                    memory[number] = 1
            
        return True       



def main():
    solve = Solution()

    list_board = [
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

        [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

    ]

    result = []
    for board in list_board:
        result.append(solve.isValidSudoku(board=board))


    print(result)


if __name__ == "__main__":
    main()