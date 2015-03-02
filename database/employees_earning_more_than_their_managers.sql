-- Since Mon Mar  2 18:14:08 CST 2015
SELECT Name AS Employee
FROM Employee AS e1
WHERE ManagerId IS NOT NULL AND Salary > (SELECT Salary
                                          FROM Employee
                                          WHERE Id = e1.ManagerId)
