#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/binary-tree-inorder-traversal/

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

Since Apr-10-2014
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if not root:
            return []
        else:
            return (self.inorderTraversal(root.left) + [root.val] +
                    self.inorderTraversal(root.right))


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    print(s.inorderTraversal(n1))

    # tree 2: https://en.wikipedia.org/wiki/Tree_traversal
    for i in 'ABCDEFGHI':
        locals()['n%c' % i.lower()] = TreeNode(i)
    nf.left = nb
    nf.right = ng
    nb.left = na
    nb.right = nd
    nd.left = nc
    nd.right = ne
    ng.right = ni
    ni.left = nh
    print(s.inorderTraversal(nf))
