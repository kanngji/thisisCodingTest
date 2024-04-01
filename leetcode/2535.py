class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum=sum(nums)
        digitSum=''.join(str(s) for s in nums)
        digitSum=sum(int(s)for s in digitSum)
        return elementSum - digitSum
    
# ''.join(문자열리스트를 인자로)