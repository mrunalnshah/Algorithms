"""
Author: Mrunal Nirajkumar Shah
Date  : 25th March, 2026

LeetCode: 206. Reverse Linked List

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head

        prevNode = None
        nextNode = None
        while curNode != None:
            nextNode = curNode.next

            curNode.next = prevNode
            prevNode = curNode

            curNode = nextNode
        
        head = prevNode

        return head

def main():
    # TestCase 1
    node5 = ListNode(val=5)
    node4 = ListNode(val=4, next=node5)
    node3 = ListNode(val=3, next=node4)
    node2 = ListNode(val=2, next=node3)
    node1 = ListNode(val=1, next=node2)
    head = node1

    # TestCase 2
    nodet2 = ListNode(val=2)
    nodet1 = ListNode(val=1, next= nodet2)
    head2 = nodet1

    # TestCase 3
    nodex1 = None
    head3 = nodex1

    solve = Solution()

    result = []
    
    heads = [head, head2, head3]
    for head in heads:
        result.append(solve.reverseList(head=head))

    for i, head in enumerate(result):
        print("TestCase", i)
        while head != None:
            print("Value", head.val)
            head = head.next

if __name__ == "__main__":
    main()
