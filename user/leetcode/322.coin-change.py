#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        # coins.sort(reversed=True)
        n = amount+1
        dp = [11111] * n # 因为amout 的最大值是 10^4
        dp[0] = 0
        for c in coins:
            for i in range(c, n):
                dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] != 11111 else -1

        
# @lc code=end

