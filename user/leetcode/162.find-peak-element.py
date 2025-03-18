#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        这题可以用二分的原理是:
        - 首先, 数组外是 -inf, 连续两个数不相同, 这两点都可以利用
        - m < m+1, 说明 m 右边一定有一个更高点
        - m > m+1, 说明 m+1 左边一定有一个更高点

        那么可以开始红蓝染色
        - 红色: 右边必有峰顶
        - 蓝色: 当前位置或左边必有峰顶
        """

        if len(nums) == 1: return 0

        #  左闭右开
        l = 0
        r = len(nums)-1 #
        
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[m+1]: 
                l = m+1
            else: # 不存在相等
                r = m
        return l
        
# @lc code=end

