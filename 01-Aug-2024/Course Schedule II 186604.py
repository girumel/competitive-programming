# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []