# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Understand: Insert a node into a BST
        Input: root, val (val of node to insert)
        Output: root of BST
        Edge Case: if root is null -> create new node and return it as root
        Plan:
            - Iterate with a while loop from root node  
            - For the current node check if:
                - val > curr.val and curr.right is not null:
                    - if curr.right is null: insert new node towards curr.right
                    - if curr.right is not null: move towards right node
                - val < curr.val and curr.left is not null: 
                    - if curr.left is null: insert new node towards curr.left
                    - if curr.left is not null: move towards left node
            - Exit from the while loop once the node is inserted
        """
        # Edge Case
        if not root:
            return TreeNode(val, None, None)
        
        # Variables
        curr = root

        # Main Logic
        while curr:
            if val > curr.val and curr.right:
                curr = curr.right
            elif val > curr.val and not curr.right:
                curr.right = TreeNode(val, None, None)
                return root
            elif val < curr.val and curr.left:
                curr = curr.left
            elif val < curr.val and not curr.left:
                curr.left = TreeNode(val, None, None)
                return root
                