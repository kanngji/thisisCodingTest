class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(sorted(nums, reverse=True))
        if len(nums) < 3:
            return nums[0]
        return nums[2]
        
