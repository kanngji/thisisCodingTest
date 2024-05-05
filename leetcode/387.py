class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = dict()

        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = (i,1)
            else:
                idx , count = dict1[s[i]]
                dict1[s[i]] = (idx , count+1)
        
        remove = []
        
        for key ,value in dict1.items():
            if value[1] >= 2:
                remove.append(key)

        for key in remove:
            del dict1[key]

        res = [x[0] for x in dict1.values()]

        if len(res)==0:
            return -1
        else:
            return res[0]
        

# Counter 
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        return min([i for i in range(len(s)) if c[s[i]] == 1], default = -1)