# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi = float("-inf")
        def backtrack(root):
            if not root:
                return 0
            lh = max(0,backtrack(root.left))
            rh = max(0,backtrack(root.right))
            self.maxi = max(self.maxi,lh+rh+root.val)
            return root.val + max(lh,rh)
        backtrack(root)
        return self.maxi
