"""
Author: Mrunal Nirajkumar Shah
Date  : 26th March, 2026

LeetCode: 21. Merge Two Sorted List

[PYTHONIC]
Solution Description:
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        cur1 = list1
        cur2 = list2

        head = None
        tail = None

        while cur1 is not None and cur2 is not None:
            if cur1.val < cur2.val:
                if head is None:
                    head = cur1
                    tail = head
                else:
                    tail.next = cur1
                    tail = tail.next
                cur1 = cur1.next
            else:
                if head is None:
                    head = cur2
                    tail = head
                else:
                    tail.next = cur2
                    tail = tail.next

                cur2 = cur2.next
            
        while cur1 is not None:
            tail.next = cur1
            tail = tail.next

            cur1 = cur1.next

        while cur2 is not None:
            tail.next = cur2
            tail = tail.next

            cur2 = cur2.next

        return head


def main():
    # Test Case 1
    node13 = ListNode(val=4)
    node12 = ListNode(val=2, next=node13)
    node11 = ListNode(val=1, next=node12)

    node23 = ListNode(val=4)
    node22 = ListNode(val=3, next=node23)
    node21 = ListNode(val=1, next=node22)

    head1 = node11
    head2 = node21

    # Test Case 2
    head_21 = None
    head_22 = None

    # Test Case 3
    node_31 = ListNode(val=0)

    head_31 = None
    head_32 = node_31

    # TEST
    test_case = [
        (head1, head2),
        (head_21, head_22),
        (head_31, head_32)
    ]

    solve = Solution()

    results = []
    for case in test_case:
        results.append(solve.mergeTwoLists(list1=case[0], list2=case[1]))

    for i, result in enumerate(results):
        currNode: ListNode = result
        
        print("TESTCASE", i)
        while currNode != None:
            print(currNode.val)

            currNode = currNode.next
        
    
if __name__ == "__main__":
    main()