"""
Author: Mrunal Nirajkumar Shah
Date  : 4th February, 2026

LeetCode: 242. Valid Anagram

[BEST SOLUTION]
Solution Description: Time Limit Exceeds
- Time Complexity:  O(n)
- Space Complexity: O(n)
"""

class Solution:          
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

        for val in count.values():
            if val != 0:
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