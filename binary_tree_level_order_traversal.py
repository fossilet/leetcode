#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/binary-tree-level-order-traversal/

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Since Apr-10-2014 18:36
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        res = []
        if not root:
            return []
        else:
            cur_level_nodes = [root]
            res.append([node.val for node in cur_level_nodes])
            while True:
                next_level_nodes = []
                for node in cur_level_nodes:
                    if node.left:
                        next_level_nodes.append(node.left)
                    if node.right:
                        next_level_nodes.append(node.right)
                if not next_level_nodes:
                    break
                res.append([node.val for node in next_level_nodes])
                cur_level_nodes = next_level_nodes
        return res


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
    print(s.levelOrder(n1))
    print(s.levelOrder(None))
