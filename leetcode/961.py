class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dict1=dict()
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1

        l = len(nums)//2

        for k,v in dict1.items():
            if v==l:
                return k
