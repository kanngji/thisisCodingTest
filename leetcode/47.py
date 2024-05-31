import itertools 
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permus = itertools.permutations(nums,len(nums))
        s = set()
        ans = []
        for perm in permus:
            s.add(perm)

        for i in s:
            ans.append(list(i))

        return ans