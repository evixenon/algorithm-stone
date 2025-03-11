#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)
        left = 0
        for right, c in enumerate(s):
            # 往右一步
            cnt[c] -= 1
            while cnt[c] < 0: # 太多, 左标移到下一个本字符
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)
        return ans

# @lc code=end

