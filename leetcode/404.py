# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        if root is None:
            return 0
        
        left_sum = 0

        if root.left and isLeaf(root.left):
            left_sum = root.left.val
        
        return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# 알고리즘
# 현재 노드가 null이면 0을 반환합니다.
# 현재 노드의 왼쪽 자식이 잎사귀 노드인 경우, 그 값을 저장하고 오른쪽 서브트리에서 왼쪽 잎사귀 노드의 합을 계산합니다.
# 그렇지 않은 경우, 왼쪽과 오른쪽 서브트리에서 각각 왼쪽 잎사귀 노드의 합을 계산합니다.
# 이 합을 반환합니다.
