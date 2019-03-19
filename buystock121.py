"""   
@Project Name: LeetCode
@Author: Shen Hongcai
@Time: 2019-03-19, 14:51
@Python Version: python3.6
@Coding Scheme: utf-8
@Interpreter Name: PyCharm
"""
# 买卖股票的最佳时机，返回最大利润


class Solution:

    def buystock(self, prices):

        min_price = prices[0]
        maxprofit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            maxprofit = max(prices[i]-min_price, maxprofit)
        return maxprofit


test = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.buystock(test))









