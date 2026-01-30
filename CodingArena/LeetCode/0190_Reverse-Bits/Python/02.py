"""
Author: Mrunal Nirajkumar Shah
Date  : 21st January, 2026

LeetCode: 190. Reverse Bits

Solution Description (String Swap):
Time Complexity: O(n / 2) ~ O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseBits(self, n: int) -> int:   
        bin_n = format(n & 0xFFFFFFFF, '032b')
        bin_list = list(bin_n)
      
        i = 0
        j = len(bin_list) - 1

        while i <= j:
            temp = bin_list[i]
            bin_list[i] = bin_list[j]
            bin_list[j] = temp
            i += 1
            j -= 1

        return int(''.join(bin_list), 2)

def main():
    solve = Solution()

    nums = [43261596, 2147483644]

    result = []
    for num in nums:
        result.append(solve.reverseBits(num))

    print(result)

if __name__ == "__main__":
    main()