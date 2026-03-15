"""
Author: Mrunal Nirajkumar Shah
Date  : 5th March, 2026

LeetCode: 3. Longest Substring Without Repeating Characters

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start_pointer = 0
        
        seen = set()

        for i, char in enumerate(s):
            if char in seen:
                max_length = max(max_length, len(seen))
                
                if s[i] == s[i - 1]:
                    seen.clear()
                    seen.add(char)
                    start_pointer = i
                    continue
                
                while start_pointer < i:
                    seen.remove(s[start_pointer])
                    start_pointer += 1

                    if s[start_pointer - 1] == char:
                        break

                seen.add(char)
            else:
                seen.add(char)

        max_length = max(max_length, len(seen))

        return max_length

def main():
    s_list = [
        "abcabcbb", 
        "bbbbb",
        "pwwkew",
        "acabcbabdadakmno",
        " ",
        "dvdf",
        "bpfbhmipx"
        ]
    
    solve = Solution()

    result = []
    for s in s_list:
        result.append(solve.lengthOfLongestSubstring(s))

    print(result)

if __name__ == "__main__":
    main()