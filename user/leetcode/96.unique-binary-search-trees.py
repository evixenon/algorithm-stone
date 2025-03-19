# @before-stub-for-debug-begin
from python3problem96 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # # 递归会超时?
        # if n == 1 or n == 0:
        #     return 1
        # # 以 i 为根节点时, 左子树有 i-1 个节点, 右子树有 n-i 个节点
        # num = 0
        # for i in range(1, n+1):
        #     num += self.numTrees(i-1) * self.numTrees(n-i)
        # return num
        if n == 1 or n == 0:
            return 1
        dp = [1,1]
        # 有 j 个点
        for j in range(2, n+1):
            # # 以 i 为根节点时, 左子树有 i-1 个节点, 右子树有 n-i 个节点
            num = 0
            for i in range(1, j+1):
                num += dp[i-1] * dp[j-i]
            dp.append(num)
        return dp[n]

            
# @lc code=end

