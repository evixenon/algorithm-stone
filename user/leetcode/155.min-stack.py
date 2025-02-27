#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.st = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_val or val <= self.min_val[-1]:
            self.min_val.append(val)

    def pop(self) -> None:
        if self.min_val[-1] == self.st.pop():
            self.min_val.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

