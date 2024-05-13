from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [x for x in range(1,n+1)]
        ans = []
        combs = list(combinations(arr,k))
        for comb in combs:
            ans.append(comb)

        return ans