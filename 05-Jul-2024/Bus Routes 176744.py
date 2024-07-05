# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        routes = [set(route) for route in routes]
        stop_routes = defaultdict(set)
        visited = set()
        queue = deque([(source, 0)])

        for i, route in enumerate(routes):
            for stop in route:
                stop_routes[stop].add(i)

        while queue:
            stop, buses = queue.popleft()
            for i in stop_routes[stop]:
                if i in visited:
                    continue

                visited.add(i)

                if target in routes[i]:
                    return buses + 1
                for next_stop in routes[i]:
                    queue.append((next_stop, buses + 1))

        return -1