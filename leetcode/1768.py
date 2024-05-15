from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        dq1 = deque(word1)
        dq2 = deque(word2)

        ans = []

        while dq1 and dq2:
            if dq1:
                ans.append(dq1.popleft())
            if dq2:
                ans.append(dq2.popleft())
        
        if dq1:
            ans.extend(dq1)
        if dq2:
            ans.extend(dq2)

        ans=''.join(ans)

        return ans
    
#
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # have two pointers for both word string and a result list
        p, q = 0, 0
        res = []

        # loop until one of them reaches the end
        while p < len(word1) and q < len(word2):
            res.append(word1[p])
            res.append(word2[q])
            p = p + 1
            q = q + 1
        
        # after we jump out of while loop add the remaining to the res
        res.append(word1[p:])
        res.append(word2[q:])

        return ''.join(res)