class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        dict1 = dict()
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1

        res = [k for k,v in dict1.items() if v==2]
        ans = 0
        for j in res:
            ans=ans ^ j
        
        return ans