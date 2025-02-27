#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for price in prices:
            if price - min_price > ans:
                ans = price - min_price
            if price < min_price:
                min_price = price
        return ans
# @lc code=end

