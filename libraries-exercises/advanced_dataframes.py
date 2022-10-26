import pandas as password
from pydataset import data
import numpy as np
import pandas as pd

from env import host, username, password

"""
Run python -m pip install mysqlclient pymysql from your terminal to install pymysql and the mysqlclient.
Create a notebook or python script named advanced_dataframes to do your work in for these exercises.
Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url connection string formatted like in the example at the start of this lesson.
Use your function to obtain a connection to the employees database.
Once you have successfully run a query:
a. Intentionally make a typo in the database url. What kind of error message do you see?
b. Intentionally make an error in your SQL query. What does the error message look like?
Read the employees and titles tables into two separate DataFrames.
How many rows and columns do you have in each DataFrame? Is that what you expected?
Display the summary statistics for each DataFrame.
How many unique titles are in the titles DataFrame?
What is the oldest date in the to_date column?
What is the most recent date in the to_date column?
"""

def get_db_url(username, host, password, db):
    # a typo produced 'NoSuchModuleError: Can't load plugin'
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'

"""
Copy the users and roles DataFrames from the examples above.
What is the result of using a right join on the DataFrames
What is the result of using an outer join on the DataFrames?
What happens if you drop the foreign keys from the DataFrames and try to merge them?
Load the mpg dataset from PyDataset.
Output and read the documentation for the mpg dataset.
How many rows and columns are in the dataset? last assignment
Check out your column names and perform any cleanup you may want on them.
Display the summary statistics for the dataset.
How many different manufacturers are there?
How many different models are there?
Create a column named mileage_difference like you did in the DataFrames exercises; this column should contain the difference between highway and city mileage for each car.
Create a column named average_mileage like you did in the DataFrames exercises; this is the mean of the city and highway mileage.
Create a new column on the mpg dataset named is_automatic that holds boolean values denoting whether the car has an automatic transmission.
Using the mpg dataset, find out which which manufacturer has the best miles per gallon on average?
Do automatic or manual cars have better miles per gallon?
"""
# Create the users DataFrame.
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
# Create the roles DataFrame
roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})

#right join won't work
#print(pd.concat([users, roles], axis=0, join='outer'))

mpg = data('mpg')
mpg['mileage_diff'] = -mpg.cty + mpg.hwy
mpg['mileage_avg'] = (mpg.cty + mpg.hwy) /2
mpg['automatic'] = mpg.trans.str.startswith("auto")

"""
Use your get_db_url function to help you explore the data from the chipotle database.
What is the total price for each order?
What are the most popular 3 items?
Which item has produced the most revenue?
Using the titles DataFrame, visualize the number of employees with each title.

Join the employees and titles DataFrames together.
Visualize how frequently employees change titles. ??
For each title, find the hire date of the employee that was hired most recently with that title.
Create a cross tabulation of the number of titles by department. (Hint: this will involve a combination of SQL code.) ??
"""

query = """
        SELECT title, max(from_date) most_recent_hire
        FROM employees
        JOIN titles USING(emp_no)
        GROUP BY title;
        """

query2 = """
        SELECT title, dept_name
        FROM employees
        JOIN titles USING(emp_no)
        JOIN dept_emp USING(emp_no)
        JOIN departments USING(dept_no);
        """

if __name__ == '__main__':
    
    url = get_db_url(username, host, password, 'employees')

    # a typo produced: 'ProgrammingError: "Table doesn't exist"'
    #emps = pd.read_sql('SELECT * FROM employees', url)
    #tits = pd.read_sql('SELECT * FROM titles', url)
    
    #print(tits.info()) # 443,308 x 4
    #print(emps.info()) # 300,024 x 6 #dunno, guess it's right
    
    #print(len(set(tits.title))) #7
    # 1985-03-01 to 9999-01-01
    #print(np.min(tits.to_date))
    #print(np.max(tits.to_date))
    #df = emps.merge(tits, on='emp_no', how='left')


    df = pd.read_sql(query, url)
    print(df)
    df = pd.read_sql(query2, url)
    print(pd.crosstab(df.title, df.dept_name))

    print(len(mpg.model.unique()), len(mpg.manufacturer.unique())) #38 + 15
    print(mpg[mpg.automatic==True].mileage_avg.mean(),
        mpg[mpg.automatic==False].mileage_avg.mean())
    #manual 22, auto 19 mpg
    #Honda wins, 28.5 mpg
    print(mpg.groupby('manufacturer').mean().\
        sort_values(by='mileage_avg', ascending=False).head())

    url = get_db_url(username, host, password, 'chipotle')
    orders = pd.read_sql('SELECT * FROM orders', url)
    orders.item_price = orders.item_price.str.strip('$').astype(float)
    orders['total'] = orders.quantity*orders.item_price
    print(orders.info())
    popular = orders[['item_name','quantity']].groupby('item_name').agg('sum')
    #Pollo y mas
    print(popular.sort_values(by='quantity', ascending=False).head())
    #order totals
    print(orders[['order_id','total']].groupby('order_id').agg('sum'))
    #top grossing items
    print(orders[['item_name','total']].groupby('item_name').agg('sum').\
        sort_values(by='total', ascending=False).head())

