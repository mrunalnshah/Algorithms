"""
Author: Mrunal Nirajkumar Shah
Date  : 2nd March, 2026

LeetCode: 42. Trapping Rain Water

[TWO POINTER APPROACH]
Solution Description:
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
1. Keep max of both left side of height, and right side.
2. if maxLeft < maxRight than calculate next height of i, else move j closer.
    3. storage = either 0 or min(maxLeft, maxRight) - height
    4. trap_water += storage
5. return trap_water
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        trap_water = 0
        
        i = 0
        j = len(height) - 1

        maxLeft = height[i]
        maxRight = height[j]

        while i < j:
            if maxLeft < maxRight:
                i += 1

                storage = min(maxLeft, maxRight) - height[i]
                if storage < 0:
                    storage = 0
                
                trap_water += storage

                if maxLeft < height[i]:
                    maxLeft = height[i]

            else:
                j -= 1

                storage = min(maxLeft, maxRight) - height[j]
                if storage < 0:
                    storage = 0
                
                trap_water += storage

                if maxRight < height[j]:
                    maxRight = height[j]

        
        return trap_water

def main():
    list_heights = [[0,1,0,2,1,0,1,3,2,1,2,1],
                    [4,2,0,3,2,5]
                    ]
    
    solve = Solution()

    result = []
    for heights in list_heights:
        result.append(solve.trap(heights))
    
    print(result)

if __name__ == "__main__":
    main()