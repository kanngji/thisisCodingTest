class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        small = nums[0]*nums[1]
        big = nums[-1]*nums[-2]

        return big - small 