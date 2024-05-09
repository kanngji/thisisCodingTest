class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt_zero = 0
        cnt_one = 0
        ans = ""
        for i in s:
            if i == '0':
                cnt_zero+=1
            else:
                cnt_one+=1
        
        if cnt_one == 1:
            return "0"*cnt_zero+"1"

        else:
            return "1"*(cnt_one-1)+"0"*cnt_zero+"1"