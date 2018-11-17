# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        _list = []
        results = []

        _list.append(root)

        while len(_list) != 0:
            node = _list[-1]

            if node.left is not None:
                _list.append(node.left)
            else:
                results.append(node.val)
                _list.pop()
                if node.right is not None:
                    _list.append(node.right)

        return results


