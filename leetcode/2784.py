class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(1,n):
            if i not in nums:
                return False

        max_num = max(nums)

        two_num = nums.count(max_num)

        if two_num == 2:
            return True