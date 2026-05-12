"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/

Author: Mrunal Nirajkumar Shah
Date: 12 May, 2026

Time Complexity: O(n + m) where n is size of nums and m is size of hash_map (last element inserted before returning).
Space Complexity: O(n) where n is size of nums
"""

from typing import List

class Solution:
    """
    input: [2, 7, 11, 15], 9
    output: [0, 1]
    because [](0) is 2 and [](1) is 7 and their addition is 9 which is target.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        check the difference for each num with target, if the difference is in the hash_map than return the indices of both
        value in hash_map and current indice which is used to check difference. If no difference in hash_map than store the
        current num in hash_map as key and indice as its value.
        """
        hash_map = {}

        for i, num in enumerate(nums):
            difference = target - num

            if difference in hash_map:
                return [hash_map[difference], i]

            hash_map[num] = i
        
        return []

def main():
    list_inputs = [
        ([2,7,11,15], 9),
        ([3,2,4], 6),
        ([3,3], 6),
        ([1, 5, 9, -1, 0], 0),
        ([200, -500, 300, -600, 999, 50, 55, -999], 0)
    ]

    list_output = [
        [0, 1],
        [1, 2],
        [0, 1],
        [0, 3],
        [4, 7]
    ]

    solve = Solution()

    results = []
    for inputs in list_inputs:
        results.append(solve.twoSum(inputs[0], inputs[1]))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            # print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()