"""
Author: Mrunal Nirajkumar Shah
Date  : 1st March, 2026

LeetCode: 42. Trapping Rain Water

Solution Description:
Time Complexity: O(n)
Space Complexity: O(1)

Approach:
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ...

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