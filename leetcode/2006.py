import itertools

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        combinations = itertools.combinations(nums,2)
        cnt = 0 

        for comb in combinations:
            if abs(comb[0]-comb[1])== k:
                cnt+=1
            
        return cnt