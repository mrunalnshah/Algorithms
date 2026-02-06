"""
Author: Mrunal Nirajkumar Shah
Date  : 6th February, 2026

LeetCode: 49. Group Anagrams

Solution Description:
Time Complexity: O(n * m)
Space Complexity: O(n)
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = defaultdict(list)
        
        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1

            memory[tuple(count)].append(str)

        return list(memory.values())

def main():
    list_strs = [["eat","tea","tan","ate","nat","bat"],
                 [""],
                 ["a"]]
    
    solve = Solution()

    result = []
    for strs in list_strs:
        result.append(solve.groupAnagrams(strs))

    print(result)

if __name__ == "__main__":
    main()