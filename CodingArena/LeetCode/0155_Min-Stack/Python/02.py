"""
Author: Mrunal Nirajkumar Shah
Date  : 16th February, 2026

LeetCode: 155. Min Stack

Solution Description:
Time Complexity: O(1)
Space Complexity: O(n)
"""

class MinStack:

    def __init__(self):
        self.array = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if self.min_stack == []:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)

        self.array.append(val)
        return None

    def pop(self) -> None:
        if self.array[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.array.pop()

        return None

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int: 
        return self.min_stack[-1]
    
    
def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

if __name__ == "__main__":
    main()
