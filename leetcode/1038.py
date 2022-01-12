# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root):

        self.cur_sum = 0

        def dfs(node):
            if node == None:
                return
            dfs(node.right)
            self.cur_sum += node.val
            node.val = self.cur_sum
            dfs(node.left)

        dfs(root)

        return root
