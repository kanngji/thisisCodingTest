class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        comparison = [x for x in range(1,len(nums)+1)]
        nums.sort()
        ans = []
        for i in comparison:
            if i not in nums:
                ans.append(i)

        return ans
    
## time limit issue
    
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        comparison = [x for x in range(1,len(nums)+1)]
        return list(set(comparison) - set(nums))