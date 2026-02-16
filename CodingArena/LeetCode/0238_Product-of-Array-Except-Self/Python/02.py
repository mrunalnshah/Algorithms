"""
Author: Mrunal Nirajkumar Shah
Date  : 10th February, 2026

LeetCode: 238. Product of Array Except Self

[SOLUTION]
a b c d
lr: 1 | a | a.b | a.b.c
rr: d.c.b | d.c | d | 1

lr x rr = SOLUTION

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n) // can be optimized to O(1)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = []
        right_array = []

        for i in range(len(nums)):
            if i == 0:
                left_array.append(1)
                right_array.append(1)
            else:
                left_array.append(left_array[i - 1] * nums[i - 1])
                right_array.append(right_array[i - 1] * nums[len(nums) - i])

        result_array = []
        for i in range(len(right_array)):
            result_array.append(left_array[i] * right_array[len(right_array) - i - 1])

        return result_array

def main():
    list_nums = [
        [1, 2, 3, 4], 
        [-1, 1, 0, -3, 3],
        [0, 0],
        [0, 4, 0]]

    solve = Solution()
    result = []

    for nums in list_nums:
        result.append(solve.productExceptSelf(nums))

    print(result)

if __name__ == "__main__":
    main()