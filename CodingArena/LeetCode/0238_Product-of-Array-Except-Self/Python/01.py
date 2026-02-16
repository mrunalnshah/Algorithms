"""
Author: Mrunal Nirajkumar Shah
Date  : 10th February, 2026

LeetCode: 238. Product of Array Except Self

[With division operation] -> Not Acceptable
Solution Description:
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zeros = 0

        for num in nums:
            if num == 0:
                count_zeros += 1
                continue
            
            product *= num

        
        result = []
        for num in nums:
            if count_zeros >= 2:
                result.append(0)
            elif count_zeros == 1:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            else:
                result.append(int(product / num))

        
        return result



def main():
    list_nums = [
        [1, 2, 3, 4], 
        [-1, 1, 0, -3, 3],
        [0, 0],
        [0, 4, 0]]

    solve = Solution()
    result = []

    for nums in list_nums:
        result.append(solve.productExceptSelf(nums))

    print(result)

if __name__ == "__main__":
    main()