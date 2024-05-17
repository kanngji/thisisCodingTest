class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dict1=dict()
        dict2=dict()

        for i in s1:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        for j in s2:
            if j not in dict2:
                dict2[j]=1
            else:
                dict2[j]+=1
        cnt = 0
        for i,j in zip(s1,s2):
            if i!=j:
                cnt+=1
        
        if (dict1==dict2) and (cnt==2 or cnt==0):
            return True
        return False