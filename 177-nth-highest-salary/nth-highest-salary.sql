create function getNthHighestSalary(N INT) returns int
begin
    return (
        select max(e1.salary) from Employee e1
        where (
            select count(distinct e2.salary) from Employee e2
            where e2.salary > e1.salary
        )=n-1
    );
end