"""
Author: Mrunal Nirajkumar Shah
Date  : 24th March, 2026

LeetCode: 239. Sliding Window Maximum

Decreasing Monotonic Queue (dmqueue) + Sliding Window
Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        dmqueue = deque() # index
        l = r = 0

        while r < len(nums):
            # Pop smaller values from dmqueue
            while dmqueue and nums[dmqueue[-1]] < nums[r]:
                dmqueue.pop()

            dmqueue.append(r)

            # Remove left value from window
            if l > dmqueue[0]:
                dmqueue.popleft()

            if (r + 1) >= k:
                output.append(nums[dmqueue[0]])
                l += 1

            r += 1

        return output
    

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