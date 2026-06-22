"""
Problem: 895. Maximum Frequency Stack
Link: https://leetcode.com/problems/maximum-frequency-stack/

Author: Mrunal Nirajkumar Shah
Date: 22 June, 2026

Time Complexity: O(1)
Space Complexity: O(1)
"""

from collections import OrderedDict

class FreqStack:
    """
    Build a Most Frequent Stack which pops the most frequent value, if multiple,
    than most recent frequent value.
    """
    def __init__(self):
        """
        Use count to keep track of key -> value, where i need to see
        key as frequency count.
        """
        self.count = {}
        self.maxCount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        """
        push the val to stacks in stacks[count] where
        count is how many times the val occured. Append it
        in such a way that we can maintain position.
        """
        valCount = 1 + self.count.get(val, 0)
        self.count[val] = valCount

        if valCount > self.maxCount:
            self.maxCount = valCount
            self.stacks[valCount] = []
        self.stacks[valCount].append(val)

    def pop(self) -> int:
        """
        pop from the stacks[maxCount] to downwards.
        """
        res = self.stacks[self.maxCount].pop()
        self.count[res] -= 1

        if not self.stacks[self.maxCount]:
            self.maxCount -= 1

        return res

def main():
    freqStack = FreqStack()
    freqStack.push(5)
    print(freqStack.count, freqStack.maxCount, freqStack.stacks)
    freqStack.push(7)
    print(freqStack.count, freqStack.maxCount, freqStack.stacks)
    freqStack.push(5)
    print(freqStack.count, freqStack.maxCount, freqStack.stacks)
    freqStack.push(7)
    print(freqStack.count, freqStack.maxCount, freqStack.stacks)
    freqStack.push(4)
    print(freqStack.count, freqStack.maxCount, freqStack.stacks)
    freqStack.push(5)
    print(freqStack.count, freqStack.maxCount, freqStack.stacks)
    print("POP:", freqStack.pop())
    print("POP:", freqStack.pop())
    print("POP:", freqStack.pop())
    print("POP:", freqStack.pop())
    print(freqStack.count, freqStack.maxCount, freqStack.stacks)

if __name__ == "__main__":
    main()


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()