"""
Author: Mrunal Nirajkumar Shah
Date  : 21st February, 2026

LeetCode: 84. Largest Rectangle in Histogram

Time Limit Exceeded
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        total_bar = len(heights)
        unique_values = set(heights)

        if len(unique_values) == 1:
            return total_bar * unique_values.pop()
    
        for i, num in enumerate(heights):
            count = 1

            j = i - 1
            while j >= 0 and heights[j] >= num:
                count += 1
                j -= 1
            
            j = i + 1
            while j < total_bar and heights[j] >= num:
                count += 1
                j += 1

            area = max(area, (count * num))        

        return area

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