"""
Author: Mrunal Nirajkumar Shah
Date  : 9th February, 2026

LeetCode: 271. Encode and Decode Strings

Solution Description:
Time Complexity: 
1. Encode: O(N + K)
    O(K): to convert integers to strings and join them; 
    O(N): to concatenate the actual data.
2. Decode: O(N + K)
    O(N + K): as it scans the string to find the first delimiter.

Space Complexity: O(N + K)
"""

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        index = 0

        if (strs == []):
            return ""

        length_index = []
        
        for s in strs:
            str_length = len(s) #-1 if empty
            index += str_length
            length_index.append(index - 1)
        
        string_map = "_".join([str(i) for i in length_index])
        concat_string = "".join(strs)

        encode_string = f"{string_map}%{concat_string}"

        return encode_string
        

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        indices, string = s.split("%", 1)

        list_indices = [int(index) for index in indices.split("_")]
        
        decode_string = []
        
        i = 0
        for index in list_indices:
            decode_string.append(string[i:index+1])
            i = index + 1

        return decode_string
        

def main():
    solve = Solution()

    # string = ["Hello", "World"]
    # string = ["%", " ", ""]
    string = ["", "", ""]
    encoded_string = solve.encode(string)
    decoded_string = solve.decode(encoded_string)

    print("String:", string )
    print("Encoded String:", encoded_string)
    print("Decoded String:", decoded_string)

if __name__ == "__main__":
    main()