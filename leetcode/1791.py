class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        sets = [set(sublist) for sublist in edges]

        common = set.intersection(*sets)

        for i in common:
            return i
        
# 다른 사람 풀이
        
        counts = []
        for e in edges :
            if e[0] in counts:
                return e[0]
            if e[1] in counts:
                return e[1]
            counts.append(e[0])
            counts.append(e[1])