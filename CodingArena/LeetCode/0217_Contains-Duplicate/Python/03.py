"""
Author: Mrunal Nirajkumar Shah
Date  : 4th February, 2026

LeetCode: 217. Contains Duplicate

[BEST SOLUTION]
Solution Description (Using Sets):
- Time Complexity: O(n) --> Set lookups are O(1) 
- Space Complexity: O(n)
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)    

        return False

# Compact Solution
# return len(nums) != len(set(nums))

def main():
    solve = Solution()

    list_nums = [[1, 2, 3, 1], [1, 2, 3, 4], [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]]

    result = []

    for nums in list_nums:
        result.append(solve.containsDuplicate(nums))

    print(result)

if __name__ == "__main__":
    main()

