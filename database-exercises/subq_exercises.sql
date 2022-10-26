use employees;

#1 by 101010 hire date
select emp_no, last_name from employees
where hire_date = (
		select hire_date from employees
		where emp_no = '101010');

	
#2 is there an A-A-mod? no subquery needed
#subquery only makes sense to me when you have to run a query in order to run the query

select distinct(title) from employees
	join titles t using(emp_no)
	join dept_emp de using(emp_no)
where first_name = 'Aamod' AND de.to_date > current_date;


#3. 300,024 peons - 240,124 working now = 59,900 dead peons
select count(*) - (select count(emp_no) from employees
						join dept_emp using(emp_no)
							where emp_no in (select emp_no from employees
												where to_date > current_date)) ghosts
from employees;


#4, bonus1 four women managers, alas, no subquery
select dept_name, last_name, gender from dept_manager
	join employees using(emp_no)
	join departments using(dept_no)
where to_date > current_date AND gender = 'F';


#5 above average payday
select emp_no, last_name, salary from employees
	join salaries using(emp_no)
where to_date > current_date
	and salary > (select avg(salary) from salaries) #historical average
order by salary;


###6:  count(x) > max-sigma = 83
select count(salary) top
from salaries where to_date > current_date
	and salary > (select max(salary) - std(salary)
						from salaries where to_date > current_date);
#0.03% of all
select (select count(salary)
			from salaries where to_date > current_date
				and salary > (select max(salary) - std(salary)
									from salaries where to_date > current_date)) /
						 					(select count(salary) from salaries
						 				where to_date > current_date) centile;
####


#B2-3 Find the dept. & name of the employee with the highest salary.
select dept_name, last_name, first_name, salary from employees
	join salaries s using(emp_no)
	join dept_emp using(emp_no)
	join departments using(dept_no)
where s.to_date > current_date
order by salary desc
limit 3;


