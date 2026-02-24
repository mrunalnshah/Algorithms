"""
Author: Mrunal Nirajkumar Shah
Date  : 24th February, 2026

LeetCode: 15. 3Sum

Time Limit Exceed
Solution Description:
Time Complexity: O(n^2 ~ n^3)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        memory = {}
        triplets = []

        for i in range(0, len(nums) - 1, 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] not in memory:
                    memory[nums[i] + nums[j]] = [[i,j]] 
                else:
                    memory[nums[i] + nums[j]].append([i,j]) 

        for i, num in enumerate(nums):
            if -(num) in memory:
                fetch_mem = memory[-num]
                if fetch_mem:
                    if len(fetch_mem) > 0:
                        for mem in fetch_mem:
                            if i in mem:
                                continue
                            triplet = [i]
                            triplet.extend(mem)
                            triplets.append(triplet)
                    else:
                        if i in mem:
                            continue
                        triplet = [i]
                        triplet.extend(fetch_mem)
                        triplets.append(triplet)
        
        unique_lists = list(dict.fromkeys(tuple(sorted(x)) for x in triplets if len(x) == len(set(x))))
        final_list = []
        seen_value = set()

        for index_list in unique_lists:
            decode = [nums[index] for index in index_list]

            value_key = tuple(sorted(decode))

            if value_key not in seen_value:
                seen_value.add(value_key)
                final_list.append(decode)  

        return final_list

def main():
    list_nums = [
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
        [0,0,0,0],
        [-1,0,1,2,-1,-4]
    ]
    
    solve = Solution()

    result = []
    for nums in list_nums:
        result.append(solve.threeSum(nums))

    print(result)

if __name__ == "__main__":
    main()