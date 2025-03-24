#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 这题的特别在于可以重复选取
        # 那么需要在dfs中避免选到重复的组合
        # 限制从大到小选?
        comb = []
        candidates = sorted(candidates, reverse=True)
        
        def dfs(selected, rest, cand):
            if not cand:
                return
            if rest == 0:
                comb.append(selected)
            elif rest < 0: # 超了 
                return
            else: # 没到, 继续
                k = cand[-1]
                dfs(selected+[k], rest-k, cand)  # 选k
                dfs(selected, rest, cand[:-1]) # 不选k
        
        dfs([], target, candidates)
        return comb
# @lc code=end

