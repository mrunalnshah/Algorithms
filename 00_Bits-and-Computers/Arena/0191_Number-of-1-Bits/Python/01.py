"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 191. Number of 1 Bits

Solution Description:
Its a brute-force solution. Going across multiple bits to find the count of set bits.
- Time Complexity  : O(k) - k is number of bits in number 
- Space Complexity : O(1)

Additional Resources:
1. https://en.wikipedia.org/wiki/Hamming_weight
2. A set bit refers to a bit in the binary representation of a number that has a value of 1.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            
            n = n >> 1
        
        return count


def main():
    solve = Solution()

    nums = [11, 128, 2147483645]

    result = []

    for num in nums:
        result.append(solve.hammingWeight(num))
    
    print(result)

if __name__ == "__main__":
    main()        
