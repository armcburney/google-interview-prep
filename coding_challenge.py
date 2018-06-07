"""
@author: Andrew Robert McBurney
@info:   Google Interview Challenge - Question 1
"""

import itertools
import functools

def solution(total_money, total_damage, costs, damages):
    n = len(costs)

    # O(n^2): Fill up the remaining table values
    for i in range(n):
        tuples = functools.reduce(
            list.__add__,
            list(itertools.combinations(costs, n))
        )

    print(tuples)

    for arr in tuples:
        print(arr)
        damage_array = [damages[index] for index in arr]
        costs_array =  [costs[index]   for index in arr]

        if sum(damage_array) >= total_damage and sum(costs_array) < total_money:
            return True

    return False
