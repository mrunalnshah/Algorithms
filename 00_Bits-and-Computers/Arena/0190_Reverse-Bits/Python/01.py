"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 190. Reverse Bits

Solution Description(Bitwise Version):
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseBits(self, n: int) -> int:   
        result = 0
        
        for _ in range(32):
            result = result << 1
            result += (n & 1)
            n = n >> 1

        return result

def main():
    solve = Solution()

    nums = [43261596, 2147483644]

    result = []
    for num in nums:
        result.append(solve.reverseBits(num))

    print(result)

if __name__ == "__main__":
    main()