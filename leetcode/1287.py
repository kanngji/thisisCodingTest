class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dict1 = dict()

        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        for j in dict1:
            dict1[j]=dict1[j]/len(arr)
            if dict1[j]>0.25:
                return j