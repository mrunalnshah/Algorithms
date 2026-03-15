"""
Author: Mrunal Nirajkumar Shah
Date  : 25th February, 2026

LeetCode: 11. Container With Most Water

Solution Description:
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_container = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_container = max(area, max_container)

            if height[left] < height[right]:
                current_height = height[left]

                left += 1

                while left < right and height[left] < current_height:
                    left += 1

            else:
                current_height = height[right]

                right -= 1

                while left < right and height[right] < current_height:
                    right -= 1

        return max_container

def main():
    list_heights = [[1,8,6,2,5,4,8,3,7],
                    [1,1],
                    [8,7,2,1]
                    ]
    
    solve = Solution()

    result = []
    for heights in list_heights:
        result.append(solve.maxArea(heights))
    
    print(result)


if __name__ == "__main__":
    main()