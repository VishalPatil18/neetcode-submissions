# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Input: root node
        Output: list of inorder traversal
        Plan:
            - Traverse recursively
            - first go to left node
            - process curr node
            - go to right node
        Edge Case:
            - Do this until curr node is null, in this case just return
        """
        ioT = []
        if not root:
            return ioT
        
        ioT.extend(self.inorderTraversal(root.left))
        ioT.append(root.val)
        ioT.extend(self.inorderTraversal(root.right))

        return ioT