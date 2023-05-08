# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        
        if not root:
            return root
        
        def dfs(root):
            if root:
                temp = root.left
                root.left = root.right 
                root.right = temp 
            if root and root.left:
                dfs(root.left)
            if root and root.right:
                dfs(root.right)
        
        dfs(root)
        
        return root
        