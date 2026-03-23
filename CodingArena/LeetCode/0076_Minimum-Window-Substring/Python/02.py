"""
Author: Mrunal Nirajkumar Shah
Date  : 23th March, 2026

LeetCode: 76. Minimum Window Substring

Solution Description:
Time Complexity: O(n)
Space Complexity: O(k)
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        check_hash = {}
        have_hash = {}

        for char in t:
            if char in check_hash:
                check_hash[char] += 1
            else:
                check_hash[char] = 1
                have_hash[char] = 0

        substring = ""
        matches = 0

        i = 0
        j = 0

        while j < len(s):
            # expand window
            while matches != len(check_hash) and j < len(s):
                if s[j] in check_hash:
                    have_hash[s[j]] += 1

                    if have_hash[s[j]] == check_hash[s[j]]:
                        matches += 1

                j += 1

            # shrink window
            while matches == len(check_hash) and i < j:
                string = s[i:j]

                if len(substring) == 0 or len(string) < len(substring):
                    substring = string

                if s[i] in check_hash:
                    have_hash[s[i]] -= 1

                    if have_hash[s[i]] < check_hash[s[i]]:
                        matches -= 1

                i += 1

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