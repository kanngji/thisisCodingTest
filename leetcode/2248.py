class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common_el = set(nums[0])

        for num in nums[1:]:
            common_el &= set(num)

        return sorted(common_el)