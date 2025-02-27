#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] 
        for i in range(1, n+1):
            # x 中 1的数量 = x//2 中 1的数量 + 奇1偶0
            ans.append(ans[i>>1] + (i&1))
        return ans
    
        
            
# @lc code=end

