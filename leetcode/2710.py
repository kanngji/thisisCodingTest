class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]

        ans =""
        signal = True
        for i in num:
            if i == '0' and signal==True:
                continue
            else:
                ans+=i
                signal = False

        return ans[::-1]