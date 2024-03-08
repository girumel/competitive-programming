class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        for index in range(n):
            ops = 0
            left = 0
            while left < index:
                if boxes[left] == '1':
                    ops += index - left
                left += 1
            
            right = n-1
            while right > index:
                if boxes[right] == '1':
                    ops += right - index
                right -= 1
            
            answer[index] = ops
        
        return answer
    