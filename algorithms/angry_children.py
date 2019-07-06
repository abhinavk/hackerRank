# HackerRank - Algorithms - Warmup
# Angry Children

nL = int(input())
k = int(input())
n = [int(input()) for _ in range(nL)]
n.sort()
best = n[k - 1] - n[0]
for i in range(nL - k + 1):
    if n[i + k - 1] - n[i] < best:
        best = n[i + k - 1] - n[i]

print(best)
