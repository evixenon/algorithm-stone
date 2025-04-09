--
-- @lc app=leetcode id=1280 lang=mysql
--
-- [1280] Students and Examinations
--

-- @lc code=start
# Write your MySQL query statement below
select s.student_id, student_name, su.subject_name, COUNT(e.subject_name) as attended_exams
-- select *
from Students s
CROSS JOIN Subjects su
left join Examinations e 
    on s.student_id = e.student_id
    and su.subject_name = e.subject_name
group by s.student_id, su.subject_name
order by s.student_id, su.subject_name


-- @lc code=end

