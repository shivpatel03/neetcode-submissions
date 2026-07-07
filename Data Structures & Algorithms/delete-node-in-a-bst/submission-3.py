# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # helper function to get the smallest value in the tree for replacement for later
    def findMinNode(self, root: TreeNode):
        current = root
        while current and current.left:
            current = current.left

        return current
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # if you are null, return None
        if not root: 
            return None

        # see if you are at the correct key to delete it
        if (key > root.val):
            # go right
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val):
            root.left = self.deleteNode(root.left, key)
        else:
            # you are the node, check if you have both children
            # if you have only one child, you can just return the other one
            if (not root.left): 
                return root.right
            elif (not root.right): 
                return root.left
            else: 
                # the third case - the node you are deleting has two children
                minimumNode = self.findMinNode(root.right)
                root.val = minimumNode.val
                root.right = self.deleteNode(root.right, minimumNode.val)

        return root