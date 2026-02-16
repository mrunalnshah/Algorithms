"""
Author: Mrunal Nirajkumar Shah
Date  : 4th February, 2026

LeetCode: 217. Contains Duplicate

Solution Description (Using Dictionary):
- Time Complexity: O(n) 
- Space Complexity: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for num in nums:
            try:
                if num_dict[num]:
                    return True
            except KeyError:
                num_dict[num] = 1
            
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

