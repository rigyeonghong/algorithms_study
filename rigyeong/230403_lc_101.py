# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def diff(a, b):
            if a == None and b == None:
                return True
            elif  a == None or b == None:
                return False
            else:
                return a.val ==  b.val and diff(a.left, b.right) and diff(a.right, b.left)

        return diff(root.left, root.right)
            