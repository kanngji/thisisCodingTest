from collections import deque

class Solution:
    def clearDigits(self, s: str) -> str:
        dq = deque()
        for i in s:
            if i.isdigit():
                dq.pop()
            else:
                dq.append(i)

        return (''.join(dq))