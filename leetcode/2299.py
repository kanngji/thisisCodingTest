class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        res = True
        # at least 8c
        if len(password) < 8:
            return False

        # 1 lowercase
        lowerchecker=False
        upperchecker=False
        digitchecker=False
        for i in password:
            if i.islower():
                lowerchecker=True
            if i.isupper():
                upperchecker=True
            if i.isdigit():
                digitchecker=True
        
        if lowerchecker==False or upperchecker==False or digitchecker==False:
            return False

        specials = "!@#$%^&*()-+"
        specialchecker=False
        for i in specials:
            if i in password:
                specialchecker=True
        
        if specialchecker==False:
            return False
        
        for i in range(len(password)-1):
            if password[i]==password[i+1]:
                return False
        
        return res
        

        


