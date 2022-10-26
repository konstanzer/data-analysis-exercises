USE employees;

#Irena Reutenauer to Vidya Simmen
SELECT * FROM employees
	WHERE first_name in ('Vidya', 'Maya', 'Irena')
	ORDER BY first_name;

#Irena Acton to Vidya Zweizig
SELECT * FROM employees
	WHERE first_name in ('Vidya', 'Maya', 'Irena')
	ORDER BY first_name, last_name;

#Irena Acton to Maya Zyda
SELECT * FROM employees
	WHERE first_name in ('Vidya', 'Maya', 'Irena')
	ORDER BY last_name, first_name;
	
#899 rows: 10021 Ramzi Erde to 499648 Tadahiro Erde
SELECT * FROM employees
	WHERE last_name LIKE 'E%E'
	ORDER BY emp_no;

#899 rows: Sergi Erde to Teiji Eldridge
SELECT * FROM employees
	WHERE last_name LIKE 'E%E'
	ORDER BY hire_date;	

#381 rows: Kyoichi Mawatari to Magy Feinberg
SELECT * FROM employees
	WHERE hire_date BETWEEN '1990-01-01' AND '1999-12-31'
	AND birth_date LIKE '%12-24'
	ORDER BY hire_date;
