"""
Problem: 1929. Concatenation of Array
Link: https://leetcode.com/problems/concatenation-of-array/

Author: Mrunal Nirajkumar Shah
Date: 11 May, 2026

Time Complexity: O(m) where m is size of nums.
Space Complexity: O(2 * n) ~ O(n)

PYTHONIC WAY
"""
from typing import List


class Solution:
    """
    nums = 1, 2, 1
    output = 1, 2, 1, 1, 2, 1 
    
    which is nums concatinated with nums
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        create an 'ans' array with 2 * sizeof(nums) and save each element of nums to both
        ans[i] and ans[i + len(nums)] where i is index of the element in nums.
        """
        # nums.extend(nums)
        nums = nums + nums
        
        return nums

def main():
    list_nums = [
        [1,2,1],
        [1,3,2,1],
        [9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        []
    ]

    list_output = [
        [1,2,1,1,2,1],
        [1,3,2,1,1,3,2,1],
        [9, 9],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        []
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.getConcatenation(nums))


    # Test
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print("FAIL")

if __name__ == "__main__":
    main()