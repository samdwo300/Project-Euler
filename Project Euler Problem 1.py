# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:46:59 2019

@author: Samuel
"""

############# Problem 1 #############

# If we list all the natural numbers below 10 that are multiples of 3 or 5, 

# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.






## First Attempt ###

def multiples_three_and_five_below_n(n):
    counter = 1
    x = []
    y= []
    while 5*counter < n or 3*counter < n:
        if 5*counter < n:
            x.append(5*counter)
        if 3*counter < n:
            x.append(3*counter)
        for i in x:
            if i not in y:
                y.append(i)     
        counter += 1
    return sum(y)
        
        


multiples_three_and_five_below_n(5000)


#Note: The above works but is slow

# Better method

# Use for loop and check each item in the range to see if is mutliple of 3 or 5 
# Create a list then sum


sum([x for x in range(10000) if x % 3== 0 or x % 5== 0])
