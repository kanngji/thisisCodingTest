import sys
sys.set_int_max_str_digits(10**6)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = int(''.join(map(str,num)))
        ans = res+ k

        ans = [int(x) for x in str(ans)]

        return ans
    

# ''.join(map(str,num))