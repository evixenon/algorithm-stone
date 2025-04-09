--
-- @lc app=leetcode id=570 lang=mysql
--
-- [570] Managers with at Least 5 Direct Reports
--

-- @lc code=start
# Write your MySQL query statement below
select m.name as name
from Employee m
inner join Employee e on m.id = e.managerID
group by m.id
having count(e.id) >= 5

-- @lc code=end

