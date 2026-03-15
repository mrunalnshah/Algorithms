"""
Author: Mrunal Nirajkumar Shah
Date  : 22nd February, 2026

LeetCode: 167. Two Sum II - Input Array Is Sorted

Using a Two Pointers.
Solution Description:
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if target - numbers[j] == numbers[i]:
                return [i  + 1, j + 1]
            elif target - numbers[j] > numbers[i]:
                i += 1
            else:
                j -= 1

        
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