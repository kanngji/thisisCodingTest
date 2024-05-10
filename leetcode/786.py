from itertools import combinations
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans = [] 
        comb = combinations(arr,2)
        for c in comb:
            i,j = c
            ans.append([i/j,(i,j)])
        
        ans.sort()

        return(list(ans[k-1][1]))