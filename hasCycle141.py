"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 17:55
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""


class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        """
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False



















