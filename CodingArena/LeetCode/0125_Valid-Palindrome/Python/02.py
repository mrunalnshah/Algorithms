"""
Author: Mrunal Nirajkumar Shah
Date  : 22nd February, 2026

LeetCode: 125. Valid Palindrome

Solution Description:
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:            
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                return False
            
        return True

def main():
    list_s = ["A man, a plan, a canal: Panama", 
              "race a car",
              " ",
              "A : B C D C B A"
              ]
    
    solve = Solution()

    result = []
    for s in list_s:
        result.append(solve.isPalindrome(s))

    print(result)

if __name__ == "__main__":
    main()