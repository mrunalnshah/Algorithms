"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 190. Reverse Bits

Solution Description (Simple):
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseBits(self, n: int) -> int:   
        n &= 0xFFFFFFFF

        return int(f'{n:032b}'[::-1], 2)

def main():
    solve = Solution()

    nums = [43261596, 2147483644]

    result = []
    for num in nums:
        result.append(solve.reverseBits(num))

    print(result)

if __name__ == "__main__":
    main()