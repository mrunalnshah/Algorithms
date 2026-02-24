"""
Author: Mrunal Nirajkumar Shah
Date  : 24th February, 2026

LeetCode: 15. 3Sum

Time Limit Exceed
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        
        triplets = []

        for i, num in enumerate(sorted_nums):
            if num > 0:
                break

            if i > 0 and num == sorted_nums[i - 1]:
                continue

            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                threesum = num + sorted_nums[l] + sorted_nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    triplets.append([num, sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1

                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
            
        return triplets
            

def main():
    list_nums = [
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
        [0,0,0,0],
        [-1,0,1,2,-1,-4]
    ]
    
    solve = Solution()

    result = []
    for nums in list_nums:
        result.append(solve.threeSum(nums))

    print(result)

if __name__ == "__main__":
    main()