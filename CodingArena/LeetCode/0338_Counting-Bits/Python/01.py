"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 338. Counting Bits

Solution Description:
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        while n > 0:
            ans[n] = Solution.count(n)

            n -= 1
        
        return ans
    
    @staticmethod
    def count(n: int) -> int:
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            
            n = n >> 1
        
        return count

def main():
    nums = [2, 5]
    ans = []

    solve = Solution()

    for num in nums:
        ans.append(solve.countBits(num))

    print(ans)

if __name__ == "__main__":
    main()


