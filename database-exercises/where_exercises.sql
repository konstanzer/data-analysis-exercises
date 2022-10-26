USE employees;

#709 rows
SELECT * FROM employees
	WHERE first_name in ('Vidya', 'Maya', 'Irena');

#709 rows
SELECT * FROM employees
	WHERE first_name = 'Vidya' OR first_name = 'Maya' OR first_name = 'Irena';

#0 rows
SELECT * FROM employees
	WHERE first_name in ('Vidya', 'Maya', 'Irena') AND gender = 'M';

#7,330 rows
SELECT * FROM employees
	WHERE last_name LIKE 'E%';

#30,723 rows - 7,330 = 23,393 that end e, start with not-e
#24,292 end with e
SELECT * FROM employees
	WHERE last_name LIKE '%E' OR last_name LIKE 'E%';

#899 rows
SELECT * FROM employees
	WHERE last_name LIKE 'E%E';

#135,214 rows
SELECT * FROM employees
	WHERE hire_date BETWEEN '1990-01-01' AND '1999-12-31';
	
#791 rows
SELECT * FROM employees
	WHERE birth_date LIKE '%12-24';

#381 rows
SELECT * FROM employees
	WHERE hire_date BETWEEN '1990-01-01' AND '1999-12-31'
	AND birth_date LIKE '%12-24';

#1,873 rows
SELECT * FROM employees
	WHERE last_name LIKE '%Q%';

#547 rows
SELECT * FROM employees
	WHERE last_name LIKE '%Q%'
	AND last_name NOT LIKE '%QU%';
