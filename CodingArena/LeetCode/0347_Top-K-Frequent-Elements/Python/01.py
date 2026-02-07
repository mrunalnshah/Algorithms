"""
Author: Mrunal Nirajkumar Shah
Date  : 7th February, 2026

LeetCode: 347. Top K Frequent Elements

Solution Description:
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memory = {}

        for num in nums:
            if num in memory:
                memory[num] += 1
            else:
                memory[num] = 1
        
        sorted_dict = dict(sorted(memory.items(), key=lambda count: count[1], reverse=True))

        result = []
        for key in sorted_dict:
            if k == len(result):
                break

            result.append(key)

        
        return result


def main():
    list_nums = [([1,1,1,2,2,3], 2),
                 ([1], 1),
                 ([1,2,1,2,1,2,3,1,3,2], 2)]
    
    solve = Solution()

    result = []

    for nums in list_nums:
        result.append(solve.topKFrequent(nums=nums[0], k=nums[1]))

    print(result)

if __name__ == "__main__":
    main()