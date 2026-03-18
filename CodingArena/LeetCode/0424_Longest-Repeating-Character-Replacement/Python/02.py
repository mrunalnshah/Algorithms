"""
Author: Mrunal Nirajkumar Shah
Date  : 18th March, 2026

LeetCode: 424. Longest Repeating Character Replacement

[Stack Method]
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ...



def main():
    list_s = [
        ("ABAB", 2),
        ("AABABBA", 1),
        ("ABCACCBB", 2),
        ("AAAB", 0),
        ("BAAA", 0),
        ("EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH", 7),
        ("AABA", 0)
    ]

    solve = Solution()

    result = []
    for s in list_s:
        result.append(solve.characterReplacement(s=s[0], k=s[1]))

    print(result)


if __name__ == "__main__":
    main()