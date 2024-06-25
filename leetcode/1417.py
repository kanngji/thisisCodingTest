class Solution:
    def reformat(self, s: str) -> str:
        strings = []
        digits = []

        for i in s:
            if i.isdigit():
                digits.append(i)
            else:
                strings.append(i)

        if abs(len(strings)-len(digits)) > 1:
            return ""
        ans=""
        min_l=min(len(strings),len(digits))
        
        for i in range(min_l):
            if len(strings) > len(digits):
                ans+=strings[i]
                ans+=digits[i]
            elif len(strings) <= len(digits):
                ans+=digits[i]
                ans+=strings[i]

        if len(strings) > len(digits):
            ans+=strings[-1]
        elif len(strings)< len(digits):
            ans+=digits[-1]
        return ans

# 코드를 너무 막 짠ㅓ같음..