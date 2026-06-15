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
        
        height = 1
        height += max(self.getHeight(root.left), self.getHeight(root.right))
        return height
        
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
        if abs(leftHeight - rightHeight) > 1:
            return False
        return True        
