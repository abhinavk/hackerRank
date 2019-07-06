"""
HackerRank - Algorithms - Warmup
Chocolate Feast
"""


def how_many_chocolates(n, c, m):
    wrappers = choco = n // c
    while wrappers >= m:
        exch = wrappers // m
        choco += exch
        wrappers = wrappers - exch * m + exch
    return choco


test_cases = int(input())
for _ in range(test_cases):
    inp = input()
    s = inp.split(" ")
    n, c, m = tuple(s)
    print(how_many_chocolates(int(n), int(c), int(m)))
