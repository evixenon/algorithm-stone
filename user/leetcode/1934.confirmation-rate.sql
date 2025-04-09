--
-- @lc app=leetcode id=1934 lang=mysql
--
-- [1934] Confirmation Rate
--

-- @lc code=start
# Write your MySQL query statement below
select s.user_id, round(avg(if(c.action='confirmed', 1.00, 0)),2) as confirmation_rate
from Signups s
left join Confirmations c on s.user_id = c.user_id
group by s.user_id

-- @lc code=end

