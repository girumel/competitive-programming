n = int(input())
phonebook = {}
for _ in range(n):
    name, phone = input().split()
    phonebook[name] = phone

while True:
    try:
        name = input()
        if name in phonebook:
            print(f"{name}={phonebook[name]}")
        else:
            print("Not found")
    except EOFError:
        break
