# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if node is None:
                return 0
            leftTree = height(node.left)
            rightTree = height(node.right)
            self.ans = max(self.ans, leftTree + rightTree)
            return 1 + max(leftTree, rightTree)
        if root is None:
            return 0
        self.ans= 0
        h = height(root)
        return self.ans