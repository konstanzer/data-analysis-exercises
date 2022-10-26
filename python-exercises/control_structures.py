import argparse

# requires two arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "day_one",
    help="indicate whether the word provided is Monday",
    type=str)
parser.add_argument(
    "day_two",
    help="indicate whether the word provided is in a weekend",
    type=str)
args = parser.parse_args()

weekend = ["saturday", "sunday"]

print("is Monday" if args.day_one.lower() == "monday"
                    else "is not Monday")
print("is weekend" if args.day_two.lower() in weekend
                    else "is not weekend")


hours_worked = 1
hourly_wage = 3.45
weekly_pay = hourly_wage*hours_worked
if hours_worked > 40: weekly_pay += .5*hourly_wage*(hours_worked-40)
print("$" + str(weekly_pay))


i=5
while i <= 15:
    print(i)
    i+=1
i=0
while i <= 100:
    print(i)
    i+=2
i=100
while i >= -10:
    print(i)
    i-=5
i=2
while i <= 10**6:
    print(i)
    i**=2
i=100
while i >= 5:
    print(i)
    i-=5


try:
    x = int(input("Number, please: "))
    for y in range(1,11):
        print(f"{x} x {y} = {x*y}")
except:
    print("Not a number.")


for z in range(1,10):
    print(z*str(z))


x = input("An odd number below 50, please: ")
while not x.isdigit() or int(x)%2 != 1 or int(x)>50:
    x = input("An odd number below 50, please: ")

print("I made your number disappear")
for n in range(1,50,2):
    if n == int(x): continue
    else: print(n)


x = input("A positive integer, please: ")
while not x.isdigit() or int(x)<0:
    x = input("A positive integer, please: ")
for n in range(0, int(x)+1): print(n)
print("And reversed...")
for n in range(int(x), 0, -1): print(n)


###fizzbuzz
for x in range(1,101):
    if x%3==0:
        if x%5==0:
            print('fizzbuzz')
        else:
            print('fizz')
    if x%5==0:
        print('buzz')
    else:
        print(x)


x = int(input("I demand a positive integer: "))
for i in range(1, x+1):
    print("n: " + str(i) + " | square: " +\
             str(i**2) + " | cube: " + str(i**3))


x = int(input("A GRADE UP TO 100: "))
g = dict(B=80, A=88, C=67, D=60)
grade = 'F'

for k,v in g.items():
    if x >= v:
        if k < grade:
            grade = k
print(grade)


