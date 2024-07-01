class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}

        stack = []

        for num in nums2[::-1]:
            # 스택의 마지막 요소가 현재 요소 보다 작거나 같으면 제거
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                next_greater[num] = stack[-1]
            else:
                next_greater[num] = -1
            stack.append(num)

        return [next_greater[num] for num in nums1]
    
# 이해가 잘...