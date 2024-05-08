class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums.pop()
        b = nums.pop()
        return (a-1)*(b-1)