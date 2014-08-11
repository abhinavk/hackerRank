# HackerRank's Euler problem 5
# I didn't think of this method the first time :)
# It still leaks 1
from collections import Counter

prime_sundry = [2,3,5,7,11,13,17,19,21,23,29,31,37]


def outvalue(n):
    p=Counter(prime_factors(n))
    reqproduct=1
    # Here is the real thing
    for i in range(n-1,1,-1):
        p |= Counter(prime_factors(i))
    for i in list(p.elements()):
        reqproduct*=i
    print(reqproduct)


def prime_factors(n):
    p=[]
    for i in prime_sundry:
        while not n%i:
            p.append(i)
            n /= i
        if n == 1:
            break
    return p


def main():
    t=int(input())
    for _ in range(t):
        outvalue(int(input()))


if __name__ == '__main__':
    main()
