"""
Problem: 706. Design HashMap
Link: https://leetcode.com/problems/design-hashmap/

Author: Mrunal Nirajkumar Shah
Date: 20 May, 2026

Time Complexity: Specific
Space Complexity: Specific  
"""

class MyHashMap:
    """
    Implementation of Hash Map (keys --> value)
    """
    def __init__(self):
        """
        Initializing list to keep track of hash_map with [X, Y] 
        where X is Key and Y is Value

        Time Complexity: O(1)
        Space Complexity: O(n) where n is max size of elements to be inserted       
        """
        self.hash_map = list()

    def put(self, key: int, value: int) -> None:
        """
        adds key and value to hash_map if not duplicate, if duplicate exists than it
        replaces the value assigned to the key with new value.

        Time Complexity: O(n) where n is number of elements in hash_map
        Space Complexity: O(1)
        """
        if self.contains(key):
           for map in self.hash_map:
               if map[0] == key:
                   map[1] = value
        else:
            self.hash_map.append([key, value])

    def get(self, key: int) -> int:
        """
        if key exists, then get the value else return -1.

        Time Complexity: O(n) where n is number of elements in hash_map
        Space Complexity: O(1)        
        """
        if not self.contains(key):
            return -1
        
        for map in self.hash_map:
            if map[0] == key:
                return map[1]
        
        return -1

    def remove(self, key: int) -> None:
        """
        remove the key and value if key exists.

        Time Complexity: O(n) where n is number of elements in hash_map
        Space Complexity: O(1)   
        """
        if not self.contains(key):
            return
        
        for map in self.hash_map:
            if map[0] == key:
                self.hash_map.remove([map[0], map[1]])
                return
            
    def contains(self, key: int) -> bool:
        """
        if key exists, return True else False.

        Time Complexity: O(n) where n is number of elements in hash_map
        Space Complexity: O(1)   
        """
        for map in self.hash_map:
            if key == map[0]:
                return True
        
        return False

def main():
    myHashMap = MyHashMap()
    myHashMap.put(1, 1)
    print(myHashMap.hash_map)
    myHashMap.put(2, 2)
    print(myHashMap.hash_map)
    print(myHashMap.get(1))
    print(myHashMap.get(3))
    myHashMap.put(2, 1)
    print(myHashMap.hash_map)
    print(myHashMap.get(2))
    myHashMap.remove(2)
    print(myHashMap.hash_map)
    print(myHashMap.get(2))

if __name__ == "__main__":
    main()