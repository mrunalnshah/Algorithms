"""
Author: Mrunal Nirajkumar Shah
Date  : 13th February, 2026

LeetCode: 20. Valid Parentheses

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for char in s:
            if char not in ["(", "{", "[", ")", "}", "]"]:
                continue
            else:
                if char in ["(", "{", "["]:
                    stack.append(char)
                else:
                    if len(stack) == 0:
                        return False
                    
                    closing_paren = stack.pop()
                    if (char == ")" and closing_paren == "(") or (char == "}" and closing_paren == "{") or (char == "]" and closing_paren == "["):
                        continue
                    else:
                        return False

        if len(stack) != 0:
            return False
        
        return True

def main():
    list_s = ["()",
              "()[]{}",
              "(]",
              "([])",
              "([)]",
              "["
              ]
    
    solve = Solution()

    result = []
    for s in list_s:
        result.append(solve.isValid(s))

    print(result)

if __name__ == "__main__":
    main()
