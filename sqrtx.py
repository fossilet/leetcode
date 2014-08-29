#! /usr/bin/env python3

"""
http://oj.leetcode.com/problems/sqrtx/

Implement int sqrt(int x).

Compute and return the square root of x.

Tue Apr 15 17:19:05 CST 2014
"""


def sqrt(x, precision=0.001):
    # TODO: This does not converge.
    assert 0 <= x <= 1
    y = (x + 1) / 2
    while abs(x - y**2) > precision:
        print(y)
        if x - y**2 > precision:
            y = (y + 1) / 2
        else:
            y /= 2
    return y


if __name__ == '__main__':
    print(sqrt(0.5))
