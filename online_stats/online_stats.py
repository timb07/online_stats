# -*- coding: utf-8 -*-

from math import sqrt


class Statistics:
    """
    Compute variance and standard deviation "online", that is, without needing
    all the values to be stored.

    A Python implementation of Welford's method as described here:
    https://www.johndcook.com/blog/standard_deviation/
    """

    n = 0
    old_s = 0.0

    def __init__(self, initial=None):
        if initial:
            for x in initial:
                self.append(x)

    def append(self, x):
        self.n += 1
        if self.n == 1:
            self.old_m = x
            self.new_m = x
        else:
            self.new_m = self.old_m + (x - self.old_m) / self.n
            self.new_s = self.old_s + (x - self.old_m) * (x - self.new_m)
            self.old_m = self.new_m
            self.old_s = self.new_s

    def mean(self):
        if self.n == 0:
            raise ValueError('Mean is undefined')
        return self.new_m

    def variance(self):
        if self.n <= 1:
            raise ValueError('Variance is undefined')
        return self.new_s / (self.n - 1)

    def stdev(self):
        return sqrt(self.variance())
