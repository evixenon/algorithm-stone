--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below
SELECT today.id
FROM Weather today
CROSS JOIN Weather yesterday
WHERE datediff(yesterday.recordDate, today.recordDate) = -1
AND yesterday.temperature < today.temperature

-- @lc code=end

