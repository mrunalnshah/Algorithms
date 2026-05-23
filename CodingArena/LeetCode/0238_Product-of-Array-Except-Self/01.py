"""
Problem: 238. Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Author: Mrunal Nirajkumar Shah
Date: 23 May, 2026

Time Complexity: O(n + n)
Space Complexity: O(n + 2)
where n is size of nums and 2 is two variables: one for total_zeros and one for total_product
"""

from typing import List

class Solution:
    """
    Input = [1,2,3,4]
    Output = [24,12,8,6]
    where 
    [0] = 2 * 3 * 4
    [1] = 1 * 3 * 4
    [2] = 1 * 2 * 4
    [3] = 1 * 2 * 3
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        we keep count of number of total_zeros and product of all elements except 0.
        if zeros are more than 2, all res will be 0's, if zeros is equals to 1 then
        only the index where its zero, will have total product else everything is 0's,
        and if no zeros than ith index will total product divide by number at ith index.
        """
        total_zeros = 0
        total_product = 1

        for num in nums:
            if num == 0:
                total_zeros += 1
                continue
            total_product *= num

        res = []
        if total_zeros > 1:
            res = [0] * len(nums)
            return res

        for num in nums:
            if num == 0:
                res.append(total_product)
            elif num != 0 and total_zeros == 1:
                res.append(0)
            else:
                res.append(int(total_product / num))
        
        return res

def main():
    list_nums = [
        [1,2,3,4],
        [-1,1,0,-3,3],
        [1, 2, 3, 0, 0, 5],
        [1, 2, 3, 4, 0, 5]
    ]

    list_outputs = [
        [24,12,8,6],
        [0,0,9,0,0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 120, 0]
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.productExceptSelf(nums))
    
    # TEST
    for result, output in zip(results, list_outputs):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()