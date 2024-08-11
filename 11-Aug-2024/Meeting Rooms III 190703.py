# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ongoing = []
        meetings_count = [0] * n
        available = list(range(n))
        heapq.heapify(available)

        for start, end in meetings:
            while ongoing and ongoing[0][0] <= start:
                end_time, room = heapq.heappop(ongoing)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(ongoing, (end, room))
            else:
                end_time, room = heapq.heappop(ongoing)
                new_end = end_time + (end - start)
                heapq.heappush(ongoing, (new_end, room))
            meetings_count[room] += 1

        max_meetings = max(meetings_count)
        for i in range(n):
            if meetings_count[i] == max_meetings:
                return i