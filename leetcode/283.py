from collections import deque
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==0 and nums[j] !=0:
                    nums[i],nums[j] = nums[j],nums[i]
        
        return nums
## 시간
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums
    