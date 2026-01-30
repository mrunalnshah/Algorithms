"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 190. Reverse Bits

Solution Description (How CPU's Do it):
Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:   
        n &= 0xFFFFFFFF

        n &= 0xFFFFFFFF
        n = ((n >> 1)  & 0x55555555) | ((n & 0x55555555) << 1)
        n = ((n >> 2)  & 0x33333333) | ((n & 0x33333333) << 2)
        n = ((n >> 4)  & 0x0F0F0F0F) | ((n & 0x0F0F0F0F) << 4)
        n = ((n >> 8)  & 0x00FF00FF) | ((n & 0x00FF00FF) << 8)
        n = ( n >> 16)               | ( n               << 16)
        
        return n & 0xFFFFFFFF

def main():
    solve = Solution()

    nums = [43261596, 2147483644]

    result = []
    for num in nums:
        result.append(solve.reverseBits(num))

    print(result)

if __name__ == "__main__":
    main()