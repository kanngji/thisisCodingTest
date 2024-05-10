class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict1 = dict()
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        
        ans = [x for x in dict1 if dict1[x]>=2]
        return ans