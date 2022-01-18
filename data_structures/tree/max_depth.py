'''
    Leetcode - Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            # if one of the subtree is None, you should return the depth of another subtree.
            # if all of the subtree is not None, you should return the minimum depth of the two subtrees
            if root.left is None:
                return self.maxDepth(root.right) + 1
            elif root.right is None:
                return self.maxDepth(root.left) + 1
            else:
                return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
