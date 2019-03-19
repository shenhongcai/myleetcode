"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 15:26
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.left=None
        self.right=None


class Solution:

    def maxDepth(self, root):

        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth= self.maxDepth(root.right)
        return max(left_depth, right_depth)+1


    def maxDepth2(self,root):

        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, root.left))
                stack.append((current_depth+1, root.right))
        return depth

















