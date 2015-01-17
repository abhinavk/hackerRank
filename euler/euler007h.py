# Create the prime sieve upto 10000


def create_sieve(lim=10000):
    x = [0 if not i%2 else 1 for i in range(10001)]
    x[2]=1
    for i in range(3,105,2):
        for j in range(i+1,10001):
            if not j%i:
                x[j]=0
    for i,j in enumerate(x):
        if x[i]==1:
            print(i, end=" ")
    newa = [term+2 for term,val in enumerate(x[2:]) if val is 1]
    for i in newa:
        print(i,end=' ')

create_sieve()
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         print(int(get_result(int(input()))))

