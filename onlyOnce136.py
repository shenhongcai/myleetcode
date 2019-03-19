"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 19:25
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in nums:
            k ^= i          # 按位异或。位相同，结果为0；位不同，结果为1
            print(k)
        return k


sol=Solution()
test=[1, 1, 2, 2, 5, 7, 7]
sol.singleNumber(test)










