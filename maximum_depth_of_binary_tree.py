#! /usr/bin/env python3

"""

Tue Apr  8 16:53:27 CST 2014
"""
# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and not root.right:
            return self.maxDepth(root.left) + 1
        elif not root.left and root.right:
            return self.maxDepth(root.right) + 1
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1 


if __name__ == '__main__':
    s = Solution()
    # XXX: tests are not complete.
    # tree 1
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n4.right = n5
    print(s.maxDepth(n1))
    # tree 2
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.left = n3
    print(s.maxDepth(n1))
