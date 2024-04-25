from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        dq1 = deque(s)
        dq2 = deque(goal)

        for _ in range(len(goal)):
            if dq1==dq2:
                return True
            else:
                dq2.append(dq2.popleft())
        return False
    
    