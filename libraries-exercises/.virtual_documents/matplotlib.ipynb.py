import matplotlib.pyplot as plt
import numpy as np
import math


def f(x): return pow(x,2) - x + 2
x = np.linspace(0,10)

plt.plot(x, f(x))
plt.annotate('(0,0)',(0,0), xytext=(-.5,5));


def f1(x): return pow(x,.5)
def f2(x): return pow(x,3)
def f3(x): return pow(2,x)
def f4(x): return 1 / (x+1)

f, ax = plt.subplots(2,2, figsize=(9,5))

ax[0,0].plot(x, f1(x))
ax[1,0].plot(x, f2(x))
ax[0,1].plot(x, f3(x))
ax[1,1].plot(x, f4(x))

plt.show()


f, ax = plt.subplots(1,1, figsize=(9,5))

ax.plot(x, f1(x))
ax.plot(x, f2(x))
ax.plot(x, f3(x))
ax.plot(x, f4(x))

plt.ylim(0,10)
plt.xlim(0,5)

plt.title("graphology")
plt.xlabel("x")
plt.ylabel("y")

plt.legend(['y=sqrt(x)', 'y=x^3', 'y=2^x', 'y=1/(x+1)'])
plt.show()


fig, ax = plt.subplots(1,1, figsize=(16,9))

f = lambda x: 0*x + 1
ax.plot(x, f(x))

f = lambda x: np.log(x)
ax.plot(x, f(x))

f = lambda x: x
ax.plot(x, f(x))

f = lambda x: x * np.log(x)
ax.plot(x, f(x))

f = lambda x: pow(x,2)
ax.plot(x, f(x))

f = lambda x:  pow(2,x)
ax.plot(x, f(x))

f = lambda x: math.factorial(x//1) #type error
Y = [math.factorial(X//1) for X in x]
ax.plot(x, Y)

f = lambda x: pow(x,x)
ax.plot(x, f(x))

plt.ylim(0,100)
plt.xlim(0,10)
plt.title("Big-O Notation")
plt.xlabel("Elements")
plt.ylabel("Operations")
plt.legend(['O(1)', 'O(log n)', 'O(n)', 'O(n log n)',\
            'O(n^2)', 'O(2^n)', 'O(nget_ipython().getoutput(")', 'O(n^n)'])")
plt.show()



