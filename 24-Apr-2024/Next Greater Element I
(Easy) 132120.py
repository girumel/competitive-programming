# Problem: Next Greater Element I
(Easy) - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] 
        res = {}
        ans = []

        for num in nums2:
            while stack and stack[-1] < num:
                res[stack.pop()] = num
            stack.append(num)

        for x in nums1:
            ans.append(res.get(x, -1))
        return ans