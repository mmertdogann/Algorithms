'''
    Codewars - Split Strings: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
'''


def solution(s):
    size = len(s)
    result = list()

    for i in range(0, size, 2):
        if i == size - 1 and size % 2 != 0:
            result.append(s[i] + "_")
        else:
            result.append(s[i] + s[i+1])

    return result
