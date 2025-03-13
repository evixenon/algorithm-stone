#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, hold):
            # 第0天, 买 or 不卖
            if i < 0:
                return -inf if hold else 0
            if hold:  # 第i天结束时持有
                return max(dfs(i-1, True),  # 前面买,今天不动
                           dfs(i-2, False) - prices[i]) # 今天买入, 前一天不能是卖出
            else : # 第i天结束时未持有
                return max(dfs(i-1, False), # 不动
                           dfs(i-1, True) + prices[i]) # 今天卖出
        
        return dfs(len(prices)-1, False)

        
# @lc code=end

