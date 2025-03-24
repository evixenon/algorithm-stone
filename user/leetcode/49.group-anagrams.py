#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            k = "".join(sorted(s))
            if k not in d:
                d[k] = [s]
            else:
                d[k].append(s)
        
        return list(d.values())
# @lc code=end

