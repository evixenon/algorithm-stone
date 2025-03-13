# @before-stub-for-debug-begin
from python3problem347 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        arr = [[x, cnt[x]] for x in cnt]

        # 快排升序, 舍弃 k 之后的不排
        def qs(arr,k):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr)//2]
            less = [x for x in arr if x[1] < pivot[1]]
            greater = [x for x in arr if x[1] > pivot[1]]
            eq = [x for x in arr if x[1] == pivot[1]]
            if len(greater) < k:
                less = qs(less, k)
            greater = qs(greater, k)
            return greater + eq + less
        arr = qs(arr, k)
        
        ans = []
        for i in range(k):
            ans.append(arr[i][0])
        return ans

        
# @lc code=end

