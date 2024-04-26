from collections import deque
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls = deque(nums)
        rs = deque(nums)
        rslist=deque()
        lslist=deque()
        # ls
        ls.appendleft(0)
        # rs
        rs.append(0)

        # ls
        lssum=0 
        for i in range(len(nums)):
            lssum+=ls[i]
            lslist.append(lssum)
        
        rssum=0
        for i in range(len(nums),0,-1):
            rssum+=rs[i]
            rslist.appendleft(rssum)
        ans = []
        for i,j in zip(lslist,rslist):
            ans.append(abs(i-j))

        return ans
        

