#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 Part 1."""


def listDivide(numbers=list, divide=2):
    """This takes a list and returns how many items of the list are divisable
    by a number.

    Args:
        numbers (list): Arg to find what items in mubers are divisable by
        divide.
        divide (int): Arg to find items in numbers list that are divisable by
        itself.

    Returns:
        int: len of new list  from numbers that are divisable by divide.

    Examples:

        >>> listDivide([1, 2, 3, 4, 5])
        2

        >>> listDivide([30, 54, 63, 98, 100], divide=10)
        2

        >>> listDivide([1, 2, 3, 4, 5], 1)
        5
    """
    numdivide = []
    for num in numbers:
        if num % divide == 0:
            count = 0
            numdivide.append(num)
            count += 1
    return len(numdivide)


class ListDivideException(Exception):
    """This defines the custom exception ListDivideException."""
    pass


def testListDivide():
    """This test particular out comes of the listDivide function.

    Returns:
        Exception: if an answer to listDivide is wrong is raises
        ListDivideException + string explaining the error. If it dose not find
        an error it returns nothing.

    Examples:

        >>> testListDivide()
        >>>

        >>> testListDivide()
        Traceback (most recent call last):
        File "<pyshell#4>", line 1, in <module>
        testListDivide()
        File "/home/da12263683/IS211_Assignment1/assignment1_part1.py", line 61, in testListDivide
        raise ListDivideException('Wrong! should = 2!')
        ListDivideException: Wrong! should = 2!
    """
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException('Wrong! should = 2!')
    elif listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException('Wrong! should = 5!')
    elif listDivide([30, 54, 63, 98, 100], divide=10) != 2:
        raise ListDivideException('Wrong! should = 2!')
    elif listDivide([]) != 0:
        raise ListDivideException('Wrong! should = 0!')
    elif listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException('Wrong! should = 5!')
    else:
        pass

testListDivide()
