#!/usr/bin/env python3
"""
Input a string and reduce characters if found same successively
For example, for input "aaabccddd", output "abd"
and, for input "baab", output "Empty String"
"""


def reduce_string(s):
    """
    Solve using stack
    """
    _stack = []

    for c  in s:
        if not _stack or c != _stack[-1] :
            _stack.append(c)
        else:
            _stack.pop()

    if len(_stack) > 0:
        return ''.join(_stack)
    return 'Empty String'

if __name__ == '__main__':
    input_string = input()
    print(reduce_string(input_string))
