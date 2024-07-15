# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        seen = set()
        return self.dfs(root,k,seen)

    def dfs(self, node,k,seen):
        if not node:
            return False
        if k - node.val in seen:
            return True
        
        seen.add(node.val)
        return self.dfs(node.left,k,seen) or self.dfs(node.right,k,seen)