"""
Author: Mrunal Nirajkumar Shah
Date  : 18th March, 2026

LeetCode: 424. Longest Repeating Character Replacement

[Sliding Method]
Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = {}

        left = 0
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            windowLen = right - left + 1
            if windowLen - max(count.values()) <= k:
                result = max(result, windowLen)
            else:
                while windowLen - max(count.values()) > k:
                    count[s[left]] -= 1
                    left += 1
                    windowLen = right - left + 1

                result = max(result, windowLen - max(count.values()))
            
        return result

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