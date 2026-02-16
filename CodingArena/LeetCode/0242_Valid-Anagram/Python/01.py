"""
Author: Mrunal Nirajkumar Shah
Date  : 4th February, 2026

LeetCode: 242. Valid Anagram

try/except and dict comparison are optimized by CPython
Solution Description: Time Limit Exceeds
- Time Complexity: O(n) 
- Space Complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}

        for i in range(len(s)):
            try:
                dict_s[s[i]] += 1
            except KeyError:
                dict_s[s[i]] = 1

            try:
                dict_t[t[i]] += 1
            except KeyError:
                dict_t[t[i]] = 1

        if dict_s != dict_t:
            return False
            
        return True

def main():
    solve = Solution()

    test_case = [("anagram", "nagaram"), ("rat", "car"), ("HATED", "DEATH")]

    result = []
    for case in test_case:
        result.append(solve.isAnagram(case[0], case[1]))

    print(result)

if __name__ == "__main__":
    main()