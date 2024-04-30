# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 제일 깊숙한거를 먼저 찾아내니 dfs 쓰기
        ans = []
        def dfs(node):
            if node:
                dfs(node.left)
                ans.append(node.val)
                dfs(node.right)
        dfs(root)
        return ans

