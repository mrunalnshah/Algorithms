"""
Problem: 217. Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/

Author: Mrunal Nirajkumar Shah
Date: 11 May, 2026

Time Complexity: O(n) 
Space Complexity: O(n)
where n is size of nums.

PYTHONIC WAY
"""

from typing import List

class Solution:
    """
    nums = 1, 2, 3, 1
    output = True
    because 1 is more than 1 time in the nums. (no repeatations)
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Create a hash-map and check if the number is already in hash-map, if not than store the number in hash-map
        and repeat until last element. If number found in hash-map than return True, else return False.
        """
        
        set_nums = set(nums)

        if len(nums) != len(set_nums):
            return True
        else:
            return False


def main():
    list_nums = [
        [1,2,3,1],
        [1,2,3,4],
        [1,1,1,3,3,4,3,2,4,2]
    ]

    list_output = [
        True,
        False,
        True
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.containsDuplicate(nums))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print("FAIL")           

if __name__ == "__main__":
    main()