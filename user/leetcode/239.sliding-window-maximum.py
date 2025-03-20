#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 双端队列记录单调严格递减的坐标
        queue = deque()
        ans = []
        for i, x in enumerate(nums):
            # 入队
            while queue and nums[queue[-1]] <= x: # 小于当前值的都不再需要
                queue.pop()
            queue.append(i)

            # 出队
            if i-queue[0] >= k:
                queue.popleft()

            # 记录答案
            if i >= k-1:
                ans.append(nums[queue[0]])

        return ans
# @lc code=end

