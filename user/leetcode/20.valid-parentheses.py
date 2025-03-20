#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "[": "]", "{": "}"}
        st = []
        for c in s:
            if c in mapping:
               st.append(mapping[c]) 
            else:
                if not st or c != st.pop():
                    return False
        return True if not st else False
                
        
# @lc code=end

