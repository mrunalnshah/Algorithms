"""
Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Author: Mrunal Nirajkumar Shah
Date: 31 May, 2026

Time Complexity: O(n) 
Space Complexity: O(n)
where n is the size of input
"""

class Solution:
    """
    Input = "()"
    Output = True
    ( -> starts and ) -> closes.
    """
    def isValid(self, s: str) -> bool:
        """
        Use a stack to keep track of opening paranethesis and pop as the closing
        paranthesis are spotted.
        """
        stack = []

        for paranthesis in s:
            if paranthesis in ("(", "[", "{"):
                stack.append(paranthesis)
            else:
                if len(stack) == 0:
                    return False
                
                if (paranthesis == ")" and stack[-1] == "(") \
                        or (paranthesis == "]" and stack[-1] == "[") \
                        or (paranthesis == "}" and stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
    
        return True

def main():
    list_s = [
        "()",
        "()[]{}",
        "(]",
        "([])",
        "([)]"
    ]

    list_output = [
        True,
        True,
        False,
        True,
        False
    ]

    solve = Solution()

    results = []
    for s in list_s:
        results.append(solve.isValid(s))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()