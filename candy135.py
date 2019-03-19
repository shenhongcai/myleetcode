"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 19:41
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""

class Solution:

    def candy(self, arr):

        n = len(arr)
        dp = [1 for i in range(n)]
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                dp[i] = dp[i-1]+1
        print("第一次遍历结果:", dp)
        for j in range(0,n-1)[::-1]:
            if arr[j] > arr[j+1]:
                dp[j] = dp[j+1]+1
        print("第二次遍历结果:", dp)
        return sum(dp)


test=[1,-4,2,4,4]
sol=Solution()
print("至少需要%d块糖果" % sol.candy(test))
"""
第一次遍历结果: [1, 1, 2, 3, 1]
第二次遍历结果: [2, 1, 2, 3, 1]
至少需要9块糖果

"""













