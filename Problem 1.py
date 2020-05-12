# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:49:02 2020
Project Euler: Problem 1
@author: samdw
"""
import numpy as np
import  pandas as pd
import matplotlib as plt
import random as rd

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000

# Test for number below 10
cum_sum = sum([i for i in range(0,10) if i%3 == 0 or i%5 == 0 ])

# Solution to problem 1: 233168
cum_sum = sum([i for i in range(0,1000) if i%3 == 0 or i%5 == 0 ])


