class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        d = [0] * 101
        cnt = 0
        for i in nums:
            start , end = i
            for j in range(start,end+1):
                d[j] = 1

        for i in d:
            if i==1:
                cnt+=1
        return cnt
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
       
        
        seen=set()
        
        for a,b in nums:
            for i in range(a,b+1):
                seen.add(i)
        
        return len(seen)