
palsl=set()
def pals():
    a = 999
    b = 999
    i = 0
    for a1 in range(a, 100, -1):
        for b1 in range(101, b+1, 1):
            if b1 > a1:
                break
            x=a1*b1
            if Palindrome(x):
                palsl.add(x)

def Palindrome(n):
    n = str(n)
    l = [x for x in n]
    if l == l[::-1]:
        return int(n)
    return False
t=int(input())
pals()
for _ in range(t):
    for i in range(int(input()),101100,-1):
        if i in palsl:
            print(i)
            break
