import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        permutations = list(itertools.permutations(nums))
        ans = []
        for perm in permutations:
            ans.append(perm)
        
        return ans