"""
Problem: 705. Design HashSet
Link: https://leetcode.com/problems/design-hashset/

Author: Mrunal Nirajkumar Shah
Date: 13 May, 2026

Time Complexity: Specific
Space Complexity: Specific  
"""

from typing import List

class MyHashSet:
    """
    Implementation of Hash Set
    """
    def __init__(self):
        """
        Initializing a List to keep track of keys

        Time Complexity: O(1)
        Space Complexity: O(n) where n is max size of elements to be inserted
        """
        self.hash_map = list()   
        
    def add(self, key: int) -> None:
        """
        adds key to hash_map if not duplicate

        Time Complexity: O(n) where n is number of elements in hash_map
        Space Complexity: O(1)
        """
        if self.contains(key):
            return
        
        self.hash_map.append(key)

    def remove(self, key: int) -> None:
        """
        removes key from list if exists

        Time Complexity: O(n + n) where n is number of elements in hash_map
        Space Complexity: O(1)
        """
        if not self.contains(key):
            return
        
        self.hash_map.remove(key)

    def contains(self, key: int) -> bool:
        """
        checks if key exists in hash_map. If key exists then it returns True else False.

        Time Complexity: O(n) where n is number of elements in hash_map
        Space Complexity: O(1)
        """
        for num in self.hash_map:
            if num == key:
                return True
        
        return False

def main():
    myHashSet = MyHashSet()
    myHashSet.add(1)
    print("HASH_MAP:", myHashSet.hash_map)
    myHashSet.add(2)
    print("HASH_MAP:", myHashSet.hash_map)
    print(myHashSet.contains(1)) 
    print(myHashSet.contains(3)) 
    myHashSet.add(2)
    print("HASH_MAP:", myHashSet.hash_map)
    print(myHashSet.contains(2))
    myHashSet.remove(2)
    print("HASH_MAP:", myHashSet.hash_map)  
    print(myHashSet.contains(2))

if __name__ == "__main__":
    main()