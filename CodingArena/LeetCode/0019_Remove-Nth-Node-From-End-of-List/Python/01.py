"""
Author: Mrunal Nirajkumar Shah
Date  : 28th March, 2026

LeetCode: 19. Remove Nth Node From End of List

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        curNode = head
        while curNode:
            count += 1

            curNode = curNode.next


        if n == count:
            return head.next

        curNode = head
        counter = 0
        while counter != (count - n - 1):
            counter += 1

            curNode = curNode.next
        
        curNode.next = curNode.next.next
        
        return head


def main():
    # Test Case 1
    node15 = ListNode(val=5)
    node14 = ListNode(val=4, next=node15)
    node13 = ListNode(val=3, next=node14)
    node12 = ListNode(val=2, next=node13)
    node11 = ListNode(val=1, next=node12)
    head1 = node11
    n1 = 2

    # Test Case 2
    node21 = ListNode(val=1)
    head2 = node21
    n2 = 1

    # Test Case 3
    node32 = ListNode(val=2)
    node31 = ListNode(val=1, next=node32)
    head3 = node31
    n3 = 1

    testcases = [
        (head1, n1),
        (head2, n2),
        (head3, n3)
    ]

    solve = Solution()

    results = []
    for testcase in testcases:
        results.append(solve.removeNthFromEnd(head=testcase[0], n=testcase[1]))

    for i, result in enumerate(results):
        print("TEST CASE", i)
        
        curNode: ListNode = result
        while curNode:
            print(curNode.val)

            curNode = curNode.next

if __name__ == "__main__":
    main()