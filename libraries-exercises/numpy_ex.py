import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
#questions lol
print(a)
print("pos/neg")
print(4)
print(5)
print(3)
print(10)

print('moments')
print(np.mean(pow(a,2)))
print(np.std(pow(a,2)))

print('centering')
print(np.mean(a))
print(a-np.mean(a))
print(np.mean(a-np.mean(a)))

print("z-scores")
def Z(x): return((x-np.mean(x))/np.std(x))
print(Z(a))


#MOAR
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum_a = np.sum(a)
mean_a = np.mean(a)
max_a = np.max(a)
min_a = np.min(a)
prod_a = np.prod(a)
sq_a = pow(a,2)
evens_a = a[a%2==0]

b = np.array([[3, 4, 5], [6, 7, 8]])
sum_b = np.sum(b)
mean_b = np.mean(b)
max_b = np.max(b)
min_b = np.min(b)
prod_b = np.prod(b)
sq_b = pow(b,2)
evens_b = b[b%2==0]
odds_b = b[b%2==1]
print(b.shape)
b = b.T
b = np.ravel(b)
b = b.reshape(6,1)

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
std_c = np.std(c)
var_c = np.var(c)
print(c.shape)
c=c.T
dot_c = c@c
print(np.sum(c * c.T))
print(np.prod(c * c.T))

d = np.array([[90, 30, 45, 0, 120, 180],
			[45, -90, -30, 270, 90, 0],
			[60, 45, -45, 90, -45, 180]])

sin_d = np.sin(d)
cos_d = np.cos(d)
tan_d = np.tan(d)
neg_d = d[d<0]
pos_d = d[d>0]
#arrays are "unhashable"
unique_d = set(list(np.ravel(d)))
print(len(unique_d))
print(d.shape)
d = d.T
d = d.reshape(9,2)


