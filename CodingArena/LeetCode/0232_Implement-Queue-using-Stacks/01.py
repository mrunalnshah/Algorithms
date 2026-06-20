"""
Problem: 232. Implement Queue using Stacks
Link: https://leetcode.com/problems/implement-queue-using-stacks/

Author: Mrunal Nirajkumar Shah
Date: 31 May, 2026

Time Complexity: AS PER FUNCTION
Space Complexity: AS PER FUNCTION

AMMORTIZED SOLUTION O(1) in general

where n is the max_size of any of the queue (both will be same size)
"""

class MyQueue:
    """
    Implementing a Queue using stack (push to end, and pop from end)
    """
    def __init__(self):
        """
        Use two stack to keep track of elements

        Time Complexity: O(1)
        Space Complexity: O(2 * n)
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push to the end of stack 1

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.stack1.append(x)


    def pop(self) -> int:
        """
        pop from the end of stack 2, if stack 2 is empty. pop stack 1 elements and append in stack 2.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


    def peek(self) -> int:
        """
        return stack2[-1] from the stack 2, if not available pop stack 1 elements and append in stack 2
        and return last element by -1 index which is top.
    
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]


    def empty(self) -> bool:
        """
        if any of the stack is non-zero, than return False, else return True.
        
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        return max(len(self.stack1), len(self.stack2)) == 0

def main():
    myStack = MyQueue()
    myStack.push(1)
    print(myStack.stack1, myStack.stack2)
    myStack.push(2)
    print(myStack.stack1, myStack.stack2)
    print("TOP:", myStack.peek())
    print(myStack.stack1, myStack.stack2)
    print("POP:", myStack.pop())
    print(myStack.stack1, myStack.stack2)
    print("IS EMPTY:", myStack.empty())
    

if __name__ == "__main__":
    main()