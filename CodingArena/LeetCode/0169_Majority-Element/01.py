"""
Problem: 169. Majority Element
Link: https://leetcode.com/problems/majority-element/

Author: Mrunal Nirajkumar Shah
Date: 13 May, 2026

Time Complexity: O(n + m) where n is size of nums and m is size of hash_map
Space Complexity: O(n) where n is size of nums  
"""

from typing import List

class Solution:
    """
    input: [3, 4, 3]
    output: 3
    because 3 has maximum occurance
    """
    def majorityElement(self, nums: List[int]) -> int:
        """
        store every num in hash_map with key as num and count as its occurence. 
        return the key with maximum value in hash_map.
        """
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        mode_value = max(hash_map.items(), key=lambda x: x[1])[0]

        return mode_value


def main():
    list_nums = [
        [3,2,3],
        [2,2,1,1,1,2,2],
        [1, 2, 3, 4, 5, 6, 6],
        [0],
        [3, 3, 4]
    ]

    list_outputs = [
        3,
        2,
        6,
        0,
        3
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.majorityElement(nums))

    # TEST
    for result, output in zip(results, list_outputs):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()