"""
HackerRank - Algorithms - Implementation
Save the Prisoner
"""


def solve_case():
    n, m, s = input().strip().split(" ")
    n, m, s = [int(n), int(m), int(s)]
    if m > n:
        m = m % n
    last = s - 1 + m
    if last > n:
        print(str(last - n))
    else:
        print(str(last))


t = int(input())

for _ in range(t):
    solve_case()
