"""
Problem: 14. Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Author: Mrunal Nirajkumar Shah
Date: 12 May, 2026

Time Complexity: O(n + m) where n is number of strings and m is length of shortest string
Space Complexity: O(m) where m is length of shortest string ~ O(1) because constant
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
        initialize char_iter to 0 and check each character in each string with the char at the char_iter index, if cur_char not matches
        with any of the char in each string than return prefix_str else add the cur_char to prefix_str and continue. 
        """
        prefix_str = ""

        char_iter = 0
        while True:
            cur_char = ""
            for word in strs:
                if char_iter >= len(word):
                    return prefix_str
            
                if cur_char == "":
                    cur_char = word[char_iter]
                    continue

                if word[char_iter] == cur_char:
                    continue
                else:
                    return prefix_str
            prefix_str += cur_char
            char_iter += 1

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