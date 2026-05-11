"""
Author: Mrunal Nirajkumar Shah
Date  : 28th March, 2026

LeetCode: 143. Reorder List

Solution Description:
Time Complexity: O(n)  
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
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        prevNode = None
    
        # Reverse the second half
        while second_half:
            temp = second_half.next

            second_half.next = prevNode
            prevNode = second_half
            second_half = temp

        first_half = head
        second_half = prevNode

        # Merge two halfs
        while second_half:
            temp1 = first_half.next
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2
        

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