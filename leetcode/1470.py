class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        xarr=nums[:n]
        yarr=nums[n::]
        ans=[]

        for i in range(n):
            ans.append(xarr[i])
            ans.append(yarr[i])
        return ans
