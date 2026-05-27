"""
Problem: 560. Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Author: Mrunal Nirajkumar Shah
Date: 27 May, 2026

Time Complexity: O(n)
Space Complexity: O(m)
where n is the input size and m is the size of hash_map with unique elements

PREFIX SUM
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
        Use hash_map to keep track of prefix_sum with 0: 1 init,
        keep adding sum += num, and check is sum - k is in prefix, if
        yes than add count += prefix[sum - k]. add each sum to hash_map
        with increasing count of it.
        """
        subarray_count = 0
        
        prefix_sum = {0: 1}
        sum = 0

        for num in nums:
            sum += num

            if (sum - k) in prefix_sum:
                subarray_count += prefix_sum[sum - k]
            
            if sum in prefix_sum:
                prefix_sum[sum] += 1
            else:
                prefix_sum[sum] = 1
        
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
        ([0,0,0,0,0,0,0,0,0,0], 0),
        ([1, -1, 1, 1, 1, 1], 3)
    ]

    list_outputs = [
        2,
        2,
        0,
        1,
        3,
        3,
        4,
        55,
        4
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