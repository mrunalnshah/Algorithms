"""
Problem: 225. Implement Stack using Queues
Link: https://leetcode.com/problems/implement-stack-using-queues/

Author: Mrunal Nirajkumar Shah
Date: 31 May, 2026

Time Complexity: AS PER FUNCTION
Space Complexity: AS PER FUNCTION

where n is the max_size of any of the queue (both will be same size)
"""

class MyStack:
    """
    Implementing a stack using queue (push to end, and pop from front)
    """
    def __init__(self):
        """
        Use two queues to keep track of elements and a use variable to have active queue

        Time Complexity: O(1)
        Space Complexity: O(2 * n)
        """
        self.queue1 = []
        self.queue2 = []
        self.use = 1

    def push(self, x: int) -> None:
        """
        Push to the end

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.use == 1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self) -> int:
        """
        pop from the front from active queue and push to the end of alternative queue, 
        don't push last element of active queue.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.use == 1:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))
            
            val = self.queue1.pop(0)
            self.use = 2
        else:
            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.pop(0))

            val = self.queue2.pop(0)
            self.use = 1

        return val
        
    def top(self) -> int:
        """
        pop from the front from active queue and push to the end of alternative queue,
        store the top_val of the last element and push it to alternative queue and also return
        top_val.
    
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.use == 1:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.pop(0))
            
            top_val = self.queue1.pop(0)
            self.queue2.append(top_val)

            self.use = 2
        else:
            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.pop(0))
            
            top_val = self.queue2.pop(0)
            self.queue1.append(top_val)

            self.use = 1

        return top_val


    def empty(self) -> bool:
        """
        for active queue, check if len(active queue) > 0 and return False else return True

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if self.use == 1:
            if len(self.queue1) > 0:
                return False
            
            return True
        else:
            if len(self.queue2) > 0:
                return False
            
            return True

def main():
    myStack = MyStack()
    myStack.push(1)
    print(myStack.queue1, myStack.queue2)
    myStack.push(2)
    print(myStack.queue1, myStack.queue2)
    print("TOP:", myStack.top())
    print(myStack.queue1, myStack.queue2)
    print("POP:", myStack.pop())
    print(myStack.queue1, myStack.queue2)
    print("IS EMPTY:", myStack.empty())
    

if __name__ == "__main__":
    main()