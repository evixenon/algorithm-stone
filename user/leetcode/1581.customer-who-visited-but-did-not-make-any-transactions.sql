--
-- @lc app=leetcode id=1581 lang=mysql
--
-- [1581] Customer Who Visited but Did Not Make Any Transactions
--

-- @lc code=start
# Write your MySQL query statement below
select customer_id, COUNT(v.visit_id) as count_no_trans
from Visits v
left join Transactions t on v.visit_id = t.visit_id
where transaction_id is NULL
group by customer_id

-- @lc code=end

