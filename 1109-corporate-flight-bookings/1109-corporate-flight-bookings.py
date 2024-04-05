class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        total = [0] * n
        
        for first, last, seats in bookings:
            total[first-1] += seats
            
            if last < n:
                total[last] -= seats
        
        for i in range(1, n):
            total[i] += total[i-1]
        
        return total