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
        # first, check if you are null
        if not root:
            return None
        
        # then check if you are the target value
        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val):
            root.left = self.deleteNode(root.left, key)
        # if you ARE the value, then do the replacement
        # if there are two child nodes, just make the other node the result
        else:
            if (not root.left):
                return root.right
            elif (not root.right):
                return root.left
            else:
                # find the minimum value in the tree
                minimum = self.findMinNode(root.right)
                root.val = minimum.val
                # delete that minimum value
                root.right = self.deleteNode(root.right, minimum.val)
        return root

