#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0 or n ==1:
            return 1
        fib = [1, 1]
        n = n-1
        while n:
            fib.append(fib[-1] + fib[-2])
            n -= 1
        return fib[-1]
        
        
# @lc code=end

