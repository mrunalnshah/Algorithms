"""
Author: Mrunal Nirajkumar Shah
Date  : 4th February, 2026

LeetCode: 217. Contains Duplicate

Solution Description: Time Limit Exceeds
- Time Complexity: O(n log n) 
- Space Complexity: O(1)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0, len(nums) - 1, 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] == nums[j]:
                    return True
                
        return False


def main():
    solve = Solution()

    list_nums = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

    result = []

    for nums in list_nums:
        result.append(solve.containsDuplicate(nums))

    print(result)

if __name__ == "__main__":
    main()

