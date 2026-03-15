"""
Author: Mrunal Nirajkumar Shah
Date  : 22nd February, 2026

LeetCode: 167. Two Sum II - Input Array Is Sorted

Using a Hash Map.
Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memory = {}

        for i, number in enumerate(numbers):
            if target - number in memory:
                return [memory[target - number] + 1, i + 1]
            else:
                memory[number] = i
        
        return [0, 0]


def main():
    list_numbers = [([2,7,11,15], 9),
                    ([2,3,4], 6),
                    ([-1,0], -1)]
    
    solve = Solution()

    result = []
    for numbers in list_numbers:
        result.append(solve.twoSum(numbers=numbers[0], target=numbers[1]))

    print(result)

if __name__ == "__main__":
    main()