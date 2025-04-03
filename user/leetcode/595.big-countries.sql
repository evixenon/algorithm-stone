--
-- @lc app=leetcode id=595 lang=mysql
--
-- [595] Big Countries
--

-- @lc code=start
# Write your MySQL query statement below
select name, population, area from World where population >= 25000000 or area >= 3000000
-- @lc code=end

