from collections import deque
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        sig=False
        dq = deque(nums)
        
        l = len(nums)
        i=0
        if list(dq) == sorted_nums:
            return 0
        while(i<l):
            dq.appendleft(dq.pop())
            i+=1
            
            if list(dq)==sorted_nums:
                sig=True
                return i
        if sig==False:
            return -1