class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        node = root
        stack = [root]

        in_idx = 0
        pre_idx = 1

        while in_idx < len(inorder) and pre_idx < len(preorder):

            new_node = TreeNode(preorder[pre_idx])
            add_right = False
            print(in_idx, pre_idx)
            while stack and in_idx < len(inorder) and inorder[in_idx] == stack[-1].val:
                print('aaaaaa', in_idx, pre_idx)
                in_idx += 1
                node = stack.pop()
                add_right = True

            if add_right:
                node.right = new_node
            else:
                node.left = new_node
            node = new_node
            stack.append(new_node)
            pre_idx += 1

        return root


if __name__ == '__main__':
    s = Solution()
    s.buildTree([3,9,20,15,7], [9,3,15,20,7])