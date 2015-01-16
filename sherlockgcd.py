# Hackerrank - Algorithms - Warmup
# Sherlock and GCD

import math

def get_sieve(lim=10000):
    x = [0 if not i%2 else 1 for i in range(lim+1)]
    x[2]=1
    for i in range(3,math.ceil(math.sqrt(lim+1)),2):
        for j in range(i+1,lim+1):
            if not j%i:
                x[j]=0
    return {term+2 for term,val in enumerate(x[2:]) if val is 1}

def yesorno(total, numbers, sieve):
    ctr = 0
    factor = 0
    if 1 in numbers:
        return 'YES'
    for i in numbers:
        if i in sieve:
            ctr += 1
            factor = i
        if ctr == 2:
            return 'YES'
    if ctr ==1:
        for i in numbers:
            if not i%factor and i!=factor:
                return 'NO'
        return 'YES'
    else: # ie 0
        return 'NO'


if __name__ == '__main__':
    t = int(input())
    sieve = get_sieve(100000)
    for _ in range(t):
        n = int(input())
        array_str = input()
        arr = array_str.split(' ')
        arr = [int(x) for x in arr]
        print(yesorno(n,arr,sieve))
