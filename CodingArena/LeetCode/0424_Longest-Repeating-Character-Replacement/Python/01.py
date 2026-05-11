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
        max_replacement = 0
      
        for char in set(s):
            i = 0
            stack = []
            replacement_count = k
            
            while i < len(s):
                if s[i] == char:
                    stack.append(s[i])
                else:
                    if replacement_count > 0:
                        stack.append(s[i])
                        replacement_count -= 1
                    else:
                        max_replacement = max(max_replacement, len(stack))
                        
                        if k == 0:
                            stack.clear()

                        while stack and replacement_count == 0:
                            left_char = stack.pop(0)
                            if left_char != char:
                                stack.append(s[i])
                                break                                    

                i += 1
            
            max_replacement = max(max_replacement, len(stack))

        return max_replacement



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