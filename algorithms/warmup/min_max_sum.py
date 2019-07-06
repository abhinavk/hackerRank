#!/usr/bin/python3

number = [int(i) for i in input().split(" ")]
number.sort()
print(str(sum(number[:4])) + " " + str(sum(number[1:5])))
