class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = 0
        for i in range(len(nums)):
            if nums[i]<target:
                ans = i+1
            
        
        return ans
# Binary Search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0 # 왼쪽
        r = len(nums) - 1 # 오른쪽

        while l<= r:
            mid = (l+r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        
        return l 