"""
Problem: 27. Remove Element
Link: https://leetcode.com/problems/remove-element/

Author: Mrunal Nirajkumar Shah
Date: 13 May, 2026

Time Complexity: O(n * m) where n is size of nums and m is shifting if num is equals to val
Space Complexity: O(1) 
"""

from typing import List

class Solution:
    """
    input: nums = [3, 2, 2, 3] val = 3
    output: 2 (nums = [2, 2])
    remove all occurence of 3 from nums.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        shift the index one to the left if target value is found. If not than continue.
        We keep account of index with i and bound with top. use j to shift one time to left to remove the occurence
        and pop the last element.
        """
        top = len(nums) - 1

        i = 0
        while i <= top:
            if nums[i] == val:
                j = i
                while j <= top - 1:
                    nums[j] = nums[j + 1]

                    j += 1
                nums.pop()
                top -= 1
                
            else:
                i += 1

        return len(nums)

def main():
    list_inputs = [
        ([3,2,2,3], 3),
        ([0,1,2,2,3,0,4,2], 2),
        ([0], 0),
        ([0, 0, 0], 0),
        ([1, 2, 3, 4, 5, 6], 7)
    ]

    list_output = [
        2,
        5,
        0,
        0,
        6
    ]

    solve = Solution()

    results = []
    for input in list_inputs:
        results.append(solve.removeElement(input[0], input[1]))

    # TEST
    for result, output in zip(results, list_output):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()