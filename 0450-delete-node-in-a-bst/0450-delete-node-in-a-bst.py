# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        def backtrack(node):
            if not node:
                return None
            if key<node.val:
                node.left = backtrack(node.left)
            elif key>node.val:
                node.right = backtrack(node.right)
            else:
                if node.left == None:
                    return node.right
                elif node.right == None:
                    return node.left
                else:
                    temp = node.left
                    temp2 = node.left
                    while temp.right:
                        temp = temp.right
                    temp.right = node.right
                    return temp2
            return node
        return backtrack(root)