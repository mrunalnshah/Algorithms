"""
Author: Mrunal Nirajkumar Shah
Date  : 31st March, 2026

LeetCode: 2. Add Two Numbers

Solution Description:
n is len(l1) and m is len(l2)
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tail = None

        carry = 0

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            val = val_1 + val_2 + carry
            carry = val // 10
            val = val % 10

            node = ListNode(val=val)

            if head is None:
                head = node
                tail = node
            else:
                tail.next = node
                tail = tail.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head

def main():
    # Test Case 1
    node113 = ListNode(val=3)
    node112 = ListNode(val=4, next=node113)
    node111 = ListNode(val=2, next=node112)

    node123 = ListNode(val=4)
    node122 = ListNode(val=6, next=node123)
    node121 = ListNode(val=5, next=node122)

    head11 = node111
    head12 = node121

    # Test Case 2
    node211 = ListNode(val=0)

    node221 = ListNode(val=0)

    head21 = node211
    head22 = node221

    # Test Case 3
    node317 = ListNode(val=9)
    node316 = ListNode(val=9,next=node317)
    node315 = ListNode(val=9,next=node316)
    node314 = ListNode(val=9,next=node315)
    node313 = ListNode(val=9,next=node314)
    node312 = ListNode(val=9, next=node313)
    node311 = ListNode(val=9, next=node312)

    node324 = ListNode(val=9)
    node323 = ListNode(val=9,next=node324)
    node322 = ListNode(val=9, next=node323)
    node321 = ListNode(val=9, next=node322)   

    head31 = node311
    head32 = node321

    heads = [
        (head11, head12),
        (head21, head22),
        (head31, head32)
    ]

    solve = Solution()

    results = []
    for head in heads:
        results.append(solve.addTwoNumbers(l1=head[0], l2= head[1]))

    
    for i, result in enumerate(results):
        print("Test Case", i)

        curNode = result
        while curNode:
            print(curNode.val)

            curNode = curNode.next      

if __name__ == "__main__":
    main()