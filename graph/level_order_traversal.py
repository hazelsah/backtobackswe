class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # Points to another TreeNode object
        self.right = None


class Solution:
    def levelOrderTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: list of list of int
        '''
        queue = []
        sol = []

        queue.append(root)

        while len(queue) > 0:
            current_layer = []
            layer_size = len(queue)
            for i in range(0, layer_size):
                current_node = queue.pop(0)

                current_layer.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)
            sol.append(current_layer)
        return sol


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    s = Solution()
    print(s.levelOrderTraversal(root))
