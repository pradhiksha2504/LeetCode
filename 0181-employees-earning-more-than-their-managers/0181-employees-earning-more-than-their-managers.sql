# Write your MySQL query statement below
select e.name as employee  from employee e where salary > (select salary from employee  where id = e.managerid);