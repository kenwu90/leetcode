# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        Given a binary tree, return all root-to-leaf paths.
           1
         /   \
        2     3
         \
          5

        Output: ["1->2->5", "1->3"]
        :type root: TreeNode
        :rtype: List[str]
        """

        if root:
            paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
            if len(paths) == 0:
                return [str(root.val)]
            else:
                return [str(root.val) + '->'+ path for path in paths]
        else:
            return []
