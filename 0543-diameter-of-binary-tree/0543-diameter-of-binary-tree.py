# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node, ans):
            if node is None:
                return 0
            leftTree = height(node.left, ans)
            rightTree = height(node.right, ans)
            ans[0] = max(ans[0], leftTree + rightTree)
            return 1 + max(leftTree, rightTree)
        if root is None:
            return 0
        ans = [-99999999999]
        h = height(root, ans)
        return ans[0]