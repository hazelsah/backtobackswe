class Solution:
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None  # Points to another TreeNode object
            self.right = None  # Points to another TreeNode object

    def isSymmetric(self, root):
        '''
        :type root: TreeNode
        :rtype: bool
        '''
        return self.check(root)

    def check(self, root):
        if root is None:
            return True
        return self.check_helper(root.left, root.right)

    def check_helper(self, sub_left, sub_right):
        if (sub_left is None) and (sub_right is None):
            return True
        if (sub_left is not None) and (sub_right is not None):
            return (sub_left.val == sub_right.val and self.check_helper(sub_left.right,
                                                                        sub_right.left) \
                    and self.check_helper(sub_left.left, sub_right.right))

        return False


if __name__ == '__main__':
    s = Solution()
    t = s.TreeNode(2)
    t.left = s.TreeNode(1)
    t.right = s.TreeNode(1)
    print(s.isSymmetric(t))
