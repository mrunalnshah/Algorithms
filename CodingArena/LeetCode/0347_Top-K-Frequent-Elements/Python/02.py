"""
Author: Mrunal Nirajkumar Shah
Date  : 7th February, 2026

LeetCode: 347. Top K Frequent Elements

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result

def main():
    list_nums = [
        ([1,1,1,2,2,3], 2),
        ([1], 1),
        ([1,2,1,2,1,2,3,1,3,2], 2)
    ]
    
    solve = Solution()
    result = []

    for nums in list_nums:
        result.append(solve.topKFrequent(nums=nums[0], k=nums[1]))

    print(result)

if __name__ == "__main__":
    main()
