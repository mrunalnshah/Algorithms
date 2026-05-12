"""
Problem: 14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Author: Mrunal Nirajkumar Shah
Date: 12 May, 2026

Time Complexity: O(n + m) where n is number of strings and m is length of shortest string
Space Complexity: O(m) where m is length of shortest string ~ O(1) because constant

NEETCODE SOLUTION
"""

from typing import List

class Solution:
    """
    input = ["flower", "flow", "flight"]
    output = "fl"
    because fl is common in all the string's prefix.
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        iterate through each char in first string of the strs, with nested loop iterating for each string in strs and checking if the char
        at ith index matches with char at ith index for first string. if yes, than concatinate the char to res else return res. At the end
        return res when loops end.
        """
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if len(s) == i or s[i] != strs[0][i]:
                    return res

            res += strs[0][i]

        return res 

def main():
    list_strs = [
        ["flower","flow","flight"],
        ["dog","racecar","car"],
        ["mrunal", "mrinal", "munal"],
        ["mrunal", "mrunal", "mrunal"],
        ["", "", ""],
        ["shah", "shahiwala", "shahji"]
    ]

    list_output = [
        "fl",
        "",
        "m",
        "mrunal",
        "",
        "shah"
    ]

    solve = Solution()

    results = []
    for strs in list_strs:
        results.append(solve.longestCommonPrefix(strs))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()