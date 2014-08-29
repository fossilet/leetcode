#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

Since Apr-10-2014 16:05
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head.next is not head:  # single circular list
            return False
        else:
            return self.hasCycle(head.next)


if __name__ == '__main__':
    s = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    print(s.hasCycle(n1))

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n1
    print(s.hasCycle(n1))
