# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 왼쪽 트리 오른쪽 트리 없을때 출력 
        # 먼저 왼쪽 트리
        # 다음 오른쪽 트리
        def postorder(node , res):
            if not node:
                return
            postorder(node.left,res)
            postorder(node.right,res)
            res.append(node.val)
        result = []
        postorder(root,result)
        return result
