#!/usr/bin/env python

import math
import random

def in_area(x, y):
    x = float(x)
    y = float(y)
    if x < 5.0 or x >= 20:
        return False
    elif x >= 5 and x < 10:
        y_max = 5 - math.sqrt(25 - math.pow(x - 5, 2))
        return y < y_max
    elif x >= 10 and x < 20 and y < 5:
        y_max = 5 - math.sqrt(25 - math.pow(x - 15, 2))
        return y < y_max
    elif x >= 10 and x < 20 and y >= 5:
        y_min = 5 + math.sqrt(25 - math.pow(x - 15, 2))
        y_max = 0.5 * x
        return y_min <= y < y_max
    else:
        return False

def main():
    total_count = 1000 * 1000 * 1000 * 10
    hit_count = 0
    for i in xrange(total_count):
        x = random.random() * 20
        y = random.random() * 10
        if in_area(x, y):
            hit_count += 1
    print hit_count, total_count, hit_count * 200.0 / total_count
if __name__ == '__main__':
    main()

