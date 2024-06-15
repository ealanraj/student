#LAMBDA 

sq = lambda x : x**2
sq(2)

cube = lambda y : y**3
cube(2)

add = lambda x,y : x+y

#Global variable 
#local variable

a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

print("end")

#Map Filter Reduce
#Syntax: 
#    map (function, iterable/sequence)
#    filter (function, iterable/sequence)
# from functools import reduce
#    Reduce (function, iterable/sequence)

l = [1,2,3,4]

sq = lambda x : x**2
print(list(map(sq, l)))

evenOdd = lambda x : x%2==0
print(list(filter(evenOdd, l)))

from functools import reduce
add = lambda x,y : x+y
print((reduce(add,l)))
