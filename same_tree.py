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
