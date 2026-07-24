# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root: 
                return 0

            # you are going to find the:
            # max diameter on the left side
            # and then max diameter on the right side

            # however, what do you do at every node?
            # you should find the max between res and left_max + right_max
            left_max = dfs(root.left)
            right_max = dfs(root.right)
            res = max(res, left_max + right_max)

            return 1 + max(left_max, right_max)

        dfs(root)
        return res