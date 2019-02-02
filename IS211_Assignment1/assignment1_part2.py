#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 1 Part 2."""


class Book(object):
    """Docstring.

    Attributes:
        author (str): An empty string.
        title (str): An empty string.

    """
    author = ''
    title = ''

    def __init__(self, author, title):
        """This is the constructor for the Book class.

        Args:
            author (str): Name of an author of a book.
            title (str): Title of a book.

        """
        self.author = author
        self.title = title

    def display(self):
        """Takes in author and title and places it into a string.

        Returns:
            str: title and author concatonated into a string.
            'title, writen by author'

        Examples:

            >>> B1 = Book('John Steinbeck', 'Of Mice and Men')
            >>> B1.display()
            Of Mice and Men, written by John Steinbeck

            >>> B2 = Book('Harper Lee', 'To Kill a Mockingbird')
            >>> B2.display()
            To Kill a Mockingbird, written by Harper Lee
        """
        return '{}, written by {}'.format(self.title, self.author)


B1 = Book('John Steinbeck', 'Of Mice and Men')
B2 = Book('Harper Lee', 'To Kill a Mockingbird')
print B1.display()
print B2.display()
