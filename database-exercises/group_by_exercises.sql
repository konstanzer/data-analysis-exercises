use employees;

select count(distinct(title)) 'titles' from titles;
#3
SELECT last_name, COUNT(last_name)
FROM employees
WHERE last_name LIKE 'e%e'
GROUP BY last_name;
#4
SELECT first_name, last_name, COUNT(last_name) 'count'
FROM employees
WHERE last_name LIKE 'e%e'
GROUP BY first_name, last_name
ORDER BY count DESC;
#5-6 chleq, lindqvist, qiwen
SELECT last_name, COUNT(last_name)
FROM employees
WHERE last_name LIKE '%Q%' AND last_name NOT LIKE '%QU%'
GROUP BY last_name;
#7
SELECT first_name, gender, COUNT(first_name) 'count'
FROM employees
WHERE first_name IN  ('Irena', 'Vidya', 'Maya')
GROUP BY first_name, gender
ORDER BY count DESC;

#8: 285872
SELECT DISTINCT(lower(concat(substr(first_name, 1, 1), substr(last_name, 1, 4),
		'_', substr(birth_date, 6, 2), substr(birth_date, 3, 2)))) 'username',
		COUNT('username') 'total'
FROM employees
GROUP BY username
ORDER BY total DESC;

#B: 300024 - 285872 = 14152 duplicates
SELECT COUNT(*) - COUNT(DISTINCT(lower(concat(substr(first_name, 1, 1), substr(last_name, 1, 4),
		'_', substr(birth_date, 6, 2), substr(birth_date, 3, 2))))) 'dupes' FROM employees;
		

