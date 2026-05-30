"""
Problem: 128. Longest Consecutive Sequence
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Author: Mrunal Nirajkumar Shah
Date: 26 May, 2026

Time Complexity: O(n + n)
Space Complexity: O(n)
where n is size of nums
"""

from typing import List

class Solution:
    """
    Input = [100, 4, 200, 1, 3, 2]
    Output = 4
    
    Max Consecutive = [1, 2, 3, 4]
    Other Consecutives = [100], [200]
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Use hash_map to store key = num and value = num + 1 if num + 1 exists in nums.
        If num - 1 exists, than add num to num - 1 in hash_map as value. By default keep
        it None. Use this hash_map to calculate max_consecutive by doing to the lowest
        connected key by decreasing key by 1, and then start calculating consecutive.
        """
        hash_map = {}

        for num in nums:
            if num + 1 in hash_map:
                hash_map[num] = num + 1
            else:
                hash_map[num] = None

            if num - 1 in hash_map:
                hash_map[num - 1] = num
        
        max_consecutive = 0
        consecutive = 0
        for key in list(hash_map.keys()):
            if key not in hash_map:
                continue

            cur_key = key
            while cur_key - 1 in hash_map:
                cur_key = cur_key - 1

            consecutive = 1
            while hash_map[cur_key] != None:
                old_cur_key = cur_key
                cur_key = hash_map[cur_key]
                hash_map.pop(old_cur_key)

                consecutive += 1
            
            max_consecutive = max(max_consecutive, consecutive)
            consecutive = 0

        return max_consecutive

def main():
    list_nums = [
        [100,4,200,1,3,2],
        [0,3,7,2,5,8,4,6,0,1],
        [1,0,1,2],
        [],
        [1],
        [999, 998, 997, 0, 1, 2, 3]
    ]

    list_output = [
        4,
        9,
        3,
        0,
        1,
        4
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.longestConsecutive(nums))
    
    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()