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
        unique_values = set(heights)
        area = 0

        for value in unique_values:
            count = 0
            num_found = False
            
            for num in heights:
                if num > value:
                    count += 1
                elif num == value:
                    count += 1
                    num_found = True
                else:
                    if num_found:
                        area = max(area, (value * count))
                        count = 0
                    else:
                        count = 0

            area = max(area, (value * count))

        return area

def main():
    list_heights = [[2,1,5,6,2,3],
                    [2,4],
                    [1,1,1,1,1,1,1,1,1,1,9]]
    
    solve = Solution()

    result = []
    for heights in list_heights:
        result.append(solve.largestRectangleArea(heights))

    print(result)

if __name__ == "__main__":
    main()