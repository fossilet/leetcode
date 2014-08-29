#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Since Apr-11-2014 15:53
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates0(self, head):
        if not head:
            return None
        elif not head.next:  # Only one
            return head
        else:
            cur_head = head
            res_head = head
            res_pointer = res_head
            while True:
                if cur_head.next.val == cur_head.val:
                    cur_head = cur_head.next
                    continue
                else:
                    res_pointer.next = cur_head.next
                    # res_pointer = res_head
                if not cur_head.next:
                    break
            return res_head

    def deleteDuplicates(self, head):
        p1 = head
        new_head = ListNode(head.val)  # Copy
        p2 = new_head

        while p1.next:
            if p1.val != p1.next.val:
                pass


if __name__ == '__main__':
    s = Solution()
    # n1 = ListNode(1)
    # n2 = ListNode(1)
    # n3 = ListNode(2)
    # n1.next = n2
    # n2.next = n3
    # res = s.deleteDuplicates(n1)
    # print(res.val)
    # print(res.next.val)
    #
    # n1 = ListNode(1)
    # n2 = ListNode(2)
    # n3 = ListNode(2)
    # n1.next = n2
    # n2.next = n3
    # res = s.deleteDuplicates(n1)
    # print(res.val)
    # print(res.next.val)

    n1 = ListNode(1)
    n2 = ListNode(1)
    n1.next = n2
    res = s.deleteDuplicates(n1)
    print(res.val)
    print(res.next.val)
