from collections import deque
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        n = [x for x in n]
        dq = deque(n)
        pos =[]
        neg = []
        while dq:
            if dq:
                pos.append(int(dq.popleft()))
            if dq:
                neg.append(int(dq.popleft()))
        
        return sum(pos)-sum(neg)
