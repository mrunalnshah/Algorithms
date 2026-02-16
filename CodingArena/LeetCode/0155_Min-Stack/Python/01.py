"""
Author: Mrunal Nirajkumar Shah
Date  : 16th February, 2026

LeetCode: 155. Min Stack

Solution Description:
Time Complexity: O(n)
Space Complexity: O(n)
"""

class MinStack:

    def __init__(self):
        self.array = []
        self.min_value = None

    def push(self, val: int) -> None:
        if self.min_value == None:
            self.min_value = val
        else:
            if val < self.min_value:
                self.min_value = val

        self.array.append(val)
        return None

    def pop(self) -> None:
        num = self.array.pop()

        if num == self.min_value:
            self.min_value = None
            self.reassign_min()

        return None

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int: 
        return self.min_value
    
    def reassign_min(self):
        for num in self.array:
            if self.min_value == None:
                self.min_value = num
            else:
                if num < self.min_value:
                    self.min_value = num
    
def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

    print(obj.array)


if __name__ == "__main__":
    main()
