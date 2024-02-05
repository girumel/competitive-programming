#!/bin/python3

if __name__ == "__main__":
    N = int(input())
    result = []
    while N != 0:
        command = input()
        if command.count(" ") == 0:
            operation = command
        elif command.count(" ") == 1:
            operation, value = command.split(" ")
            value = int(value)
        elif command.count(" ") == 2:
            operation, value, index = command.split(" ")
            value = int(value)
            index = int(index)
        if operation == "print":
            print(result)
        elif operation == "append":
            result.append(value)
        elif operation == "remove":
            result.remove(value)
        elif operation == "insert":
            result.insert(value, index)
        elif operation == "sort":
            result.sort()
        elif operation == "pop":
            result.pop()
        elif operation == "reverse":
            result.reverse()
        N -= 1
