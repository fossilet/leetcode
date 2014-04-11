#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/

Since Apr-10-2014 18:33
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        cur_level_nodes = [root]
        while True:
            next_level_nodes = []
            for i in range(len(cur_level_nodes)):
                if i == 0:
                    if len(cur_level_nodes) == 1:  # root
                        cur_level_nodes[i].next = None
                    else:
                        cur_level_nodes[i].next = cur_level_nodes[i + 1]
                elif i == len(cur_level_nodes) - 1:
                    cur_level_nodes[i].next = None
                else:
                    cur_level_nodes[i].next = cur_level_nodes[i + 1]
            for node in cur_level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            if not next_level_nodes:
                break
            cur_level_nodes = next_level_nodes


if __name__ == '__main__':
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    s.connect(n1)
    locals = locals().copy()
    for i in range(1, 8):
        next = locals['n%s' % i].next
        print(next) if next is None else print(next.val)
