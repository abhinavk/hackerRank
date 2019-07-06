"""
HackerRank - Algorithm - Search
Ice Cream Parlor
"""


def solve_problem():
    m = int(input())
    n = int(input())
    c = map(int, input().split(" "))

    hashmap = {}

    for i, ic in enumerate(c):
        rem = m - ic
        if rem in hashmap:
            print(" ".join(sorted([hashmap[rem], i])))
        else:
            hashmap[rem] = i


if __name__ == "__main__":
    testcase = int(input())
    for _ in range(testcase):
        solve_problem()
