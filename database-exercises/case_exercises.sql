use employees;

# current mean salary by dept. group: R&D, S&M, P&Q, F&H
Select case when dept_name in ('research', 'development') then 'R&D'
					when dept_name in ('sales', 'marketing') then 'Sales & Marketing' 
					when dept_name in ('Production', 'Quality Management') then 'Prod & QM'
				 when dept_name in ('Finance', 'Human Resources') then 'Finance & HR'
					else dept_name
			End as division,
			round(avg(salary), 0) mean_salary

From salaries s
	join dept_emp de using(emp_no)
	join departments using(dept_no)
	
Where de.to_date > current_date and s.to_date > current_date

Group by division;







SELECT last_name, first_name,
		CASE last_name
			WHEN last_name NOT BETWEEN 'A' AND 'I' THEN 'A-H'
			WHEN last_name NOT BETWEEN 'I' AND 'R' THEN 'I-Q'
			ELSE 'R-Z'
			END AS alpha_group
FROM employees
ORDER BY last_name;

