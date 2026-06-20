"""
Problem: 155. Min Stack
Link: https://leetcode.com/problems/min-stack/

Author: Mrunal Nirajkumar Shah
Date: 2 June, 2026

Time Complexity: O(1)
Space Complexity: O(2 * n)

where n is the size of the max a stack can become.
"""

class MinStack:
    """
    Implemented a Stack with push, pop, top and getMin.

    PUSH: append the val in stack, append the min of val and min_stack[-1].
    POP: pop from stack and min_stack
    top: return stack[-1]
    getMin: return min_stack[-1]
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
    
def main():
    minStack = MinStack()
    minStack.push(-2)
    print(minStack.stack, minStack.min_stack)
    minStack.push(0)
    print(minStack.stack, minStack.min_stack)
    minStack.push(-3)
    print(minStack.stack, minStack.min_stack)
    print("MIN:", minStack.getMin())
    minStack.pop()
    print(minStack.stack, minStack.min_stack)
    print("TOP:", minStack.top())
    print("MIN:", minStack.getMin())

if __name__ == "__main__":
    main()
