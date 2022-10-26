import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data

'''
iris = sns.load_dataset('iris')

# 1. to 6.9 length range
print(iris.describe())

#saves plot locally, use open command to view
#petal divides well
sns.relplot(x='petal_length', y='petal_width', hue='species',
	data=iris).savefig('petal.png')
#sepal can't divide versicolor and virginica
sns.relplot(x='sepal_length', y='sepal_width', hue='species',
	data=iris).savefig('sepal.png')

Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
Plot the x and y values from the anscombe data. Each dataset should be in a separate column. ?? plots have columns ??
Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.
Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:
Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)
Does whether or not a province is Catholic influence fertility?
What measure correlates most strongly with fertility?
Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.
Load the sleepstudy data and read it's documentation. Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.
'''

ansc = sns.load_dataset('anscombe')
#same means & variances for x and y, diffent ranges
print(ansc.groupby('dataset').agg(['mean','var','max','median','min']).T)
sns.relplot(x='x', y='y', hue='dataset', kind='line',
	data=ansc).savefig('anscombe.png')

bug = data('InsectSprays') #, show_doc=True)
print(bug.head())
plt.title("Bug Lethality")
sns.boxplot(data=bug, x='spray', y='count').figure.savefig('spray.png')
plt.clf() #clear figure

swiss = data('swiss')
print(swiss.head())
plt.title("Where are all the Catholics?")
sns.histplot(swiss.Catholic).figure.savefig("catholics.png")
swiss["is_catholic"] = swiss.Catholic > 50
plt.title("Catholics Don't Use Condoms")
sns.boxplot(data=swiss, x="is_catholic", y="Fertility").figure.savefig('catholicbabies.png')
sns.pairplot(swiss, hue="is_catholic").savefig("fertility.png")
print(swiss.corr().Fertility)

plt.clf()
plt.figure(figsize=(16,9))
sleep = data('sleepstudy')
sleep['Subject'] = 'Subject_' + sleep.Subject.astype(str)
sns.lineplot(data=sleep, x='Days', y='Reaction', hue='Subject')
sns.lineplot(data=sleep, x='Days', y='Reaction',
	color='black', estimator='mean').figure.savefig('sleep.png')












