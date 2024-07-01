# Problem: C - Radio Station - https://codeforces.com/gym/500425/problem/C

num_servers, num_commands = map(int, input().split())
servers = {}
result = []

for _ in range(num_servers):
    name, ip = input().split()
    servers[ip] = name

for _ in range(num_commands):
    command, ip = input().split()
    ip = ip[:-1]
    result.append(f"{command} {ip}; #{servers[ip]}")

print("\n".join(result))