"""
Author: Mrunal Nirajkumar Shah
Date  : 28th March, 2026

LeetCode: 143. Reorder List

Solution Description:
Time Complexity: O(n^2)  
Space Complexity: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count = 0

        curNode = head
        while curNode:
            count += 1

            curNode = curNode.next
        
        curNode = head
        while count > 1:
            nextNode = curNode.next
            
            prevNode = None
            counterNode = curNode

            while counterNode.next:
                prevNode = counterNode
                counterNode = counterNode.next

            if prevNode:
                prevNode.next = None

            curNode.next = counterNode
            counterNode.next = nextNode

            curNode = nextNode

            count -= 2

        curNode.next = None

def main():
    # Test Case 1
    node14 = ListNode(val=4)
    node13 = ListNode(val=3, next=node14)
    node12 = ListNode(val=2, next=node13)
    node11 = ListNode(val=1, next=node12)

    head1 = node11

    # Test Case 2
    node25 = ListNode(val=5)
    node24 = ListNode(val=4, next=node25)
    node23 = ListNode(val=3, next=node24)
    node22 = ListNode(val=2, next=node23)
    node21 = ListNode(val=1, next=node22)

    head2 = node21

    heads = [head1, head2]

    solve = Solution()

    for head in heads:
        solve.reorderList(head=head)
    
    for i, head in enumerate(heads):
        print("Test Case", i)
        curNode: ListNode = head

        while curNode:
            print(curNode.val)

            curNode = curNode.next



if __name__ == "__main__":
    main()