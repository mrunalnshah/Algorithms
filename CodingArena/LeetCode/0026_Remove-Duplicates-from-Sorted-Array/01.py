"""
Problem: 26. Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Author: Mrunal Nirajkumar Shah
Date: 11 June, 2026

Time Complexity: O(n)
Space Complexity: O(1)

where n is the size of nums
"""

from typing import List

class Solution:
    """
    Input = [1, 1, 2]
    Output = 2

    unique elements are [1, 2] therefore 2.
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Check current and next element, if they are same than pop it.
        """
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                nums.pop(j)
                
            i = j

        return len(nums)


def main():
    list_nums = [
        [1,1,2],
        [0,0,1,1,1,2,2,3,3,4],
        [0],
        [0,0,0,0,0,0,0,0,0],
        [1,2,3,4,5,6,7,8,9,0],
        [-100, -99, -99, 98, 99]
    ]

    list_output = [
        2,
        5,
        1,
        1,
        10,
        4
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.removeDuplicates(nums))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()

