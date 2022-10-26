use employees;
#1
select last_name, d.dept_name, salary-dept_mean diff
from employees
join salaries s using(emp_no)
join dept_manager dm using(emp_no)
join departments d using(dept_no)
join (select dept_no, avg(salary) dept_mean
			from salaries
				join dept_emp using(emp_no)
			where salaries.to_date > current_date
			group by dept_no) mean_sal using(dept_no)
where s.to_date > current_date and dm.to_date > current_date
order by diff;

use world;
#2
select language, percentage from countrylanguage
join city using(countrycode)
where name = 'Santa Monica';
#3
select count(name), region from country
group by region;
#4
select sum(population), region from country
group by region;
#5
select sum(population), continent from country
group by continent;

#6 --should be weighted by population!
select sum(population * lifeexpectancy /
						(select sum(population) from country))
from country;

#7
select avg(lifeexpectancy) life, continent from country
group by continent
order by life;

#bOnUs
select name, localname from country
where localname != name;

select name, lifeexpectancy
from country
where lifeexpectancy < 40;

select district, country.name, region from country
join city on city.countrycode = country.code
where city.name = 'Dallas';

#note this is country, not city, life expectancy
select city.name, lifeexpectancy
from country
join city on city.countrycode = country.code
where city.name = 'Cary';

#BoNuS sAkIlA
use sakila;

select first_name, phone, title from customer
join address using(address_id)
join rental using(customer_id)
join inventory using(inventory_id)
join film using(film_id)
where return_date is null;

