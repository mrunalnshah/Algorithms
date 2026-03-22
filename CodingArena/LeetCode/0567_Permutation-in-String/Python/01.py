"""
Author: Mrunal Nirajkumar Shah
Date  : 19th March, 2026

LeetCode: 567. Permutation in String

Time Limit Exceeded
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        i = 0
        while i < len(s2):
            j = i 
            if s2[j] in s1:
                temp_checker = list(s1)
                while j < i + len(s1) and i + len(s1) <= len(s2):
                    if s2[j] in temp_checker:
                        temp_checker.remove(s2[j])
                    else:
                        break

                    j += 1
                
                if len(temp_checker) == 0:
                    return True
            
            i += 1
        
        return False

def main():
    list_s = [
        ("ab", "eidbaooo"),
        ("ab", "eidboaoo"),
        ("abc", "cba"),
        ("omg", "ilovegodmog"),
        ("adc", "dcda"),
        ("a", "a"),
        ("ab", "a")
    ]

    solve = Solution()
    
    result = []
    for s in list_s:
        result.append(solve.checkInclusion(s1=s[0], s2=s[1]))

    print(result)

if __name__ == "__main__":
    main()