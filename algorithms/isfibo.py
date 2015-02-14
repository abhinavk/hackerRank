# HackerRank - Algorithms - Warmup
# Is Fibo

from math import sqrt

def isfibo(n):
    if not sqrt((5*n*n)-4)%1 or not sqrt((5*n*n)+4)%1:
        return "IsFibo"
    return "IsNotFibo"


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(isfibo(int(input())))
