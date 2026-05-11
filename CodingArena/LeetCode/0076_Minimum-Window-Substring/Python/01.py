"""
Author: Mrunal Nirajkumar Shah
Date  : 23th March, 2026

LeetCode: 76. Minimum Window Substring

Time Limit Exceeded
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(m) m is len(t)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        substring = ""
        for i, char in enumerate(s):
            checker = list(t)

            if char not in checker:
                continue

            j = i
            k = len(s)

            while j < k:
                if s[j] in checker:
                    checker.remove(s[j])

                if len(checker) == 0:
                    string = s[i:j+1] # start is inclusive, stop is exclusive
                    
                    if len(substring) == 0:
                        substring = string
                    elif len(string) < len(substring):
                        substring = string
                                        
                    break

                j += 1


        return substring


def main():
    list_input = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("MRUNALNSHAH", "ANS"),
        ("cabwefgewcwaefgcf", "cwae")
    ]

    solve = Solution()

    result = []
    for input in list_input:
        result.append(solve.minWindow(s=input[0], t=input[1]))

    print(result)

if __name__ == "__main__":
    main()