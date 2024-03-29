class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        sum=0
        for i in range(len(nums)):
            sum=nums[i]+sum
            ans.append(sum)
        return ans