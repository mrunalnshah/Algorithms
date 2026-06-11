"""
Problem: 394. Decode String
Link: https://leetcode.com/problems/decode-string/

Author: Mrunal Nirajkumar Shah
Date: X June, 2026

Time Complexity: 
Space Complexity:
"""

class Solution:
    def decodeString(self, s: str) -> str:
        ...

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