from collections import deque
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums=deque(nums)
        ans=[]
        arr=[]
        while len(nums)>0:
            ans.append(nums[1])
            ans.append(nums[0])
            nums.popleft()
            nums.popleft()
        return ans
    
# from collections import deque
    
# deque(list)