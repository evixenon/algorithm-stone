# @before-stub-for-debug-begin
from python3problem207 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        
        # 建立入度表和邻接表
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
            
        # 将入度0的节点入队
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        
        # bfs 拓扑排序
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        
        return not numCourses
        
# @lc code=end

