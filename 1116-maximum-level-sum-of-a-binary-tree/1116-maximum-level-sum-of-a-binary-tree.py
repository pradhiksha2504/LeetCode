# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def findHeight(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            leftH = findHeight(node.left)
            rightH = findHeight(node.right)
            return 1 + max(leftH, rightH)
        
        def calculateSum(node: Optional[TreeNode], level: int, total: List[int]):
            if node is None:
                return
            if level >= len(total):
                total.append(0)
            total[level] += node.val
            calculateSum(node.left, level + 1, total)
            calculateSum(node.right, level + 1, total)
        
        height = findHeight(root)
        total = [0] * height
        calculateSum(root, 0, total)
        
        # Find the level with the maximum sum
        max_sum = max(total)
        max_level = total.index(max_sum) + 1  # Convert to 1-based index
        
        return max_level