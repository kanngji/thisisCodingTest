class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = []

        for i in range(0,n):
            ans.append(start+2*i)

        res = ans[0]
        for i in range(1,len(ans)):
            res = ans[i]^res

        return res