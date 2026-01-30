"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 338. Counting Bits

Solution Description:
Time Complexity: O(n log n)
Space Complexity: O(n) + O(log n)
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        while n > 0:
            ans[n] = bin(n).count('1')

            n -= 1
        
        return ans

def main():
    nums = [2, 5]
    ans = []

    solve = Solution()

    for num in nums:
        ans.append(solve.countBits(num))

    print(ans)

if __name__ == "__main__":
    main()


