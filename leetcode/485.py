class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        max_cnt = 0
        for i in nums:
            if i==1:
                cnt+=1
            else:
                if cnt>=max_cnt:
                    max_cnt=cnt
                cnt=0
        return max(max_cnt,cnt)