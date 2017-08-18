# -*- coding:utf8 -*-
"""
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
FIRST_VALUE = 3
SECOND_VALUE = 5
MAX_VALUE = 1000

# 첫번째 방법
mul_of_3 = set(range(FIRST_VALUE, MAX_VALUE, FIRST_VALUE))
mul_of_5 = set(range(SECOND_VALUE, MAX_VALUE, SECOND_VALUE))

union = mul_of_3.union(mul_of_5)
total = 0
for value in union:
    total += value

print(total)

# 두번째 방법
total = [x for x in range(MAX_VALUE) if (x % FIRST_VALUE == 0) or (x % SECOND_VALUE == 0)]
print(sum(total))
