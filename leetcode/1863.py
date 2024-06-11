from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = sum(nums) # 요소 한 개의 xor은 그냥 요소 하나 (초기값)
        for i in range(2,len(nums)+1):
            combs = combinations(nums,i)

            for comb in combs:
                res = 0
                for i in comb:
                    res = res ^ i
                ans+=res
        return ans