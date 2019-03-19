"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 09:16
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""


class Solution:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        index = 0  # 设置游标
        for i in range(1, len(nums)):
            while nums[index] != nums[i]:
                index += 1   # 每当当前元素与后一个元素不同，游标值+1
                nums[index] = nums[i]
        return index+1


sol = Solution()
print(sol.removeDuplicates([1, 1, 2, 3, 4]))


