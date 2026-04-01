"""
Author: Mrunal Nirajkumar Shah
Date  : 1st April, 2026

LeetCode: 287. Find the Duplicate Number

[Floyds Algorithm - Hard]
Solution Description:
Time Complexity: O(n)  
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find Intersection of slow and fast
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find Intersection of slow from Intersection and slow2 = 0
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        return slow # slow2 also works
           
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

