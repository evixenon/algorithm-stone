#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        cnt = Counter()
        left = 0
        ans = 0
        for right, c in enumerate(s):
            cnt[c] = cnt.get(c, 0) + 1
            while cnt.get(c, 0) > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
        
# @lc code=end

