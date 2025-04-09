--
-- @lc app=leetcode id=1661 lang=mysql
--
-- [1661] Average Time of Process per Machine
--

-- @lc code=start
# Write your MySQL query statement below
select a.machine_id, ROUND(AVG(b.timestamp - a.timestamp),3) as processing_time
from Activity a
CROSS JOIN Activity b  
Where a.machine_id = b.machine_id 
AND a.process_id = b.process_id
AND a.activity_type = "start"
AND b.activity_type = "end"

GROUP BY machine_id

-- @lc code=end

