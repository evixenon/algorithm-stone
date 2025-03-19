#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ans = []
        n = len(digits)
        def dfs(s, i):
            if i == n: 
                ans.append(s)
                return
            
            for c in MAPPING[int(digits[i])]:
                dfs(s+c, i+1)
                
        dfs("", 0)
        return ans
        
# @lc code=end

