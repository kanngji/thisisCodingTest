class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxNum=max(nums)
        minNum=min(nums)
        ans = 1
        for i in range(2,maxNum+1):
            if minNum%i==0 and maxNum%i==0:
                ans = max(ans,i)

        return ans