# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        values = list(inorder(root))
        # 오른쪽 자식들만 만든다는 코드라는데...
        dummy = TreeNode(-1)
        current = dummy
        for val in values:
            current.right = TreeNode(val)
            current = current.right

        return dummy.right
            