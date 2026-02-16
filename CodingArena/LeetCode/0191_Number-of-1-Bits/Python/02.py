"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 191. Number of 1 Bits

Solution Description (Brian Kernighan's Algorithm):
- Time Complexity  : O(m) ~ O(log n) - m is count of 1s, n is number 
- Space Complexity : O(1)

Additional Resources:
1. https://en.wikipedia.org/wiki/Hamming_weight
2. A set bit refers to a bit in the binary representation of a number that has a value of 1.
3. https://medium.com/@wizzywooz/brian-kernighans-algorithm-c65d796a7112
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= (n - 1)
            count += 1
            
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
