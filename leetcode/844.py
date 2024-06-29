from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ds = deque()
        dt = deque()

        for i in s:
            if i == '#':
                if len(ds)>0:
                    ds.pop()
            else:
                ds.append(i)


        for i in t:
            if i == '#':
                if len(dt)>0:
                    dt.pop()
            else:
                dt.append(i)

        ds = ''.join(ds)
        dt = ''.join(dt)

        return ds==dt