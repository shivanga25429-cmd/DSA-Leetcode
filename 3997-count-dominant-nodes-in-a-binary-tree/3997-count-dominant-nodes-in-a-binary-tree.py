# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.count = 0
        def backtrack(node):
            if not node:
                return -1
            maxi = max(backtrack(node.left),backtrack(node.right))
            if node.val>=maxi:
                self.count += 1
                maxi = node.val
            return maxi
        backtrack(root)
        return self.count
            
        