# Problem: E - Is Valid Permutation? - https://codeforces.com/gym/515369/problem/E

t = int(input())
for _ in range(t):
    n = int(input())
    ps = list(map(int, input().split()))

    max_prefix = 0
    total_sum = n * (n + 1) // 2
    invalid = False

    for prefix in ps:
        if prefix <= max_prefix:
            invalid = True
        max_prefix = max(max_prefix, prefix)

    if max_prefix > total_sum or invalid:
        print("NO")
        continue

    if ps[-1] != total_sum:
        if ps[0] <= 0 or ps[0] > n:
            print("NO")
            continue
        ps.append(total_sum)
        seen = {ps[0]}
        is_valid = True
        for i in range(1, len(ps)):
            diff = ps[i] - ps[i - 1]
            if diff <= 0 or diff > n or diff in seen:
                print("NO")
                is_valid = False
                break
            seen.add(diff)
        if is_valid and len(seen) != n:
            print("NO")
        elif is_valid and len(seen) == n:
            print("YES")
    else:
        seen = set()
        temp = []
        for i in range(1, len(ps)):
            diff = ps[i] - ps[i - 1]
            if diff not in seen and 0 < diff <= n:
                seen.add(diff)
                total_sum -= diff
            else:
                temp.append(diff)
        if not temp and len(seen) == n - 2 and total_sum == ps[0]:
            print("YES")
        elif len(temp) == 1 and len(seen) == n - 3:
            if ps[0] in seen or ps[0] > n or ps[0] <= 0:
                print("NO")
            elif total_sum - ps[0] == temp[0]:
                print("YES")
        else:
            print("NO")