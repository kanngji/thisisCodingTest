class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [x**2 for x in nums]
        squared_nums = sorted(squared_nums)
        return squared_nums
    
# 리스트 컴프리헨션