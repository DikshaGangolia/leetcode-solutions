select d.name AS Department,e.name AS Employee, e.salary AS Salary from Employee e
join Department d
on e.departmentId = d.id
where e.salary = (
    select MAX(salary)
    from Employee
    where departmentId = e.departmentId
);