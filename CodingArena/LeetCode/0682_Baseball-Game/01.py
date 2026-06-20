"""
Problem: 682. Baseball Game
Link: https://leetcode.com/problems/baseball-game/

Author: Mrunal Nirajkumar Shah
Date: 31 May, 2026

Time Complexity: O(2 * n)
Space Complexity: O(n)
where n is the size of input operations
"""

from typing import List

class Solution:
    """
    Input = ["5", "2", "C", "D", "+"]
    Output = 30

    SUM of [5, 10, 15] = 30 
    """
    def calPoints(self, operations: List[str]) -> int:
        """
        Create a stack and apply all the operations, and later calculate sum of stack elements.
        """
        stack = []

        for operation in operations:
            if operation == "C":
                stack.pop()
            elif operation == "D":
                val = stack[-1]
                stack.append(val * 2)
            elif operation == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
            else:
                stack.append(int(operation))
        
        res = 0
        for val in stack:
            res += val
        
        return res

def main():
    list_ops = [
        ["5","2","C","D","+"],
        ["5","-2","4","C","D","9","+","+"],
        ["1","C"]
    ]

    list_output = [
        30,
        27,
        0
    ]

    solve = Solution()

    results = []
    for ops in list_ops:
        results.append(solve.calPoints(ops))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()