"""
Author: Mrunal Nirajkumar Shah
Date  : 19th March, 2026

LeetCode: 567. Permutation in String

Time Limit Exceeded
Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        starting_index = 0        
        checker = list(s1)
        stack = []

        for i, char in enumerate(s2):
            if char in checker:
                checker.remove(char)
                stack.append(char)

                if len(checker) == 0:
                    return True
                
            else:
                if char in s1:
                    while starting_index < i:
                        if stack:
                            element = stack.pop(0)
                            checker.append(element)
                        
                        if s2[starting_index] == char:
                            starting_index += 1
                            break
                        else:
                            starting_index += 1
                        
                    stack.append(char)
                    checker.remove(char)

                else:
                    stack.clear()
                    checker = list(s1)
                    starting_index = i + 1 
        
        return False
            

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