"""
Problem: 271. Encode and Decode Strings
Link: https://leetcode.com/problems/encode-and-decode-strings
NeetCode Link: https://neetcode.io/problems/string-encode-and-decode/question

Author: Mrunal Nirajkumar Shah
Date: 22 May, 2026

Time Complexity: O(n + m) (2 times - encode + decode)
Space Complexity: O(k + o) (2 times - encode + decode)
where n is number of strings in a array, m is to join index_array and string,
k is size of the index array and o is the size of encoded string.
"""

from typing import List

class Solution:
    """
    INPUT = ["bello", "globo"]
    OUTPUT = ["bello", "globo"]

    what we did is we encoded the input array into a string, and later decoded the string into output array.
    where input array is equals to output array. 
    """
    def encode(self, strs: List[str]) -> str:
        """
        We encode like this
        index1_index_2_..._index_n%string

        index here are end index of a word in string.
        """
        if strs == []:
            return ""

        str_index_array = []
        
        concat_string = ''

        index = 0
        for word in strs:
            index += len(word)
            
            concat_string += word
            
            str_index_array.append(str(index))

        encoded_string = '_'.join(str_index_array) + "%" + concat_string

        return encoded_string
    
    
    def decode(self, s: str) -> List[str]:
        """
        we split the string into 2 parts on first %, and use the [0] as index_array
        and [1] as concatinated_string. [0] is later split into multiple index array on "_"
        and used to fetch words or strings from the concat_string [1].
        """
        if s == "":
            return []
        
        str_index_array, concat_string = s.split("%", maxsplit=1) 

        index_array = str_index_array.split("_")

        decoded_string = []
        
        iter = 0
        for index in index_array:
            int_index = int(index)
            decoded_string.append(concat_string[iter:int_index])

            iter = int_index
        
        return decoded_string


def main():
    list_strs = [
        ["Hello","World"],
        [""],
        ["Mrunal%", "%Mrunal"],
        ["%"],
        ["%", "%", "%"],
        ["%MRUNAL", ""],
        []
    ]

    list_outputs = [
        ["Hello","World"],
        [""],
        ["Mrunal%", "%Mrunal"],
        ["%"],
        ["%", "%", "%"],
        ["%MRUNAL", ""],
        []
    ]

    solve = Solution()

    results = []
    for strs in list_strs:
        results.append(solve.decode(solve.encode(strs)))

    # TEST
    for result, output in zip(results, list_outputs):
        if result == output:
            print("PASS")
        else:
            print(result, output)
            print("FAIL")

if __name__ == "__main__":
    main()