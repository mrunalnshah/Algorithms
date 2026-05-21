"""
Problem: 912. Sort an Array
Link: https://leetcode.com/problems/sort-an-array/

Author: Mrunal Nirajkumar Shah
Date: 20 May, 2026

Time Complexity: O(n + 100001) where n is length of nums and 100001 is the iteration to build a new array from count_array.
Space Complexity: O (100001 + m) where 100001 is Contraint Defined and m is the size of the unique values in nums.

COUNT SORT
"""

from typing import List

class Solution:
    """
    input  = [5,2,3,1]
    output = [1,2,3,5]
    ASCENDING SORT
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Defined a array of size 100001 as constraints defined.
        for each ith index is i + offset and stores the count of how many times repeat of (i + offset) num.

        later iterate through the count_array to create res array with extending the count. return res
        """
        if len(nums) == 1 or len(nums) == 0:
            return nums

        offset = 50000
        count_array = [0] * 100001

        for num in nums:
            count_array[num + offset] += 1

        res = []
        for i, count in enumerate(count_array):
            if count == 0:
                continue

            res.extend([i - offset] * count)
        
        return res

def main():
    list_nums = [
        [5,2,3,1],
        [5,1,1,2,0,0]
    ]

    list_output = [
        [1,2,3,5],
        [0,0,1,1,2,5]
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.sortArray(nums))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL") 

if __name__ == "__main__":
    main()