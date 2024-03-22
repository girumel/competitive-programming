class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        max_subarray = 0
        
        i = 1
        while i < n - 1:
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                l = i
                r = i
            
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1
                    
                while r < n - 1 and arr[r] > arr[r+1]:
                    r += 1

                max_subarray = max(max_subarray, r-l+1)
            
            i += 1
        
        return max_subarray
        