#!/bin/python3

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    result = []

    for i in arr:
        result.append(i)
    result.sort()
    for i in result:
        while result.count(i) > 1:
            result.remove(i)
    print(result[-2])
