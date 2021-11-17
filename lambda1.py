# clear the screen
import os
# the return value of this is a function
def clear(): return os.system("cls")


clear()
# so if you type "cls" in the terminal, it will now clear the terminal screen

# 5 divided by 2 has a remainder of 1 (traditional way):


def remainder(num):
    return num % 2


#
#
print(remainder(5))

# lambda function way


def remainder(num): return num % 2


print(type(remainder))  # shows lambda is a function
print(remainder(5))

# x times y function w lambda


def product(x, y): return x*y


print(product(2, 3))

# create two functions out of this.
# we have an argument and our multiplier
# this creates the function then plug it in
#


def myfunction(num):
    return lambda x: x*num


result10 = myfunction(10)  # plugged it in
# result10 type is a function
# the 10 in myfunction(10) represents num
print(result10)  # it is missing an argument
print(result10(9))  # this gives an argument of 9

#
#
#
#


def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(2)  # represents n
mytripler = myfunc(3)  # represents n as well

print(mydoubler(11))  # this is a
print(mytripler(11))  # this is a


# make a list
numbers = [2, 4, 6, 8, 10, 3, 18, 14, 21]

# create a filtered list of all numbers > 7
# give a function, interable
# lsit() makes a new list
filtered_list = list(filter(lambda num: (num > 7), numbers))
print(filtered_list)

# applies a function to every element in the list
# shows 0 and 1 becuase it is the left over of the %
mapped_list = list(map(lambda num: num % 2, numbers))
print(mapped_list)

# assigns 5 to a


def x(a): return a + 10


print(x(5))

# assigns 5,6,7 in order of a,b,c then executes


def x(a, b, c): return a + b + c


print(x(5, 6, 7))

# traditional way


def addition(n):
    return n + n


numbers = [1, 2, 3, 4]
result = map(addition, numbers)
print(list(result))

# new way
numbers = [1, 2, 3, 4]
result = map(lambda n: n + n, numbers)
print(list(result))
