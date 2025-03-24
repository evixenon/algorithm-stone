# @before-stub-for-debug-begin
from python3problem279 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start

# 写在外面，多个测试数据之间可以共享，减少计算量
@cache
# i: 现在排除到的数 未平方
def dfs(i, rest):
    if i==0: # 没有数了
        return inf if rest else 0
    if rest < i*i: # 超出了
        return dfs(i-1, rest) # 只能不选
    else:
        return min(dfs(i-1, rest), dfs(i, rest - i*i) + 1) # 不选, 选

class Solution:
    def numSquares(self, n: int) -> int:
            
        # isqrt(x) = int(sqrt(x))
        ans = dfs(isqrt(n), n)
        return ans
        
# @lc code=end

