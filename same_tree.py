#!/usr/bin/env python3

"""
http://oj.leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and
the nodes have the same value.

Wed Apr  9 16:40:26 CST 2014
"""
# Definition for a binary tree node


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q
        elif p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))

    def isSameTree1(self, p, q):
        """ A version from an interviewee, too long but right.
        """
        if p is None or q is None:
            if p is None and q is None:
                return True
            else:
                return False
        else:
            if p.left and q.left:
                l = self.isSameTree1(p.left, q.left)
            elif p.left is None and q.left is None:
                l = True
            else:
                l = False

            if p.right and q.right:
                r = self.isSameTree1(p.right, q.right)
            elif p.right is None and q.right is None:
                r = True
            else:
                r = False

            if not (l and r):
                return False
            elif p.val == q.val:
                return True
            else:
                return False


if __name__ == '__main__':
    # These test cases guarantee a 100% coverage.
    s = Solution()

    p = q = None
    assert s.isSameTree(p, q)
    assert s.isSameTree1(p, q)

    p = None
    q = TreeNode(1)
    assert not s.isSameTree(p, q)
    assert not s.isSameTree1(p, q)

    p = TreeNode(1)
    q = None
    assert not s.isSameTree(p, q)
    assert not s.isSameTree1(p, q)

    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(1)
    n5 = TreeNode(2)
    n6 = TreeNode(3)
    n4.left = n5
    n4.right = n6
    p = n1
    q = n4
    assert s.isSameTree(p, q)
    assert s.isSameTree1(p, q)

    p = n1
    q = n2
    assert not s.isSameTree(p, q)
    assert not s.isSameTree1(p, q)

    p = n1
    n7 = TreeNode(4)
    n8 = TreeNode(5)
    n9 = TreeNode(6)
    n7.left = n8
    n7.right = n9
    q = n7
    assert not s.isSameTree(p, q)
    assert not s.isSameTree1(p, q)
