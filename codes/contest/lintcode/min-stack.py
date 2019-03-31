#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class MinStack:
    def __init__(self):
        # do intialization if necessary
        self.values = []
        self.mins = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.values.append(number)
        if not self.mins or self.mins[-1] >= number:
            self.mins.append(number)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        value = self.values[-1]
        self.values.pop()
        if value == self.mins[-1]:
            self.mins.pop()
        return value

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        return self.mins[-1]
