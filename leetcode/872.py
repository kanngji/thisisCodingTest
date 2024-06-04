# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        return dfs(root1) == dfs(root2)
    
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def bfs(root):
            if not root:
                return []
            queue = deque([root])
            leaves = []
            while queue:
                node = queue.popleft()
                if not node.left and not node.right:  # 리프 노드인지 확인
                    leaves.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return leaves
        
        return bfs(root1) == bfs(root2)
