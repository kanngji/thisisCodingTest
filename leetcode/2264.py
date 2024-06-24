class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ''
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                triplet = num[i:i+3]
                if triplet > ans:
                    ans = triplet
        return ans 
    
# "66">"55" 이게 True가 나오네 몰랐는딩
    