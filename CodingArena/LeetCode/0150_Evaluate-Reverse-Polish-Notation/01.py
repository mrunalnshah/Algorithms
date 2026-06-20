"""
Problem: 150. Evaluate Reverse Polish Notation
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Author: Mrunal Nirajkumar Shah
Date: 2 June, 2026

Time Complexity: O(n)
Space Complexity: O(n)

where n is the size of tokens
"""

from typing import List

class Solution:
    """
    Input = ["2","1","+","3","*"]
    Output = 9
    
    (2 + 1) * 3 = 9
    """
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Store nums in stack, and for +, -, *, / pop last two elements and append the
        result to stack.
        """
        t_stack = []

        for token in tokens:
            match token:
                case '+' | '-' | '*' | '/':
                    num2 = t_stack.pop()
                    num1 = t_stack.pop()

                    if token == '+':
                        t_stack.append(num1 + num2)
                    elif token == '-':
                        t_stack.append(num1 - num2)
                    elif token == '*':
                        t_stack.append(num1 * num2)
                    else:
                        t_stack.append(int(num1 / num2)) # Truncate - Use int() or math.trunc()
                case _:
                    t_stack.append(int(token))

        return t_stack[-1]

def main():
    list_tokens = [
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
        ["5"],
        ["100", "50", "-", "60", "/"]
    ]

    list_output = [
        9,
        6,
        22,
        5,
        0
    ]

    solve = Solution()

    results = []
    
    for tokens in list_tokens:
        results.append(solve.evalRPN(tokens))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()