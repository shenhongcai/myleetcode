"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 18:59
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # 构造辅助函数，判断子树是否对称
        def helper(root, mirror):

            if not root and not mirror:   # 若左右子结点均为空，则返回True，也是递归的出口
                return True
            if root and mirror:          # 加判断，防止出现空指针
                if root.val == mirror.val:
                    return helper(root.left, mirror.right)\
                           and helper(root.right, mirror.left) # 递归
            return False

        return helper(root, root)













