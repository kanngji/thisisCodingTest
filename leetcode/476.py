class Solution:
    def findComplement(self, num: int) -> int:
        changed = ""
        a = bin(num)
        a = a[2::]
        for i in a:
            if i == "1" :
                changed += "0"
            else:
                changed += "1"

        return (int(changed,2))