"""
Problem: 41. First Missing Positive
Link: https://leetcode.com/problems/first-missing-positive/

Author: Mrunal Nirajkumar Shah
Date: 30 May, 2026

Time Complexity: O(n + m)
Space Complexity: O(m)
where n is the size of nums, and m is the size of set_memory.

NOT VALID BASED ON QUESTION (Have to use O(1) Auxilury memory)
"""

from typing import List

class Solution:
    """
    Input = [1, 2, 0]
    Output = 3
    Smallest Poitive integer missing is 3
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Use a hash_set to keep track of elements, also if the smallest_positive integer is available,
        then use a loop to find the smallest_positive integer which is not in hash_set.
        """
        smallest_positive = 1
        set_memory = set()

        for num in nums:
            if num == smallest_positive:
                smallest_positive += 1

                loop = True
                while loop:
                    if smallest_positive in set_memory:
                        smallest_positive += 1
                    else:
                        loop = False
    
            set_memory.add(num)
            

        return smallest_positive

def main():
    list_nums = [
        [1,2,0],
        [3,4,-1,1],
        [7,8,9,11,12],
        [-1, 1, 2, 3, 4, 5],
        [1],
        [-999, -998, -997, 1000, 10001],
        [100000, 3, 4000, 2, 15, 1, 99999]
    ]

    list_output = [
        3,
        2,
        1,
        6,
        2,
        1,
        4
    ]

    solve = Solution()

    results = []
    for nums in list_nums:
        results.append(solve.firstMissingPositive(nums))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()