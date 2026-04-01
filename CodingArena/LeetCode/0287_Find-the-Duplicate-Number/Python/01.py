"""
Author: Mrunal Nirajkumar Shah
Date  : 1st April, 2026

LeetCode: 287. Find the Duplicate Number

[Time Limit Exceeded]
Solution Description:
Time Complexity: O(n^2)  
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] == nums[j] and i != j:
                    return nums[i]
            
def main():
    list_nums = [
        [1,3,4,2,2],
        [3,1,3,4,2],
        [3,3,3,3,3],
        [4,3,1,4,2]
    ]

    solve = Solution()

    result = []
    for nums in list_nums:
        result.append(solve.findDuplicate(nums))
    
    print(result)

if __name__ == "__main__":
    main()

