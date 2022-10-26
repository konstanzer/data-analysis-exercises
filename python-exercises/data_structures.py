#THE JUICE ISN'T WORTH THE SQUEEZE
"""
How many students are there?
How many students prefer light coffee? For each type of coffee roast?
How many types of each pet are there?
How many grades does each student have? Do they all have the same number of grades?
What is each student's grade average?
How many pets does each student have?
How many students are in web development? data science?
What is the average number of pets for students in web development?
What is the average pet age for students in data science?
What is most frequent coffee preference for data science students?
What is the least frequent coffee preference for web development students?
What is the average grade for students with at least 2 pets?
How many students have 3 pets?
What is the average grade for students with 0 pets?
What is the average grade for web development students? data science students?
What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
What is the average number of pets for medium coffee drinkers?
What is the most common type of pet for web development students?
What is the average name length?
What is the highest pet age for light coffee drinkers?
"""

from students import students
import numpy as np

student_count = 0
coffee_preference = dict(light=0, medium=0, dark=0)
pets_data = dict()
student_grades = dict()
student_pets = dict()

for student in students:


    student_count += 1
    student_grades[student['student']] = [len(student['grades']),
                                            np.mean(student['grades'])]

    if student['coffee_preference'] == 'light':
        coffee_preference['light'] += 1
    if student['coffee_preference'] == 'medium':
        coffee_preference['medium'] += 1
    if student['coffee_preference'] == 'dark':
        coffee_preference['dark'] += 1


    pets = student['pets']
    for pet in pets:
        
        species = pet['species']
        age = pet['age']

        if species in student_pets:
            student_pets[species] += 1
        else:
            student_pets[species] = 1



if __name__ == "__main__":

    from pprint import pprint
    
    #print(pprint(students))

    print("\nVARIABLES")
    all_vars = dir()
    for v in all_vars:
        if not v.startswith("__") and not v=="students":
            print(v, eval(v))







