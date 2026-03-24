"""
Author: Mrunal Nirajkumar Shah
Date  : 24th March, 2026

LeetCode: 239. Sliding Window Maximum

Sliding + Monotonic Stack
Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 and k == 1:
            return nums
        
        result = []
        stack = []
        max_value = None

        i = 0
        j = 0
        while j < k:
            stack.append(nums[j])   
            j += 1

        max_value = max(stack)
        result.append(max_value)

        j -= 1
        while i < len(nums) - k:
            i += 1
            j += 1

            stack.pop(0)
            stack.append(nums[j])
            
            max_value = max(stack)

            result.append(max_value)
        
        return result
        
def main():
    list_input = [
        ([1,3,-1,-3,5,3,6,7], 3),
        ([1], 1),
        ([1, -1], 1)
    ]

    solve = Solution()

    result = []
    for input in list_input:
        result.append(solve.maxSlidingWindow(nums=input[0], k=input[1]))

    print(result)


if __name__ == "__main__":
    main()