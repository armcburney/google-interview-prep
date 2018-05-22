#!/usr/bin/python3

"""
plus_one.py

@author: Andrew Robert McBurney
@info:   Cracking the Coding Interview question.
"""


def plus_one(digits):
    remainder = 0
    size = len(digits) - 1

    if digits[size] is 9:
        remainder = 1

    digits[size] = (digits[size] + 1) % 10

    if remainder is 1:
        for i in range(size - 1, -1, -1):
            digits[i] = (digits[i] + remainder) % 10

            if remainder is 1 and digits[i] is not 0:
                remainder = 0

        if remainder is 1:
            return [1] + digits

    return digits
