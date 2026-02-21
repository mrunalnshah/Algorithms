"""
Author: Mrunal Nirajkumar Shah
Date  : 21st February, 2026

LeetCode: 84. Largest Rectangle in Histogram

Solution Description [MONOTONIC STACK]:
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        total_bar = len(heights)

        for i, num in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i] :
                index, height = stack.pop()

                max_area = max(max_area, height * (i - index))
                start = index 

            stack.append((start, num)) 


        for index, height in stack:
            max_area = max(max_area, height * (total_bar - index))

        return max_area

def main():
    list_heights = [[2,1,5,6,2,3],
                    [2,4],
                    [1,1,1,1,1,1,1,1,1,1,9],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    solve = Solution()

    result = []
    for heights in list_heights:
        result.append(solve.largestRectangleArea(heights))

    print(result)

if __name__ == "__main__":
    main()