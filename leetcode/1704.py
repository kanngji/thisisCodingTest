class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s= s.lower()
        mo = ["e","a","o","i","u"]
        s1 = s[:len(s)//2]
        s2 = s[len(s)//2::]
        cnt_s1=0
        cnt_s2=0

        for i in s1:
            if i in mo:
                cnt_s1+=1

        for j in s2:
            if j in mo:
                cnt_s2+=1

        if cnt_s1 == cnt_s2:
            return True
        
        return False
        