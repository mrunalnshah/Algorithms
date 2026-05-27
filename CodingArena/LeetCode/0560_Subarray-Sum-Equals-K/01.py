"""
Problem: 560. Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Author: Mrunal Nirajkumar Shah
Date: 27 May, 2026

Time Complexity: O(n * m)
Space Complexity: O(m)
where n is the input size and m is the size of hash_map

TIME LIMIT EXCEEDED
"""

from typing import List

class Solution:
    """
    Input: nums = [1, 1, 1], k = 2
    Output: 2
    [X, 1, 1], [1, 1, X] == 2
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Use hash_map to store each index and keep adding sum to each
        index in hash_map for each num. if num == k than we += 1 count.
        """
        hash_map = {}
        subarray_count = 0

        for i, num in enumerate(nums):
            for key in list(hash_map.keys()):
                if hash_map[key] + num == k:
                    subarray_count += 1
                
                hash_map[key] += num
        
            if num == k:
                subarray_count += 1

            hash_map[i] = num
            
        return subarray_count

def main():
    list_inputs = [
        ([1,1,1], 2),
        ([1,2,3], 3),
        ([1], 5),
        ([1], 1),
        ([-1000, 200, 500, 300, 0], 0),
        ([1,-1,0], 0),
        ([100,1,2,3,100,1,2,3,4], 3),
        ([0,0,0,0,0,0,0,0,0,0], 0)
    ]

    list_outputs = [
        2,
        2,
        0,
        1,
        3,
        3,
        4,
        55
    ]

    solve = Solution()

    results = []
    for inputs in list_inputs:
        results.append(solve.subarraySum(inputs[0], inputs[1]))

    # TEST
    for result, output in zip(results, list_outputs):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()