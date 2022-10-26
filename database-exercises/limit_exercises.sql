USE employees;

#Aamodt, Acton, Adachi, ...
SELECT DISTINCT last_name FROM employees
	ORDER BY last_name
	LIMIT 10;
	
#Mawatari, Denti, Panienski, ...
SELECT * FROM employees
	WHERE hire_date BETWEEN '1990-01-01' AND '1999-12-31'
	AND birth_date LIKE '%12-24'
	ORDER BY hire_date
	LIMIT 5;
	
#Sury, Schmittgen, Kading, ...
SELECT * FROM employees
	WHERE hire_date BETWEEN '1990-01-01' AND '1999-12-31'
	AND birth_date LIKE '%12-24'
	ORDER BY hire_date
	LIMIT 5
	OFFSET 45;
	
