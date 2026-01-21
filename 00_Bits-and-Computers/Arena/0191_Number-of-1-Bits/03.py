"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 191. Number of 1 Bits

Solution Description:
Time Complexity: bin(n) = O(log n) + .count('1') = O(log n) = O(log n)
Space Complexity: O(log n)

Additional Resources:
1. https://en.wikipedia.org/wiki/Hamming_weight
2. A set bit refers to a bit in the binary representation of a number that has a value of 1.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        The Hamming weight of a binary string or number is the count of its nonzero bits, which typically corresponds to the number of '1's in its binary representation. 
        
        :param n: a number
        :type n: int
        :return: count of set bits in number
        :rtype: int
        """
        return bin(n).count('1')


def main():
    solve = Solution()

    nums = [11, 128, 2147483645]

    result = []

    for num in nums:
        result.append(solve.hammingWeight(num))
    
    print(result)

if __name__ == "__main__":
    main()        
