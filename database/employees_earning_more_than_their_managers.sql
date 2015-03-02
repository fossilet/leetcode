-- Since Mon Mar  2 18:14:08 CST 2015
select Name as Employee from Employee as e1 where ManagerId is not NULL and Salary > (select Salary from Employee where Id = e1.ManagerId) 
