class Solution:
    def addDigits(self, num: int) -> int:
        
        while(len(str(num))!=1):
            ans=""
            hap=0
            num=str(num)
            for i in num:
                ans+=i
            for i in ans:
                hap+=int(i) 
            num=hap
        return num
            
        
        