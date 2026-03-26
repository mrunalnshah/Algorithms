"""
Author: Mrunal Nirajkumar Shah
Date  : 26th March, 2026

LeetCode: 21. Merge Two Sorted List

Solution Description:
Time Complexity: O(n + m)  
Space Complexity: O(n + m)
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
        result = None

        while cur1 != None and cur2 != None:
            node = ListNode()
            if cur1.val < cur2.val:
                node.val = cur1.val
                cur1 = cur1.next
            else:
                node.val = cur2.val
                cur2 = cur2.next
            if result == None:
                result = node
                head = result
            else:
                result.next = node
                result = result.next

        while cur1 != None:
            node = ListNode()
            node.val = cur1.val

            result.next = node
            result = result.next

            cur1 = cur1.next

        while cur2 != None:
            node = ListNode()
            node.val = cur2.val

            result.next = node
            result = result.next

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