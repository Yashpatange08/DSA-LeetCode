# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        def inoder(root):
            if not root:
                return
            inoder(root.left)
            res.append(root.val)
            inoder(root.right)
        inoder(root)
        return res