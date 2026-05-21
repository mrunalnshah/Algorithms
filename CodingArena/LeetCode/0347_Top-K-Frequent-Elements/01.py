"""
Problem: 347. Top K Frequent Elements
Link: https://leetcode.com/problems/top-k-frequent-elements/

Author: Mrunal Nirajkumar Shah
Date: 21 May, 2026

Time Complexity: O(n + m log m)
Space Complexity: O(m)
where n is the total number of elements, and m is the number of unique elements
"""

from typing import List

class Solution:
    """
    Input: nums= [1,1,1,2,2,3] ; k = 2
    Output = [1, 2]

    because 1 and 2 have highest number of duplicates and also k = 2 therefore 
    we returned to top k frequency.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Create an hash_map and keep the num to count (key to value).
        Later sort the hash_map descending, and pick up top k values.
        """
        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
                
        sorted_hash_map = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_hash_map[i][0])

        return res

def main():
    list_inputs = [ 
        ([1,1,1,2,2,3], 2),
        ([1], 1),
        ([1,2,1,2,1,2,3,1,3,2], 2)
    ]

    list_outputs = [
        [1,2],
        [1],
        [1,2]
    ]

    solve = Solution()

    results = []
    for input in list_inputs:
        results.append(solve.topKFrequent(input[0], input[1]))

    # TEST
    for result, output in zip(results, list_outputs):
        if sorted(result) == sorted(output):
            print("PASS")
        else:
            print(result, output)
            print("FAIL")
    

if __name__ == "__main__":
    main()


