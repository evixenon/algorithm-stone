#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        n = len(people)
        i = 0
        while i < n:
            if people[i][1] != i:
                people.insert(people[i][1], people[i])
                people.pop(i+1)
            i += 1
        return people
# @lc code=end

