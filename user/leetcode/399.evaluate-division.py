# @before-stub-for-debug-begin
from python3problem399 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
# from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(x, target, prod, vst):
            if x == target: return prod
            found = 0
            for y, r in g[x]:
                if y in vst: continue
                vst.add(y)
                found = dfs(y, target, prod*r, vst)
                if found : return found
            return 0
                    
        # g = defaultdict(list)
        g = {}
        # 先建图, g[x] = [(y, r=x/y) ... ]
        for (x, y), r in zip(equations, values):
            if x not in g: g[x] = []
            if y not in g: g[y] = []
            g[x].append((y, r))
            g[y].append((x, 1/r))
            
        ans = []
        for x, target in queries:
            if x not in g or target not in g:
                ans.append(-1.)
            else:
                tmp = dfs(x, target, 1, set())
                ans.append(tmp if tmp else -1)
        return ans
        
# @lc code=end

