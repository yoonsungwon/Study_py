# -*- coding:utf8 -*-
"""
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import exceptions
import itertools

ran = lambda stop: iter(itertools.count().next, stop)
VALUE = 600851475143

for val in ran(600851475143):
    try:
        if VALUE % val == 0:
            result = val
    except ZeroDivisionError:
        continue

print result
