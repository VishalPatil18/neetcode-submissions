# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Helper Function to find min node in a tree
    def findMin(self, root):
        while root and root.left:
            root = root.left
        return root.val   

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Understand: Step 1: Search for the node to remove
                    Step 2: Remove the node found
        Input: root, key (val of the node to remove)
        Output: root of new tree
        Edge Case: 
            - Empty Tree
            - Single Node Tree
        Plan:
            - Iterate over the tree starting from the root to find the node to delete
            - while loop with curr not None:
                - if curr.val > key: move towards left subtree
                - if curr.val < key: move towards right subtree
                - if curr.val == key: we found the node to remove
                    - check if left of curr is None: return right of it in 
                    recursive call of remove
                    - check if right of curr is None: return left of it in
                    recursive call of remove
                    - if it has both children nodes:
                        - find the min node in the subtree and replace the val of node to be
                        deleted with that min val and remove the in val by making a recursive
                        call to that val now 
        """
        # Edge Case
        if not root:
            return None
        if not root.right and not root.left:
            if root.val == key:
                return None
            else:
                return root 

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
            
            valToReplace = self.findMin(root)
            root.val = valToReplace
            root.left = self.deleteNode(root.left, valToReplace)
        return root