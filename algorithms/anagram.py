# HackerRank - Algorithms - Strings
# Anagrams


def shifts_required(input_str):
    shifts = 0
    if len(input_str) % 2:
        return -1
    a, b = input_str[: len(input_str) // 2], input_str[len(input_str) // 2 :]
    dict = {}
    dicta = {}
    for i in b:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
            dicta[i] = 0
    for i in a:
        if i in dicta.keys():
            dicta[i] += 1
        else:
            dicta[i] = 1
    for i in dict.keys():
        if dict[i] > dicta[i]:
            shifts += dict[i] - dicta[i]
    return shifts


t = int(input())
for _ in range(t):
    print(shifts_required(input()))
