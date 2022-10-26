from pydataset import data
import pandas as pd
import numpy as np

np.random.seed(0)

#1. grades
"""
Copy the code from the lesson to create a dataframe full of student grades.
Create a column named passing_english that indicates whether each student has a passing grade in english.
Sort the english grades by the passing_english column. How are duplicates handled?
Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)
Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.
"""
students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']
# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})


df['passing_english'] = df['english'] > 65
df = df.sort_values(by=['passing_english','english'])
df['overall_grade'] = (df.english+df.math+df.reading) /3

"""
Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
How many rows and columns are there?
What are the data types of each column?
Summarize the dataframe with .info and .describe
Rename the cty column to city.
Rename the hwy column to highway.
Do any cars have better city mileage than highway mileage?
Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.
Which car (or cars) has the highest mileage difference?
Which compact class car has the lowest highway mileage? The best?
Create a column named average_mileage that is the mean of the city and highway mileage.
Which dodge car has the best average mileage? The worst?
"""
#2 MPG
# data('mpg', show_doc=True) # view the documentation for the dataset
mpg = data('mpg') # load the dataset and store it in a variable

#print(mpg.info()) #11 cols x 234 rows (obj, float, int)
mpg.rename(columns={'cty':'city', 'hwy':'highway'}, inplace=True)
#mpg['better_city_mileage'] = mpg.city > mpg.highway #No
mpg['mileage_diff'] = -mpg.city + mpg.highway
mpg['mileage_avg'] = (mpg.city + mpg.highway) /2
mpg.sort_values(by=['mileage_diff'], ascending=False, inplace=True) #Honda Civic, VW Beetle
#print(mpg.head())
#print(mpg[mpg['class']=='compact'].sort_values(by='highway')) #both VW Jetta: 2.8L V6, 1.9L I4
#print(mpg[mpg['manufacturer']=='dodge'].sort_values(by='mileage_avg')) #2008 Ram & Durango worst, 1999 Caravan best

"""
Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
How many rows and columns are there?
What are the data types?
Summarize the dataframe with .info and .describe
What is the the weight of the fastest animal?
What is the overal percentage of specials?
How many animals are hoppers that are above the median speed? What percentage is this?
"""

#3
mam = data('mammals')
#print(mam.info()) #2 float cols x 62 rows
print(mam.tail()) #no speed in this one!





