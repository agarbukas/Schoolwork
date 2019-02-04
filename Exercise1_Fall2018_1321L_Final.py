#CS1321L Final Fall 2018
#Name:  Andy Garbukas
#Student ID Number: 000569062
#Date: 12/7/18
#Lab Instructor: Solomon Walker


#NOTE: Turn this file in with the others in D2L after you are finished with the final

#Here you will write the code to compare two equal-sized arrays
# and determine if they are equal. Please test at least three times,
# comparing non-equal and equal arrays at least once.

from array import *

size = int(input("enter a length for the arrays"))


array1 = array('i', [0] * size)
array2 = array('i', [0] * size)


for x in range(len(array1)):
    element = 0
    array1[x] = int(input("Enter a number for your array 1 element "))
    element += 1

for x in range(len(array2)):
    element = 0
    array2[x] = int(input("Enter a number for your array 2 element "))
    element += 1

if array1 == array2:
    print("\nYour arrays are a match!!")
    print("\nArray 1: ", array1)
    print("\nArray 2: ", array2)
else:
    print("\nYour arrays are not a match!")
    print("\nArray 1: ", array1)
    print("\nArray 2: ", array2)