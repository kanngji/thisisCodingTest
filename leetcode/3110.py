class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(len(s)-1):
            j=i+1
            ans+=(abs(ord(s[i])-ord(s[j])))
        return ans
    
# ord() , chr() , abs()