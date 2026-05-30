"""
Problem: 75. Sort Colors
Link: https://leetcode.com/problems/sort-colors/

Author: Mrunal Nirajkumar Shah
Date: 21 May, 2026

Time Complexity: O(n^2)
Space Complexity: O(1)

BUBBLE SORT
"""

from typing import List

class Solution:
    """
    Input = [2, 0, 1]
    Output = [0, 1, 2]
    JUST SORT
    
    COLOR CODE
    0 is RED
    1 is WHITE
    2 is BLUE

    Originally in LeetCode you are not suppose to return anything, I have return to test.
    """
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Using Bubble Sort which swaps each element if bigger than its ith + 1 index.
        Every iteration will have one element sorted on the right.
        """

        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    temp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp

        return nums

def main():
    list_nums = [
        [2,0,2,1,1,0],
        [2,0,1]
    ]

    list_output = [
        [0,0,1,1,2,2],
        [0,1,2]
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.sortColors(nums))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()