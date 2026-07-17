# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case, if there is no node here, return 0
        if not root: 
            return 0
        
        # for every node, check the maximum of the left and right subtrees
        # + 1 because the node you are currently on counts as 1 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
