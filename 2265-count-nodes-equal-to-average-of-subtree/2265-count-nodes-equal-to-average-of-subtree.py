# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = [0]
        def backtrack(node):
            if not node:
                return [0,0]
            left,cl = backtrack(node.left)
            right,cr = backtrack(node.right)
            sumi = left+right+node.val
            avg = sumi//(cl+cr+1)
            if avg == node.val:
                count[0] += 1
            return [sumi,cl+cr+1]
        backtrack(root)
        return count[0]

        