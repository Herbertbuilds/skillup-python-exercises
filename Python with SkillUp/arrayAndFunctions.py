from array import *

arr = array ('i', [1, 2, 3, 4, 5])

for pnt in range(4):
    print(pnt, arr[pnt])

arr.append(6)
print(arr)


def welcome():
    print("Welcome to the array and functions module!")

welcome()

def add(a, b):
    sum = a + b
    return sum

result = add(3, 5)   
print("The sum is {}".format(result)) 