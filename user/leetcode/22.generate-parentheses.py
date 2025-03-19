#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = n # 目前可用的左括号
        right = 0 # 目前可用的右括号
        ans = []
        def dfs(s, left, right):
            if not left and not right:
                ans.append(s)
                return

            if not left:
                dfs(s+")", left, right-1)
            elif not right:
                dfs(s+"(", left-1, right+1)
            else:
                dfs(s+"(", left-1, right+1)
                dfs(s+")", left, right-1)
        dfs("", n, 0)
        return ans
# @lc code=end

