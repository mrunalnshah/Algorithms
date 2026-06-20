"""
Problem: 394. Decode String
Link: https://leetcode.com/problems/decode-string/

Author: Mrunal Nirajkumar Shah
Date: 20 June, 2026

Time Complexity: Depends on Input
Space Complexity: O(n)

where n is the size of string input.
"""

class Solution:
    """
    Input: "3[a]2[bc]"
    Output: aaabcbc
    """
    def decodeString(self, s: str) -> str:
        """
        append all char to stack until "]". once end brackets are detected,
        append the substring * k to the stack.
        """
        s_stack = []

        for i in range(len(s)):
            if s[i] != "]":
                s_stack.append(s[i])
            else:
                substring = ""

                while s_stack[-1] != "[":
                    substring = s_stack.pop() + substring
                
                s_stack.pop()

                k = ""
                while s_stack and s_stack[-1].isdigit():
                    k = s_stack.pop() + k

                k = int(k)

                s_stack.append(k * substring)
        
        return "".join(s_stack)


def main():
    list_s = [
        "3[a]2[bc]",
        "3[a2[c]]",
        "2[abc]3[cd]ef"
    ]

    list_output = [
        "aaabcbc",
        "accaccacc",
        "abcabccdcdcdef"
    ]

    solve = Solution()

    results = []
    for s in list_s:
        results.append(solve.decodeString(s))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()