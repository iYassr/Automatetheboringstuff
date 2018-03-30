#!/bin/python3

import sys


def camelcase(st):
    counter = 1
    for i in st:
        if i.isupper():
            counter = counter + 1
    return counter


if __name__ == "__main__":
    s = input()
    result = camelcase(s)
    print(result)
