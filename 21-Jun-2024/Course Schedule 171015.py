# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        visiting = set()

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def has_cycle(course):
            if course in visited:
                return False
            if course in visiting:
                return True

            visiting.add(course)
            for prereq in graph[course]:
                if has_cycle(prereq):
                    return True
            visited.add(course)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True