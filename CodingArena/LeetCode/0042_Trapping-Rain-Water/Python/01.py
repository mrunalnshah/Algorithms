"""
Author: Mrunal Nirajkumar Shah
Date  : 1st March, 2026

LeetCode: 42. Trapping Rain Water

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)

Approach:
I am calculating:
1. maxLeft, maxRight such that the maximum value exist right or left of the height[i]
2. for each i, storage = min(0, min(maxLeft, maxRight) - height[i])
    3. trap_water += storage

4. return trap_water

"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        mL = 0
        mR = 0

        for i in range(len(height)):           
            if maxLeft == [] and maxRight == []:
                maxLeft.append(0)
                maxRight.append(0)

                mL = max(height[i], 0)
                mR = max(height[len(height) - 1], 0)
                continue
            else:
                maxLeft.append(mL)
                maxRight.append(mR)

            mL = max(maxLeft[-1], height[i])
            mR = max(maxRight[-1], height[len(height) - 1 - i])

        maxRight.reverse()
        
        trap_water = 0
        for i in range(len(height)):
            storage = (min(maxLeft[i], maxRight[i]) - height[i])
            if storage < 0:
                storage = 0
            trap_water += storage

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