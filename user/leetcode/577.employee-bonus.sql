--
-- @lc app=leetcode id=577 lang=mysql
--
-- [577] Employee Bonus
--

-- @lc code=start
# Write your MySQL query statement below
select name, bonus 
from Employee e
left join Bonus b on e.empID = b.empID
where bonus is NULL or bonus < 1000

-- @lc code=end

