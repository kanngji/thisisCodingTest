from collections import deque

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        dq = deque(s)
        ans = []
        res = ""
        while len(dq) > k:
            res = ''
            for _ in range(k):
                res+=dq.popleft()
            ans.append(res)
        
        if len(dq)>0:
            res = ''.join(dq)
            for _ in range(k-len(dq)):
                res+=fill
        ans.append(res)
        return ans