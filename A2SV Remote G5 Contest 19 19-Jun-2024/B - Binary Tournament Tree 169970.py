# Problem: B - Binary Tournament Tree - https://codeforces.com/gym/529269/problem/B

def build_tree(n, sequence):
    depths = [0] * n

    def backtrack(start, end, depth):
        if start > end:
            return

        sub_array = sequence[start : end + 1]
        max_index = start + sub_array.index(max(sub_array))
        depths[max_index] = depth

        backtrack(start, max_index - 1, depth + 1)
        backtrack(max_index + 1, end, depth + 1)

    backtrack(0, n - 1, 0)
    return depths


t = int(input())
for _ in range(t):
    n = int(input())
    sequence = list(map(int, input().split()))
    depths = build_tree(n, sequence)
    print(" ".join(map(str, depths)))