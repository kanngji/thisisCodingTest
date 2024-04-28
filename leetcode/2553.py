class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums = ''.join(str(i) for i in nums)

        ans = []
        for i in nums:
            ans.append(int(i))

        return ans