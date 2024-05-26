class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dict1 = dict()

        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        ans = [v for k,v in dict1.items()]

        for i in ans:
            if i>=3:
                return False
        return True