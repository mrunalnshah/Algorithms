"""
Author: Mrunal Nirajkumar Shah
Date  : 30th March, 2026

LeetCode: 138. Copy List With Random Pointer

Simple Description: Create a new copy from old copy.(deep copy)

Solution Description:
Time Complexity: O()  
Space Complexity: O()
"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {
            None: None
        }

        # Map old nodes to hash map with new Nodes
        cur = head
        while cur:
            copy = Node(x=cur.val)

            oldToCopy[cur] = copy

            cur = cur.next

        # assign next and random to new Nodes from old nodes
        cur = head
        while cur:
            copy = oldToCopy[cur]

            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]

            cur = cur.next

        return oldToCopy[head]


def main():
    # Test Case 1
    node15 = Node(x=1)
    node14 = Node(x=10, next=node15)
    node13 = Node(x=11, next=node14)
    node12 = Node(x=13, next=node13)
    node11 = Node(x=7, next=node12)

    node11.random = None
    node12.random = node11
    node13.random = node15
    node14.random = node13
    node15.random = node11

    head1 = node11

    # Test Case 2
    node22 = Node(x=2)
    node21 = Node(x=1, next=node22, random=node22)

    node22.random = node22

    head2 = node21

    # Test Case 3
    node33 = Node(x=3)
    node32 = Node(x=3, next=node33)
    node31 = Node(x=3, next=node32)

    node31.random = None
    node32.random = node31
    node33.random = None

    head3 = node31


    heads = [
        head1,
        head2,
        head3
    ]

    solve = Solution()

    results = []
    for head in heads:
        results.append(solve.copyRandomList(head=head))

    for i, result in enumerate(results):
        print("TEST CASE", i)
        curNode = result

        while curNode:
            print(curNode.val)

            curNode = curNode.next


if __name__ == "__main__":
    main()