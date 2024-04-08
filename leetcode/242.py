class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1=dict()
        ans=dict()

        for i in s:
            if i not in dict1:
                dict1[i]=0
            else:
                dict1[i]+=1
        
        for i in t:
            if i not in ans:
                ans[i]=0
            else:
                ans[i]+=1
        
        
        return dict1==ans
        
# for문으로 비교할려했는데 딕셔너리는 순서가 없다.
    