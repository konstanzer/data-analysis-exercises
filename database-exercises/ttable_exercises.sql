use germain_1479;

create temporary table employees_with_departments
select length(concat(first_name, ' ',last_name)) full_name, dept_name
from employees.employees
	join employees.dept_emp d using(emp_no)
	join employees.departments using(dept_no)
where d.to_date > now();

#using global avg, should be by dept
use employees;
select dept_name, round((avg(salary) - (
					select avg(salary) from salaries)) / (
				 select std(salary) from salaries), 2) z
from salaries
	join dept_emp d using(emp_no)
	join departments using(dept_no)
where d.to_date > now()
group by dept_name
order by z desc;


#2
create temporary table centavos
select amount from sakila.payment;

alter table centavos modify column amount decimal(10,2);

update centavos
set amount = round(amount*100,0);

select floor(amount) from centavos;

drop table centavos;
drop table employees_with_departments;
