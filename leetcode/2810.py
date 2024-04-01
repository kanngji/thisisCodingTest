class Solution:
    def finalString(self, s: str) -> str:
        s=list(s)
        ans=[]
        for i in s:
            if i=='i':
              ans.reverse()
            else:
                ans.append(i)

        return ''.join(ans)
    
#list.reverse() 결과값 자동반환