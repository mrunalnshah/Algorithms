"""
Author: Mrunal Nirajkumar Shah
Date  : 17th February, 2026

LeetCode: 150. Evaluate Reverse Polish Notation

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)

Remember:
3 4 - ===> 3 - 4
3 4 / ===> 3 / 4

TL;DR
num2 num1 X ===> num2 X num1 [X can be + - * /]
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        array = []

        for token in tokens:
            if token == '+':
                num1 = array.pop()
                num2 = array.pop()

                result = num2 + num1

                array.append(result)
            elif token == '-':
                num1 = array.pop()
                num2 = array.pop()

                result = num2 - num1

                array.append(result)
            elif token == '*':
                num1 = array.pop()
                num2 = array.pop()

                result = num2 * num1

                array.append(result)
            elif token == '/':
                num1 = array.pop()
                num2 = array.pop()

                result = int(num2 / num1)
                
                array.append(result)
            else:
                array.append(int(token))
        
        return array.pop()

def main():
    list_tokens = [["2","1","+","3","*"],
                   ["4","13","5","/","+"],
                   ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]
    
    solve = Solution()

    result = []
    for tokens in list_tokens:
        result.append(solve.evalRPN(tokens))

    print(result)

if __name__ == "__main__":
    main()