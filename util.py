import math
import matplotlib.py plot as plt
import numpy as np


def average_sample(data):
    summary = 0
    n = len(data)
    for i in range(n):
        summary += data[i]

    return summary / n


def standard_deviation(data):
    average = average_sample(data)

    n = len(data)
    summary2 = 0
    for i in range(n):
        summary2 += (data[i] - average) ** 2

    return summary2 / n
