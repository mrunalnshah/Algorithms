"""
Author: Mrunal Nirajkumar Shah
Date  : 6th February, 2026

LeetCode: 49. Group Anagrams

Solution Description:
Time Complexity: O(n * k log k) -> n: for and k: sorted
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memory = {}
        
        for str in strs:
            # key = sorted(str) # this won't work as its list and list can't be key or hashable
            key = ''.join(sorted(str))

            if key in memory:
                memory[key].append(str)
            
            else:
                memory[key] = [str]


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