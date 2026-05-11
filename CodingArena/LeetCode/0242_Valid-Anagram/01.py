"""
Problem: 242. Valid Anagram
Link: https://leetcode.com/problems/valid-anagram/

Author: Mrunal Nirajkumar Shah
Date: 11 May, 2026

Time Complexity: O(n + m + o) 
Space Complexity: O(n)
where 
n is size of s,
m is size of t,
o is size of hash-map.
"""

class Solution:
    """
    s = mrunal
    t = mrrnal
    output: False
    because not anagram.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Continue is len(s) and len(t) are same else return False. hash-map is used to store each element from s with its count. 
        Uses this hash-map to decrease the count based on elements from t while checking if char is not in hash-map or if count is less than 0. 
        in any-case return False, else return True. 
        """
        if len(s) != len(t):
            return False

        freq = {} # hash-map

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        for char in t:
            if char not in freq:
                return False
            
            freq[char] -= 1
            if freq[char] < 0:
                return False
                   
        return True


def main():
    list_testcase = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("mrunal", "shah"),
        ("mrunal", "namrul"),
        ("", ""),
        ("a", ""),
        ("mrrnal", "mrunal")
    ]       

    list_output = [
        True,
        False,
        False,
        True,
        True,
        False,
        False
    ]

    solve = Solution()

    # TEST
    results = []
    for testcase in list_testcase:
        results.append(solve.isAnagram(s=testcase[0], t=testcase[1]))

    
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print("FAIL")

if __name__ == "__main__":
    main()