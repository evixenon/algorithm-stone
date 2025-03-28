# @before-stub-for-debug-begin
from python3problem4 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # i: a 组中, 下标为 i 的数(及其前)在中位数前
        # 二分最大的 i, 满足 a_i​ ≤ b_{j+1}​. 
        # 二分结束后，我们有 a_i ​≤ b_{j+1} ​且 a_{i+1} > b_j。
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n ,m
        
        # 开区间
        # 循环不变量：a[left] <= b[j+1]
        # 循环不变量：a[right] > b[j+1]
        left, right = -1, m
        while left + 1 < right: # 区间不为空
            i = (left + right) // 2
            j = (m + n + 1) // 2 - 2 - i
            if nums1[i] <= nums2[j+1]: # 说明要找的 i 在 现在的i 或更右
                left = i
            else:
                right = i
        
        i = left
        j = (m + n + 1) // 2 - 2 - i
        ai = nums1[i] if i >= 0 else -inf
        bj = nums2[j] if j >= 0 else -inf
        ai1 = nums1[i+1] if i+1 < m else inf
        bj1 = nums2[j+1] if j+1 < n else inf
        if (m+n) % 2: # odd
            return max(ai, bj)
        else:
            return (max(ai,bj) + min(ai1,bj1)) / 2 

# @lc code=end

