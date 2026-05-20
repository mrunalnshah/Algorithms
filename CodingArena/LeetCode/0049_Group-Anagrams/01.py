"""
Problem: 49. Group Anagrams
Link: https://leetcode.com/problems/group-anagrams/

Author: Mrunal Nirajkumar Shah
Date: 12 May, 2026

Time Complexity: O(n + m log m) where n is number of strings and m log m is sorting of the string
Space Complexity: O(n) where n is number of strings.
"""

from typing import List

class Solution:
    """
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    output is a list of list where each list in the main list is grouped anagrams.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        we use hash_map to store key(sorted string) and values(originl string). We loop through each string and check
        if sorted version of the string is in hash_map, if yes than we append the original string to its sorted string key. if not
        we create new key with sorted_string and assign it a list with its first element as original string. At the end we return
        list(hash_map.values())
        """
        hash_map = {}
        
        for str in strs:
            sort_str = "".join(sorted(str))

            if sort_str in hash_map:
                hash_map[sort_str].append(str)
            else:
                hash_map[sort_str] = [str]
        
        return list(hash_map.values())

def normalize(x):
    """
    This is the function used to compare results with original test_case outputs.
    It normalizes the list of list for comparison.
    """
    sorted_groups = [sorted(group) for group in x]

    return sorted(sorted_groups)

def main():
    list_strs = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
    ]

    list_output = [
        [["bat"],["nat","tan"],["ate","eat","tea"]],
        [[""]],
        [["a"]]
    ]

    solve = Solution()

    results = []
    for strs in list_strs:
        results.append(solve.groupAnagrams(strs))
    
    # TEST
    for result, output in zip(results, list_output):
        if normalize(result) == normalize(output):
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()