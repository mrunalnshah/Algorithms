"""
Author: Mrunal Nirajkumar Shah
Date  : 27th March, 2026

LeetCode: 141. Linked List Cycle

[Tortoise and Hare Algorithm]
Solution Description:
Time Complexity: O(n)  
Space Complexity: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    

def main():
    # Test Case 1
    node11 = ListNode(x=3)
    node12 = ListNode(x=2)
    node13 = ListNode(x=0)
    node14 = ListNode(x=-4)

    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node12

    head1 = node11

    # Test Case 2
    node21 = ListNode(x=1)
    node22 = ListNode(x=2)

    node21.next = node22
    node22.next = node21

    head2 = node21

    # Test Case 3
    node31 = ListNode(x=1)

    head3 = node31

    list_heads = [
        head1, 
        head2, 
        head3
    ]

    solve = Solution()

    result = []
    for head in list_heads:
        result.append(solve.hasCycle(head))

    print(result)

if __name__ == "__main__":
    main()