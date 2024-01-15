# Write your MySQL query statement below
select 
    case
        when (select count(DISTINCT salary) from Employee) = 1 then NULL
        else (
            select max(salary) 
                from Employee 
                where salary < (select max(salary) from Employee)
        )
    end as SecondHighestSalary;
