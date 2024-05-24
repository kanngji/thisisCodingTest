class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        dict1 = dict()

        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        for key,val in dict1.items():
            
            if key == val : 
                ans = max(ans,val)

        return ans