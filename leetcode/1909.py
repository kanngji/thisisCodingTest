import itertools

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        combinations = list(itertools.combinations(nums,len(nums)-1))

        for comb in combinations:
            sorted_arr = sorted(set(comb))
            if sorted_arr == list(comb):
                return True

        return False