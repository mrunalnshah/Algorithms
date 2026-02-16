"""
Author: Mrunal Nirajkumar Shah
Date  : 5th February, 2026

LeetCode: 1. Two Sum

Solution Description (Brute-Force):
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums), 1):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        
        return [-1, -1]


def main():
    list_nums = [([2, 7,  11, 15, 9], 9),
                 ([3, 2, 4], 6),
                 ([3, 3], 6)]

    solve = Solution()

    result = []
    for nums, target in list_nums:
        result.append(solve.twoSum(nums=nums, target=target))

    print(result)

if __name__ == "__main__":
    main()