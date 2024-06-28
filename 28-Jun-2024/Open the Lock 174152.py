# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends:
            return -1
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1

        queue = deque(['0000'])
        visited = set('0000')
        turns = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()
                if current == target:
                    return turns
                for i in range(4):
                    for j in [-1, 1]:
                        combination = current[:i] + str((int(current[i]) + j) % 10) + current[i + 1:]
                        if combination not in visited and combination not in deadends:
                            queue.append(combination)
                            visited.add(combination)
            turns += 1
        
        return -1