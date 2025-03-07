#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        n = x^y
        while n:
            cnt += 1&n
            n >>= 1
        return cnt
        # return (x ^ y).bit_count()
        
# @lc code=end

