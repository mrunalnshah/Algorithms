"""
Author: Mrunal Nirajkumar Shah
Date  : 22th March, 2026

LeetCode: 567. Permutation in String

Time Limit Exceeded
Solution Description:
Time Complexity: O(26 . n)
Space Complexity: O(26 * 2)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count = [0] * 26
        s2Count = [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1           

            l += 1
        
        return matches == 26

def main():
    list_s = [
        ("ab", "eidbaooo"),
        ("ab", "eidboaoo"),
        ("abc", "cba"),
        ("omg", "ilovegodmog"),
        ("adc", "dcda"),
        ("a", "a"),
        ("ab", "a"),
        ("hello", "ooolleoooleh")
    ]

    solve = Solution()
    
    result = []
    for s in list_s:
        result.append(solve.checkInclusion(s1=s[0], s2=s[1]))

    print(result)

if __name__ == "__main__":
    main()