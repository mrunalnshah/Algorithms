"""
Problem: 41. First Missing Positive
Link: https://leetcode.com/problems/first-missing-positive/

Author: Mrunal Nirajkumar Shah
Date: 30 May, 2026

Time Complexity: O(3 . n)
Space Complexity: O(1)
where n is the size of nums, we used nums array as our memory so O(1)
"""

from typing import List

class Solution:
    """
    Input = [1, 2, 0]
    Output = 3
    Smallest Poitive integer missing is 3
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Use nums array as memory. First convert all negatives to 0, then
        if each num is between 1 and len(nums) than make it negative of itself, and if its 0
        than make it -1 * (len(nums) + 1). later loop and check if nums is >= 0 than return ith else
        return len(nums) + 1.
        """
        # Mark negatives as 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0


        for i in range(len(nums)):
            val = abs(nums[i])
            
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        
        return len(nums) + 1
    
def main():
    list_nums = [
        [1,2,0],
        [3,4,-1,1],
        [7,8,9,11,12],
        [-1, 1, 2, 3, 4, 5],
        [1],
        [-999, -998, -997, 1000, 10001],
        [100000, 3, 4000, 2, 15, 1, 99999],
        [2, 1]
    ]

    list_output = [
        3,
        2,
        1,
        6,
        2,
        1,
        4,
        3
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.firstMissingPositive(nums))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()