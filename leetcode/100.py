# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 두 트리의 루트 노드가 모두 None 이면 동일하다고 판단
        if not p and not q:
            return True
        # 두 투리 중 하나의 루트 노드만 None인 경우 동일하지 않다고 판단
        if not p or not q:
            return False
        # 두 트리의 루트 노드의 값이 다르면 동일하지 않다고 판단
        if p.val != q.val:
            return False
        # 왼쪽 서브트리와 오른쪽 서브트리를 재귀적으로 비교a
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    

# self. 트리