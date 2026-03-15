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
        max_i = 0

        for i in range(len(height) - 1):
            if height[i] <= max_i:
                print(height[i])
                continue
            else:
                max_i = height[i]
            
            current_max = 0
            j = len(height) - 1

            while j > i:
                if current_max < height[j]:
                    current_max = height[j]

                    area = (j - i) * (min(height[j], height[i]))
                    max_container = max(area, max_container)
                
                j -= 1
            
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