"""
Author: Mrunal Nirajkumar Shah
Date  : 25th February, 2026

LeetCode: 11. Container With Most Water

Time Limit Exceeded
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container = 0

        for i in range(0, len(height) - 1):
            for j in range(i + 1, len(height)):
                area = (j - i) * (min(height[i], height[j]))

                max_container = max(max_container, area)

        return max_container


def main():
    list_heights = [[1,8,6,2,5,4,8,3,7],
                    [1,1]]
    
    solve = Solution()

    result = []
    for heights in list_heights:
        result.append(solve.maxArea(heights))
    
    print(result)


if __name__ == "__main__":
    main()