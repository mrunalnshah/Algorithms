"""
Author: Mrunal Nirajkumar Shah
Date  : 12th February, 2026

LeetCode: 128. Longest Consecutive Sequence

[DICT- HASHMAP (Abit unoptimized)]
Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memory = {}

        for num in nums:
            if num in memory:
                continue
            
            memory[num] = 0
            if (num + 1) in memory:
                memory[num] = 1
            
            if (num - 1) in memory:
                memory[num - 1] = 1

        consecutive, max_consecutive = 0, 0
        for key in memory:
            consecutive = 0
            if (key - 1) in memory:
                continue
            else:
                if (key + 1) in memory:
                    consecutive += 1
                    next_key = key + 1
                    while memory[next_key] != 0:
                        next_key += 1
                        consecutive += 1
                    consecutive += 1
                else:
                    consecutive = 1
                
                max_consecutive = max(consecutive, max_consecutive)

            
        return max_consecutive



def main():
    list_nums = [[100,4,200,1,3,2],
                 [0,3,7,2,5,8,4,6,0,1],
                 [1,0,1,2],
                 [0, 1, 2, 3, 99, 100],
                 [0],
                 []]
    
    solve = Solution()

    result = []

    for nums in list_nums:
        result.append(solve.longestConsecutive(nums))

    print(result)

if __name__ == "__main__":
    main()