#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        @cache
        def dfs(i, j):
            if i < 0:
                return j+1 # 删除所有
            if j < 0:
                return i+1
            if word1[i] == word2[j]:
                # 相同消除
                return dfs(i-1, j-1)
            # 插入, 删除, 替换
            return min(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1)) +1

        return dfs(m-1, n-1)
# @lc code=end

