"""
Author: Mrunal Nirajkumar Shah
Date  : 5th February, 2026

LeetCode: 1. Two Sum

[Best Solution- Hash Map]
Solution Description:
Time Complexity: O(n) (dictionary lookups are O(1))
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for i in range(len(nums)):         
            compliment = target - nums[i]
            
            if compliment in memory:
                return [memory[compliment], i]
            
            memory[nums[i]] = i
                
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