class Solution:
    # Helper Function to find min node in a tree
    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root.val   

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Edge Case
        if not root:
            return None
        
        # Main Logic
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # We found the node to remove
            # Check if no child, single child or both children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            valToReplace = self.findMin(root.right)
            root.val = valToReplace
            root.right = self.deleteNode(root.right, valToReplace)
        return root