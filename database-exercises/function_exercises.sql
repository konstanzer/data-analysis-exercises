use employees;

#2-3
select upper(concat(first_name,' ',last_name)) 'full_name' from employees
where last_name like 'e%e';
#4
select *, datediff(current_date, hire_date) 'days' from employees
where hire_date between '1990-01-01' and '1999-12-31'
and birth_date like '%12-25'
order by hire_date;
#5
select max(salary), min(salary) from salaries;
#6
select *, lower(concat(substr(first_name, 1, 1), substr(last_name, 1, 4),
				'_', substr(birth_date, 6, 2), substr(birth_date, 3, 2)))
				'username' from employees limit 10;