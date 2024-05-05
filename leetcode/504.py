class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        ans = ""
        negative=False
        if num<0:
            negative=True
        num = abs(num)
        while (num>0):
            ans+=str(num%7)
            num=num//7

        if negative==True:
            
            ans=ans[::-1]
            ans=int(ans)*-1
            return str(ans)
        else:
            return ans[::-1]
        
