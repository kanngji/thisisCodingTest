class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rng=len(nums)
        for i in range(0,rng+1):
            if i in nums:
                continue
            else:
                return i
            
# 성능 체크.