# Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        dict1 = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        return dict1[0][0]