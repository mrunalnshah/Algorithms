"""
Problem: 229. Majority Element II
Link: https://leetcode.com/problems/majority-element-ii/

Author: Mrunal Nirajkumar Shah
Date: 27 May, 2026

Time Complexity: O(n + m)
Space Complexity: O(m)
where n is size of input nums, and m is the size of hash_map.
"""

from typing import List

class Solution:
    """
    Input = [3, 2, 3]
    Output = [3]
    because len(Input) = 3 and 3 // 3 == 1
    so, as per question any unique value, more than 1 is result.
    therfore 3.
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Use hash_map to keep track of count of unique values. Use
        hash_map to than select values that are more than len(nums) // 3.
        """
        hash_map = {}
        res = []

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        for key, value in hash_map.items():
            if value > (len(nums) // 3):
                res.append(key)

        
        return res

def main():
    list_nums = [
        [3,2,3],
        [1],
        [1,2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 1, 0, 5, 7, 7, 9, 10, 11, 12, 13, 1, 1]
    ]

    list_output = [
        [3],
        [1],
        [1, 2],
        [],
        [1]
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.majorityElement(nums))

    # TEST
    for result, output in zip(results, list_output):
        if sorted(result) == sorted(output):
            print("PASS")
        else:
            print(sorted(result), sorted(output))
            print("FAIL")

if __name__ == "__main__":
    main()