"""
Author: Mrunal Nirajkumar Shah
Date  : 2nd April, 2026

LeetCode: 146. LRU Cache

Reference: https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU

Solution Description:
Time Complexity: O(n^2)  
Space Complexity: O(n)
"""

from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {}
        self.queue = deque(maxlen=capacity)
        self.capacity = capacity
        self.top = 0        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        self.queue.remove(key)
        self.queue.append(key)

        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            popKey = self.queue.remove(key)
            self.queue.append(key)

            self.hashmap[key] = value
            return

        if self.top != self.capacity:
            self.hashmap[key] = value
            self.queue.append(key)
            self.top += 1
        else:
            popKey = self.queue.popleft()
            self.hashmap.pop(popKey)

            self.hashmap[key] = value
            self.queue.append(key)
    
def main():
    # Test Case
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))

if __name__ == "__main__":
    main()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)