# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = 1 + self.getHeight(root.left)
        rightHeight = 1 + self.getHeight(root.right)
        if abs(leftHeight - rightHeight) <= 1:
            return max(leftHeight, rightHeight)
        
        return -1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Understand: find if subtree height difference is more than 1
        Input: root node
        Output: bool
        Plan:
            - find height of left subtree
            - find height of right subtree
            - compare and check if diff is more than 1
                - if yes -> return false
                - else -> return true
        Base Case: if root is None
        """
        if not root:
            return True

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if leftHeight == -1:
            return False

        if rightHeight == -1:
            return False

        if abs(leftHeight - rightHeight) > 1:
            return False
        
        return True        
