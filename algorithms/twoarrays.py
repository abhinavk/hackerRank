# HackerRank - Algorithms - Arrays and Sorting
# Two Arrays

def get_result(n,k,a,b):
    a = [int(x) for x in a]
    a.sort(reverse=True)
    b = [int(x) for x in b]
    b.sort()
    for i in range(n):
        if a[i] + b[i] < k:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,k = input().split(' ')
        a = input().split(' ')
        b = input().split(' ')
        print(get_result(int(n),int(k),a,b))
