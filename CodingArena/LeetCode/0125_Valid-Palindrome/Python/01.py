"""
Author: Mrunal Nirajkumar Shah
Date  : 22nd February, 2026

LeetCode: 125. Valid Palindrome

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = []
        for char in s:
            if char.isalnum():
                char_list.append(char.lower())
             
        i = 0
        j = len(char_list) - 1

        while i <= j:
            if char_list[i] == char_list[j]:
                i += 1
                j -= 1
                continue
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